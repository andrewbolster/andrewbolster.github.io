# andrewbolster.github.io

Personal blog and portfolio for Andrew Bolster - [andrewbolster.info](https://andrewbolster.info)

## Quick Start

```bash
# Install Hugo and initialize theme
make install

# Run development server with drafts
make serve

# Create a new post
make draft

# Build for production
make build
```

## Tech Stack

- **Static Site Generator**: [Hugo](https://gohugo.io/)
- **Theme**: [PaperMod](https://github.com/adityatelange/hugo-PaperMod)
- **Hosting**: GitHub Pages via GitHub Actions
- **Preview**: Netlify Deploy Previews

## Project Structure

```
content/
├── posts/          # Blog posts (2007-present)
├── about.md        # About page
├── resume/         # Resume
├── now.md          # Now page
└── ideas.md        # Ideas page

static/             # Images and assets
themes/PaperMod/    # Theme (git submodule)
hugo.toml           # Site configuration
```

See [CLAUDE.md](CLAUDE.md) for detailed development instructions.
