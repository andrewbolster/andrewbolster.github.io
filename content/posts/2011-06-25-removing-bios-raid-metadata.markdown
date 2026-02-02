---
categories:
- Instructional
comments: true
date: 2011-06-25 11:58:31+00:00
slug: removing-bios-raid-metadata
tags: []
title: Removing BIOS RAID Metadata
---


Had an issue with Fedora 15 not liking my harddrives that used to be RAIDed. Noting for future reference.

“Disk contains BIOS metadata, but is not part of any recognized BIOS RAID sets."

Solution:
`dmraid -r -E /dev/????`

Stolen from [Kezhong](http://kezhong.wordpress.com/2011/06/14/how-to-remove-bios-raid-metadata-from-disk-on-fedora/)
