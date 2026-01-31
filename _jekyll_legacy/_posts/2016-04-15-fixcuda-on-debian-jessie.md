---
category: ''
description: ''
layout: post
tags:
- Ubuntu
- Debian Jessie
- Linux
- Operating System
- Package Management
- GPU
- NVIDIA
- Graphics
- CUDA
- Programming
title: FIX:CUDA on Debian Jessie
---

{% include JB/setup %}


Hopefully a super quick one (while I'm procrastinating from procrastinating).

Debian Jessie is a lovely operating system until you try and do anything with it. Lots of Package deprecations etc etc etc.

Anyway, I've got a [history](/2011/04/lu-decomposition-in-c-and-under-cuda) with GPU stuff and I've been playing with integrating it into some of my [research](/2014/05/so-what-is-it-you-do-again), but in a bout of insanity I decided while I'm over in Liverpool (for another 4 hours) to wipe my old workstation and bring it over from Ubuntu 15.04 to Jessie (which I've been using on my main laptop for a while now).

This was painful. Basically, NVIDIA somewhere along the line deprecated the whole Debian base-family (even if it's [derivitives](http://www.ubuntu.com/) are supported). But we can rebuild it, we have the technology!

# The Problem

~~~
bolster@yossarian /usr/local/cuda/samples/2_Graphics/Mandelbrot  
➜   make  
>>> WARNING - libGL.so not found, refer to CUDA Getting Started Guide for how to find and install them. <<<
>>> WARNING - libGLU.so not found, refer to CUDA Getting Started Guide for how to find and install them. <<<
>>> WARNING - libX11.so not found, refer to CUDA Getting Started Guide for how to find and install them. <<<
[@] /usr/local/cuda-7.5/bin/nvcc -ccbin g++ -I../../common/inc -m64 -gencode arch=compute_20,code=sm_20 -gencode arch=compute_30,code
=sm_30 -gencode arch=compute_35,code=sm_35 -gencode arch=compute_37,code=sm_37 -gencode arch=compute_50,code=sm_50 -gencode arch=comp
ute_52,code=sm_52 -gencode arch=compute_52,code=compute_52 -o Mandelbrot.o -c Mandelbrot.cpp
~~~
{:lang="bash"}

Even though I do have these packages, and have updated my `LD_LIBRARY_PATH`, etc. etc.

# The Guide

[Extended from this brilliant answer on Stack Exchange by einpoklum](http://unix.stackexchange.com/questions/218163/how-to-install-cuda-toolkit-7-x-on-debian-8-jessie-or-9-stretch)


    sudo apt-get install gcc g++ gcc-4.8 g++-4.8 gcc-4.9 g++-4.9 libxi6 libxi-dev libglu1-mesa libglu1-mesa-dev libxmu6 linux-headers-amd64 linux-source freeglut3-dev

Then

* `wget http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/cuda_7.5.18_linux.run`
* `chmod a+x cuda_*.run`
* Drop into a root shell
* `bash cuda_*.run`

Yes yes yes and install the things wherever you like them. The problem comes when trying to build the sample projects.

# The Fix

The problem is the `findgllib.mk` "helper" file use by all of the sample projects. Basically, with Debian, some key variables never get assigned, and theres no "catchall" fall-down case in the logic, so they end up blank which, well, screws things up.

YMMV but in my case, the location of the missing libraries was `/usr/lib/x86_64-linux-gnu. This can be found using the `locate` command


~~~
➜   locate libGL.so  
/usr/lib/libGL.so.1
/usr/lib/x86_64-linux-gnu/libGL.so
/usr/lib/x86_64-linux-gnu/libGL.so.1
/usr/lib/x86_64-linux-gnu/libGL.so.352.39
bolster@yossarian ~/NVIDIA_CUDA-7.5_Samples/2_Graphics/Mandelbrot  
➜   locate libGLU.so  
/usr/lib/x86_64-linux-gnu/libGLU.so
/usr/lib/x86_64-linux-gnu/libGLU.so.1
/usr/lib/x86_64-linux-gnu/libGLU.so.1.3.1
bolster@yossarian ~/NVIDIA_CUDA-7.5_Samples/2_Graphics/Mandelbrot  
➜   locate libX11.so  
/usr/lib/x86_64-linux-gnu/libX11.so
/usr/lib/x86_64-linux-gnu/libX11.so.6
/usr/lib/x86_64-linux-gnu/libX11.so.6.3.0
~~~
{:lang="bash"}

So, take your `$LIBRARY_PATH` and place it in a copy of the `findgllib.mk` file somewhere;

`cp /usr/local/cuda/samples/common/findgllib.mk /tmp/`

Edit it in your favourite editor to add the following lines before the commented line `# find libGL, libGLU, libXi, `

~~~
GLPATH ?= /usr/lib/x86_64-linux-gnu
GLLINK ?= -L/usr/lib/x86_64-linux-gnu
DFLT_PATH ?= /usr/lib
~~~

But as I said, there's a version of this file for every sample project, which is a bit pointless IMO, but we can fix that easily enough by replacing them all

`find /usr/local/cuda/samples/ -name "findgllib.mk" -exec cp findgllib.mk '{}' \;`

And boom, all the samples should build.
