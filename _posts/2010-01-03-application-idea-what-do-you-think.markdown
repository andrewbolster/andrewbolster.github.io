---
author: admin
comments: true
date: 2010-01-03 20:18:55+00:00
layout: post
slug: application-idea-what-do-you-think
title: 'Application Idea: What do you think?'
wordpress_id: 186
categories:
- Instructional
tags:
- android
- blackberry
- cell
- Embedded
- hardware
- iphone
- mobile
- networking
- programming
---

As part of the whole [New Years Resolutions](http://www.andrewbolster.info/2009/12/new-years-resolutions/) plan, I'm gonna get started on the OSS development thing.

The Gist: Cross Platform Mobile application to collect international data on cell reception.

The Gimmick: While [services that do this exist](http://www.cellreception.com/), they assume even circular propagation of the signal. Granular reception maps that tell you where to head to to get more bars.

The Detail: Low level should be relatively simple; the [Android](http://developer.android.com/reference/packages.html), [Blackberry](http://www.blackberry.com/developers/docs/5.0.0api/index.html) and [Iphone ](http://developer.apple.com/iphone/library/navigation/index.html)API stacks allow easy reading of the current [cell ID](http://developer.android.com/reference/android/telephony/NeighboringCellInfo.html), [RSSI](http://www.blackberry.com/developers/docs/5.0.0api/net/rim/device/api/system/GPRSInfo.GPRSCellInfo.html), and [GPS Co-ords.](http://developer.apple.com/iphone/library/documentation/CoreLocation/Reference/CoreLocation_Framework/index.html) Upload those three values over [XML ](http://en.wikipedia.org/wiki/XML)(or [Something](http://en.wikipedia.org/wiki/Lightweight_markup_language)), Web service plugs that into a MySQL server, which is then aggregated, and [displayed ](http://code.google.com/apis/maps/)on the Web, and can be queried by the mobile app.
The Potential: While its unlikely that its going to 'blow up' since there is relatively little incentive for the end user, since the Applications are going to be free, there will be some that will install it for the sake of it. There is the opportunity to license the data gained service providers but the aggregated data will be made available online in open formats.

The Dream: Development of accurate localised RF propagation modelling for dirt cheap compared to professional surveying, so maybe people like [AT&T ](http://forums.wireless.att.com/cng/board/message?board.id=apple&thread.id=12071)and [others ](http://forum.o2.co.uk/viewtopic.php?p=151120)could give better service in built up areas...

I'll be keeping notes on the relevant [Trac page](http://andrewbolster.info/receptur)

What do we think?
