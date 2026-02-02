---
author: admin
categories:
- Commentary
comments: true
date: 2012-09-10 18:56:21+00:00
layout: post
slug: 4g-and-the-northern-ireland-problem
tags:
- IoT
- Networking
- 'Northern Ireland'
- Technology
- mobile
- 'r&d'
title: 4G and 'The Northern Ireland Problem'
---


So Everything Everywhere are [holding a press conference tomorrow](http://www.bbc.co.uk/news/technology-19542467)... Rumours abound about device selections and other bits of juicy gossip (given the state of the [global handset market](http://www.bgr.com/2012/06/25/google-tries-to-block-u-s-shipments-of-apples-iphone-over-3g-patents/)... I'm not surprised), so this seemed like a good opportunity to rant.
In Late August, OfCom, the UK's communications regulator, gave the go-ahead to bring the planned 4G spectrum allocations forward to this year. In short, 4G is go!
This was music to the ears of Everything Everywhere, and that's not hyperbole.

Everything Everywhere is the optimistically named Joint Venture between Orange and T-Mobile, who entered into a mast-sharing agreement last year that vastly improved both companies comparatively lackluster coverage maps, when compared to the likes of O2 and Vodaphone. Together, they represent a customer base of 27 million people, and a weight of investment of over £15 billion since 2000, with additional plans for £1.5 billion between now and 2015.
[http://ukmobilecoverage.co.uk/best](http://ukmobilecoverage.co.uk/best)

Disclaimer, I'm a T-Mobile customer, but for the time being, just assume I'm an agnostic observer...

The more I thought on it, Everything Everywhere is a particularly saavy brand decision, that I had initially scoffed at.

Back in 2009, I was working as an R&D placement engineer at Ericsson LMI in Athlone. This was around the time of initial LTE testing in the US and Finland, and we were starting to see results come back from test sites. As such, we had many courses and briefings on the technology and how it was going. At the time, I thought that LTE was a horribly bloated derivative technology with a load of useless add ons involving about a dozen different modulation and multiplexing schemes, something called 'full HD voice', and multicast broadcasting, but as time went on, it was clear that this was pretty much what it says on the tin; LTE stands for Long Term Evolution, and here was a protocol that was a bit like the American CDMA standards, with a dash of the Japanese DoCoMo, and could finally replace the aging GPRS Core network while improving on the power and capacity efficiencies of HSDPA.

Here was a protocol that was designed with almost every reasonable use case in mind; real time audio-video teleconferencing with low latency (optimally around 5ms) for smartphones / mobile working; the ability to maintain multi-megabit up and down rates up to a client speed of 500kph for train-based wifi rollouts; bandwidth efficient mobile TV; the ability for seamless voice hand-off between LTE, 3G and WiFi access; low power beaconing for service monitoring appliances, client-to-core authentication providing secure access even if the local base station is compromised, and many other advances.

Everything Everywhere indeed.

But there's always another harder, better, faster, stronger widget - what's so special about 4G?

Well, nothing really. Or everything. Depends on your perspective.

Analog cell phones (1G) allowed people to speak on the move.

Digital Phones (2G/2.5G/2.75G) aka GSM, GPRS, EDGE respectively, allowed people to text, access text based Internet, and then (for the really patient), images from the internet, with some Media Messaging functionality that never really took off when email attachments and then Facebook / Twitter took over.

Then came along the marketing juggernaut that was 3G/3.5G/ aka 3G and HSDPA and HSDPA+. With a price tag of [£22.5 billion](http://news.bbc.co.uk/1/hi/business/727831.stm) for the spectrum alone, 3G operators promised everything, from mobile TV, High Definition Voice and Teleconferencing, High Speed Internet and seamless handoff... Hold on a second...

The elephant in the room around the 3G/4G discussion is that the 3G rollout was such a bodged job that only really in the last few years (over a decade since the initial spectrum auction) have the long promised 98% of the population got their tasty 3G. The reasons for this bodged job are many, but the fundamental one (in my personal opinion) is that 3G was a terrible terrible name. Not from a marketing perspective, but from a technological perspective.

As hinted above, we had 2G and many in-between stages. [GPRS](http://en.wikipedia.org/wiki/General_Packet_Radio_Service), usually referred to as 2.5G, [EDGE](http://en.wikipedia.org/wiki/EGPRS), often desperately termed anything between 2.75-2.99G. The provision of additional services across this evolution was immense, but data rates still lagged.

Then, the [ITU](http://en.wikipedia.org/wiki/International_Telecommunication_Union) decided in 2000 to draw a big arbitrary line in the sand and say "maybe it's time to bring the international community under one mobile technology", producing the [UMTS](http://en.wikipedia.org/wiki/UMTS) standard, which the Americans and Koreans promptly ignored and threw together [CDMA2000](http://en.wikipedia.org/wiki/CDMA2000). The ITU eventually did the only thing a standards body can do when a hemisphere sticks two fingers up to a standard; says that it's part of the standard...

Anyway, the dream of global commerce under the soft shade of 3G had died. The technology was still there, and pretty good too, but without global roaming and device interoperability, the world was still stuck in a walled garden approach to telecommunications. We had teleconferencing if your carrier allowed it, we had high speed data (HSDPA can get similar speeds as domestic WiFi), 3 did show off UK based mobile TV broadcasting, but it was [horrifically crippled and expensive](http://en.wikipedia.org/wiki/3_mobile_tv_(UK)) (to recoup the costs of the spectrum auction, which also slowed mast-rollout).

Roll out also caused severe problems for Northern Ireland specifically; as part of the original OfCom spectrum auction rules, the networks set up their networks in the most populous areas first. Not a problem, that’s exactly the way people would do any kind of high-impact rollout. But that meant that by the time they got to Northern Ireland, that had already 'serviced' a significant portion of the UK population, and then basically said 'We're done'. They came in, covered less than 85% of the Greater Belfast area, less than 60% of North Down, gave Newtonabby, Carrickfergus, Craigavon, Limavady, and Coleraine a few token masts covering an average of less than 15% of the areas, and left. (Statistics from [Here](http://maps.ofcom.org.uk/mobile/index.html), the UK Mobile Services Map 2011).

Anyone who has ever used the Derry line will tell you; 3G does not work in Northern Ireland. As such, no one uses it traveling, and 'hops' between wifi access points. Which was not the point.

3G was supposed to be a ubiquitous networked future with an always-on, 'internet of things', but ended up being a frustration. As such, I'm very glad to hear that OfCom have set the regional requirements for 4G rollout in Northern Ireland to 95% of population by 2017.

But I don't think it'll happen... but it will fix 3G...

Having LTE / 4G in some areas, as well as the required core-network upgrades, will force operators to upgrade their remaining 2.XG masts to 3G to maintain competitive advantage.

If you're traveling and you manage to get 4G at the airport, and as soon as you hop on the bus, you're back to 2G. That's not a 'service degradation', that's 'completely incapacitated'

4G is really just 3G done properly; 4G masts will satisfy the ‘big data’ demand of the urban areas that always get hit first, and the technology upgrades will push the ‘old’ 3G/UMTS/HSDPA standards out to the rest of the population, meaning that everyone is on the same services, but at different service levels.

In short, the only thing that really worked with 3G in the ‘naughties’, was high-speed data. That was a boon for services like Facebook, Twitter, and Skype, that often supplanted if not straight replaced the concept of 'calling someone'; while device email and push notification revolutionized the mobile workspace, and the idea of being able to download applications for a device, on a device created whole new economies in the 'app' world.

Imagine if they had got the rest to work?

Imagine if they got it to work for Everyone, on Everything, Everywhere?
