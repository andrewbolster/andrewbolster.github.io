---
author: admin
comments: true
date: 2010-05-31 14:29:03+00:00
layout: post
slug: automagic-kernel-cleaning-under-ubuntu
title: Automagic Kernel Cleaning under Ubuntu
categories:
- Instructional
tags:
- bash
- boot
- code
- linux
- programming
- software
- Ubuntu
- workstation
---

Sick of having dozens of old kernels sitting under your /boot/ dir? Want a simpler boot-life? Well we've got the solution for you. 

Just one course of [cleankernel](http://andrewbolster.info/scraps/cleankernel) once an upgrade cycle will remove all previous kernel entries from your bootloader and /boot/ dir.

Basically, it lists what kernels you currently have in your /boot/ and removes them using [apt](http://en.wikipedia.org/wiki/Advanced%20Packaging%20Tool) .
