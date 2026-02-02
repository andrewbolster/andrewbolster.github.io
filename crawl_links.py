#!/usr/bin/env uv run
# /// script
# dependencies = [
#   "requests",
#   "beautifulsoup4",
#   "click"
# ]
# ///
"""
Site crawler to find broken internal links on localhost:1313
"""
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import time
import click
from collections import defaultdict
from pathlib import Path

class SiteCrawler:
    def __init__(self, base_url="http://localhost:1313"):
        self.base_url = base_url
        self.domain = urlparse(base_url).netloc
        self.visited_pages = set()
        self.all_links = set()
        self.broken_links = []
        self.link_sources = defaultdict(list)  # Track where each link was found
        self.link_cache = {}  # Cache link test results: {url: (is_working, status)}
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'SiteCrawler/1.0 (Internal Link Checker)'
        })

    def is_internal_link(self, url):
        """Check if URL is internal to our site"""
        parsed = urlparse(url)
        return parsed.netloc == self.domain or parsed.netloc == ''

    def normalize_url(self, url):
        """Normalize URL for comparison"""
        parsed = urlparse(url)
        # Remove fragment (anchor) for testing but keep it for reporting
        normalized = parsed._replace(fragment='').geturl()
        return normalized

    def get_page_links(self, url):
        """Extract all links from a page"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            links = []

            # Find all anchor tags with href
            for link in soup.find_all('a', href=True):
                href = link.get('href')
                if href:
                    absolute_url = urljoin(url, href)
                    if self.is_internal_link(absolute_url):
                        links.append(absolute_url)
                        self.link_sources[absolute_url].append(url)

            return links
        except Exception as e:
            click.echo(f"Error crawling {url}: {e}", err=True)
            return []

    def test_link(self, url):
        """Test if a link is working (with caching)"""
        # Normalize for testing (remove fragment)
        test_url = self.normalize_url(url)

        # Check cache first
        if test_url in self.link_cache:
            return self.link_cache[test_url]

        try:
            response = self.session.head(test_url, timeout=10, allow_redirects=True)
            if response.status_code >= 400:
                result = (False, response.status_code)
            else:
                result = (True, response.status_code)
        except Exception as e:
            result = (False, str(e))

        # Cache the result
        self.link_cache[test_url] = result
        return result

    def crawl_site(self, max_pages=200):
        """Crawl the site starting from base_url"""
        click.echo(f"🕷️  Starting crawl of {self.base_url}")

        # Start with home page
        to_visit = [self.base_url]
        pages_crawled = 0

        with click.progressbar(length=max_pages, label='Crawling pages') as bar:
            while to_visit and pages_crawled < max_pages:
                url = to_visit.pop(0)

                if url in self.visited_pages:
                    continue

                self.visited_pages.add(url)
                pages_crawled += 1
                bar.update(1)

                # Get links from this page
                page_links = self.get_page_links(url)

                # Add new links to our sets
                for link in page_links:
                    self.all_links.add(link)

                    # Add new pages to visit queue (only pages, not files)
                    normalized = self.normalize_url(link)
                    if (normalized not in self.visited_pages
                        and normalized not in [self.normalize_url(u) for u in to_visit]
                        and not normalized.endswith(('.pdf', '.jpg', '.png', '.gif', '.css', '.js', '.xml'))):
                        to_visit.append(normalized)

                # Small delay to be nice to the server
                time.sleep(0.05)

        click.echo(f"✅ Crawled {pages_crawled} pages, found {len(self.all_links)} unique links")
        return pages_crawled

    def check_all_links(self):
        """Check all discovered links for errors"""
        # Filter out mailto links
        testable_links = [link for link in self.all_links if not link.startswith('mailto:')]
        skipped_count = len(self.all_links) - len(testable_links)

        if skipped_count > 0:
            click.echo(f"📧 Skipping {skipped_count} mailto links")

        click.echo(f"🔗 Testing {len(testable_links)} links...")

        cache_hits = 0
        with click.progressbar(testable_links, label='Testing links') as links:
            for link in links:
                # Track cache hits
                test_url = self.normalize_url(link)
                was_cached = test_url in self.link_cache

                is_working, status = self.test_link(link)

                if was_cached:
                    cache_hits += 1

                if not is_working:
                    self.broken_links.append({
                        'url': link,
                        'status': status,
                        'found_on': self.link_sources[link][:5]  # First 5 sources
                    })

                # Small delay between requests (skip for cached results)
                if not was_cached:
                    time.sleep(0.02)

        # Report cache performance
        if cache_hits > 0:
            click.echo(f"⚡ Cache hits: {cache_hits}/{len(testable_links)} ({cache_hits/len(testable_links)*100:.1f}%)")

    def generate_report(self, output_file=None):
        """Generate a report of broken links"""
        if not self.broken_links:
            click.echo("✅ No broken links found!")
            return

        click.echo(f"❌ Found {len(self.broken_links)} broken links:")
        click.echo()

        for i, broken in enumerate(self.broken_links, 1):
            click.echo(f"{i}. {broken['url']}")
            click.echo(f"   Status: {broken['status']}")
            click.echo(f"   Found on: {', '.join(broken['found_on'][:2])}")
            if len(broken['found_on']) > 2:
                click.echo(f"   ... and {len(broken['found_on']) - 2} other pages")
            click.echo()

        if output_file:
            self.write_detailed_report(output_file)

    def write_detailed_report(self, output_file):
        """Write detailed report to file"""
        with open(output_file, 'w') as f:
            f.write(f"Broken Link Report - Generated at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{'='*60}\n\n")

            if self.broken_links:
                for broken in self.broken_links:
                    f.write(f"URL: {broken['url']}\n")
                    f.write(f"Status: {broken['status']}\n")
                    f.write(f"Found on pages:\n")
                    for source in broken['found_on']:
                        f.write(f"  - {source}\n")
                    f.write("\n")
            else:
                f.write("No broken links found.\n")

        click.echo(f"📄 Detailed report saved to: {output_file}")

@click.command()
@click.option('--url', '-u', default='http://localhost:1313', help='Base URL to crawl')
@click.option('--max-pages', '-p', default=200, help='Maximum pages to crawl')
@click.option('--output', '-o', help='Output file for detailed report')
def main(url, max_pages, output):
    """Crawl a Hugo site and find broken internal links."""

    crawler = SiteCrawler(url)

    # Test if the site is running
    try:
        response = requests.get(crawler.base_url, timeout=5)
        response.raise_for_status()
        click.echo(f"✅ Site is accessible at {crawler.base_url}")
    except Exception as e:
        click.echo(f"❌ Cannot reach {crawler.base_url}: {e}", err=True)
        click.echo("Make sure Hugo server is running with: hugo serve")
        raise click.Abort()

    # Crawl the site
    crawler.crawl_site(max_pages)

    # Check all links
    crawler.check_all_links()

    # Generate report
    if not output:
        output = 'broken_links_report.txt'

    crawler.generate_report(output)

if __name__ == "__main__":
    main()
