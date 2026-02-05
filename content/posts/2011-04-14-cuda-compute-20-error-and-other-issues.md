---
aliases:
- /2011/04/cuda-compute-20-error-and-other-issues/
- /2011/04/cuda-compute-20-error-and-other-issues.html
categories:
- Instructional
comments: true
date: 2011-04-14 11:48:01+00:00
slug: cuda-compute-20-error-and-other-issues
tags:
- C/C++
- CUDA
- GPU
- Programming
title: CUDA Compute 20 Error and other issues
---
There's a quirk of using older CUDA drivers is that  the latest [NVIDIA SDK code examples](http://developer.download.nvidia.com/compute/cuda/sdk/website/samples.html) are not backward compatible, i.e compiling the 3.0 SDK against the 2.3 toolkit (that I've spent the last day doing) is a fools errand (Thanks very much to @thebaron on #cuda on freenode and tkerwin on [StackO﻿verflow](http://stackoverflow.com/questions/3047909/nvidia-cuda-sdk-examples-compilation-unsupported-architecture-computer-20).)

Basically, the 3.x drivers reclassify newer cards based on the; previously, the 'compute' value (a measure of [OpenCL](http://en.wikipedia.org/wiki/OpenCL) adherence) would max out at 1.3, but now the range is extended up to 2.0, but the 2.3 toolkit does not recognise this value, so craps out.

`nvcc fatal   : Unsupported gpu architecture 'compute_20'`

The first solution is to try to use the 2.3 SDK instead, and thankfully, NVIDIA keeps a tidy library of back-releases. But upon installation of the [2.3 SDK](http://developer.nvidia.com/object/cuda_2_3_downloads.html), a new problem appeared. Lack of OpenGL Libraries... Unfortunately the machine I'm working on isn't exactly standard issue so I'll be asking the maintenance team to check it out on my behalf.

The secondary fix is to force nvcc to to use the older 1_3 capabilities in the makefile of the problematic kernels;

`# CUDA source files (compiled with cudacc)
CUFILES_sm_13		:= *.cu
`

There are a variety of these CUFILES_sm_XX clauses for different capabilities. Dig around the ../sdk/C/common/common.mk file for more hints.

PS This is a really old draft I found disgarded in my queue, so excuse me if this is very out of date.
