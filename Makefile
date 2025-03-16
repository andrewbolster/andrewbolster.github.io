# Install dependencies
install:
	gem install bundler
	bundle install

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

# Compile LESS to CSS with source maps
compile-css:
	lessc style.less style.css -m=always

# Default target
all: install update compile-css
