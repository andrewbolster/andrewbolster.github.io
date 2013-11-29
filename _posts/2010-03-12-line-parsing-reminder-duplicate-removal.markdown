---
author: admin
comments: true
date: 2010-03-12 15:37:50+00:00
layout: post
slug: line-parsing-reminder-duplicate-removal
title: Line Parsing Reminder (Duplicate removal)
wordpress_id: 268
categories:
- Instructional
tags:
- bash
- code
- linux
- software
- workstation
---

So, say you have a long list of instruction (like multiple apt-get install lines) and you want to eliminate common words?

<!-- more -->Easiest way to do it is (assuming you have all of the instrustions in "list.txt")

[FYI the '\' character indicates a continuation of a single line ]


> cat list.txt\

| tr ' ' '\n' \            #Expands all space characters to new lines

| sort | uniq \    #sorts each line, and then eliminates duplicates

| tr '\n' ''               #turns all the new-lines into spaces


Depending on the actual content, it may be necessary to remove specific entries, (such as apt-get or sudo). Thats an exercise for the reader.
