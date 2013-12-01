---
author: admin
comments: true
date: 2010-07-08 19:53:40+00:00
layout: post
slug: intel-4965-poor-wireless-performance-under-ubuntu
title: 'Intel 4965: Poor wireless performance under Ubuntu'
categories:
- Instructional
tags:
- compat-wireless
- drivers
- intel
- iwlagn
- lenovo
- Ubuntu
- wifi
- Wireless
---

I had an incident recently where the [Windows 7](http://www.youtube.com/watch?v=XaqaDZZ_P0g) side of my laptop connected easily to an open AP, but the [Ubuntu 10.04](http://releases.ubuntu.com/lucid/) (or [9.04](http://releases.ubuntu.com/9.04/), tried both) wouldn't, with the [Intel Iwlagn](http://wiki.debian.org/iwlagn) drivers reporting in syslog a [deauth (reason=6), basically the card spoke too soon.](http://steev.wordpress.com/2010/03/31/deauthentication-reason-codes/) I eventually found the solution.

After several weeks of asking the [same](http://superuser.com/questions/152427/ubuntu-9-04-cannot-connect-to-visible-open-wifi-ap-reason-6) [question](http://ubuntuforums.org/showthread.php?p=9460960) everywhere I could think of (as well as emailing Intel...) I found the answer a lot closer to home, from a PhD student ^H^H^H^H^H^H^H Graduate in my [University](http://www.qub.ac.uk/) over [LinkedIn](http://www.linkedin.com/groupItem?view=&gid=146569&type=member&item=24215281&qid=66023166-c30e-4ec7-96e3-2e6adad4a03f&goback=.gmp_146569) ([Ironically enough, I'm actually working with him on my Final Year Project next year...](http://www.andrewbolster.info/2010/05/coming-soon/?utm_source=rss&utm_medium=rss&utm_campaign=coming-soon) Good stuff to come :D )

The Answer is to use the [compat-wireless](http://wireless.kernel.org/en/users/Download) drivers instead of the stock drivers. [In Ubuntu, this is really easy](http://wireless.kernel.org/en/users/Download#Getting_compat-wireless_on_Ubuntu) (as long as you don't want to [roll-your-own,](http://wireless.kernel.org/en/users/Download#Building_and_installing) which doesn't take much longer).

`# For Ubuntu 8.10 Intrepid users:
sudo apt-get install linux-backports-modules-intrepid`

`# For Ubuntu 9.04 Jaunty users:
sudo apt-get install linux-backports-modules-jaunty`

`# For Ubuntu 9.10 Karmic users:
sudo apt-get install linux-backports-modules-karmic`

`# For Ubuntu 10.04 Lucid users (one of the following depending on the installed kernel. Most user should choose generic):
sudo apt-get install linux-backports-modules-wireless-lucid-generic
sudo apt-get install linux-backports-modules-wireless-lucid-generic-pae
sudo apt-get install linux-backports-modules-wireless-lucid-preempt
sudo apt-get install linux-backports-modules-wireless-lucid-server`

After that, just restart (easier than messing around with [modprobe](http://en.wikipedia.org/wiki/Modprobe) etc), and the job is done!
