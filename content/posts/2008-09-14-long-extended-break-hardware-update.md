---
aliases:
- /2008/09/long-extended-break-hardware-update.html
categories:
- Commentary
comments: false
date: 2008-09-14 14:13:00+00:00
slug: long-extended-break-hardware-update
tags:
- Bash
- Desktop
- Linux
- Perl
- Router
- Ubuntu
- remote access
title: 'Long Extended Break: Hardware Update'
---
[![](http://1.bp.blogspot.com/_ZZeoHBuNcEU/SM0ew7ciunI/AAAAAAAACBc/hWypq44rn5Y/s400/SL730122.JPG)](http://1.bp.blogspot.com/_ZZeoHBuNcEU/SM0ew7ciunI/AAAAAAAACBc/hWypq44rn5Y/s1600-h/SL730122.JPG)
So, gonna do a quick write up on my current setup.

Ok, from the top:

Linksys WRT54GL DD-WRT v24 std firmware (also running on the bottom right screen)

Generic Wireless headphones (not used since i heard someone else on the channel :P )

top screens : Windows server 2008 AMD Athlon X2 64 6000+ on an Nvidia MCP 65 based motherboard carrying 6GB, with the dangerous RAID 0 arrangement of two 500GB sata drives and an IDE 320GB for essential backups. (this system is hidden, lol)

The bottom two screens run off of an old Toshiba Laptop that i "repurposed", more or less the keyboard has been removed and the screen flipped around and re positioned, Intel Celeron something or other, 512 MB memory, 60 GB HDD, running Ubuntu Hardy Heron that i mainly use for chat, downloads, news, system monitoring and notes.

Fairly standard hidden speakers and everythings as hidden so i get to be messy the rest of the time.

As for functionality, i use the laptop as an always on remote access hub that also lets me dial into work from anywhere. Also, since the laptop is keyboard mouseless, I use synergy to automatically start the client on the laptop (using the desktop as the server)

FYI easy enough to set up, just insert this:

/usr/bin/killall synergyc

/usr/bin/synergyc (server)

in these

/etc/gdm/Init/Default

/etc/gdm/PostLogin/Default

/etc/gdm/PostSession/Default

/etc/gdm/PreSession/Default

And this more or less starts and stops the server at every stage of bootup and login (note, you are not going to get to play with BIOS options et al, read the synergy [FAQ](http://synergy2.sourceforge.net/)

Anyway, Otherwise, I've been working on alot of bash script that I will post about separatly, but I am going to be learning perl so i will hopefully be using this thing alot more than usual.

Later guys

Please at least pretend to click my ads. I know they're a joke, but still, it dont cost ya anything!
