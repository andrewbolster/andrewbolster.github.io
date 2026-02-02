.PHONY: install update draft publish serve build clean precommit all

# Install Hugo (assumes brew on macOS, or provides instructions)
install:
	@echo "Installing Hugo..."
	@if command -v brew >/dev/null 2>&1; then \
		brew install hugo; \
	elif command -v apt-get >/dev/null 2>&1; then \
		sudo apt-get update && sudo apt-get install -y hugo; \
	elif command -v snap >/dev/null 2>&1; then \
		sudo snap install hugo --channel=extended; \
	else \
		echo "Please install Hugo manually: https://gohugo.io/installation/"; \
		exit 1; \
	fi
	@echo "Initializing git submodules for theme..."
	git submodule update --init --recursive

# Run pre-commit hooks
precommit:
	pre-commit run --all-files

# Update theme submodule
update:
	git submodule update --remote --merge

# Create a new draft post
draft:
	@read -p "Enter the title of the draft: " title; \
	hugo new content/posts/$$(date +%Y-%m-%d)-$$(echo "$$title" | tr '[:upper:]' '[:lower:]' | tr ' ' '-').md

# Publish drafts (move from draft: true to draft: false)
# In Hugo, drafts are controlled by front matter, not directory location
publish:
	@echo "In Hugo, remove 'draft: true' from front matter to publish."
	@echo "Alternatively, use: hugo server -D to preview drafts locally."

# Serve the site locally with drafts
serve:
	hugo server --buildDrafts --buildFuture --navigateToChanged

# Build the production site
build:
	hugo --gc --minify

# Clean generated files
clean:
	rm -rf public resources

# Default target
all: install build
