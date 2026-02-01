---
author: admin
categories:
- Instructional
comments: false
date: 2007-12-16 23:50:00+00:00
layout: post
slug: installation-of-vmware-server-windows
tags:
- virtualisation
- BackTrack Linux
- virtual machine creation
- live booting
- server virtualisation
- network tools
- IP assignment
- network addressing
- VM setup
- windows
- beta version
- client console
- boot configuration
- bridged connection
- DHCP
- linux
- vm
- networking setup
- Flux
- VMWare
- BT3
title: Installation of VMWare Server (Windows)
---


So, to do most of this playing about, I need a virtualisation environment, and VMware is the easiest, simplest and, at the moment, cheapest.

VMWare released their [server virtualisation tool](http://www.vmware.com/products/server/) to "free"dom recently, and the newest version (2.0) is currently sitting in beta.

I have tried it out before but it didnt feel as solid as the older versions so I'm sticking with the oldskool 1.0.3

The Setup itself is just a simple "next, next, finish" with a free registration key provided. I recommend also downloading and installing the client console package; this is handy both for administring and viewing the VM's in situ, but also to administer remote installations.

[![](http://bp2.blogger.com/_ZZeoHBuNcEU/R2W73YD-kMI/AAAAAAAAA4U/HBKJT0ouyFw/s320/Untitled-1.jpg)](http://bp2.blogger.com/_ZZeoHBuNcEU/R2W73YD-kMI/AAAAAAAAA4U/HBKJT0ouyFw/s1600-h/Untitled-1.jpg)

As for a test system, i recently downloaded the newest beta of the [BackTrack Linux Live CD](http://forums.remote-exploit.org/showthread.php?p=56678) and thought that this would be a simple test for live booting.

Logging into the the local setup naturally doesnt need a password.

[![](http://bp1.blogger.com/_ZZeoHBuNcEU/R2W8kID-kNI/AAAAAAAAA4c/92K6CvP5fYw/s200/Untitled-2.jpg)](http://bp1.blogger.com/_ZZeoHBuNcEU/R2W8kID-kNI/AAAAAAAAA4c/92K6CvP5fYw/s1600-h/Untitled-2.jpg)At the next screen you are presented with plenty of options but since we've got nothing to work with yet, Its straight into "Create New Virtual Machine".

For most setups the defaults are suitable, and dont worry about selecting a OS type or distro as long as 32 and 64 bit OS's arent mixed.  Also, a Virtual Hard Disk will be generated, and for space concerns, i reduced mine down from the default 8GB to 4GB and have it simply as a live cd hard disk.

Networking considerations will be different in different setups. I have Athena gigabit connected to Apollo (I'm working on Apollo in this post) and also have Apollo and Athena separatly connected to my home router. Inside the VMWare Program Folder, there is a "Manage Virtual Networks" that can allow for more configuration, for instance, i removed my gigabit adapter from the bridging system.

[![](http://bp3.blogger.com/_ZZeoHBuNcEU/R2W-JoD-kOI/AAAAAAAAA4k/6KvPl9imvOM/s200/Untitled-3.jpg)](http://bp3.blogger.com/_ZZeoHBuNcEU/R2W-JoD-kOI/AAAAAAAAA4k/6KvPl9imvOM/s1600-h/Untitled-3.jpg)

Anyway, moving on. VMWare defaults to booting off harddrive first, then CD drive automatically, so all that needs to be done is reference the VM to boot from the ISO image downloaded. Of course, VMWare can be set to read straight from an existing drive without locking out the host system also.

[![](http://bp2.blogger.com/_ZZeoHBuNcEU/R2W-_YD-kPI/AAAAAAAAA4s/WbfmJCXDruo/s200/Untitled-4.jpg)](http://bp2.blogger.com/_ZZeoHBuNcEU/R2W-_YD-kPI/AAAAAAAAA4s/WbfmJCXDruo/s1600-h/Untitled-4.jpg)

Once that is set up, simply power up the VM. BT3 presents a standard boot up screen, i just settled for using [Flux](http://fluxbox.sourceforge.net/).

This post isnt about BT3, but i do recommend it as being an all-in-one live boot cd with network tools. The response of the VM is sprightly to say the least, but, i would point out that once you click inside the window, you lose mouse and keyboard control until you press CTRL+ALT...... I learnt this by trial and error, got very worried for a bit.

In short, it all works, networking is automatically set up over the bridged connection, so the VM gets assigned an IP from your own network over DHCP, and can be directly addressed from outside as well.

Heres a paradox photo

[![](http://bp3.blogger.com/_ZZeoHBuNcEU/R2XAVoD-kQI/AAAAAAAAA40/N34qTQQkXfY/s200/Untitled-5.jpg)](http://bp3.blogger.com/_ZZeoHBuNcEU/R2XAVoD-kQI/AAAAAAAAA40/N34qTQQkXfY/s1600-h/Untitled-5.jpg)

Please at least pretend to click my ads. I know they're a joke, but still, it dont cost ya anything!
