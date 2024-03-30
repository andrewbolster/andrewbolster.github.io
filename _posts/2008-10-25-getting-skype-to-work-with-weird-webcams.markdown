---
author: admin
categories:
- Instructional
comments: false
date: 2008-10-25 21:45:00+00:00
layout: post
slug: getting-skype-to-work-with-weird-webcams
tags:
- Ubuntu
- linux
- jaunty
- lib32v4l-0
- lib32v4l-dev
- cheese
- v4l1
- '8.10'
- ubuntu
- webcam
- skype
- v4l2
title: Getting Skype to work with weird webcams.
---


I'll keep this as informative.
If your webcam works in ubuntu (I'm running the 8.10 RC atm, fantastic btw) under cheese but not with skype, I did a bit of digging and cheese uses v4l2 (the 'new' webcam api) which inherently screws up skype that uses v4l1.

So, its easy enough since i came across [this post](http://forum.skype.com/index.php?showtopic=218861&view=findpost&p=995701) and after chasing up my own system locations (this guy must be on 64bit, but i didnt ask) dead easy, instead of in the terminal going
# skype
**UPDATE:25/4/9**

After a fresh install  jaunty i discovered i was missing a step

Need to install lib32v4l-0 and lib32v4l-dev (i think the -dev is unnessary but i install them anyway)

look in your library directories (/usr/lib/ or /usr/lib32/) for v4l1compat.so,

eg " find /usr/lib\* -name '\*v4lcompat.so' "
{%highlight bash%}
# LD_PRELOAD=/path/to/v4l1compat.so skype
{%endhighlight%}
this, obv, preloads that library forcing skype to use teh right interface library.

If my explanation is wrong please correct me
