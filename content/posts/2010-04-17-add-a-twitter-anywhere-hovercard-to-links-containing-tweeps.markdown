---
categories:
- Instructional
comments: true
date: 2010-04-17 21:13:04+00:00
slug: add-a-twitter-anywhere-hovercard-to-links-containing-tweeps
tags:
- JavaScript
- 'Social Media'
- 'Web Development'
title: Add a Twitter @anywhere hovercard to links containing tweeps
---


Everyone and their dog has a walkthrough of adding @anywhere hovercards to your blog. But the default has a small failing that irked me when I was re-doing my Blogroll (check them out, they're all great! I promise!), and that was that if you take a tweep, like @god for example, it'll happily wrap the hovercard around it, but if you have a link to this [great status that @god posted](http://twitter.com/god/status/11603782129), @anywhere won't pick this @god up.

Quick and dirty solution; add the following code-block inside your


    onAnywhereLoad(twitter)

section of script.

>

>
>     twitter("a").hovercards({
>     infer=true
>     });
>
>

Then thats you done! No muss, no fuss.
Thanks go to @stuartgibson for help.
If I've missed anything, scream at me in the comments or @bolster

**Update**
Of course I'd missed something; this unfortunately makes @anywhere inspect every link on your site, including navigational ones, so for my usecase (blogroll), i modified my code to only infer when inside the id of my blogroll, ie

>

>
>     twitter("#linkcat-2 a").hovercards({
>     infer=true
>     });
>
>

YMMV
