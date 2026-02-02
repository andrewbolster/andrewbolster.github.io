#!/usr/bin/env uv run
# /// script
# dependencies = [
#   "requests",
#   "beautifulsoup4"
# ]
# ///

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def check_page_for_broken_links(url):
    print(f"\n🔍 Checking: {url}")

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        broken_links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if 'human-factors-in-autonomous-systems' in href or '2020/10/a-stranger-in-a-strange-land' in href:
                full_url = urljoin(url, href)
                print(f"  Found: {href} -> {full_url}")
                print(f"  Link text: '{link.get_text()[:50]}...'")
                broken_links.append(full_url)

        if not broken_links:
            print("  ✅ No problematic links found")

        return broken_links

    except Exception as e:
        print(f"  ❌ Error: {e}")
        return []

if __name__ == "__main__":
    # Check both versions of the lies-damned-lies page
    pages = [
        "http://localhost:1313/2022/01/lies-damned-lies-and-data-science/",
        "http://localhost:1313/2022/01/lies-damned-lies-and-data-science.html"
    ]

    for page in pages:
        links = check_page_for_broken_links(page)
