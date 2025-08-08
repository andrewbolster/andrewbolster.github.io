# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based personal blog and portfolio website for Andrew Bolster. The site is hosted on GitHub Pages and uses the "the-minimum" theme with custom modifications. The site contains blog posts dating back to 2007, covering topics including technology, academia, data science, and Northern Ireland tech community activities.

## Development Commands

### Dependencies and Setup
```bash
# Install Ruby dependencies
bundle install

# Update dependencies
bundle update

# Install bundler for user
gem install bundler --user-install
```

### Content Creation
```bash
# Create a new draft post
bundle exec jekyll draft "<TITLE>"
# Or use the Makefile
make draft

# Publish all drafts
bundle exec jekyll publish _drafts/*
# Or use the Makefile  
make publish
```

### Development Server
```bash
# Serve the site locally with drafts included
bundle exec jekyll serve --drafts
# Or use the Makefile
make serve
```

### Styling
```bash
# Compile LESS to CSS with source maps
lessc style.less style.css -m=always
# Or use the Makefile
make compile-css
```

### Resume Generation
```bash
# Generate PDF resume using Docker and Pandoc
make resume
```

### Pre-commit Hooks
```bash
# Run pre-commit checks
make precommit
```

## Architecture

### Jekyll Structure
- **_config.yml**: Main Jekyll configuration with site metadata, plugins, and theme settings
- **_layouts/**: Layout templates that delegate to theme files
- **_includes/**: Reusable template components and theme includes
- **_posts/**: Blog posts in Markdown format (dating from 2007-2025)
- **_drafts/**: Unpublished draft posts
- **_site/**: Generated static site (excluded from git)

### Styling
- Uses LESS preprocessing for CSS
- Main stylesheet: `assets/css/style.less`
- Theme-based styling with custom color scheme
- Responsive design with mobile considerations

### Theme Integration
- Uses Jekyll-Bootstrap framework
- Theme: "the-minimum"
- Custom modifications in `_includes/theme/` and `_layouts/`
- Asset management through Jekyll-Bootstrap's ASSET_PATH system

### Content Types
- **Blog posts**: Technical writing, tutorials, opinion pieces
- **Resume**: Markdown-based resume with PDF generation
- **Static pages**: About, archive, categories, tags
- **Media**: Images, notebooks, and other assets in organized directories

### Plugins and Features
- GitHub Pages compatible plugins
- Emoji support via jemoji
- Gist integration
- Mentions and redirects
- Sitemap generation
- Syntax highlighting with Rouge
- Analytics integration (Google Analytics)
- Comments via Disqus

## File Organization

### Posts Structure
Posts follow Jekyll naming convention: `YYYY-MM-DD-title.extension`
- Markdown files with YAML front matter
- Categories and tags for organization
- Asset files organized by year in `img/` and `uploads/`

### Media Management
- `img/`: Images organized by year and topic
- `uploads/`: Additional assets and files
- `assets/`: CSS, JavaScript, and other web assets
- `icons/`: Site icons and logos

### Generated Content
- Feed files (Atom and RSS)
- Sitemap and robots.txt
- Category and tag index pages
- Archive pages

## Development Notes

### Local Development
- Uses Ruby bundler for dependency management
- Jekyll serve with `--drafts` for development
- LESS compilation required for styling changes
- Pre-commit hooks available for code quality

### Deployment
- Automated deployment to GitHub Pages
- Custom domain: andrewbolster.info
- SSL enforcement configured

### Content Guidelines
- Posts support Kramdown markdown syntax
- Code blocks with syntax highlighting
- Image optimization recommended
- Front matter required for all posts

## Common Tasks

### Adding a New Post
1. Create draft: `make draft` or `bundle exec jekyll draft "Title"`
2. Edit in `_drafts/`
3. Publish: `make publish` or `bundle exec jekyll publish _drafts/post-name.md`

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
- Review recent posts in `_posts/` folder to understand existing patterns
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

# 2. Publish draft to _posts/
make publish

# 3. Commit published post
git add _posts/YYYY-MM-DD-*.md _drafts/
git commit -m "Publish: [Post Title]"

# 4. Merge to master and deploy
git checkout master
git merge [feature-branch]
git push
```

### Modifying Styles
1. Edit `assets/css/style.less` or related LESS files
2. Compile: `make compile-css`
3. Test locally: `make serve`

### Resume Updates
1. Edit `resume/index.md`
2. Generate PDF: `make resume`

### Theme Customization
- Override theme files in `_includes/theme/`
- Modify layouts in `_layouts/`
- Customize variables in LESS files

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
