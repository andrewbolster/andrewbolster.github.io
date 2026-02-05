---
aliases:
- /2011/10/vim-latex-suite-install-on-ubuntu/
- /2011/10/vim-latex-suite-install-on-ubuntu.html
categories:
- Instructional
comments: true
date: 2011-10-05 14:43:50+00:00
slug: vim-latex-suite-install-on-ubuntu
tags:
- Linux
- Ubuntu
- latex
- package management
title: Vim Latex Suite Install on Ubuntu
---
Ubuntu doesn't manage vim's addons, so installing the `vim-latexsuite` package doesn't actually put all the relevant hooks into your vim installation. To do that, (after installing the package) execute;
`sudo vim-addons -w install latex-suite`
