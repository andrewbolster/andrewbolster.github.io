---
author: admin
comments: false
date: 2009-07-13 08:49:40+00:00
layout: post
slug: delayed-post-how-i-installed-windows-7-from-usb-hdd
title: 'Delayed Post: How I Installed Windows 7 From USB HDD'
categories:
- Instructional
tags:
- HDD
- ISO
- laptop
- lenovo
- USB
- Windows 7
---

As was noted in my [LENOVO ROCKS](http://www.andrewbolster.info/?p=151) post, I recieved a virgin hard drive for a laptop with no disk drives.

This is a problem that has been[ long solved in Linux Distros](http://www.google.com/search?q=linux%20install%20from%20USB&hl=en&safe=off&num=100&output=search&tbs=tl:1&tbo=1) but is not so good for Windows, but i did find[ this brilliant guide by Sandip](http://www.blogsdna.com/2016/how-to-install-windows-7-from-usb-drive-without-windows-7-iso-dvd.htm) from earlier this year, i just wanted to point out a few difference that i made to the process that i think make it slightly more transparent whats going on.

	
  1. Get a USB drive > 4GB

	
  2. Use The Disk Managment pane in Computer Managment (Control Panel > Administrative tools)

	
  3. Find your drive and right-click > Format the partition as NTFS

	
  4. Once its formatted, right click it again and 'Mark Partition as Active'

	
  5. Use a image mounter such as [WinCDEmu](http://wincdemu.sysprogs.org/) to mount the Windows 7 image

	
  6. Drop into a cmd prompt and navigate to the drive where the Window7 image is mounted, cd to 'boot' and execute 'bootsect /nt60 X:' where X: is the drive letter the target partition is mounted on.

	
  7. Copy the contents of the mounted Windows 7 image to 'X:'

	
  8. Reboot and if you dont know how to boot from a USB drive, you probably arn't reading this, [but if not...](http://lmgtfy.com/?q=boot+from+usb)

I know  there are alternative methods for doing this in Linux, but since i didnt use them in this instance, i cant comment on them.

FYI: Windows 7 is now my full time OS, and frankly im suprised; Theres a few things I miss, like a nice easy command line networking, SSH built in, a decent X11 server, but for a  all round notes/documentation/lil-bit-o-code machine, the Tableting pros few  out-weigh the cons. E.G [The wonderous marvelous stupendous Math Input Panel that outputs in MathML!](http://www.gottabemobile.com/2008/10/29/windows-7-math-input-panel-screenshots/)
