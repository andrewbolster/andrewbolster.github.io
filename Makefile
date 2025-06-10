.PHONY: install update draft publish serve resume compile-css all
# Install dependencies
install:
	gem install bundler --user-install
	bundle install

precommit:
	pre-commit run --all-files

# Update dependencies
update:
	bundle update

# Draft a new post
draft:
	@read -p "Enter the title of the draft: " title; \
	bundle exec jekyll draft "$$title"

# Publish all drafts
publish:
	bundle exec jekyll publish _drafts/*

serve:
	bundle exec jekyll serve --drafts

resume:
	docker run --rm \
	    --platform linux/amd64 \
		--volume "$$(pwd):/data" \
		--user $$(id -u):$$(id -g) \
		pandoc/extra resume/index.md -o resume/AndrewBolster.pdf --template eisvogel --listings

# Compile LESS to CSS with source maps
compile-css:
	lessc style.less style.css -m=always

# Default target
all: install update compile-css
