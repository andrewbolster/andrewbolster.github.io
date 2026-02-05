---
aliases:
- /2010/03/chmod-on-lots-of-files/
- /2010/03/chmod-on-lots-of-files.html
categories:
- Instructional
comments: true
date: 2010-03-23 22:42:20+00:00
slug: chmod-on-lots-of-files
tags:
- Bash
- Embedded Systems
- Linux
- Storage
- file management
title: Chmod on lots of files
---
My lil-NAS has plenty of space but is maddeningly underpowered.

I came across a permissions issue where, depending on how the files in question got there, they would not be accessible to my windows boxes because they were owned by root (I have no doubt that its my fault!)

So, first attempt was nice and easy.

>

>
>     $chown -R smbusr:smbusr *
>
>

But this was taking a horrific amount of time, so I thought "There must be a better way".

Chown does whatever you tell it to do, whether its needed or not. So why not check that first with 'find'.

>

>
>     $find . -user badnastyawkwarduser -exec chown -R smbusr:smbusr {} \;
>
>

and it worked brilliantly!

If you have any shortcuts, let me know in the comments!
