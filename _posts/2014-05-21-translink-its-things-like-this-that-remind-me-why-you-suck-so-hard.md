---
category: ''
description: ''
layout: post
tags:
- crowdsourcing
- data sharing
- Translink
- Belfast
- rant
- web post
- public transport
- LPS
- Google Transit
title: Translink, it's things like this that remind me why you suck so hard
---

{% include JB/setup %}

`<rant>`

There was a post on [r/Belfast](http://www.reddit.com/r/Belfast/comments/264m7u/is_there_a_site_which_lays_out_the_bus_routes_of/) today from someone moving to Belfast looking to make a decision on where they wanted to live.

As any sane person would (who doesn't drive), they wanted to find somewhere close to public transport routes, or to decide to go further out of the city for cheaper but still be able to get into work/school/uni/college/etc.

> I'm moving to Belfast and trying to find somewhere to live. I don't drive so I'm looking for places close to public transport, but I can't seem to find any proper maps with the routes laid out. Translink's site has some route maps which look similar to a tube map (http://www.translink.co.uk/Documents/Services/metro/Metro_schematic2.pdf[1] ), but without knowing the streets or surrounding ares I'm struggling to piece the routes together from names alone. For Dublin I can use something like http://hittheroad.ie/[2] to see the routes mapped out properly, but i can't seem to find anything similar for Belfast.
> Does such a thing exist?

It took all my composure not to just respond with laughter. 

There are several problems with this; it's an open data problem and relies on one of two things happening;

* **The people who have the data, [give it out](https://dataissexy.wordpress.com/2014/04/26/is-ni-too-small-for-open-data-opendata/)**. This is extremely unlikely to happen in Translinks case and I and many others been [actively trying for about 4 years now](http://cimota.com/blog/2011/08/09/translink-just-close-the-doors-and-turn-off-the-lights/). In the same boat is Land and Property Services (LPS) not releasing accurate geocoding information for fecking anything (Interestingly on the bus/train routes angle, I tried to get Translink to submit to [Google Transit](http://maps.google.co.uk/intl/en/landing/transit/#dmy) in around 2008 but I was told that they couldn't because LPS couldn't tell them where their stops were. Go figure.)
* **People filter/collect the data themselves and hope not to get sued**. The best NI Train [app](https://play.google.com/store/apps/details?id=AppZappy.NIRailAndBus) was 'instructed' to give preference to linking to the (shitty) Journey Planner as apparently the timetables of ~80% publicly funded travel is 'proprietary information'. God forbid all those 'competitors' get a leg up on your stellar service (hint; there are none).

There was talk a few years ago about making some 'geo-checkin' app for people to manually crowd-source the actual bus and train times and locations, circumventing not only the timetable-theiving accusation but also the need for LPS info. 

Only problem is that you'd pretty much need every traveller in Belfast using it for at least a month before the variability of stops, times, buses, routes etc levelled out so that you could work out what the actual information was.

But the fundamental point, that is not new, or original, or even clever, is that **if** Translink simply dumped their data onto Google Transit, the following currently impossible things would happen automatically, instantly, at **no** ongoing cost to Translink or the public purse.

* **International Travellers and Business People** (cough [FDI](http://www.investni.com/invest-in-northern-ireland.html) cough) could walk off the planes at Aldergrove, City, or *shock* City Of Derry, and know instantly not only where they are, but how far they are from the bus or [train](http://www.belfasttelegraph.co.uk/news/local-national/northern-ireland/plans-for-rail-link-to-belfast-international-airport-unveiled-30286881.html) that would take them to their destination, as well as the price of the fare, that they could pick up at the ATM's in the terminals rather that walking back and forth up that bloody ramp only to discover that the next bus is half an hour away rather than every 15 minutes as promised because our version of 'peak travel times' often get conflated with 'office hours'.
* **Foreign Tourists** would be able to work out how to get to the wonders this wee land has, in the language of their choice, with live transfer-by-transfer information, rather than desperately trying to find someone in Bushmills whom an American could understand, let alone a Mandarin or French speaker. (Disclaimer: My partner is from Bushmills. When she is on the phone to her family, **_I_** miss words).
* **_Native_ Tourists** (aye, that's right, there's a whole world beyond Black Mountain). For people who don't often come into the cities, it's a complex place, where often you sit on a bus going completely the wrong direction initially, scaring the crap out of you, only to discover it's dodging a one way system. Having this kind of route information online and accessible would keep passengers informed, giving people a higher level of confidence in taking public transport.
* **Commutters** who don't live or work along a direct arterial route would be able to work out the best transfers for arriving and leaving work at different times of day, avoiding rush hour, spending less time in transit, and generally being efficient people (until they realise, that means another pint in the pub after, but can't blame em').
* **Hackers**, oh boy would we have a field day with this. Imagine [cafe's](http://establishedcoffee.co) and [spaces](http://farsetlabs.org.uk) across the city where people could put up terminus-style boards for the next trains and buses going to [key places](http://digitalfantastico.blogspot.co.uk/2013/01/a-big-bite-of-raspberry-pi-having.html), or [announcing](http://gbg.hackerspace.se/projects/members/raccoon/gliderbot#line_changes_and_incident_reports) when there are delays so people can squeeze just a few...precious...minutes...of...hackery.

All in all, this is not just strikingly... no.. blindingly obvious as a 'good thing', but it would also save money, save lives, save time, make the place more attractive to business and tourism, and be so bloody easy that the fact that it **hasn't** been done should be a major talking point outside of our wee development community who know **exactly** how easy this would be to pull off....

Bloody hell, just look at the transit companies covered by [Google Transit at the minute](http://maps.google.co.uk/landing/transit/cities/index.html#Europe), Northern Ireland is literally the least connected part of the UK. 

You can get from [Lands End to John O'Groats](https://maps.google.co.uk/maps/ms?ie=UTF8&oe=UTF8&msa=0&msid=102323256180048216474.00046d470c1ab6984cb90&dg=feature) in just over a day, walking a grand total of 26 minutes. 

![Lands End Express](/img/2014/landsendexpress_700.png)

Contrast that with [Derry to Belfast](https://maps.google.co.uk/maps/ms?ie=UTF8&oe=UTF8&msa=0&msid=102323256180048216474.00046d470c1ab6984cb90&dg=feature) in 6 and a half hours via Dublin because, that's right **BUS EIRANN SUBMIT THEIR DATA TO GOOGLE TRANSIT**

![Dammit Translink](/img/2014/dammittranslink_700.png)


AAAAAAAARRRRRGGGHHHHHHHhhhhhhhh!

`</rant>`

TL;DR **Translink are bastards, LPS are just ignorant fools**

