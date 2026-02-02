#!/usr/bin/env python3
"""
Tag Migration Script for Blog Posts
Consolidates 1751 tags down to ~130 based on finalized mappings.
"""

import os
import re
import sys
from pathlib import Path

# Tags to DELETE entirely (no replacement)
TAGS_TO_DELETE = {
    # Years (specific - keep decades like 1960s)
    '1963', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
    '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025',
    # Version numbers (handled separately - mapped to Ubuntu)
    '64-bit',
    # Meaningless/too generic
    'a', 'see', 'doing', 'general', 'info', 'value', 'warn', 'fun', 'funny',
    'experience', 'explore', 'new-content', 'uncategorized', 'index.html',
    'obsoletet', 'assessment_test', 'job_application', 'update', 'system',
    # Very generic tags
    'code', 'software', 'hardware', 'workstation', 'remote', 'video',
    'internet', 'engineering', 'design', 'collaboration', 'blog', 'scripting',
}

# Simple 1:1 mappings (old -> new)
SIMPLE_MAPPINGS = {
    # Typos
    'hackersapce': 'Hackerspace',
    'progamming': 'Programming',

    # Case normalization - ensure consistent capitalization
    'technology': 'Technology',
    'programming': 'Programming',
    'hacking': 'Hacking',
    'social-media': 'Social Media',
    'web-development': 'Web Development',
    'innovation': 'Innovation',
    'finance': 'Finance',
    'privacy': 'Privacy',
    'politics': 'Politics',
    'networking': 'Networking',
    'personal': 'Personal',
    'community': 'Community',
    'marketing': 'Marketing',
    'google': 'Google',

    # Consolidations
    'uni': 'Academia',
    'data-analysis': 'Data Science',
    'software-engineering': 'Software Engineering',
    'hard-drive': 'Storage',
    'lifehacker': 'Productivity',
    'eee': 'EeePC',
    'mybook': 'Storage',
    'unix': 'Linux',
    'career': 'Career',
    'embedded': 'Embedded Systems',
    'instructional': 'Tutorial',

    # Data Management
    'data_management': 'Data Management',

    # Click Router (NS-3)
    'click': 'Click Router',

    # AI & Machine Learning
    'ai': 'AI',
    'ai-bubble': 'AI',
    'ai-ethics': 'AI',
    'ai-hype': 'AI',
    'ai-winter': 'AI',
    'aiops': 'AI',
    'artificial-intelligence': 'AI',
    'bias-in-ai': 'AI',
    'ethical-ai': 'AI',
    'generative-ai': 'AI',
    'robopsychologist': 'AI',

    'machine-learning': 'Machine Learning',
    'ml': 'Machine Learning',
    'mlops': 'Machine Learning',
    'fine-tuning': 'Machine Learning',
    'gans': 'Machine Learning',
    'rlhf': 'Machine Learning',

    'chatgpt': 'LLM',
    'claude': 'LLM',
    'claude-code': 'LLM',
    'deepseek': 'LLM',
    'github-copilot': 'LLM',
    'large-language-model': 'LLM',
    'llm': 'LLM',
    'llms': 'LLM',
    'mcp': 'LLM',
    'model-context-protocol': 'LLM',
    'openai': 'LLM',
    'rag': 'LLM',

    'data-science': 'Data Science',
    'data-scientists': 'Data Science',
    'natural-language-processing': 'NLP',

    # Programming Languages
    'python': 'Python',
    'python3': 'Python',
    'python-3': 'Python',
    'oo-python': 'Python',

    'javascript': 'JavaScript',
    'js': 'JavaScript',
    'node': 'JavaScript',
    'nodejs': 'JavaScript',

    'c': 'C/C++',
    'c++': 'C/C++',
    'cpp': 'C/C++',

    'csharp': 'CSharp',
    'java': 'Java',
    'scala': 'Scala',
    'groovy': 'Groovy',
    'ruby': 'Ruby',
    'perl': 'Perl',
    'perl-scripting': 'Perl',

    'bash': 'Bash',
    'bash-scripting': 'Bash',
    'shell': 'Shell',
    'shell-script': 'Shell',
    'shell-scripting': 'Shell',

    'html': 'HTML',
    'css': 'CSS',
    'php': 'PHP',
    'r-programming': 'R',
    'matlab': 'MATLAB',
    'octave': 'MATLAB',
    'sql': 'SQL',

    # Operating Systems - Ubuntu
    'ubuntu': 'Ubuntu',
    'ubuntu-9.10': 'Ubuntu',
    'ubuntu-10.04': 'Ubuntu',
    'ubuntu-hardy-heron': 'Ubuntu',
    'ubuntu-linux': 'Ubuntu',
    'ubuntu-server': 'Ubuntu',
    'lucid': 'Ubuntu',
    'lucid-lynx': 'Ubuntu',
    'hardy-heron': 'Ubuntu',
    'jaunty': 'Ubuntu',
    '10.04': 'Ubuntu',
    '8.04': 'Ubuntu',
    '8.10': 'Ubuntu',

    # Linux distros
    'linux': 'Linux',
    'linux-distros': 'Linux',
    'linux-servers': 'Linux',
    'debian': 'Debian',
    'fedora': 'Fedora',
    'mint': 'Linux Mint',
    'linux-mint': 'Linux Mint',

    # Windows
    'windows': 'Windows',
    'windows-7': 'Windows',
    'windows-vista': 'Windows',
    'vista': 'Windows',
    'winxp': 'Windows',

    # Android
    'android': 'Android',
    'android-api': 'Android',
    'android-development': 'Android',
    'android-market': 'Android',
    'cyanogenmod': 'Android',

    # Desktop environments
    'gnome': 'Gnome',
    'gnome-shell': 'Gnome',
    'gnome-do': 'Gnome',
    'kde': 'KDE',

    # Community & Location
    'farset': 'Farset Labs',
    'farset-labs': 'Farset Labs',
    'farsetlabs': 'Farset Labs',

    'hackerspace': 'Hackerspace',
    'hackerspaces': 'Hackerspace',

    'belfast': 'Belfast',
    'dublin': 'Dublin',
    'liverpool': 'Liverpool',
    'northern-ireland': 'Northern Ireland',
    'ni': 'Northern Ireland',
    'ulster': 'Northern Ireland',
    'ireland': 'Ireland',
    'uk': 'UK',

    'qub': 'QUB',
    'queens-university-belfast': 'QUB',
    'university-belfast': 'QUB',
    'ecit': 'ECIT',
    'university-of-liverpool': 'University of Liverpool',

    # Academia
    'academic': 'Academia',
    'academic-conferences': 'Academia',
    'academic-references': 'Academia',
    'academic-videos': 'Academia',
    'college': 'Academia',
    'university': 'Academia',

    'phd': 'PhD',
    'phd-research': 'PhD',
    'thesis': 'PhD',
    'thesis-writing': 'PhD',
    'dissertation': 'PhD',
    'viva': 'PhD',

    'research': 'Research',
    'research-methodologies': 'Research',
    'lit-review': 'Research',
    'literature-review': 'Research',

    'trust': 'Trust',
    'trust-management-frameworks': 'Trust',
    'multi-vector-trust-management': 'Trust',

    'robotics': 'Robotics',
    'robots': 'Robotics',
    'rov': 'Robotics',

    'autonomous-systems': 'Autonomous Systems',
    'autonomous-vehicles': 'Autonomous Systems',
    'autonomy': 'Autonomous Systems',
    'collaborative-autonomy': 'Autonomous Systems',
    'unmanned-systems': 'Autonomous Systems',

    # Media & Entertainment
    'film': 'Film',
    'movie-trailer': 'Film',
    'animation': 'Film',
    'trailer': 'Film',
    'star-wars': 'Star Wars',

    'tv': 'TV',
    'iptv': 'TV',
    'doctor-who': 'Doctor Who',

    'music': 'Music',
    'music-video': 'Music',
    'musicians': 'Music',
    'live-performance': 'Music',
    'remix': 'Music',

    'video-games': 'Gaming',
    'videogames': 'Gaming',
    'video-game': 'Gaming',
    'games': 'Gaming',
    'gaming': 'Gaming',
    'steam': 'Gaming',
    'xbox': 'Gaming',
    'portal': 'Gaming',

    'book': 'Books',
    'books': 'Books',
    'kindle': 'Books',
    'ebook-reader': 'Books',
    'science-fiction': 'Science Fiction',

    'podcast': 'Podcasts',
    'podcasts': 'Podcasts',

    'facebook': 'Social Media',
    'twitter': 'Social Media',
    'linkedin': 'Social Media',
    'youtube': 'Social Media',
    'reddit': 'Social Media',

    # Hardware
    'laptop': 'Laptop',
    'laptops': 'Laptop',
    'thinkpad-x61s': 'Laptop',
    'desktop': 'Desktop',
    'pc': 'Desktop',
    'server': 'Server',

    'gpu': 'GPU',
    'graphics-card': 'GPU',
    'nvidia': 'NVIDIA',
    'cuda': 'CUDA',
    'intel': 'Intel',
    'amd': 'AMD',

    'router': 'Router',
    'dd-wrt': 'Router',
    'wrt54g': 'Router',
    'wrt54gl': 'Router',
    'linksys': 'Router',

    'wifi': 'WiFi',
    'wi-fi': 'WiFi',
    'wireless': 'WiFi',

    'usb': 'USB',
    'ssd': 'Storage',
    'hdd': 'Storage',
    'nas': 'Storage',

    '3g': 'Mobile Network',
    '4g': 'Mobile Network',
    'lte': 'Mobile Network',

    # Politics & Society
    'democracy': 'Politics',
    'elections': 'Politics',
    'ni-assembly': 'Politics',
    'dup': 'Politics',

    'banking': 'Finance',
    'economy': 'Finance',
    'economic-development': 'Finance',
    'taxation': 'Finance',
    'investment': 'Finance',
    'algorithmic-trading': 'Finance',

    'covid': 'Health',
    'pandemic': 'Health',
    'lockdown': 'Health',

    'global-warming': 'Environment',
    'climate': 'Environment',

    # Version Control
    'git': 'Git',
    'github': 'GitHub',
    'github-migration': 'GitHub',
    'bitbucket': 'Bitbucket',
    'mercurial': 'Version Control',
    'subversion': 'Version Control',

    # Data Science tools
    'pandas': 'Pandas',
    'numpy': 'NumPy',
    'scipy': 'SciPy',
    'jupyter': 'Jupyter',
    'jupyter-notebooks': 'Jupyter',
    'jupyterlab': 'Jupyter',
    'ipython': 'Jupyter',
    'ipython-notebook': 'Jupyter',
    'matplotlib': 'Matplotlib',
    'seaborn': 'Seaborn',
    'plotly': 'Plotly',
    'plotly-express': 'Plotly',
    'anaconda': 'Anaconda',
    'conda': 'Anaconda',
    'statistics': 'Statistics',
    'statistical-analysis': 'Statistics',

    # Databases
    'mysql': 'SQL',
    'postgresql': 'SQL',
    'sqlite': 'SQL',
    'mongodb': 'NoSQL',
    'redis': 'NoSQL',
    'database': 'Database',
    'databases': 'Database',

    # Web & APIs
    'wordpress': 'WordPress',
    'wordpress-plugins': 'WordPress',
    'wordpress-security': 'WordPress',
    'drupal': 'Drupal',
    'drupal-6': 'Drupal',
    'jekyll': 'Jekyll',
    'jquery': 'jQuery',

    'api': 'API',
    'rest': 'API',
    'restful': 'API',
    'graphql': 'GraphQL',
    'json': 'JSON',
    'xml': 'XML',

    'apache': 'Apache',
    'nginx': 'Nginx',

    # Education & STEM
    'education': 'Education',
    'e-learning': 'Education',
    'elearning': 'Education',
    'learning': 'Education',
    'learning-resources': 'Education',
    'programming-education': 'Education',
    'teaching': 'Education',
    'google-courses': 'Education',
    'google-code-university': 'Education',

    'community-education': 'CoderDojo',
    'code-club': 'CoderDojo',
    'coder-dojo': 'CoderDojo',

    'stem': 'STEM',
    'stem-education': 'STEM',
    'stem-outreach-activities': 'STEM',
    'stem-subjects': 'STEM',

    'conference': 'Conferences',
    'conferences': 'Conferences',
    'nidc': 'NIDC',
    'tedx': 'TEDx',
    'tedxbelfast': 'TEDx',
    'pycon': 'PyCon',
    'pyconie': 'PyCon',
    'bsides': 'BSides',

    'speaking': 'Speaking',
    'speaker': 'Speaking',
    'talks': 'Speaking',
    'meetup': 'Meetups',
    'meetups': 'Meetups',

    # Open Source & Maker
    'open-source': 'Open Source',
    'opensource': 'Open Source',
    'foss': 'Open Source',
    'floss': 'Open Source',
    'open-data': 'Open Data',
    'creative-commons': 'Creative Commons',

    'maker': 'Maker',
    'makers': 'Maker',
    'making': 'Maker',
    '3d-printing': '3D Printing',
    '3d-printer': '3D Printing',
    'diy': 'DIY',
    'electronics': 'Electronics',
    'soldering': 'Electronics',

    # Misc Tech
    'iot': 'IoT',
    'internet-of-things': 'IoT',
    'smart-home': 'Smart Home',
    'home-automation': 'Smart Home',

    'vr': 'VR/AR',
    'virtual-reality': 'VR/AR',
    'ar': 'VR/AR',
    'augmented-reality': 'VR/AR',

    'blockchain': 'Blockchain',
    'cryptocurrency': 'Cryptocurrency',
    'bitcoin': 'Cryptocurrency',
    'ethereum': 'Cryptocurrency',

    'gps': 'GPS',
    'gps-iii': 'GPS',
    'navigation': 'Navigation',
    'geolocation': 'Navigation',

    'simulation': 'Simulation',
    'simulator': 'Simulation',
    'ns-3': 'Simulation',

    # Personal & Lifestyle
    'tutorial': 'Tutorial',
    'how-to': 'Tutorial',
    'guide': 'Tutorial',
    'review': 'Review',
    'reviews': 'Review',
    'opinion': 'Opinion',
    'commentary': 'Opinion',

    'travel': 'Travel',
    'food': 'Food',
    'cooking': 'Food',
    'recipe': 'Food',
    'whiskey': 'Drinks',
    'whisky': 'Drinks',
    'coffee': 'Drinks',
    'beer': 'Drinks',

    'productivity': 'Productivity',
    'workflow': 'Productivity',
    'automation': 'Automation',
}

