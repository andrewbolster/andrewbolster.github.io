---
categories:
- Instructional
comments: true
date: 2011-09-29 11:52:23+00:00
slug: force-32-bit-installs-on-64-bit-systems-debrpm
tags:
- Debian
- Fedora
- Linux
- Ubuntu
title: Force 32 bit installs on 64 bit systems (Deb/RPM)
---


Pre-built packages not releasing 64 bit versions? No Problem.

Debian/Ubuntu based:
`dpkg -i --force-architecture whatever.deb`

RH/Fedora based:

`rpm -i --ignorearch whatever.rpm`
