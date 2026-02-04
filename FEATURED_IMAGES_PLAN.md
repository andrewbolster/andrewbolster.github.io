# AI-Generated Featured Images for Hugo Blog

## Project Overview

Implement a **local authoring workflow** to generate featured images for blog posts using AI image generation, integrated with Hugo's PaperMod theme featured image capabilities. This approach gives full creative control while streamlining the image creation process.

## Key Findings

### Hugo/PaperMod Featured Image Support
- ✅ PaperMod fully supports featured images via `cover:` front matter
- ✅ Images display in post lists, single posts, and social media cards
- ✅ Existing `/static/img/` structure is compatible
- ✅ Supports responsive images and accessibility features

### AI Image Generation Options
- ❌ GitHub Copilot Agent: No image generation (vision only)
- ⚠️ Your Core LLM Gateway: Only 5 text models, no image generation
- ✅ **Your Labs LLM Gateway**: **40+ image generation models available!**
  - DALL-E 3, GPT Image 1
  - Amazon Titan (multiple versions)
  - Google Gemini/Imagen (15+ variants)
  - Stability AI Stable Diffusion (20+ variants with different sizes/steps)
- ✅ Direct APIs: Still available as fallback
- ✅ Multiple providers: Bedrock, Vertex AI, direct OpenAI

**Key Finding**: The **labs gateway has extensive image generation support** with models from all major providers!

## Proposed Implementation: Local Authoring Workflow

### Phase 1: Local Tooling Setup
**Goal**: Create a local script for on-demand image generation during writing/editing

**Components**:
1. **Local CLI Script**: `./scripts/generate-featured-image.js`
2. **Interactive Prompts**: Author refines prompts before generation
3. **Hugo Integration**: Automatically updates post front matter
4. **Preview & Iterate**: Generate multiple options, pick the best

**Usage**: `npm run featured-image content/posts/my-new-post.md`

### Phase 2: Batch Processing Tool
**Goal**: Process existing posts selectively with author oversight

**Components**:
1. **Bulk Processing Mode**: Process multiple posts with confirmation prompts
2. **Smart Filtering**: Skip posts with existing images or certain categories
3. **Manual Review**: Preview before committing to post
4. **Regeneration**: Easy re-run with different prompts

**Usage**: `npm run featured-images:batch --filter="tag:AI" --year="2024"`

### Phase 3: Enhanced Creative Control
**Goal**: Advanced features for consistent brand and quality

**Components**:
1. **Style Templates**: Predefined prompts for different post categories
2. **Brand Consistency**: Custom style descriptors for your blog's aesthetic
3. **Image Variants**: Generate multiple options per post
4. **Local Stable Diffusion**: Option for full creative control without API costs

## Technical Architecture

### Local CLI Tool Structure
```bash
# Management script with click commands
./scripts/manage.py test-image-generation                          # Test available models
./scripts/manage.py generate --model <model> <post-file>           # Generate for single post
./scripts/manage.py generate --model <model> --batch [options]    # Batch process multiple posts
./scripts/manage.py preview <image>                                # Preview generated images
```

### Core Script Design
```python
#!/usr/bin/env python3
# scripts/generate_featured_image.py

import os
import yaml
import click
from pathlib import Path
from litellm import image_generation
from PIL import Image
import frontmatter
from rich.console import Console
from rich.prompt import Prompt, Confirm

class FeaturedImageGenerator:
    def __init__(self):
        self.console = Console()
        self.style_templates = self.load_style_templates()

        # litellm proxy configuration (using existing environment)
        self.api_key = os.getenv('LITELLM_PROXY_API_KEY')
        self.api_base = os.getenv('LITELLM_PROXY_URL')  # LLM gateway

    def generate_for_post(self, post_path):
        """Generate featured image for a single post with interactive prompts"""
        # 1. Parse post front matter and content
        # 2. Suggest prompt based on title/category/content
        # 3. Interactive prompt refinement with user
        # 4. Generate image with litellm
        # 5. Preview and confirm with user
        # 6. Save image and update front matter
        pass

    def batch_process(self, filters):
        """Process multiple posts with confirmation prompts"""
        # 1. Find posts matching criteria
        # 2. For each post, run interactive generation
        # 3. Allow skip/regenerate per post
        pass

    def generate_image(self, prompt, model="dall-e-3"):
        """Generate image using litellm"""
        response = image_generation(
            model=model,
            prompt=prompt,
            api_key=self.api_key,
            api_base=self.api_base,
            size="1024x1024",
            quality="standard",
            n=1
        )
        return response
```