# Tags that map to MULTIPLE new tags (old -> [new1, new2, ...])
MULTI_MAPPINGS = {
    # Cybersecurity sub-categories (+ Cybersecurity parent)
    'application-security-posture-management': ['Application Security', 'Cybersecurity'],
    'vulnerability': ['Application Security', 'Cybersecurity'],
    'sql-injection': ['Application Security', 'Cybersecurity'],
    'exploit': ['Application Security', 'Cybersecurity'],

    'data-breach': ['Data Security', 'Cybersecurity'],
    'data-breaches': ['Data Security', 'Cybersecurity'],
    'data-protection': ['Data Security', 'Cybersecurity'],
    'passwords': ['Data Security', 'Cybersecurity'],
    'password-security': ['Data Security', 'Cybersecurity'],

    'firewall': ['Network Security', 'Cybersecurity'],
    'network-security': ['Network Security', 'Cybersecurity'],
    'authentication': ['Network Security', 'Cybersecurity'],

    'encryption': ['Cryptography', 'Cybersecurity'],
    'tls': ['Cryptography', 'Cybersecurity'],
    'traffic-encryption': ['Cryptography', 'Cybersecurity'],

    'anonymity': ['Privacy', 'Cybersecurity'],
    'digital-rights': ['Privacy', 'Cybersecurity'],
    'internet-freedom': ['Privacy', 'Cybersecurity'],
    'internet-privacy': ['Privacy', 'Cybersecurity'],
    'net-neutrality': ['Privacy', 'Cybersecurity'],
    'surveillance': ['Privacy', 'Cybersecurity'],

    'aircrack': ['Hacking', 'Cybersecurity'],
    'backtrack-4': ['Hacking', 'Cybersecurity'],
    'backtrack-linux': ['Hacking', 'Cybersecurity'],
    'hacker': ['Hacking', 'Cybersecurity'],
    'hackers': ['Hacking', 'Cybersecurity'],
    'nmap': ['Hacking', 'Cybersecurity'],
    'password-cracking': ['Hacking', 'Cybersecurity'],
    'phishing': ['Hacking', 'Cybersecurity'],
    'social-engineering': ['Hacking', 'Cybersecurity'],
    'wireshark': ['Hacking', 'Cybersecurity'],

    'cyber-security': ['Cybersecurity'],
    'information-security': ['Cybersecurity'],
    'security': ['Cybersecurity'],

    # Cloud providers (+ Cloud parent)
    'aws': ['AWS', 'Cloud'],
    'azure': ['Azure', 'Cloud'],
    'google-cloud': ['Google Cloud', 'Cloud'],
    'gcp': ['Google Cloud', 'Cloud'],
    'rackspace': ['Cloud'],
    'dreamhost': ['Cloud'],

    # DevOps tools (+ DevOps parent)
    'docker': ['Docker', 'DevOps'],
    'kubernetes': ['Kubernetes', 'DevOps'],
    'k8s': ['Kubernetes', 'DevOps'],
    'terraform': ['Terraform', 'DevOps'],
    'ansible': ['Ansible', 'DevOps'],
    'jenkins': ['Jenkins', 'DevOps'],

    # AUV/Maritime (triplicate)
    'auv': ['Autonomous Systems', 'Maritime', 'Robotics'],
    'auvs': ['Autonomous Systems', 'Maritime', 'Robotics'],
    'maritime-autonomy': ['Autonomous Systems', 'Maritime', 'Robotics'],

    # Raspberry Pi / Arduino (+ Microcontrollers)
    'raspberry-pi': ['Raspberry Pi', 'Microcontrollers'],
    'arduino': ['Arduino', 'Microcontrollers'],

    # Rant (+ Opinion)
    'rant': ['Rant', 'Opinion'],

    # Web Development (html + css)
    # Note: html and css individually map to HTML and CSS
    # but if you want them to also add Web Development, handle separately
}


