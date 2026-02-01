---
author: admin
categories:
- Instructional
comments: true
date: 2012-04-30 17:07:44+00:00
layout: post
slug: ns-3-click-integration
tags:
- linux
- shared library files
- router networks
- routing architecture
- router library
- click
- examples
- root access
- configuration
- kernel
- modular
- ns-3
- installation guide
title: NS-3 Click integration
---


# Intro

[Click](http://read.cs.ucla.edu/click/) is a modular router library developed at [UCLA](http://read.cs.ucla.edu/), allowing Click-definied router networks to be 'attached' to an ns-3- nodes layer 3 functionality. It has very little relevance to my own research, but was interesting to play with.

In a nutshell, [Click](http://pdos.csail.mit.edu/papers/click:tocs00/paper.pdf) is an extention to the linux kernel that provides a highly performant and configurable routing architecture.

Requirements


  * Already installed ns-3


  * git


  * ~/src directory

# Get 'er dun

`cd ~/src; git clone git://read.cs.ucla.edu/git/click ; cd click`
`sudo ./configure --enable-nsclick --enable-userlevel; sudo make; sudo make install`

_Sudo ./configure is required to grant access to some root-only areas of the kernel tree_

This should install everything under /usr/local/include/click, but leaves the shared library files in the src dir (This tripped me up a bit...)

`cd ~/src/<ns3-working-dir>/`

./waf distclean

`./waf --enable-nsclick=~/src/click --enable-examples` $(plus whatever additional clauses you use, I like `--visualize --enable-mpi --enable-tests --enable-sudo`)

`./waf --run nsclick-simple-lan`

Jobs a good one
