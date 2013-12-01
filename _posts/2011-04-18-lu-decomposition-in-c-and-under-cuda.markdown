---
author: admin
comments: true
date: 2011-04-18 13:00:23+00:00
layout: post
slug: lu-decomposition-in-c-and-under-cuda
title: LU Decomposition in C (and under CUDA)
categories:
- Instructional
tags:
- C
- cuda
- gpu
- linalg
- Meng
- programming
---

As part of any major project, it occasionally happens that you assume something is a 'solved problem' when its really not.

In my case it was solving small linear systems, of the form Ax=B, where A is an nxn matrix, B is a n vector. This is a problem that's been solved in libraries such as [LAPACK](http://www.netlib.org/lapack/), [LINPACK](http://www.netlib.org/linpack/), [BLAS](http://www.netlib.org/blas/), etc etc.

The issue appears when you're trying to do this stuff within a specific hardware environment ([CUDA](http://www.andrewbolster.info/tag/cuda/)), and you cannot call host functions from the device, and the [cuBLAS](http://www.gsic.titech.ac.jp/~ccwww/tebiki/tesla_e/tesla5_e.html) libraries cater only to large matrices processed in parallel

Anyway, without going into architectural specifics, say for whatever reason you needed a small dense matrix solver, including [LU Decomposition](http://en.wikipedia.org/wiki/LU_decomposition) with maximal (or complete) [pivoting](http://en.wikipedia.org/wiki/Pivot_element#Partial_and_complete_pivoting) for numerical stability, here it comes.

Before I code dump, I have to give serious thanks to all the folks on the stackexchange network for their help in this, especially [talonmies](http://stackoverflow.com/users/681865/talonmies) who seemed to pop up in every question I had!

Moving on; I've got two versions of this code; one is my cpu-bound experiments, and the second is my 'proof of concept' gpu code implementing the cpu bound algorithm. I know its not parallelised and I'm probably missing lots of optimisation tricks, but it works.

[CPU](http://paste.ubuntu.com/595501/) ([ALT](http://pastebin.com/Kz8CKZS7))

[GPU](http://paste.ubuntu.com/615403/) ([ALT](http://pastebin.com/jEvJDmdt))

I had a serious amount of pain to understand this problem, so hopefully this will make someone elses life easier.

Today you, tomorrow me.
