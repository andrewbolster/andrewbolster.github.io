#!/usr/bin/env python3
"""
Analyze internal links in Hugo blog migration from Jekyll.
Systematically check for broken internal links in markdown files.
"""

import os
import re
import glob
from pathlib import Path
from collections import defaultdict
from urllib.parse import urlparse

def extract_internal_links(content, filepath):
    """Extract all internal links from markdown content."""
    links = []

    # Pattern to match markdown links [text](url)
    link_pattern = r'\[([^\]]*)\]\(([^)]+)\)'

    for match in re.finditer(link_pattern, content, re.MULTILINE):
        text = match.group(1)
        url = match.group(2)
        line_num = content[:match.start()].count('\n') + 1

        # Check if it's an internal link (starts with / or relative path)
        if url.startswith('/') or (not url.startswith('http') and not url.startswith('mailto:') and not url.startswith('#')):
            links.append({
                'text': text,
                'url': url,
                'line': line_num,
                'file': filepath,
                'match_start': match.start(),
                'match_end': match.end()
            })

    # Also check for image references ![alt](src)
    img_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'

    for match in re.finditer(img_pattern, content, re.MULTILINE):
        alt = match.group(1)
        src = match.group(2)
        line_num = content[:match.start()].count('\n') + 1

        # Check if it's an internal image (starts with / or relative path)
        if src.startswith('/') or (not src.startswith('http') and not src.startswith('mailto:') and not src.startswith('#')):
            links.append({
                'text': f'![{alt}]',
                'url': src,
                'line': line_num,
                'file': filepath,
                'match_start': match.start(),
                'match_end': match.end(),
                'type': 'image'
            })

    return links

def check_jekyll_patterns(content, filepath):
    """Check for Jekyll-specific patterns that may not work in Hugo."""
    issues = []

    # Check for {{ BASE_PATH }} template variables
    base_path_pattern = r'\{\{\s*BASE_PATH\s*\}\}'
    for match in re.finditer(base_path_pattern, content):
        line_num = content[:match.start()].count('\n') + 1
        issues.append({
            'type': 'jekyll_template',
            'pattern': '{{ BASE_PATH }}',
            'line': line_num,
            'file': filepath,
            'description': 'Jekyll template variable that needs Hugo equivalent'
        })

    # Check for .html extensions in internal links
    html_link_pattern = r'\[([^\]]*)\]\((/[^)]*\.html)\)'
    for match in re.finditer(html_link_pattern, content):
        line_num = content[:match.start()].count('\n') + 1
        issues.append({
            'type': 'html_extension',
            'pattern': match.group(2),
            'line': line_num,
            'file': filepath,
            'description': 'Link to .html file may need adjustment for Hugo'
        })

    return issues

def verify_link_target(url, site_root):
    """Verify if the target of an internal link exists."""
    if url.startswith('/'):
        # Absolute internal link
        # Try different possible locations
        candidates = [
            os.path.join(site_root, 'static', url.lstrip('/')),
            os.path.join(site_root, 'content', url.lstrip('/')),
            os.path.join(site_root, url.lstrip('/'))
        ]

        # For posts, check if it matches a post pattern
        if re.match(r'/\d{4}/\d{2}/.*', url):
            # This looks like a Jekyll post URL pattern
            # Try to find matching post file
            year_month = re.match(r'/(\d{4})/(\d{2})/', url)
            if year_month:
                year = year_month.group(1)
                month = year_month.group(2)
                slug = url.split('/')[-1].rstrip('.html')

                # Look for post files that match
                post_pattern = os.path.join(site_root, 'content/posts', f"{year}-{month}-*{slug}*")
                matches = glob.glob(post_pattern)
                if matches:
                    return True, f"Found matching post: {matches[0]}"

        for candidate in candidates:
            if os.path.exists(candidate):
                return True, f"Found at: {candidate}"

        return False, f"Not found. Checked: {candidates}"

    return True, "Relative link - not checked"

def analyze_posts(posts_dir, site_root):
    """Analyze all posts for internal links."""
    results = {
        'internal_links': [],
        'jekyll_issues': [],
        'broken_links': [],
        'stats': defaultdict(int)
    }

    # Find all markdown files
    post_files = glob.glob(os.path.join(posts_dir, '*.md')) + \
                 glob.glob(os.path.join(posts_dir, '*.markdown'))

    print(f"Analyzing {len(post_files)} post files...")

    for filepath in post_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract internal links
            links = extract_internal_links(content, filepath)
            results['internal_links'].extend(links)
            results['stats']['total_files'] += 1
            results['stats']['total_links'] += len(links)

            # Check Jekyll patterns
            issues = check_jekyll_patterns(content, filepath)
            results['jekyll_issues'].extend(issues)

            # Verify link targets
            for link in links:
                exists, details = verify_link_target(link['url'], site_root)
                if not exists:
                    results['broken_links'].append({
                        **link,
                        'reason': details
                    })

        except Exception as e:
            print(f"Error processing {filepath}: {e}")

    return results

