---
categories:
- Instructional
comments: true
date: 2011-07-28 10:22:56+00:00
slug: the-road-to-coreboot-part-the-first-introduction
tags:
- AMD
- EeePC
- Embedded Systems
- IRC
- Open Source
- embedded systems
title: 'The Road to Coreboot, Part the First: Introduction'
---

![Coreboot Logo](https://coreboot.org/assets/images/banner.svg)

So as part of my [IAESTE](http://iaeste.ch) placement with [PC Engines](http://www.pcengines.ch/), I'm investigating the possibility of them making a new board based around the AMD [Fusion](https://en.wikipedia.org/wiki/AMD_Fusion) series of APU's  (CPU+(something else, usually GPU) on single die) and for that board to work with the Open Source [Coreboot](http://www.coreboot.org/) BIOS. This is my story.

Disclaimer

I am not a hardware guy, and have never done any pre-OS x86 hardware programming. This will bore
the pants of anyone who is an x86 expert, but hopefully some will find it useful and will contribute to the Coreboot project.

# Part The First: Intro

My particular board ([MS 7698 / E350IA-E45](http://www.msi.com/product/mb/E350IA-E45.html)) is not supported by the Coreboot project (yet), but after some investigation, most of the components on the board are, so in theory it should be a case of chopping existing board definitions up and reusing them to make my life easy (that's always the dream)...

But first, some explanation of whats going on.

Most x86-architecture PC's have three major components; [CPU](http://en.wikipedia.org/wiki/Central_processing_unit), [Chipset](http://en.wikipedia.org/wiki/Chipset), and [SuperIO](http://en.wikipedia.org/wiki/SuperIO). Most people are pretty confident about the first, and aware of the second, but not many know about the last.

[![Motherboard Diagram](http://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Motherboard_diagram.svg/1000px-Motherboard_diagram.svg.png)](http://en.wikipedia.org/wiki/Motherboard)

I'll skip CPU for simplicity, but the chipset usually consists of two devices; north-bridge and south-bridge. (Note: I've had 5 years of electronics and software education and this project has taught me more about computer architecture than any of that; the case for open source dev work in universities?...).

Put simply, [North-bridge](http://en.wikipedia.org/wiki/Northbridge_(computing)) is a blisteringly fast (many Gbps) interconnect between the CPU, main memory, and (usually) graphics adapters. Since as we'll see, this interface is largely interal, one doesn't need to do to much to 'wake up' the Northbridge specifically.

The South-bridge on the other hand, is usually a hundred Mbps, and handles almost all of the 'lower rate' interfaces such as PCI, IDE, SATA, USB, etc. Of particular interest is the LPC Bus, shown in the diagram. This [Low-Pin Count](http://en.wikipedia.org/wiki/Low_Pin_Count) interface connects the South-bridge to not just the BIOS, but also, to the SuperIO controller.

The [SuperIO](http://en.wikipedia.org/wiki/Super_I/O) device looks after a range of low-bandwidth, low level interfaces like Serial, etc.

Now, that's simple enough when you're thinking in a CPU-centric perspective; if the CPU needs to send something out the Serial port, it hands it to the NB, which passes it to the SB, which sends it out the serial port via the SIO. [Simples](http://www.youtube.com/watch?v=Hl545RF6dXA)!

But what happens when you push the button on the front of your machine? Peter Stuge does a good introduction to this (and Coreboot in general) in his[ CCC26 Talk](http://events.ccc.de/congress/2009/Fahrplan/events/3661.en.html), but the long story short is that the power switch wakes up the BIOS; the BIOS wakes up the SIO and (hopefully) the SB, which in turn wakes up the on-board controllers and the NB which eventually initialises the memory controllers, CPU, and all that good stuff. (Peter does a much much better job at explaining this than I do...).

And there in lies my problem: guess which part of this ecosystem of components is currently _completly_ unsupported by Coreboot? The first thing the BIOS touches... the SIO.

**Incoming Ranty bit, feel free to skip**

This means that if I take the stock Coreboot ROM for a board that is _fairly_ close to mine, it falls at the first hurdle and is completely useless.Oh, and to make matters worse; the chipset on this particular board does not allow booting off LPC, so the nice fast flashrom-to-second-LPC-chip doesn't work (I discovered this after soldering three different TPM/LPC adapters...), and instead I've had to desolder the SPI BIOS off the motherboard, reset it in a chip holder and use a universal serial programmer, which is slow as all hell...

**/RANT**

Anyway, after discussing with the very helpful #coreboot IRC channel, they suggested that I first work on getting the SIO recognised by (the[ even more unsupported](http://www.coreboot.org/Superiotool)) SuperIOTool, which queries device registers on the SIO and compares them against known 'default' values. Thats the next fun project, but I'll leave it at the for today...