### Interactive Workflow Example
```bash
$ python scripts/generate_featured_image.py content/posts/2024-02-19-ai-security.md

📝 Analyzing post: "Generative AI: Impact on Software Development and Security"
🎨 Suggested prompt: "Modern cybersecurity illustration with AI elements, purple and indigo theme, professional tech style"

? Refine the prompt? (Y/n) y
? Enter custom prompt: Modern visualization of AI protecting software code, purple gradient, minimalist tech illustration

🎨 Generating image with dall-e-3... (30s)
✅ Generated: ai-security-impact-1024x1024.jpg

? Preview image? (Y/n) y
[Opens image in system viewer]

? Use this image? (Y/n) y
✅ Saved to: static/img/generated/2024/ai-security-impact.jpg
✅ Updated front matter with cover block

Dependencies installed:
- litellm (unified LLM API)
- click (CLI framework)
- pyyaml (YAML parsing)
- python-frontmatter (front matter parsing)
- pillow (image processing)
- rich (beautiful terminal output)
```

### LiteLLM Proxy Configuration

Your existing environment is already configured for litellm via your LLM gateway:

```bash
# Already configured in your environment:
LITELLM_PROXY_API_KEY=sk-xxx...
LITELLM_PROXY_URL=https://your-llm-gateway.com

# Script will use these automatically - no additional setup needed!
```

This means the script will work through your LLM gateway, which should provide:
- Centralized billing and cost control
- Potentially better rate limits
- Compliance with AI usage policies

### Front Matter Template
```yaml
cover:
  image: "img/generated/2024/ai-generated-post-title.jpg"
  alt: "AI-generated featured image for [post title]"
  caption: "Generated with DALL-E based on post content"
  relative: false
  hidden: false
```

## Content-Aware Prompt Generation

### Prompt Templates by Category
- **AI/Technology**: "Modern tech illustration showing [topic], clean minimal design, purple and indigo color scheme"
- **Data Science**: "Data visualization concept for [topic], charts and analytics theme, professional style"
- **Northern Ireland**: "Belfast/Northern Ireland themed illustration for [topic], local landmarks, cultural elements"
- **Academia**: "Academic research illustration for [topic], scholarly design, clean typography"

### Smart Prompt Building
1. **Base Context**: "Professional blog featured image for technical blog post"
2. **Topic Integration**: Extract key concepts from title and first paragraph
3. **Style Consistency**: Maintain brand colors (indigo/purple theme)
4. **Accessibility**: Generate meaningful alt text from prompt

## Quality Control & Review Process

### Automated Checks
- Image resolution (minimum 1200x630)
- File size optimization (<500KB)
- Alt text generation
- Brand color compliance

### Manual Review Workflow
1. **PR Creation**: Generated images create PR instead of direct commit
2. **Review Interface**: GitHub PR with image previews
3. **Approval Process**: Manual approve/reject/regenerate options
4. **Override Capability**: Manual image replacement for important posts

## Cost Management & Optimization

### Budget Controls
- **Daily Limits**: Maximum API calls per day
- **Approval Required**: Bulk operations need manual trigger
- **Cost Tracking**: Log generation costs per batch

### Efficiency Improvements
- **Prompt Caching**: Store successful prompts for reuse
- **Batch API Calls**: Group multiple generations
- **Quality Tiers**: Different resolution/quality for different post types

## Rollout Strategy

### Week 1: Setup & Testing
- [ ] Create GitHub Actions workflow
- [ ] Test image generation on 5 recent posts
- [ ] Verify Hugo integration works correctly
- [ ] Set up monitoring and cost tracking

### Week 2: Limited Deployment
- [ ] Enable automatic generation for new posts
- [ ] Process 20 high-traffic older posts manually
- [ ] Collect feedback on image quality and relevance
- [ ] Refine prompts and styling

### Week 3: Bulk Processing
- [ ] Run bulk generation on all ~400 existing posts
- [ ] Create PR for manual review
- [ ] Implement any needed quality improvements
- [ ] Full deployment

## Success Metrics

### Technical Metrics
- Image generation success rate (target: >95%)
- Average generation time (target: <30 seconds)
- File size optimization (target: <500KB avg)
- Cost per image (target: <$0.04)

### Content Quality Metrics
- Visual consistency with blog theme
- Relevance to post content
- Accessibility compliance
- Social media engagement improvement

## Risk Mitigation

### Content Policy Compliance
- Review OpenAI content policies
- Implement content moderation
- Manual review for sensitive topics

### Technical Risks
- API rate limits and downtime
- Image quality inconsistency
- Storage and bandwidth costs
- Git repository size growth

### Backup Plans
- Manual image override system
- Alternative API providers (Stability AI)
- Self-hosted fallback option
- Rollback capability for bad generations

## Next Steps

1. **Prototype Development**: Build basic image generation script
2. **Hugo Integration Test**: Verify featured images work correctly
3. **GitHub Actions Setup**: Create automated workflow
4. **Pilot Program**: Test on 10 posts across different categories
5. **Quality Assessment**: Review results and refine approach
6. **Full Rollout**: Deploy to all posts with monitoring

---

*This plan balances automation, quality control, and cost management to deliver professional featured images for the entire blog while maintaining editorial oversight and brand consistency.*
