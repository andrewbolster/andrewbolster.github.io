---
category: code diary
description: ''
layout: post
tags:
- code
- niceness value
- Monte Carlo simulation
- random number generation
- multiprocessing
- simulation
- python
- parallel processing
- Unix
title: Multiprocessing Niceness in Python
---


Quick and dirty one that tripped me up.

Recently I've been doing lots of [multiprocessing](https://docs.python.org/2/library/multiprocessing.html) and [joblib](https://pythonhosted.org/joblib/)-based parallel processing, with loooong simulation times.

In an effort to make sure that my machine was still useable during these runs, I changed the ['niceness'](http://en.wikipedia.org/wiki/Nice_(Unix)) value of the spawned processes... or so I thought.

```python
import os
...
def thread_mask(args):
    # Properly Parallel RNG
    #http://stackoverflow.com/questions/444591/convert-a-string-of-bytes-into-an-int-python
    myid=current_process()._identity[0]
    np.random.seed(myid^struct.unpack("<L",os.urandom(4))[0])

    os.nice(5)

    return long_simulation(args)
```

First part is a handy way to make sure that your subprocess simulations actually use different random numbers.... which for [Monte Carlo style simulation](http://en.wikipedia.org/wiki/Monte_Carlo_method) is pretty damned important...

But, simple enough `os.nice` call. I reads like it says "Set the niceness value of this process to 5".

It does not, it _[Increments](https://docs.python.org/2/library/os.html#os.nice)_ the niceness value. (And returns the new value)

This means that after a few repeated iterations of this simulation, my processes end up with the maximum niceness (i.e. least priority) of 19. Which is not ideal.

Simple enough fix however; swap the `os.nice(5)` call with:

```python
    # Be Nice
    niceness=os.nice(0)
    os.nice(5-niceness)
```
