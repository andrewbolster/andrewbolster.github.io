---
author: admin
comments: true
date: 2010-04-09 14:58:31+00:00
layout: post
slug: listing-just-dot-files
title: Listing just dot-files
categories:
- Instructional
tags:
- bash
- code
- linux
- programming
- software
- Ubuntu
---

Its a problem that I've come across, and I'm [not the only one](http://www.unix.com/unix-dummies-questions-answers/42734-command-list-dot-files.html), so heres what works for me to find those pesky files that start with a .
`ls -a | egrep -i "^\."`

This only works in the current working directory, which is the normal usage.

FYI the reason that this is problematic is that the '.' symbol is a single character wildcard; most people are familiar with the asterisk '\*' indicating 'anything, however long', whereas the '.' means 'any single character'.

The command works by looking only at the first character of the file ('^', thats called a caret) and then removing the special meaning of '.' by escaping it with the slash.

**Update:18/4/10**
@stevebiscuit correctly pointed out that the `-i` flag is unnecessary.

`-i`instructs egrep to ignore the case of any matches, so that 'HeLlO' matches if you egrep -i for 'hello'. Since there is no case for the '.' symbol, the `-i` is pointless.
