---
author: admin
comments: true
date: 2011-10-26 13:45:59+00:00
layout: post
slug: unicode-characters-in-mendeley-bibliography-breaking-latex
title: Unicode Characters in Mendeley Bibliography Breaking Latex?
categories:
- Instructional
tags:
- bibtex
- code
- eclipse
- latex
- mendeley
- pdflatex
- tex
- texclipse
- unicode
- xelatex
---

[![](http://www.andrewbolster.info/wp-content/uploads/2011/10/oem.png)](http://www.andrewbolster.info/2011/10/unicode-characters-in-mendeley-bibliography-breaking-latex/oem/)I use Mendeley for my reference and citation management.

I use TexClipse for (most) of my $latex \LaTeX$ editing, ViM otherwise.

I use Xelatex / pdflatex for project building.

These don't always work so well together. 

One issue I came across was that Mendeley can insert some weird Unicode whitespace characters that 'disappear' in TexClipse / Vim, but break xelatex/pdflatex.

Easy solution: set the project encoding in TexClipse to ignore these characters upon pasting.

Right click on your project -> Properties - > set Text File Encoding to US-ASCII; Apply

Job Done; No more Unicode woes!
