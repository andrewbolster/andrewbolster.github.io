---
author: admin
categories:
- Commentary
comments: false
date: 2008-05-24 12:06:00+00:00
layout: post
slug: eeepc-note
tags:
- Ubuntu
- Aircrack
- linux
- Linux
- GPS
- Eee
- eee
- Webcam
- Hardy Heron
- Kismet
- Wireless
- Dual Boot
- Battery Life
- '8.04'
title: EEEpc note
---


Ok, got the 900, sorry this blog is very very late

Pros:
AMAZINGLY small, you wont believe how small it is until you use one
The keyboard is just managable
the Webcam is amazing quality when it works
More responsive than i imagined
The Extra 16GB SSD really helps
Wonderfully fast bootups (If you never plug it in to any accessories (other than charger) set the Boot Booster enabled under the BIOS, trims a second or two)

Cons:
Battery life[ less than expected](http://forum.eeeuser.com/viewtopic.php?id=27140)
Wireless strength depends on the driver you use
Webcam and Webcam-mic not fully functional (currently) under Ubuntu 8.04

What I've done:
Managed to get a dual boot system between the Xandros OS and Ubuntu 8.04 by resizing my home partition on the 16GB SSD and installing in there (dont bother with a swap drive)
Grub works wonderfully and straight out of the install i still have both the standard and recovery boot options thru xandros.

As for install, [use this](http://www.pendrivelinux.com/2008/05/15/usb-ubuntu-804-persistent-install-from-linux/)
And for tweaking use [this](http://eee.ricey.co.uk/files/eee/RiceeeyTweak.sh) BUT to fix the sound you have to go back in and re fix alsa (the 700 tweak doesnt work for the 900)

	
  * Edit /etc/modprobe.d/alsa-base and change the line “options snd-hda-intel model=3stack-dig”to “options snd-hda-intel model=auto”

	
  * ALSO, run the following command:

    
    sudo alsactl store

	
  * Run:

sudo alsactl restore

I think that was all i had to do for basic operations.

Also got Kismet and the Aircrack-ng suites working with a bit of giggery pokery with an aim of stealing my dads old GPS and getting gpsmap to work properly,  My personal recommendation is to install both from source, in the case of aircrack, you need to go into the folder that was built and make sure that all of the generated binary files are copied to /usr/bin or /usr/sbin depending on how paranoid you are (I'm not) because the install script doesnt install airmon, aireply, ivstools, packetforge, and a few other things i cant remember off the top of my head

As for the kismet source, i use source=madwifi_ag,atho,atheros and instead of relying on kismet to open the card as monitor, i use airmon and wlanconfig to kill the other interfaces first, eg

sudo wlanconfig ath0 destroy
sudo airmon-ng start wifi0
kismet (i did the suidinstall of kismet so there is no need for sudo. for a single user system the suidinstall is probably easiest)

I cant really talk about the performance of aircrack because truth be told i wouldnt have the patience for a 900MHz to get thru that kinda work, i collect as many packets as i can and get my dual core 3GHz 64bit system to do the dirty work (also usually do this over ssh if i can get an alternate connection, am working on a system where the ivs file can be emailed and an email reply will be sent back, with either the key, or "MEGAFAIL")

Anyway
Battery life. thats a joke. Its less that the 701 my dad has. yeah, yeah, i know, its more powerful, bigger screen, that wud be fine if it wasnt just the UK getting the kneecapped batteries:

List of countries getting 5200mAh battery:TW,HK,USA,CAN,IT
4400mAh:UK

If anyone is reading this please go to [http://forum.eeeuser.com/viewtopic.php?id=27140](http://forum.eeeuser.com/viewtopic.php?id=27140) and make your voice heard, cus i want the battery that was handed out to reviewers! (the forum explains it better than me)

Please at least pretend to click my ads. I know they're a joke, but still, it dont cost ya anything!
