---
author: admin
categories:
- Commentary
comments: true
date: 2010-03-24 16:39:16+00:00
layout: post
slug: my-experience-with-ubuntu-10-04-lucid-lynx
tags:
- Ubuntu
- workstation
- Lucid Lynx
- Ubuntu fan
- Launchpad
- live CD
- install
- lucid
- lynx
- hardware
- serverfault
- rant
- '10.04'
- installation troubleshooting
- daily build
- bug report
- linux
- boot issues
- beta
title: My Experience with Ubuntu 10.04, Lucid Lynx
---


**Updates(26/3/10): **Thought I'd give the liveCD another go (this  time using the dailyx64 image and using [unetbootin](http://unetbootin.sourceforge.net/)), thinking  it must be something simple; so during boot i just kept pressing escape,  before the splash screen came up. This got me around the splash screen  issue and it seems as if everything is fine. Also, I found a matching [bug report](https://bugs.launchpad.net/xsplash/+bug/539020) on launchpad, but no resolution as of yet. Guess we'll have to wait and  see.

**Updates(25/3/10): **With the greatest thanks to the guys at [serverfault](http://serverfault.com/questions/125950/ubuntu-10-04-install-frozen-at-splash-no-errors),  I've still not been able to fix this issue, and will be lodging a bug  report to [launchpad](https://launchpad.net/ubuntu) whenever I get a  chance

I'm a big Ubuntu fan; have been since my first Dapper Drake install, but I have never had such weirdness as I've had so far with Lucid.
I am at a loss to explain or even describe the trouble I've had with this.

First off, I tried the amd64 alternate daily build; did the usual cd verification et al, got half way through the installation, and the install crapped out due to mixed up dependencies inside the openoffice.org package.

Thought 'eh, its a daily build, no worries', and picked up the regular beta amd64 alternate disk; install blew through, restarted aaaaaaaand I'm presented with the lovely purple splash screen telling me my disks need to be checked, fair enough, but the lack of any kind of process indication irked me, but it was late in the night so i thought, 'screw it, i'll be done by morning'. Lo' an behold, i awake to exactly the same screen.

I can't access any of the background consoles (ctrlalt F1, F2, etc), but i figure, this early in the boot process they're probably not started yet.

So i figure, try the regular desktop build. So download, hashcheck, boot.... boot.... ummm. nope - I have the very tasteful purple splash screen of the livecd booting up, and thats it. No motion, no activity, and most importantly no error messages.

Has anyone else seen anything like this or am i cursed?

As for 'Have you checked the hardware' Memtest says I'm fine, and the ubuntu install i had in before was fine, I've changed every conceivable ACPI setting in the BIOS just in case, and still nothing.
