---
author: admin
comments: true
date: 2009-11-09 17:34:56+00:00
layout: post
slug: lenovo-not-so-rocking-anymore
title: Lenovo, not so rocking anymore
---

This blog is starting to turn into a Lenovo ad, but this time, there are no good factors to my recent experience.

My X61 Tablet died, completly braindead, no power, no nothing.

Unfortunatly I left it a bit longer than was nessary due to home moving, going back to university, restarting and old job and starting a new one, aswell as becoming Design Editor for my [university's independent newspaper](http://www.thegown.org.uk).

Eventually, I made the [call to Lenovo](http://www-307.ibm.com/pc/support/site.wss/document.do?lndocid=MIGR-4HWSE3), and they were great as always with dealing with my query. After posting off the laptop (the week of the 18th of October), minus hard drive and battery (call it paranoia), I waited. And two weeks-ish later, the laptop arrived (4th October), and all was well after a motherboard replacement.

Well, not really.

The laptop had been out of action so long that the [Windows 7 RC](http://www.andrewbolster.info/2009/07/delayed-post-how-i-installed-windows-7-from-usb-hdd/) that I had been using had been deactivated, so laptop was essentially dead until I re-jigged it ([thankyouverymuch ](http://www.qub.ac.uk/schools/eeecs/Education/StudentStudyInformation/QUBMSDNAA/)Queens University/Microsoft).

When I did, something wasnt right, the wireless wasnt working :S. Hooked up to my network, downloaded all the updates and firmware upgrades I could find. Still no joy. Now, to clarify, the wireless WORKS, but you have to have the accesspoint up ones backside for it to be detected, with one 'bar'.

Of course, it doesnt take much to work out what happened; whoever replaced the motherboard, neglected to reattach the wireless antenna.

Not looking foward to sending it away for the sake of a few cables, I emailed lenovo the below;

Hello

I took delivery of this last week but haven't had a chance to set it up since then, and lo and behold, my wireless is now broken. Not boken as in non function, the kind of broken where i have to sit on top of my access point (i mean this literally) to get a wireless signal.

Considering the repair docket states that the motherboard was replaced, this leads me to believe that one of your repair staff neglected to reconnect the wireless antenna after the replacement.

I refuse to send the device away for another month to attach one cable. I would have expected more-than-cursory inspection of a full motherboard replacement.

I now have a brilliant tablet with perfect battery life that is next to useless unless tethered.

Please advise as to what can be done to resolve this.

PS Is the replacement motherboard covered by a fresh warranty?

Regards
Andrew Bolster

Still waiting on even an automated reply so when I got back this evening, I cracked it open and lo' and behold.

[caption id="attachment_168" align="alignright" width="300" caption="Kind enough to tape them down too..."]![Kind enough to tape them down too...]({{ BASE_PATH}}/uploads/2009/11/SL730674-300x225.jpg)[/caption]

So, the fix was simple, there are three connection points on the Intel Wireless Card (4965AG), TR1 R0 and TR2, and only 2 connections (Gray and Black). In case anyone else comes across something like this i put the gray in TR1 and black in R0, although I assume that as long as one of the TR's and one of the R0's is connected you should be grand.

Anyway, I hope Lenovo won't void my warranty...
