#!/usr/bin/env uv run
# /// script
# dependencies = [
#   "requests",
#   "click",
#   "litellm",
#   "pyyaml",
#   "python-frontmatter",
#   "pillow",
#   "rich"
# ]
# ///
"""
Blog management script for AI-generated featured images and other tasks.

This script provides comprehensive featured image generation for blog posts using AI image
generation models with automatic content analysis, brand-consistent styling, watermarking,
and Hugo integration.

## Commands

### test-image-generation
Test LLM gateway connectivity and discover available image generation models.

Example:
    ./manage.py test-image-generation --base-url https://your-llm-gateway.example.com --api-key sk-xxx

### generate
Generate AI-powered featured images for blog posts with automatic content analysis.

Examples:
    # Generate for a specific post (recommended)
    ./manage.py generate ../content/posts/2025-01-01-my-post.md \
        --image-model dall-e-3 \
        --text-model claude-sonnet-4 \
        --output static/img/my-post.generated.png \
        --url "andrewbolster.info/2025/01/my-post.html" \
        --base-url https://your-llm-gateway.example.com \
        --api-key sk-xxx

    # Generate with custom text prompt
    ./manage.py generate \
        --image-model dall-e-3 \
        --text "A cyberpunk workspace with AI elements in dark purple tones" \
        --output static/img/custom-image.generated.png \
        --url "example.com" \
        --base-url https://your-llm-gateway.example.com \
        --api-key sk-xxx

### add-featured-images
Bulk add featured images from existing first images in posts.

Example:
    ./manage.py add-featured-images --dry-run    # Preview changes
    ./manage.py add-featured-images             # Apply changes

## Configuration

### Environment Setup
The script uses the service-llm configuration from ~/src/service-llm/manage.ini.
For llm.labs environment:
- base_url: https://your-llm-gateway.example.com
- api_key: (set via LITELLM_PROXY_API_KEY environment variable)

### Image Specifications
- Default dimensions: 860x530 (optimized for blog headers)
- DALL-E compatibility: Automatically uses 1792x1024 then resizes to target
- Format: PNG with watermarking applied after resize for readability
- Watermarks: Copyright (bottom-right) and URL (bottom-left)

### Brand Guidelines
All generated images follow consistent branding:
- Color scheme: Dark indigo/purple primary colors
- Style: Cyberpunk/solarpunk aesthetic elements
- Quality: Professional blog header standard
- Theme: Modern minimalist tech illustration

### File Organization
- Generated images: static/img/[post-slug].generated.png
- Hugo paths: img/[filename] (static/ prefix stripped)
- Frontmatter: Automatically updated with cover block including alt text and caption

## Best Practices

### Post File Naming
Use descriptive filenames that will become readable image names:
- Good: static/img/my-awesome-feature.generated.png
- Avoid: static/img/img1.generated.png

### Content Analysis
For best results when using post files:
- Ensure posts have clear title and tags
- Include substantive content (500+ words recommended)
- Use descriptive tags that reflect visual concepts

### URL Watermarks
Always include the canonical post URL for proper attribution:
- Format: "domain.com/path/to/post.html"
- Helps with image attribution when shared

### Model Selection
Recommended combinations:
- Image: dall-e-3 (best quality, handles brand guidelines well)
- Text: claude-sonnet-4 (excellent content analysis and prompt generation)

### Error Handling
The script includes automatic retry logic for service unavailability:
- 5 retries with exponential backoff
- Handles 500/502/503/504 errors automatically
- Session-based requests with proper timeouts

## Troubleshooting

### Common Issues
1. **503 Service Unavailable**: Automatic retries will handle temporary outages
2. **DALL-E size errors**: Script automatically handles size compatibility
3. **Path issues**: Use relative paths from script directory
4. **Watermarks unreadable**: Now applied after resize for proper scaling

### File Path Resolution
When running from scripts/ directory:
- Post files: ../content/posts/filename.md
- Output images: ../static/img/filename.png (or just static/img/filename.png)
- Frontmatter updates: Automatic with correct Hugo paths
"""
import os
import requests
from requests.adapters import HTTPAdapter, Retry
import click
import json
import frontmatter
import time
from pathlib import Path
from litellm import image_generation, completion
from rich.console import Console
from rich.prompt import Prompt, Confirm
from datetime import datetime
from urllib.parse import urlparse
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import re

