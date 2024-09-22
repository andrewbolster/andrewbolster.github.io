---
category: ''
description: ''
layout: post
tags:
- spherical surface
- PhD work
- numpy
- random walk
- behaviours
- StackOverflow
- virtual submarines
- Python
title: Generating a unit 3 vector in Python (Uniform Spherical Projection)
---

{% include JB/setup %}

Quick one more as a reminder to me than anything else.

As part of my PhD work I'm building different behaviours for virtual submarines. I'll be explaining some parts of my work in a separate post, but basically, I needed to random walk. Random walk in 2 dimensions is easy; pick two random numbers, go that way. Unfortunately [doesn't work that way on a spherical surface](http://hbfs.wordpress.com/2010/10/12/random-points-on-a-sphere-generating-random-sequences-iii/)

So to make things easier, I stole [this StackOverflow answer from dmckee](http://stackoverflow.com/a/5408843/252556) and tidied it up a bit for my purposes. (Assuming everyone else is like me and does `import numpy as np`)

{% gist 10274979 %}
