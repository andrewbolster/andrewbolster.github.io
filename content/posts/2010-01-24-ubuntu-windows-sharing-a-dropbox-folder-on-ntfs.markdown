---
author: admin
categories:
- Instructional
comments: true
date: 2010-01-24 07:25:40+00:00
layout: post
slug: ubuntu-windows-sharing-a-dropbox-folder-on-ntfs
tags:
- Ubuntu
- windows
- linux
- workstation
- file system
- ntfs-3g
- HDD
- operating system
- networking
- dual-boot
- hard drive
- fstab
- mounting
- symbolic link
- internal drives
- storage
- dropbox
- software
title: Ubuntu / Windows Sharing a Dropbox folder on NTFS
---


Take one Dual-Boot laptop, with three partitions:
/dev/sda1:Windows File System
/dev/sda2:[Linux](http://www.ubuntu.com/GetUbuntu/download) File System
/dev/sda3:Data Partition

I already had [Dropbox ](https://www.dropbox.com/referrals/NTM2OTc3NTg5)installed on the Windows side and didn't want to have things duplicated on the linux side, problem is Ubuntu currently does not mount internal drives automatically on boot, so every time I fired up Ubuntu, I had to re-mount the drive, password and all.

Easy enough fix: Make a new /etc/fstab entry for the shared drive and define a mount point.

>/dev/sda3 /media/Shared ntfs-3g defaults,locale=en_GB.UTF-8 0 0

Then change your [Dropbox](http://https://www.dropbox.com/referrals/NTM2OTc3NTg5) location to wherever you have the folder under /media/Shared/ (or as I do and just [symbolically link it ](http://kb.iu.edu/data/abbe.html)to under your Home folder, This is also a good idea because Windows defaults to calling the Dropbox folder "My Dropbox" whereas in \*nix its simply "Dropbox")

Last but not least

> sudo umount /dev/sda3

sudo mount /media/Shared

dropbox start

Then just enjoy the 2.5Gb of hard disk you just saved.