console = Console()

# Setup requests session with retry logic
session = requests.Session()
retries = Retry(
    total=5,
    backoff_factor=0.1,
    status_forcelist=[500, 502, 503, 504]
)
session.mount('http://', HTTPAdapter(max_retries=retries))
session.mount('https://', HTTPAdapter(max_retries=retries))

# Set default headers and timeout for session
session.headers.update({
    'User-Agent': 'blog-management-script/1.0'
})
# Note: API-specific headers like Authorization will be added per request


def add_watermark(image_bytes, watermark_text=None, url_text=None):
    """Add watermark text to bottom right of image, and optional URL to bottom left."""
    if watermark_text is None:
        current_year = datetime.now().year
        watermark_text = f"Andrew Bolster {current_year} - AI Generated - CC0"

    # Open image from bytes
    image = Image.open(BytesIO(image_bytes))

    # Create drawing context
    draw = ImageDraw.Draw(image)

    # Try to use a system font, fallback to default if not available
    try:
        # Try common system fonts in descending order of preference
        font_paths = [
            "/System/Library/Fonts/Arial.ttf",  # macOS
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",  # Linux
            "/Windows/Fonts/arial.ttf"  # Windows
        ]

        font = None
        for font_path in font_paths:
            if Path(font_path).exists():
                font = ImageFont.truetype(font_path, 16)
                break

        if font is None:
            font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()

    # Add copyright watermark on bottom right
    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Position in bottom right with 10px margin
    x_right = image.width - text_width - 10
    y_right = image.height - text_height - 10

    # Add semi-transparent background for readability
    padding = 5
    background_bbox = [
        x_right - padding,
        y_right - padding,
        x_right + text_width + padding,
        y_right + text_height + padding
    ]
    draw.rectangle(background_bbox, fill=(0, 0, 0, 128))

    # Add white text
    draw.text((x_right, y_right), watermark_text, fill=(255, 255, 255, 255), font=font)

    # Add URL watermark on bottom left if provided
    if url_text:
        # Get URL text size
        url_bbox = draw.textbbox((0, 0), url_text, font=font)
        url_width = url_bbox[2] - url_bbox[0]
        url_height = url_bbox[3] - url_bbox[1]

        # Position in bottom left with 10px margin
        x_left = 10
        y_left = image.height - url_height - 10

        # Add semi-transparent background for URL
        url_background_bbox = [
            x_left - padding,
            y_left - padding,
            x_left + url_width + padding,
            y_left + url_height + padding
        ]
        draw.rectangle(url_background_bbox, fill=(0, 0, 0, 128))

        # Add white URL text
        draw.text((x_left, y_left), url_text, fill=(255, 255, 255, 255), font=font)

    # Convert back to bytes with quantization for smaller file size
    output_buffer = BytesIO()

    # Reduce colors to 256 for smaller PNG files (effective for AI-generated images)
    if image.mode in ('RGB', 'RGBA'):
        try:
            quantized = image.quantize(colors=256, method=Image.Quantize.MEDIANCUT)
            # Convert back to RGB to avoid palette mode issues with further processing
            quantized = quantized.convert('RGB')
            quantized.save(output_buffer, format='PNG', optimize=True, compress_level=9)
        except:
            # Fallback to original if quantization fails
            image.save(output_buffer, format='PNG', optimize=True, compress_level=9)
    else:
        image.save(output_buffer, format='PNG', optimize=True, compress_level=9)

    return output_buffer.getvalue()

@click.group()
def cli():
    """Blog management tools for featured images and more."""
    pass

