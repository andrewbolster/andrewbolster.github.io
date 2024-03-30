---
author: admin
categories:
- Instructional
comments: true
date: 2011-09-29 11:52:23+00:00
layout: post
slug: force-32-bit-installs-on-64-bit-systems-debrpm
tags:
- Ubuntu
- linux
- packaging
- Fedora
- Debian
- Red Hat
- software
- 64-bit
title: Force 32 bit installs on 64 bit systems (Deb/RPM)
---


Pre-built packages not releasing 64 bit versions? No Problem. 

Debian/Ubuntu based:
`dpkg -i --force-architecture whatever.deb`

RH/Fedora based:

`rpm -i --ignorearch whatever.rpm`