def normalize_tag(tag):
    """Normalize a tag for comparison (lowercase, strip, convert spaces to hyphens)."""
    return tag.lower().strip().replace(' ', '-')


# Minimum frequency threshold - tags used fewer times than this will be deleted
MIN_TAG_FREQUENCY = 3

# Tags that should always be kept regardless of frequency
# (important mapped tags that might be under threshold after consolidation)
ALWAYS_KEEP = {
    'ai', 'llm', 'machine-learning', 'data-science', 'nlp',
    'cybersecurity', 'application-security', 'data-security',
    'network-security', 'cryptography', 'privacy', 'hacking',
    'python', 'javascript', 'c/c++', 'bash', 'shell',
    'ubuntu', 'linux', 'windows', 'android',
    'farset-labs', 'hackerspace', 'belfast', 'northern-ireland', 'qub',
    'phd', 'research', 'trust', 'robotics', 'autonomous-systems', 'maritime',
    'cloud', 'devops', 'docker', 'kubernetes', 'aws', 'azure',
    'git', 'github', 'jupyter', 'pandas',
    'gaming', 'music', 'film', 'books',
    'tutorial', 'opinion', 'rant', 'review',
}


def process_tags(tags):
    """Process a list of tags and return the new consolidated list."""
    new_tags = set()

    for tag in tags:
        tag_str = str(tag).strip()

        # Skip overly long tags (likely data quality issues)
        if len(tag_str) > 50:
            continue

        # Skip tags that look like URLs or markdown links
        if 'http' in tag_str.lower() or '[' in tag_str or ']' in tag_str:
            continue

        tag_lower = normalize_tag(tag_str)

        # Check if tag should be deleted
        if tag_lower in {t.lower() for t in TAGS_TO_DELETE}:
            continue

        # Check multi-mappings first
        if tag_lower in {k.lower(): k for k in MULTI_MAPPINGS}:
            # Find the actual key
            for key in MULTI_MAPPINGS:
                if key.lower() == tag_lower:
                    new_tags.update(MULTI_MAPPINGS[key])
                    break
            continue

        # Check simple mappings
        matched = False
        for old_tag, new_tag in SIMPLE_MAPPINGS.items():
            if old_tag.lower() == tag_lower:
                new_tags.add(new_tag)
                matched = True
                break

        if not matched:
            # Check frequency threshold for unmapped tags
            if tag_lower in ALWAYS_KEEP:
                new_tags.add(tag_str)
            elif TAG_FREQUENCIES.get(tag_lower, 0) >= MIN_TAG_FREQUENCY:
                new_tags.add(tag_str)
            # else: tag is below frequency threshold, skip it

    # Sort and return as list
    return sorted(list(new_tags))


