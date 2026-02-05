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

def generate_aliases(file_path):
    """Generate both clean URL and .html aliases based on filename and permalink structure."""
    filename = file_path.stem
    # Extract date and title from filename
    match = re.match(r'(\d{4})-(\d{2})-(\d{2})-(.+)', filename)
    if match:
        year, month, day, title = match.groups()
        clean_alias = f"/{year}/{month}/{title}/"
        html_alias = f"/{year}/{month}/{title}.html"
        return clean_alias, html_alias
    return None, None

def update_post_with_aliases(file_path):
    """Add both clean URL and .html aliases to a post if they don't already exist."""
    frontmatter, content = extract_frontmatter_and_content(file_path)
    if frontmatter is None:
        print(f"❌ Could not parse frontmatter for {file_path}")
        return False

    # Generate both aliases
    clean_alias, html_alias = generate_aliases(file_path)
    if not clean_alias or not html_alias:
        print(f"❌ Could not generate aliases for {file_path}")
        return False

    # Check if aliases already exist
    aliases = frontmatter.get('aliases', [])
    missing_aliases = []

    if clean_alias not in aliases:
        missing_aliases.append(clean_alias)
    if html_alias not in aliases:
        missing_aliases.append(html_alias)

    if not missing_aliases:
        print(f"✅ {file_path.name} already has all required aliases")
        return False

    # Add missing aliases
    aliases.extend(missing_aliases)
    frontmatter['aliases'] = aliases

    # Write the updated file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('---\n')
        yaml.dump(frontmatter, f, default_flow_style=False, allow_unicode=True)
        f.write('---\n')
        f.write(content)

    alias_types = []
    if clean_alias in missing_aliases:
        alias_types.append("clean URL")
    if html_alias in missing_aliases:
        alias_types.append(".html")

    print(f"✅ Added {' and '.join(alias_types)} alias(es) to {file_path.name}")
    return True

def main():
    """Process all blog posts and add both clean URL and .html aliases."""
    posts_dir = Path("content/posts")
    if not posts_dir.exists():
        print("❌ content/posts directory not found")
        return

    post_files = list(posts_dir.glob("*.md"))
    print(f"📝 Found {len(post_files)} posts to process")

    updated_count = 0
    for post_file in sorted(post_files):
        if update_post_with_aliases(post_file):
            updated_count += 1

    print(f"\n✅ Updated {updated_count} posts with URL aliases")

if __name__ == "__main__":
    main()
