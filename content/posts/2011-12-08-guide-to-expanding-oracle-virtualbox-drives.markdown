---
categories:
- Instructional
comments: true
date: 2011-12-08 12:01:43+00:00
slug: guide-to-expanding-oracle-virtualbox-drives
tags:
- Linux
- Windows
- virtualbox
- virtualisation
title: Guide to Expanding Oracle Virtualbox Drives
---


The Idiot Proof Guide for Windows-host, \*-guest setup. (Ubuntu in my case, and should work for any host)


  1. Make sure you're working with a VDI, not a VDMK (if not, File>Virtual Media Manager right-click, Copy)


  2. Drop into a command line (on windows, press Win+R, type 'cmd') and navigate to the Virtualbox directory (won't need to do this on \*nix)


  3. Execute `VBoxManage _path_to_your.vdi_ --resize _new_size_in_MB_`


  4. Download [UBCD](http://www.ultimatebootcd.com/download.html) and mount it as a DVD to your VM


  5. Boot into the live DVD (F12 -> c on Oracle Boot Screen)


  6. Select 'Parted Magic', and open GParted once it boots


  7. Manipulate and resize to your hearts content


  8. Reboot and enjoy the space!
