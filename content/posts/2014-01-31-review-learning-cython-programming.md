---
category: ''
description: ''
layout: post
tags:
- C/C++
- 'Data Science'
- MATLAB
- NumPy
- PhD
- Python
- 'Software Development'
title: 'Review: Learning Cython Programming'
---


About 6 months ago now, I had the pleasure of getting [Phil Herron](http://redbrain.co.uk/) to talk at the [Farset Labs](http://farsetlabs.org.uk) [PyBelfast](http://twitter.com/pybelfast) group about his work in GCC/Cython fron end optimisation work, which was simultaneously waaaaay over my head and really interesting.

I've been a 'Python Primary' software engineer now for about 5 years, in web-dev, infrastructure monitoring, data analysis, and scientific computing, with some esoteric stuff involving small-vector linear algebra optimisation on GPU CUDA, Matlab bridging with Octave / Oct2Py, and distributed state systems. But somehow, I've managed to dodge hardcore [Cython](http://www.cython.org).

So, when I got a chance to have a nosy at Phils ["Learning Cython Programming"](http://www.packtpub.com/learning-cython-programming/book) in exchange for selling my soul to Packt, I jumped at the chance.

But, what is Cython: The first line of the book (well, preface) sums it up;

> Cython is a tool that makes writing C extensions to Python as easy as writing Python itself

For most people this doesn't really make any sense, but the performance benefits of wrapping up intensive or 'quirky' C/C++ into a module that you can interact with sanely in Python world is immense.

I don't want to spoil the book, because after getting a chance to play most of the way through fairly methodically, I'd highly recommend it if you fall into any of the below categories:

* You deal with 'charmed' systems (legacy, restricted, 'mission critical') but need to improve your integration workflow.
* You work regularly in/with both C/C++ and Python, or would like to
* You work with systems or hardware that requires interface functionality that exists in C but not in Python
* You deal with numerically sensitive operations and while Python is attractive, you don't have the unittests to verify a reimplementation
* You deal with massive data analysis in weird ways and every ounce of performance is needed
* You like programming

This book is not for you if you don't know Python _and_ C/C++ to a reasonable level. This isn't a language guide, and infact, as Cython itself blurs the language barrier between Python and C, it can be quite difficult at times to remember where the line is anymore!

Phil makes the book really approachable, with a great (multi-platform!) introduction, provides all his sources as a well laid out [GitHub repo](https://github.com/redbrain/cython-book) and while I disagree with his [choice in editor](http://en.wikipedia.org/wiki/Editor_war), the style and pace of the first few chapters is great for blitzing through in a half-hour (particularly impressed by the vertical integration of the `logging` and `ConfigParser` modules in Cython).

I was expecting this to be a book steeped in abstraction and language features. But Phil has managed to combine realistic and relatable examples (Multiple Messaging, Extending Tmux, Unittesting C-shared libraries, etc), while also constantly drawing comparisons and links between the language sets to make sure that whether you're primary-Python or primary-C developer, you can still keep track.

Now, I'm off to go and see if I can reimplement some of my PhD code under cython, since Chapter 6 tells me that [cython and numpy](https://github.com/cython/cython/wiki/tutorials-numpy) play quite well together... I may be some time.
