---
author: admin
comments: true
date: 2013-02-11 13:04:43+00:00
layout: post
slug: it-qub-are-moving-forward
title: IT @ QUB are moving forward
categories:
- Uni
tags:
- networking
- pg forum
- qub
- qub_sec
- representative
- Uni
- university
- vpn
- web space
- wifi
---

QUB Relevant: Mostly PGR or prospective PGR

Just out of a great meeting with QUB Information Services regarding:

	
  * Researcher/ Student webspace

	
  * Email

	
  * Wifi

	
  * and VPN

# Web Space

For a while now, this has been a bee in my bonnet; many other institutions provide User-Dirs or Public Facing Pages that, while being slightly monitored, are in the control of individual researchers and students. These draw attention to the bleeding edge of an institutions academic research while maintaining ownership of the content.

The general plan is now that the proposal is going to the Universities' Web Forum next month for approval, potentially [Wordpress](http://blogs.qub.ac.uk/), [365 Pages](http://www.dotnetmafia.com/blogs/dotnettipoftheday/archive/2011/04/15/office-365-how-to-create-a-public-facing-website-with-sharepoint-online.aspx), or a [CMS](http://www.qub.ac.uk/directorates/InformationServices/Services/WebAuthoringCMS/) template solution.

The issue with web space is weird; I had always assumed that it was simply an Orwellian obsession with content control within the central university, however the truth is much more subtle than that.  Basically JANET police the content and services running from any of it's endpoints, and is one of the contributing factors to the paranoia around giving people web-space.

[Warwick](http://blogs.warwick.ac.uk/) have operated a successful student Wordpress Multi-site installation for several years, so one would imagine that the 'Best Practices' on how to deal with the 'Freedom of the Press' problem should be already done, and the case to the university should be quite simple. Here's hoping.

#  E-Mail

The perennial problem that has left PGR students with only a couple of hundred megabytes of storage with little hope of expansion, compared to multi-gigabyte storage for Undergraduate Students through Microsoft's Office 365 Framework. The stated reason for the dis-proportionality? Intellectual Property. Apparently Microsoft aren't safe enough to put any IP through, so instead we get choked into using outside services such as [Google Mail](https://mail.google.com), [Dropbox](http://dropbox.com) (the real one, not the [pretender](https://dropbox.qub.ac.uk/)...) that are COMPLETELY outside of central oversight...

(The fact that no-one has ever claimed IP violation over an email message shows that this line of thinking has but the loosest connection to reality, and when data storage is at an all time low-price (<[$3c/GB](http://www.zdnet.com/the-hard-drive-drought-is-over-7000005624/)) one wonders what the problem is?)

In the discussion it was clear that this was something that has been fought over internally for a long time inside information services, and the general sentiment is that delivering two levels of service, regardless of justification, is a waste of time and resources. I for one agree with them.

# Wifi

Ahh yes, [QUB_Sec](http://www.qub.ac.uk/directorates/InformationServices/Services/WirelessMobiles/). How we love the way you drop out randomly, take more work to set up in Windows than in any other operating system (way to play the numbers boys) and are generally a creaking, falling apart, strangled attempt at a ubiquitous WiFi installation.

The whisper around is that there's a fair amount of money being ponied up for what's called "The Wireless Campus". My first question was, what's the difference between doing QUB_SEC correctly and this campus brand? The short answer is that it's cheaper and more efficient to chuck QUB_SEC out and implement a fresh system that learns from the mistakes of the past few years.

Notable mistakes that are hopefully being resolved by this proposed system are:

	
  * EduRoam inclusion:[ Most European and World Wide institutions](http://monitor.eduroam.org/eduroam_map.php?type=all) use this system to use each other's wifi when at meetings or conferences. QUB has been left in the cold for a long time, often looking like the poor-neighbour, begging for waves... This is being tested at the minute and I've asked for a beta invite for a few areas, specifically [EEECS](http://www.qub.ac.uk/schools/eeecs/) since we're best placed to a) test it to destruction, b) make bug reports more expansive than "DA WEEFEES NO WORK", and c) we are all early adopters by nature anyway. 

	
  * Backhaul: QUB_SEC always looped back to a single router in the Lanyon building (Well, the McClay actually, but still), making a massive bottleneck for data. It gets to the insane extremes that when I want to connect to my desktop in ECIT, from the café in ECIT, I have to go via the main site. This will hopefully be fixed, meaning that wifi will have local backhaul with centralised authentication, _hopefully_ meaning that it will be able to access localised resources (such as office desktops) as if you were in the local wired network.

	
  * Crypto: IS are painfully aware of the hash (no pun intended) that was made of certificate authentication and the problems with[ 'Secure' W2](http://www.securew2.com/), and dealing with, you know, [people having their own hardware](http://en.wikipedia.org/wiki/Bring_your_own_device). This will hopefully be fixed next time around.

# VPN

To finish things off, I threw in a wildcard that wasn't a scheduled topic, and had never come up in an official capacity before, but is something that[ Farset Labs ](http://farsetlabs.org.uk/blog/about-farset/)is planning to provide for their own members, and would fit into QUB's Security Model, but having a VPN endpoint for students and staff to link into when using insecure WiFi across the globe would be a great security advantage. You could even go as far as to say that the University could mandate that all QUB laptops taken out for conferences and such had to connect to the wild west web via this VPN, giving users an added level of security. This is something else that is going to be looked at at the Web Forum, but may be sneakily rolled out before hand anyway.

# Fin

All in all, it's good to see that IS are engaging with students and their representatives. You just have to look at the leaps and bounds that they've gone through in terms of Social Media use on [Facebook](https://www.facebook.com/ITQUB) and [Twitter](https://twitter.com/itqub) where they are actually talking to individuals instead of the classic 'mass email' that everyone I talk to seems to ignore and then complains about not being kept up to date.

TL;DR IT @ QUB is trying. And that's a good thing.