@cli.command("test-image-generation")
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
@click.option('--api-key', help='Override API key (defaults to LITELLM_PROXY_API_KEY env var)')
@click.option('--base-url', help='Override base URL (defaults to LITELLM_PROXY_URL env var)')
def test_image_generation(verbose, api_key, base_url):
    """Test LLM gateway for available image generation models."""

    # Use provided arguments or fall back to environment
    api_key = api_key or os.getenv('LITELLM_PROXY_API_KEY')
    base_url = base_url or os.getenv('LITELLM_PROXY_URL')

    if not api_key:
        console.print("❌ Missing LITELLM_PROXY_API_KEY environment variable", style="red")
        raise click.Abort()

    if not base_url:
        console.print("❌ Missing LITELLM_PROXY_URL environment variable", style="red")
        raise click.Abort()

    console.print(f"🔍 Querying LLM gateway at: {base_url}")

    # Test basic connectivity
    try:
        response = session.get(
            f'{base_url}/v1/models',
            headers={'Authorization': f'Bearer {api_key}'},
            timeout=30
        )

        console.print(f"📡 Response status: {response.status_code}")

        if response.status_code == 200:
            models_data = response.json()

            if verbose:
                console.print("Raw response:")
                console.print_json(data=models_data)

            # Extract models list
            if 'data' in models_data:
                models = models_data['data']
            elif isinstance(models_data, list):
                models = models_data
            else:
                models = [models_data]

            console.print(f"📋 Found {len(models)} total models")

            image_models = []
            for model in models:
                model_id = model.get('id', 'unknown')

                # Look for image generation indicators
                is_image_model = (
                    'dall' in model_id.lower() or
                    'image' in model_id.lower() or
                    'midjourney' in model_id.lower() or
                    'stable-diffusion' in model_id.lower() or
                    'sd-' in model_id.lower() or
                    'titan-image' in model_id.lower() or
                    'imagen' in model_id.lower()
                )

                if verbose:
                    style = "green" if is_image_model else "dim"
                    console.print(f"  • {model_id}", style=style)

                if is_image_model:
                    image_models.append(model_id)

            if image_models:
                console.print(f"\n🎨 Image generation models found:", style="green bold")
                for model in image_models:
                    console.print(f"  ✅ {model}", style="green")
            else:
                console.print(f"\n⚠️  No obvious image generation models found", style="yellow")
                console.print("Try manually testing with: dall-e-3, dall-e-2")

        else:
            console.print(f"❌ Error response: {response.status_code}", style="red")
            console.print(response.text)

    except requests.exceptions.RequestException as e:
        console.print(f"❌ Request failed: {e}", style="red")
        raise click.Abort()

    # Test litellm's knowledge of image models
    console.print(f"\n🧠 LiteLLM's known image generation models:")
    try:
        from litellm.utils import get_llm_provider

        # Common image models to test
        test_models = [
            "dall-e-3", "dall-e-2",
            "stability-ai/stable-diffusion-xl-base-1.0",
            "midjourney", "replicate/stability-ai/stable-diffusion"
        ]

        for model in test_models:
            try:
                provider, _, _, _ = get_llm_provider(model)
                console.print(f"  • {model} -> {provider}", style="dim")
            except:
                pass

    except ImportError:
        console.print("  (litellm utils not available)", style="dim")


