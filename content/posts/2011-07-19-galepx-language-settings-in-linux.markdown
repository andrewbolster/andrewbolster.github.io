---
author: admin
categories:
- Instructional
comments: true
date: 2011-07-19 09:25:18+00:00
layout: post
slug: galepx-language-settings-in-linux
tags:
- MSI E350IA-E45
- BIOS level development
- Language settings
- Flashrom
- Programming tools
- BIOS modification
- Galep-5 Universal Programmer
- Coreboot project
- BIOS flashing
- AMD Fusion
title: GalepX Language settings in Linux
---


![Galep-5 Universal Programmer](http://www.conitec.net/images/g5medium.jpg) As part of my placement in Zurich, I've been doing some BIOS level development around the Coreboot project, working with Flashrom and other tools, but with a particular AMD Fusion (MSI E350IA-E45) Mobo, there was no sensible way to flash the BIOS or to add a 'vestigial' BIOS.

So, the solution arrived at was to 'acquire' a [Galep-5 Universal Programmer](http://www.conitec.net/english/galep5.php) (Not a cheap piece of kit, but apparently that's the kind of stuff they have lying around in Zurich). Anyway, long story short, went to the Galep website, [downloaded](http://www.conitec.net/english/software.php) the .run file, installed, all perfect and happy days. Except it was in German. (Even though it says its 'English only')

My German is only slightly better than my Martian, so I had no idea what was going on, but a quick look in the /opt/galepx directory showed a `mdma.settings` file. In there there's an XML section like this
```xml
        res/tr/de.tr
        false
```
Simple enough, change the _de_ to _en_ and welcome back to the anglophile world!
