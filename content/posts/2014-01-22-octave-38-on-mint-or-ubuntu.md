---
category: ''
description: ''
tags:
- Installation
- MATLAB
- 'Open Source'
- Python
title: Octave 3.8 on Mint (or Ubuntu)
---


My work has be flittering between Python and Matlab recently, and lets say I'm not a massive fan of Matlab at the best of time, and VM matlab isn't the most performant thing in the world.

So I was happy to hear that [`octave`](http://www.gnu.org/software/octave/index.html), an open source, Matlab compatible analysis framework have started testing their GUI.


# Package Requirements
~~~ shell
sudo aptitude -y build-deps octave
sudo aptitude -y install gfortran libgfortran3-dbg-arm64-cross liblapack-dev libblas-dev libarpack2-dev llvm-dev libfltk1.3-dev libglu1-mesa-dev libcurl4-gnutls-dev libfreetype6-dev libqt4-dev libfontconfig1-dev libfftw3-dev libqrupdate-dev libqscintilla2-designer texlive
~~~

# Download
I used `/dev/shm` as the build directory as it's effectivly a RAM disk, but YMMV.

`curl ftp://ftp.gnu.org/gnu/octave/octave-3.8.1.tar.gz | tar -xvzf - -C /dev/shm/; cd /dev/shm`

# Configure

I'm on a 64 bit machine with 4 real-cores, so I wanted openmp but *do not enable 64bit addressing*, it doesn't work at the minute. Both of these features are experimental and YMMV. If someone  comes up with a fix for 64bit, let me know.

Due to the way that `configure` looks for the [blas and lapack libraries](http://stackoverflow.com/questions/16363157/install-octave-no-root-missing-blas-and-lapack), you have to tell it where to go.

`./configure --enable-openmp --with-blas=/usr/lib/libblas/ --with-lapack=/usr/lib/liblapack/`

# Make
May as well use all the cores for compilation
`make -j4; make check`

# Install
This is the only operation that needs `sudo`

`sudo make install`

You'll need to add `/usr/local/bin/` to your path in whichever fashion you prefer.

# Kickoff

`/usr/local/bin/octave --force-gui`

Enjoy some "tasty" Matlab style editing. If you break it it's not my fault!
