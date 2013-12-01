---
author: admin
comments: true
date: 2011-09-29 11:52:23+00:00
layout: post
slug: force-32-bit-installs-on-64-bit-systems-debrpm
title: Force 32 bit installs on 64 bit systems (Deb/RPM)
categories:
- Instructional
tags:
- 64-bit
- linux
- packaging
- software
- Ubuntu
---

Pre-built packages not releasing 64 bit versions? No Problem. 

Debian/Ubuntu based:
`dpkg -i --force-architecture whatever.deb`

RH/Fedora based:

`rpm -i --ignorearch whatever.rpm`

