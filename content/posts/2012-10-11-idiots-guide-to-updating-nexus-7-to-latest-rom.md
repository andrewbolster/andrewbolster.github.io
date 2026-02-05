---
aliases:
- /2012/10/idiots-guide-to-updating-nexus-7-to-latest-rom.html
categories:
- Instructional
comments: true
date: 2012-10-11 16:24:11+00:00
slug: idiots-guide-to-updating-nexus-7-to-latest-rom
tags:
- Android
- Cryptography
- Cybersecurity
- Network Security
- WiFi
- backup
title: Idiots Guide to Updating Nexus 7 to Latest ROM
---
Came across a [well known issue](http://code.google.com/p/android/issues/detail?id=34212) with QUB_SEC and Android, so I decided to fix it.

Basically, Android was bailing on a particular part of the TTLS Authentication scheme that is used by millions of workplace and academic RADIUS / AD secured wireless networks, and QUB is one of them.

[This Comment](http://code.google.com/p/android/issues/detail?id=34212#c232) on the issue indicated that the problem had been fixed in the newly released 4.1.2 builds, and that we'd probably be waiting a while for the OTA updates... So I guess I'll have to do it myself!

First off, I'm frankly amazed at how easy was. Never touched a command line. Only one blip that was due to me not reading instructions. And all in all, the only thing I've lost is my widget positions...

# Backup + Unlock Boot Loader + Root

These normally 'pain in the ass' sections are all thrown together in this case, because WugFresh has made this quite literally idiot proof.

**THIS WILL VOID YOUR WARRANTY AND I AM NOT CULPABLE IN ANY WAY, YOU'RE A GROWN UP NOW**

[Show me you're not an idiot](http://www.wugfresh.com/dev/nexus-root-toolkit/)

PS Tick the 'custom bootloader' option for the rooting section. Some guides say that you have to use the Clockwork Mod recovery, but this isn't true; the one bundled with the Nexus Root Toolkit is more than sufficient.

# Flash

Once that's all done (you did back up didn't you?), you'll have a brainless device with the stock rom rooted asking for some information. Chuck it in if you like but it's not really necessary as you're going to wipe it again in a second.

Grab the latest [Grouper ROM](http://download.peteralfonso.com/grouper/rom) and drop the zip file on the internal storage over USB.

Reboot into Recovery (using either the QuickBoot app or the PWR+Both Vol button push), select 'Wipe' and then **both** Factory Reset and System.

Then drop into the install menu, select the Zip that you downloaded from Grouper and then sent onto the internal storage, and bob's you're dads bro!

It'll take a few minutes first time, and will ask the usual mess of questions, but that's fine, becausenow you can use your enterprise network to connect!

At which point, you can go back to the Nexus Root Toolkit and follow the instructions to restore your existing settings and apps, to save your precious Angry Birds score.

# Fin

That's all she wrote folks, I'll try to update this as it inevitably gets 'out of date'
