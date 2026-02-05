---
categories:
- Instructional
comments: true
date: 2013-05-03 08:14:50+00:00
slug: fix-dell-laptops-and-workstations-not-rebooting-restarting-system
tags:
- Linux
- Ubuntu
title: 'Fix: Dell Laptops and workstations not rebooting ("Restarting System")'
---

Had an interesting if annoying problem recently that I assumed would just fix itself eventually. But when you're sick of prodding a power button to force a machine to reboot, you gotta do something.

TL;DR**_ if you're getting messages like "`Restarting System`" on an attempted reboot, try setting the `reboot=pci` kernel boot flag_**

To do this, at the grub boot menu, press `e` to edit the current boot parameters. Find the line starting with "`linux`" (this is the line that actually kicks off the linux kernel) and at the end of that line, put "`reboot=pci`".

Then boot normally (`F10`) and try rebooting. It *should* work this time.

To make the change permanent, add the "`reboot=pci`" flag to the "`GRUB_CMDLINE_LINUX`" line of `/etc/default/grub`.

And tada! Reboot problems solved. Please comment on what machines you've needed to use this on. This is currently listed as a bug

**Sources and Extra Info:**

This has affected a lot of people, on Dell Laptops, Desktops, and servers. It appears to be predominantly a [64 bit problem](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/833705) and is not specific to just [Ubuntu](https://bugs.archlinux.org/task/30136).

At the time of writing I was on Raring, but had been on Oneric for ages, and even though the listed bug was 'fix released', it wasn't fixed for me. YMMV
