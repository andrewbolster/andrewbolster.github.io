#!/usr/bin/env uv run
# /// script
# dependencies = [
#   "pyyaml",
# ]
# ///
"""
Add both clean URL and .html aliases to all blog posts for universal URL support
"""
import os
import re
import yaml
from pathlib import Path

def extract_frontmatter_and_content(file_path):
    """Extract YAML frontmatter and content from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match YAML frontmatter between --- delimiters
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if not frontmatter_match:
        return None, content

    frontmatter_text = frontmatter_match.group(1)
    body_content = frontmatter_match.group(2)

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        return frontmatter, body_content
    except yaml.YAMLError:
        return None, content

def generate_html_alias(file_path):
    """Generate .html alias based on filename and permalink structure."""
    filename = file_path.stem
    # Extract date and title from filename
    match = re.match(r'(\d{4})-(\d{2})-(\d{2})-(.+)', filename)
    if match:
        year, month, day, title = match.groups()
        # Hugo permalink is "/:year/:month/:title" (no trailing slash)
        # We only need .html aliases since clean URLs are the primary format
        return f"/{year}/{month}/{title}.html"
    return None

def update_post_with_html_alias(file_path):
    """Add .html alias to a post if it doesn't already exist."""
    frontmatter, content = extract_frontmatter_and_content(file_path)
    if frontmatter is None:
        print(f"❌ Could not parse frontmatter for {file_path}")
        return False

    html_alias = generate_html_alias(file_path)
    if not html_alias:
        print(f"❌ Could not generate alias for {file_path}")
        return False

    # Check if alias already exists
    aliases = frontmatter.get('aliases', [])

    if html_alias not in aliases:
        aliases.append(html_alias)
        frontmatter['aliases'] = aliases

        # Write the updated file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('---\n')
            yaml.dump(frontmatter, f, default_flow_style=False, allow_unicode=True)
            f.write('---\n')
            f.write(content)

        print(f"✅ Added .html alias to {file_path.name}")
        return True
    else:
        print(f"✅ {file_path.name} already has .html alias")
        return False

def main():
    """Process all blog posts and add .html aliases."""
    posts_dir = Path("content/posts")
    if not posts_dir.exists():
        print("❌ content/posts directory not found")
        return

    post_files = list(posts_dir.glob("*.md"))
    print(f"📝 Found {len(post_files)} posts to process")

    updated_count = 0
    for post_file in sorted(post_files):
        if update_post_with_html_alias(post_file):
            updated_count += 1

    print(f"\n✅ Updated {updated_count} posts with .html aliases")

if __name__ == "__main__":
    main()