# Global variable for tag frequencies (set by main)
TAG_FREQUENCIES = {}


def process_file(filepath):
    """Process a single markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file has front matter
    if not content.startswith('---'):
        return False, "No front matter"

    # Find the end of front matter
    second_dash = content.find('---', 3)
    if second_dash == -1:
        return False, "Invalid front matter"

    front_matter = content[3:second_dash]
    body = content[second_dash+3:]

    # Find tags section in front matter
    # Handle both formats:
    # tags:
    # - tag1
    # - tag2
    # OR
    # tags: [tag1, tag2]

    lines = front_matter.split('\n')
    new_lines = []
    in_tags = False
    tags = []
    tags_start_idx = -1
    tags_end_idx = -1

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith('tags:'):
            tags_start_idx = i
            # Check if inline format: tags: [tag1, tag2]
            if '[' in stripped:
                match = re.search(r'\[([^\]]*)\]', stripped)
                if match:
                    tag_str = match.group(1)
                    tags = [t.strip().strip("'\"") for t in tag_str.split(',') if t.strip()]
                tags_end_idx = i
                in_tags = False
            else:
                in_tags = True
            i += 1
            continue

        if in_tags:
            if stripped.startswith('-'):
                tag = stripped[1:].strip().strip("'\"")
                tags.append(tag)
                tags_end_idx = i
            elif stripped and not stripped.startswith('#'):
                # End of tags section
                in_tags = False
                new_lines.append(line)
            else:
                # Empty line or comment within tags - keep going
                if not stripped:
                    tags_end_idx = i
        else:
            new_lines.append(line)

        i += 1

    if not tags:
        return False, "No tags found"

    # Process tags
    new_tags = process_tags(tags)

    if set(tags) == set(new_tags):
        return False, "No changes needed"

    # Rebuild front matter with new tags
    result_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith('tags:'):
            # Add new tags section
            result_lines.append('tags:')
            for tag in new_tags:
                # Quote tags that need it
                needs_quotes = any(c in tag for c in [' ', ':', '#', '[', ']', '{', '}', ',', '&', '*', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`'])
                if needs_quotes:
                    # Use double quotes if tag contains apostrophe, single quotes otherwise
                    if "'" in tag:
                        result_lines.append(f'- "{tag}"')
                    else:
                        result_lines.append(f"- '{tag}'")
                else:
                    result_lines.append(f'- {tag}')

            # Skip old tags
            if '[' in stripped:
                # Inline format - just skip this line
                i += 1
            else:
                # List format - skip until we hit non-tag line
                i += 1
                while i < len(lines):
                    if lines[i].strip().startswith('-'):
                        i += 1
                    elif not lines[i].strip():
                        i += 1
                    else:
                        break
            continue

        result_lines.append(line)
        i += 1

    # Rebuild content
    new_front_matter = '\n'.join(result_lines)
    new_content = '---' + new_front_matter + '---' + body

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, f"Updated: {len(tags)} -> {len(new_tags)} tags"


def count_all_tags(posts_dir):
    """Count frequency of all tags across all posts."""
    from collections import Counter
    tag_counts = Counter()

    for filepath in sorted(posts_dir.glob('*.md')) + sorted(posts_dir.glob('*.markdown')):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if not content.startswith('---'):
                continue

            second_dash = content.find('---', 3)
            if second_dash == -1:
                continue

            front_matter = content[3:second_dash]
            lines = front_matter.split('\n')
            in_tags = False

            for line in lines:
                stripped = line.strip()
                if stripped.startswith('tags:'):
                    if '[' in stripped:
                        match = re.search(r'\[([^\]]*)\]', stripped)
                        if match:
                            tag_str = match.group(1)
                            tags = [t.strip().strip("'\"") for t in tag_str.split(',') if t.strip()]
                            for tag in tags:
                                tag_counts[normalize_tag(tag)] += 1
                    else:
                        in_tags = True
                    continue

                if in_tags:
                    if stripped.startswith('-'):
                        tag = stripped[1:].strip().strip("'\"")
                        tag_counts[normalize_tag(tag)] += 1
                    elif stripped and not stripped.startswith('#'):
                        in_tags = False

        except Exception:
            pass

    return tag_counts


def main():
    posts_dir = Path(__file__).parent.parent / 'content' / 'posts'

    if not posts_dir.exists():
        print(f"Error: Posts directory not found: {posts_dir}")
        sys.exit(1)

    print(f"Processing posts in: {posts_dir}")
    print("=" * 60)

    # First pass: count all tag frequencies
    print("Counting tag frequencies...")
    global TAG_FREQUENCIES
    TAG_FREQUENCIES = count_all_tags(posts_dir)
    print(f"Found {len(TAG_FREQUENCIES)} unique tags")
    high_freq = sum(1 for t, c in TAG_FREQUENCIES.items() if c >= MIN_TAG_FREQUENCY)
    print(f"Tags with {MIN_TAG_FREQUENCY}+ uses: {high_freq}")
    print("=" * 60)

    updated = 0
    skipped = 0
    errors = 0

    for filepath in sorted(posts_dir.glob('*.md')) + sorted(posts_dir.glob('*.markdown')):
        try:
            changed, message = process_file(filepath)
            if changed:
                print(f"✓ {filepath.name}: {message}")
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"✗ {filepath.name}: Error - {e}")
            errors += 1

    print("=" * 60)
    print(f"Updated: {updated}")
    print(f"Skipped: {skipped}")
    print(f"Errors: {errors}")


if __name__ == '__main__':
    main()
