---
aliases:
- /2010/03/line-parsing-reminder-duplicate-removal/
- /2010/03/line-parsing-reminder-duplicate-removal.html
categories:
- Instructional
comments: true
date: 2010-03-12 15:37:50+00:00
slug: line-parsing-reminder-duplicate-removal
tags:
- Bash
- Linux
- Shell
title: Line Parsing Reminder (Duplicate removal)
---
So, say you have a long list of instruction (like multiple apt-get install lines) and you want to eliminate common words?

Easiest way to do it is (assuming you have all of the instrustions in "list.txt")

[FYI the '\' character indicates a continuation of a single line ]

> cat list.txt\

| tr ' ' '\n' \            #Expands all space characters to new lines

| sort | uniq \    #sorts each line, and then eliminates duplicates

| tr '\n' ''               #turns all the new-lines into spaces

Depending on the actual content, it may be necessary to remove specific entries, (such as apt-get or sudo). Thats an exercise for the reader.