@cli.command("generate")
@click.argument('post-file', type=click.Path(exists=True, path_type=Path), required=False)
@click.option('--image-model', required=True, help='Image generation model to use (e.g., dall-e-3)')
@click.option('--text-model', help='Text model for analyzing post content (required when using post file)')
@click.option('--text', help='Override text prompt instead of analyzing post content')
@click.option('--url', help='Optional URL to include as watermark on bottom left')
@click.option('--output', '-o', default='generated.png', help='Output filename (default: generated.png)')
@click.option('--size', '-s', default='860x530', help='Image size in WIDTHxHEIGHT format (default: 860x530, will resize from DALL-E output)')
@click.option('--api-key', help='Override API key (defaults to LITELLM_PROXY_API_KEY env var)')
@click.option('--base-url', help='Override base URL (defaults to LITELLM_PROXY_URL env var)')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
@click.option('--yes', '-y', is_flag=True, help='Skip confirmation prompts')
def generate(post_file, image_model, text_model, text, url, output, size, api_key, base_url, verbose, yes):
    """Generate a featured image for a blog post."""

    # Use provided arguments or fall back to environment
    api_key = api_key or os.getenv('LITELLM_PROXY_API_KEY')
    base_url = base_url or os.getenv('LITELLM_PROXY_URL')

    if not api_key:
        console.print("❌ Missing API key", style="red")
        raise click.Abort()

    if not base_url:
        console.print("❌ Missing base URL", style="red")
        raise click.Abort()

    console.print(f"📝 Image model: [green]{image_model}[/green]")
    if text_model:
        console.print(f"🧠 Text model: [blue]{text_model}[/blue]")

    # Validate arguments
    if not text and not post_file:
        console.print("❌ Must provide either --text or a post file", style="red")
        raise click.Abort()

    if post_file and not text_model:
        console.print("❌ Must provide --text-model when using post file", style="red")
        raise click.Abort()

    # Parse the post file if provided
    title = None
    categories = []
    tags = []

    if post_file:
        console.print(f"🎨 Generating featured image for: [bold]{post_file.name}[/bold]")
        try:
            with open(post_file, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)

            title = post.metadata.get('title', 'Untitled')
            categories = post.metadata.get('categories', [])
            tags = post.metadata.get('tags', [])
            content_snippet = post.content[:500] + "..." if len(post.content) > 500 else post.content

            console.print(f"📖 Post: [bold]{title}[/bold]")
            if categories:
                console.print(f"📂 Categories: {', '.join(categories)}")
            if tags:
                console.print(f"🏷️  Tags: {', '.join(tags[:5])}{f' (+{len(tags)-5} more)' if len(tags) > 5 else ''}")

        except Exception as e:
            console.print(f"❌ Error reading post file: {e}", style="red")
            raise click.Abort()
    else:
        console.print("🎨 Generating standalone image")

    # Generate or use provided text prompt
    if text:
        prompt = text
        console.print(f"✏️  Using provided text: [cyan]{prompt}[/cyan]")
    else:
        # Use text model to analyze post content and create rich image prompt
        console.print(f"🧠 Analyzing post with {text_model}...")

        analysis_prompt = f"""Analyze this blog post and create a detailed image generation prompt for a featured image.

BLOG POST:
Title: {title}
Categories: {', '.join(categories)}
Tags: {', '.join(tags)}
Content: {post.content}

STYLE REQUIREMENTS:
- Dark indigo/purple color scheme (primary brand colors)
- Cyberpunk or solarpunk aesthetic elements
- Modern, minimalist tech illustration style
- Professional blog header quality
- Rectangular format optimized for blog headers

TASK:
Extract the key technical concepts, themes, and memorable points from this post. Create a compelling image generation prompt that:
1. Captures the essence of the post's main topics
2. Incorporates relevant technical/visual metaphors
3. Applies the dark indigo/purple brand aesthetic
4. Adds appropriate cyberpunk/solarpunk thematic elements
5. Results in a striking, professional featured image

Return ONLY the image generation prompt, no additional text."""

        try:
            with console.status("[bold blue]Analyzing content...", spinner="dots"):
                # Use direct requests call to gateway since litellm completion()
                # has provider detection issues with custom model names
                response = session.post(
                    f"{base_url}/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": text_model,
                        "messages": [{"role": "user", "content": analysis_prompt}],
                        "max_tokens": 500,
                        "temperature": 0.7
                    }
                )

                response.raise_for_status()
                response_data = response.json()

                prompt = response_data["choices"][0]["message"]["content"].strip()
                console.print(f"✨ AI-generated prompt: [cyan]{prompt}[/cyan]")

            if verbose:
                console.print(f"Text model response: {response_data}")

        except Exception as e:
            console.print(f"❌ Text analysis failed: {e}", style="red")
            if verbose:
                import traceback
                console.print(traceback.format_exc())
            raise click.Abort()

    # Confirm before generating
    if not yes and not Confirm.ask("🎯 Generate image with this prompt?"):
        console.print("Cancelled")
        return

    # Generate image
    try:
        console.print(f"🎨 Generating image with {image_model}...")

        # For DALL-E models, use compatible size then resize
        if 'dall-e' in image_model.lower():
            # Choose best DALL-E size based on target dimensions
            target_width, target_height = map(int, size.split('x'))
            if target_width > target_height:
                dalle_size = "1792x1024"  # Landscape
            elif target_height > target_width:
                dalle_size = "1024x1792"  # Portrait
            else:
                dalle_size = "1024x1024"  # Square
            console.print(f"📏 Using DALL-E size {dalle_size}, will resize to {size}")
        else:
            dalle_size = size

        with console.status("[bold green]Generating image...", spinner="dots"):
            response = image_generation(
                model=image_model,
                prompt=prompt,
                api_key=api_key,
                api_base=base_url,
                size=dalle_size,
                quality="standard"
            )

        if verbose:
            console.print("Response:", response)

        # Extract image URL
        if hasattr(response, 'data') and response.data:
            image_url = response.data[0].url if hasattr(response.data[0], 'url') else str(response.data[0])
            console.print(f"✅ Generated: [green]{image_url}[/green]")

            # Download and save image
            try:
                with console.status("[bold green]Downloading image...", spinner="dots"):
                    img_response = session.get(image_url, timeout=60)
                    img_response.raise_for_status()

                # Parse output path and create directory if needed
                output_path = Path(output)
                output_path.parent.mkdir(parents=True, exist_ok=True)

                # Resize image to requested dimensions first
                target_width, target_height = map(int, size.split('x'))
                with console.status("[bold blue]Resizing image...", spinner="dots"):
                    pil_image = Image.open(BytesIO(img_response.content))
                    resized_image = pil_image.resize((target_width, target_height), Image.Resampling.LANCZOS)

                    # Convert back to bytes with quantization for smaller file size
                    output_buffer = BytesIO()

                    # Reduce colors to 256 for smaller PNG files (effective for AI-generated images)
                    if resized_image.mode in ('RGB', 'RGBA'):
                        try:
                            quantized = resized_image.quantize(colors=256, method=Image.Quantize.MEDIANCUT)
                            # Convert back to RGB to avoid palette mode issues with further processing
                            quantized = quantized.convert('RGB')
                            quantized.save(output_buffer, format='PNG', optimize=True, compress_level=9)
                        except:
                            # Fallback to original if quantization fails
                            resized_image.save(output_buffer, format='PNG', optimize=True, compress_level=9)
                    else:
                        resized_image.save(output_buffer, format='PNG', optimize=True, compress_level=9)

                    resized_image_bytes = output_buffer.getvalue()

                # Add watermark to resized image
                with console.status("[bold blue]Adding watermark...", spinner="dots"):
                    final_image_bytes = add_watermark(resized_image_bytes, url_text=url)

                # Save final image
                with open(output_path, 'wb') as f:
                    f.write(final_image_bytes)

                console.print(f"💾 Saved: [green]{output_path}[/green]")

                # Update post front matter if post file provided
                if post_file:
                    try:
                        # Read current post
                        with open(post_file, 'r', encoding='utf-8') as f:
                            post = frontmatter.load(f)

                        # Add cover block - strip static/ prefix if present for relative path
                        relative_image_path = str(output_path).replace('static/', '') if str(output_path).startswith('static/') else str(output_path)
                        post.metadata['cover'] = {
                            'image': relative_image_path,
                            'alt': f"AI-generated featured image for {title}",
                            'caption': "Generated with AI based on post content"
                        }

                        # Write back to file
                        with open(post_file, 'w', encoding='utf-8') as f:
                            f.write(frontmatter.dumps(post))

                        console.print(f"📝 Updated front matter in [green]{post_file}[/green]")

                    except Exception as e:
                        console.print(f"⚠️  Image saved but failed to update front matter: {e}", style="yellow")

                console.print("✅ [bold green]Complete![/bold green]")

            except Exception as e:
                console.print(f"❌ Failed to download/save image: {e}", style="red")
                raise click.Abort()

        else:
            console.print(f"❌ Unexpected response format: {response}", style="red")

    except Exception as e:
        console.print(f"❌ Image generation failed: {e}", style="red")
        if verbose:
            import traceback
            console.print(traceback.format_exc())
        raise click.Abort()


