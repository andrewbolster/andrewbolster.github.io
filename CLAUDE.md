# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Hugo-based personal blog and portfolio website for Andrew Bolster. The site is hosted on GitHub Pages using the PaperMod theme. The site contains blog posts dating back to 2007, covering topics including technology, academia, data science, and Northern Ireland tech community activities.

## Development Commands

### Dependencies and Setup
```bash
# Install Hugo and initialize theme
make install

# Update theme submodule
make update
```

### Content Creation
```bash
# Create a new draft post
make draft

# In Hugo, remove 'draft: true' from front matter to publish
# Preview drafts locally with: make serve
```

### Development Server
```bash
# Serve the site locally with drafts
make serve
# This runs: hugo server --buildDrafts --buildFuture --navigateToChanged
```

### Building
```bash
# Build the production site
make build
# This runs: hugo --gc --minify

# Clean generated files
make clean
```

### Pre-commit Hooks
```bash
# Run pre-commit checks
make precommit
```

## Architecture

### Hugo Structure
- **hugo.toml**: Main Hugo configuration with site metadata and theme settings
- **content/posts/**: Blog posts in Markdown format (dating from 2007-2025)
- **content/**: Static pages (about.md, resume/, now.md, ideas.md)
- **static/**: Images, assets, and other static files
- **themes/PaperMod/**: PaperMod theme (git submodule)
- **archetypes/**: Templates for new content
- **public/**: Generated static site (excluded from git)

### Theme
- Uses PaperMod theme (https://github.com/adityatelange/hugo-PaperMod)
- Installed as git submodule in `themes/PaperMod/`
- Configuration in `hugo.toml`

### Content Types
- **Blog posts**: Technical writing, tutorials, opinion pieces in `content/posts/`
- **Resume**: Markdown-based resume in `content/resume/`
- **Static pages**: About, now, ideas, archives, search
- **Media**: Images and assets in `static/img/` and `static/uploads/`

### Features
- Emoji support (GitHub-style shortcodes)
- Syntax highlighting with Chroma
- Built-in search
- Tag and category taxonomies
- RSS feed generation
- Sitemap generation
- Google Analytics 4 integration

## File Organization

### Posts Structure
Posts follow Hugo naming convention: `YYYY-MM-DD-title.md`
- Markdown files with YAML front matter
- Categories and tags for organization
- Asset files organized by year in `static/img/`

### URL Structure
Posts use permalink pattern: `/:year/:month/:title.html`
- Example: `/2024/02/my-post-title.html`
- Preserves legacy Jekyll URL structure for SEO

### Static Assets
- `static/img/`: Images organized by year and topic
- `static/uploads/`: Additional assets and files
- `static/assets/`: CSS, JavaScript, and fonts
- `static/icons/`: Site icons and logos

## Development Notes

### Local Development
- Hugo Extended required for SCSS processing
- `hugo server -D` for development with drafts
- Hot reload enabled by default

### Deployment
- GitHub Actions workflow in `.github/workflows/hugo.yml`
- Netlify configuration in `netlify.toml`
- Custom domain: andrewbolster.info
- SSL enforcement configured

### Content Guidelines
- Posts support CommonMark/GFM markdown syntax
- Code blocks with syntax highlighting
- Raw HTML allowed in markdown (unsafe mode enabled)
- Front matter required for all posts

## Hugo Gotchas and Common Issues

This section documents issues discovered during the Jekyll-to-Hugo migration and ongoing maintenance.

### Date Format Requirements
Hugo requires ISO 8601 date format in front matter. Non-standard formats will cause build failures.
- **Bad**: `date: 2019-05-17 08:42 +0100`
- **Good**: `date: 2019-05-17T08:42:00+01:00`

### Tags with Special Characters
Netlify cannot deploy files with `#` or `?` in filenames. Tags containing these characters will cause deployment failures.
- **Bad**: `- '#OnionPulitzer'`, `- 'C#'`, `- 'Ludum Dare #17'`
- **Good**: `- OnionPulitzer`, `- CSharp`, `- Ludum Dare 17`

### Markdown After Raw HTML Blocks
Goldmark (Hugo's markdown renderer) requires a blank line between raw HTML and markdown content. Without it, markdown following HTML is rendered as literal text.
```markdown
<!-- BAD: markdown not rendered -->
<img src="image.png"/>
**This text appears as literal asterisks**

<!-- GOOD: blank line separates HTML from markdown -->
<img src="image.png"/>

**This text is properly bold**
```

### PaperMod Configuration
The `profileMode` parameter must be a table, not a boolean:
- **Bad**: `profileMode = false`
- **Good**: `[params.profileMode]` with `enabled = false`

### Hugo Version and GLIBC
Modern Hugo versions (0.146.0+) require GLIBC 2.32+. For Netlify deployment:
- Use `[images] build = "ubuntu-22.04"` in `netlify.toml` for GLIBC 2.35
- Older Netlify images (Ubuntu 20.04/Focal) have GLIBC 2.31 which is insufficient

### Building Hugo from Source
If pre-built binaries aren't available, build from source with Go:
```bash
cd /tmp && git clone --depth 1 --branch v0.146.0 https://github.com/gohugoio/hugo.git
cd hugo && GOPROXY=direct CGO_ENABLED=1 go build -tags extended -o hugo .
```

## Common Tasks

### Adding a New Post
1. Create draft: `make draft` (prompts for title)
2. Edit the new file in `content/posts/`
3. Remove `draft: true` from front matter when ready to publish
4. Commit and push to trigger deployment

### Content Enhancement Workflow
When working with Claude Code to enhance blog posts:

#### Link Research and Addition
- **NEVER fabricate URLs** - only use verified, accessible sources
- Use WebFetch tool with real URLs to verify content before adding links
- For current events/tech topics, rely on accessible sources like:
  - Wikipedia for biographical/technical information
  - Official company websites
  - Archive.org links for stability
  - Government or academic sources
- Research systematically: identify claims first, then find supporting sources
- Add links WITHOUT modifying original content - preserve author's voice and intentional stylistic choices
- Ensure link consistency between multiple sections/versions of same content

#### Content Review Process
- Review content for spelling corrections only - leave grammar and style intact
- Respect intentional stylistic choices (informal language, emphasis, etc.)
- Focus on factual accuracy of links rather than editorial changes
- When adding links to both formal and informal versions, maintain consistency

#### Categorization and Tagging
- Review recent posts in `content/posts/` folder to understand existing patterns
- Categories: typically 2-3 broad categories (e.g., [AI, Commentary])
- Tags: comprehensive, including:
  - Technology terms (AI, LLM, machine learning)
  - People/company names mentioned
  - Conceptual themes
  - Location/event context when relevant
- Follow established conventions from similar posts

### Publishing Workflow
When ready to publish from a feature branch:
```bash
# 1. Commit all changes
git commit -am "Final edits and enhancements"

# 2. Remove draft: true from front matter if present

# 3. Commit and push
git add content/posts/YYYY-MM-DD-*.md
git commit -m "Publish: [Post Title]"

# 4. Merge to master and deploy
git checkout master
git merge [feature-branch]
git push
```

### Resume Updates
1. Edit `content/resume/_index.md`

### Theme Customization
- Override theme files by creating matching paths in project root
- Example: `layouts/_default/single.html` overrides theme's single.html
- PaperMod documentation: https://adityatelange.github.io/hugo-PaperMod/

## Best Practices for Claude Code

### Content Enhancement
- **Preserve authorial voice**: Never change content tone, style, or intentional grammar
- **Verify all sources**: Use WebFetch or accessible sources before adding any links
- **Be systematic**: Research topics thoroughly rather than guessing URLs
- **Maintain consistency**: Ensure same links appear in parallel content sections
- **Respect context**: Understand the post's audience and purpose when suggesting enhancements

### Research Methodology
- Start with Wikipedia for foundational/biographical information
- Use official websites for company/organization information
- Cross-reference claims with multiple sources when possible
- Prefer stable links (archive.org) over potentially ephemeral news articles
- Document research process for transparency

### About.md Entry Structure
When updating the "Engagements and Publications" section in about.md, follow this established structure:

**Format**: `:emoji: [Title/Content](link) - Venue/Publication - Type`

**Entry Types and Patterns**:
- **Speaking Engagements**: `:speaking_head: Talk Title - [Event/Conference](link) - Speaker`
- **Interviews**: `:movie_camera: [Article/Video Title](link) - Publication @ Venue - Interview`
- **Guest Lectures**: `:teacher: Lecture Topic - [Institution/Course](link) - Guest Lecture`
- **Commentary**: `:speech_balloon: [Article Title](link) - Publication - Commentary`
- **Authored Articles**: `:fountain_pen: [Article Title](link) - Publication - Author`
- **Panel/Discussion**: `:microphone: Event Topic - [Event](link) - Panellist`

**Link Placement Guidelines**:
- For **articles/content**: Link goes on the title/content
- For **events/talks**: Link can go on either the title (if materials available) or venue (if no specific materials)
- **Dual linking**: Both title and venue can be linked when appropriate (e.g., `[Talk Title](materials-link) - [Conference](event-link) - Speaker`)

**Additional Notes**:
- Use multiple emojis when appropriate (e.g., `:speech_balloon: :movie_camera:` for video interviews)
- Include venue context with `@` when relevant (e.g., "Publication @ Event")
- By default, new entries are added to the top of the year, but can be moved around by the user based on impact and grouping preferences
- Only include published/confirmed engagements with verifiable links
