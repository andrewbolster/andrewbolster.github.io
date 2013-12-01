---
author: admin
comments: true
date: 2012-06-13 15:13:56+00:00
layout: post
slug: unattended-upgrades-in-ubuntu
title: Unattended upgrades in Ubuntu
categories:
- Instructional
tags:
- automated
- automation
- software
- sudo
- Ubuntu
- update
- upgrade
---

_Never having to think about updates again _ is a good thing in my head, so here's how to set up Unattended Upgrades under Ubuntu for fun and profit.[![Lazy Drinker Logo](http://www.andrewbolster.info/wp-content/uploads/2012/06/LazyDAlpha-300x218.gif)](http://www.lazydrinker.com/Index.htm)

`$ sudo apt-get install unattended-upgrades`

`$sudo vim /etc/apt/apt.conf.d/50unattended-upgrades`

Uncomment the line `// "${distro_id}:${distro_codename}-updates"; `

`$ sudo vim /etc/apt/apt.conf.d/10periodic`

Make it look like this

`APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Download-Upgradeable-Packages "1";
APT::Periodic::AutocleanInterval "7";
APT::Periodic::Unattended-Upgrade "1";`
