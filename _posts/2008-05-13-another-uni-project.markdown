---
author: admin
comments: false
date: 2008-05-13 19:47:00+00:00
layout: post
slug: another-uni-project
title: 'Another Uni Project '
wordpress_id: 13
categories:
- Uni
tags:
- C
- code
- programming
- telecomms
---

If anyone is interested in [Erlang B](http://en.wikipedia.org/wiki/Erlang-B) Calculations, very relevent to any communications or engineering students, I've written a little quick piece of code to calculate them.

There are several levels of functionality in the code.
Erlang B itself only has 2 variables,  System load in Erlangs, and the number of "trunks" (read: servers/call center operators/phone lines), and its output is a blocking probability from 0 to 1

All three of these variables or none atall can be defined at runtime;



	
  * The desired blocking probability can be input to stop the calculation at that point. (default 0)

	
  * The Load can be defined (See[ Erlang A](http://en.wikipedia.org/wiki/Erlang_unit)) (default 1)

	
  * The maximum trunks to be calculated (default 100)


The code uses the unistd.h library for argument parsing so is more or less unix only (or cygwin alternativly) and long doubles for more or less everything inside the code.

Having tested the limits, it kinda conks out then calculating large (read 1000 erlangs) on large trunks (got as far as 1234 trunks, then died)

When i get a bit of time i might optimise the factorial part so it doesnt run thru the entire factorial sequence for each number.

Anyway, the code is[ here.](http://andrewbolster.info/scraps/ErlangB.c) I'm not wasting my time laying out code on blogger.

