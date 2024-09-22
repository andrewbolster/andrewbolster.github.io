---
author: admin
categories:
- Commentary
- Instructional
comments: false
date: 2009-02-15 20:05:33+00:00
layout: post
slug: hacking-weekend
tags:
- packet capture
- Aircrack
- linux
- wesside-ng
- Backtrack 4
- WEP
- desktop
- airodump-ng
- arp attacks
- subversion
- Wireless
- remote
- aireplay-ng
- software
title: Hacking Weekend
---


So, I've been experimenting over the weekend with [Backtrack 4](http://www.remote-exploit.org/backtrack_download.html). My... Lord....

Times have changed, it used to be that if you wanted to mess with WEP you have to go thru a dozen intermediate stages.[ wesside-ng](http://www.aircrack-ng.org/doku.php?id=wesside-ng) makes life so much simpler.30 minutes, fully automated.

What i had done previously was [manual ](http://www.neophob.com/serendipity/index.php?/archives/62-WEP-Cracking-with-Aircrack.html)airodump-ng, aireplay-ng with arp attacks, and then shifting the caps onto my big box to crack inside of 10 seconds, pity is the packet capture on a quiet network can take a day.

Also, if you cant be assed with the whole Backtrack thing. the whole thing can be swiped from the subversion repo


    svn co http://trac.aircrack-ng.org/svn/trunk/ aircrack-ng

Its been a long day.
