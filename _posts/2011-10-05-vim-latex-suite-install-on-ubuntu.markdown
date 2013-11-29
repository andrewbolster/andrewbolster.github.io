---
author: admin
comments: true
date: 2011-10-05 14:43:50+00:00
layout: post
slug: vim-latex-suite-install-on-ubuntu
title: Vim Latex Suite Install on Ubuntu
wordpress_id: 679
categories:
- Instructional
tags:
- install
- latex
- latex-suite
- linux
- Ubuntu
- vim
---

Ubuntu doesn't manage vim's addons, so installing the `vim-latexsuite` package doesn't actually put all the relevant hooks into your vim installation. To do that, (after installing the package) execute;
`sudo vim-addons -w install latex-suite`