def generate_report(results):
    """Generate a comprehensive report of findings."""
    report = []

    report.append("# Internal Links Analysis Report")
    report.append("=" * 50)
    report.append("")

    # Stats
    report.append("## Summary Statistics")
    report.append(f"- Total files analyzed: {results['stats']['total_files']}")
    report.append(f"- Total internal links found: {results['stats']['total_links']}")
    report.append(f"- Broken links: {len(results['broken_links'])}")
    report.append(f"- Jekyll-specific issues: {len(results['jekyll_issues'])}")
    report.append("")

    # Jekyll Issues
    if results['jekyll_issues']:
        report.append("## Jekyll-Specific Issues")
        report.append("-" * 30)

        by_type = defaultdict(list)
        for issue in results['jekyll_issues']:
            by_type[issue['type']].append(issue)

        for issue_type, issues in by_type.items():
            report.append(f"\n### {issue_type.replace('_', ' ').title()}")
            report.append(f"Found {len(issues)} instances:")
            for issue in issues[:10]:  # Show first 10
                rel_path = os.path.relpath(issue['file'])
                report.append(f"- {rel_path}:{issue['line']} - {issue['pattern']}")
            if len(issues) > 10:
                report.append(f"... and {len(issues) - 10} more")

    # Broken Links
    if results['broken_links']:
        report.append("\n## Broken Internal Links")
        report.append("-" * 30)

        by_pattern = defaultdict(list)
        for link in results['broken_links']:
            # Group by URL pattern
            url = link['url']
            if url.startswith('/img/'):
                pattern = 'Images'
            elif url.startswith('/uploads/'):
                pattern = 'Uploads'
            elif url.startswith('/notebooks/'):
                pattern = 'Notebooks'
            elif re.match(r'/\d{4}/', url):
                pattern = 'Post URLs'
            else:
                pattern = 'Other'

            by_pattern[pattern].append(link)

        for pattern, links in by_pattern.items():
            report.append(f"\n### {pattern}")
            report.append(f"Found {len(links)} broken links:")
            for link in links[:5]:  # Show first 5 per category
                rel_path = os.path.relpath(link['file'])
                report.append(f"- {rel_path}:{link['line']} -> {link['url']}")
                report.append(f"  Reason: {link['reason']}")
            if len(links) > 5:
                report.append(f"... and {len(links) - 5} more")

    # Recommendations
    report.append("\n## Recommendations")
    report.append("-" * 30)

    if any(issue['type'] == 'jekyll_template' for issue in results['jekyll_issues']):
        report.append("1. **Jekyll Template Variables**: Replace {{ BASE_PATH }} with Hugo equivalent")
        report.append("   - Hugo uses {{ .Site.BaseURL }} or relative URLs")

    if any(issue['type'] == 'html_extension' for issue in results['jekyll_issues']):
        report.append("2. **HTML Extensions**: Remove .html extensions from internal post links")
        report.append("   - Hugo uses clean URLs by default")

    if any(link['url'].startswith('/img/') for link in results['broken_links']):
        report.append("3. **Image Links**: Verify image files exist in static/img/")
        report.append("   - Check for renamed or moved image files")

    if any(re.match(r'/\d{4}/', link['url']) for link in results['broken_links']):
        report.append("4. **Post URLs**: Update Jekyll-style post URLs to Hugo format")
        report.append("   - Consider using post aliases or redirects")

    return "\n".join(report)

def main():
    # Site structure
    site_root = '/Users/bolster/src/andrewbolster.github.io'
    posts_dir = os.path.join(site_root, 'content/posts')

    print("Starting internal links analysis...")

    # Analyze posts
    results = analyze_posts(posts_dir, site_root)

    # Generate report
    report = generate_report(results)

    # Write report to file
    report_file = os.path.join(site_root, 'internal_links_analysis.md')
    with open(report_file, 'w') as f:
        f.write(report)

    print(f"Analysis complete. Report written to: {report_file}")
    print("\nSummary:")
    print(f"- Files analyzed: {results['stats']['total_files']}")
    print(f"- Internal links: {results['stats']['total_links']}")
    print(f"- Broken links: {len(results['broken_links'])}")
    print(f"- Jekyll issues: {len(results['jekyll_issues'])}")

if __name__ == "__main__":
    main()