@cli.command("add-featured-image-to-post")
@click.argument('post-file', type=click.Path(exists=True, path_type=Path))
@click.option('--override', is_flag=True, help='Replace existing featured image if present')
@click.option('--api-key', help='Override API key (defaults to LITELLM_PROXY_API_KEY env var)')
@click.option('--base-url', help='Override base URL (defaults to LITELLM_PROXY_URL env var)')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
@click.option('--yes', '-y', is_flag=True, help='Skip confirmation prompts')
def add_featured_image_to_post(post_file, override, api_key, base_url, verbose, yes):
    """Generate and add a featured image to a specific blog post.

    This command analyzes a blog post and generates a custom featured image,
    then updates the post's frontmatter. It reuses the existing 'generate'
    command functionality.
    """

    console.print(f"🎨 Processing post: [bold]{post_file.name}[/bold]")

    # Read and parse the post
    try:
        with open(post_file, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

        title = post.metadata.get('title', 'Untitled')
        existing_cover = post.metadata.get('cover')

        console.print(f"📖 Post: [bold]{title}[/bold]")

    except Exception as e:
        console.print(f"❌ Error reading post file: {e}", style="red")
        raise click.Abort()

    # Check for existing featured image in frontmatter
    if existing_cover and not override:
        console.print("⏭️  Post already has a featured image. Use --override to replace.", style="yellow")
        return

    # Generate output filename from post file
    post_stem = post_file.stem
    # Remove date prefix if present (YYYY-MM-DD-)
    if len(post_stem) > 10 and post_stem[4] == '-' and post_stem[7] == '-' and post_stem[10] == '-':
        slug = post_stem[11:]  # Remove YYYY-MM-DD- prefix
    else:
        slug = post_stem

    output_filename = f"{slug}.generated.png"
    output_path = f"static/img/{output_filename}"

    # Check if image file already exists
    if Path(output_path).exists() and not override:
        console.print("⏭️  Image file already exists. Use --override to replace.", style="yellow")
        # Still update frontmatter if it's missing
        if not existing_cover:
            console.print("📝 Adding missing frontmatter reference...")
            post.metadata['cover'] = {'image': f"img/{output_filename}"}
            with open(post_file, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))
            console.print("✅ Frontmatter updated")
        return

    console.print(f"🎯 Will generate: [green]{output_path}[/green]")

    if not yes and not Confirm.ask("🚀 Generate featured image for this post?"):
        console.print("Cancelled")
        return

    # Generate post URL for watermark
    date_match = re.match(r'(\d{4})-(\d{2})-(\d{2})', post_file.stem)
    if date_match:
        year, month, day = date_match.groups()
        post_url = f"andrewbolster.info/{year}/{month}/{slug}.html"
    else:
        post_url = f"andrewbolster.info/{slug}.html"

    # Use existing generate command by invoking it directly
    from click.testing import CliRunner

    generate_args = [
        'generate',
        str(post_file),
        '--image-model', 'dall-e-3',
        '--text-model', 'claude-sonnet-4',
        '--output', output_path,
        '--size', '860x530',
        '--url', post_url
    ]

    # Pass through optional arguments
    if api_key:
        generate_args.extend(['--api-key', api_key])
    if base_url:
        generate_args.extend(['--base-url', base_url])
    if verbose:
        generate_args.append('--verbose')
    if yes:
        generate_args.append('--yes')

    try:
        # Run the generate command
        runner = CliRunner()
        result = runner.invoke(cli, generate_args, catch_exceptions=False)

        if result.exit_code != 0:
            console.print("❌ Image generation failed", style="red")
            raise click.Abort()

        # Update frontmatter if the image was successfully generated
        if Path(output_path).exists():
            console.print("📝 Updating post frontmatter...")
            post.metadata['cover'] = {'image': f"img/{output_filename}"}

            with open(post_file, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))

            console.print("✅ Frontmatter updated")
        else:
            console.print("❌ Image file was not created", style="red")
            raise click.Abort()

    except Exception as e:
        console.print(f"❌ Failed to generate image: {e}", style="red")
        if verbose:
            import traceback
            console.print(traceback.format_exc())
        raise click.Abort()


@cli.command("add-featured-images")
@click.option('--dry-run', is_flag=True, help='Show what would be changed without making changes')
def add_featured_images(dry_run):
    """Add featured images from first image in post content."""

    def find_first_image_in_content(content):
        """Find the first image reference in markdown content."""
        # Match both markdown image syntax: ![alt](url) and [![alt](url)](link)
        image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        match = re.search(image_pattern, content)
        if match:
            alt_text = match.group(1)
            image_url = match.group(2)
            return image_url, alt_text, match.start()
        return None, None, None

    def is_image_in_valid_position(content, image_position):
        """Check if image is first element or directly after first paragraph."""
        if image_position is None:
            return False

        # Get content before the image
        content_before = content[:image_position].strip()

        # If no content before, it's the first element
        if not content_before:
            return True

        # Check if it's directly after the first paragraph
        # Split by double newlines (paragraph breaks)
        paragraphs = content_before.split('\n\n')

        # If there's only one paragraph before the image, it's valid
        if len(paragraphs) == 1:
            return True

        return False

    posts_dir = Path("content/posts")
    if not posts_dir.exists():
        console.print("❌ Posts directory not found: content/posts")
        raise click.Abort()

    # Get all markdown files
    md_files = list(posts_dir.glob('*.md')) + list(posts_dir.glob('*.markdown'))

    console.print(f"🔍 Found {len(md_files)} blog posts to analyze...")

    if dry_run:
        console.print("🧪 [yellow]DRY RUN MODE - No changes will be made[/yellow]")

    processed_count = 0
    updated_count = 0

    for post_file in sorted(md_files):
        try:
            with open(post_file, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)

            processed_count += 1

            # Skip if already has a cover image
            if 'cover' in post.metadata:
                console.print(f"⏭️  [dim]{post_file.name}[/dim] - Already has featured image")
                continue

            # Find first image in content
            image_url, alt_text, image_position = find_first_image_in_content(post.content)

            if not image_url:
                console.print(f"🚫 [dim]{post_file.name}[/dim] - No images found")
                continue

            # Check if image is in valid position
            if not is_image_in_valid_position(post.content, image_position):
                console.print(f"❌ [yellow]{post_file.name}[/yellow] - Image not in first element or after first paragraph")
                continue

            # Clean up image URL (remove leading slash if present)
            clean_image_url = image_url.lstrip('/')

            if dry_run:
                console.print(f"📋 [green]{post_file.name}[/green] - Would add featured image: [cyan]{clean_image_url}[/cyan]")
            else:
                # Add featured image to front matter
                post.metadata['cover'] = {
                    'image': clean_image_url
                }

                # Write back to file
                with open(post_file, 'w', encoding='utf-8') as f:
                    f.write(frontmatter.dumps(post))

                console.print(f"✅ [green]{post_file.name}[/green] - Added featured image: [cyan]{clean_image_url}[/cyan]")

            updated_count += 1

        except Exception as e:
            console.print(f"❌ [red]Error processing {post_file.name}:[/red] {e}")

    console.print(f"\n📊 [bold]Summary:[/bold]")
    console.print(f"  • Processed: {processed_count} posts")
    console.print(f"  • {'Would update' if dry_run else 'Updated'}: {updated_count} posts")
    console.print(f"  • Skipped: {processed_count - updated_count} posts")

    if dry_run:
        console.print(f"\n💡 Run without --dry-run to make changes")


if __name__ == "__main__":
    cli()
