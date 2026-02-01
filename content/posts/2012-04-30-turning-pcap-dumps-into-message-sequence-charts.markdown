---
author: admin
categories:
- Instructional
comments: true
date: 2012-04-30 17:37:36+00:00
layout: post
slug: turning-pcap-dumps-into-message-sequence-charts
tags:
- Ubuntu
- mscgen
- Network Flow Visualization
- Packet Capture
- NS-3
- Tshark
- Network Traffic Analysis
- PCap Files
title: Turning Pcap dumps into Message Sequence Charts
---


[![]({{ BASE_PATH}}/uploads/2012/04/avses-tosip-300x238.png)]({{ BASE_PATH}}/uploads/2012/04/avses-tosip.png)PCap files are a pain; weird format, difficult to parse viserally even if you have the 'right' tools handy. Wouldn't it be easier to be able to 'see' the network flow, like it is in all the textbooks?

# Well now you can!

In playing with NS-3, I came across this problem, and googled for a solution. Now here's an end-to-end 'I have pcap files and want to make them pretty' solution.

# Assume you have...


  * Ubuntu


  * pcap files


  * ~/src/ dir


  * a ~/bin directory on your users $PATH

# Get 'er dun

`sudo apt-get install mscgen subversion tshark`

`cd ~/src;
svn checkout http://pcap2msc.googlecode.com/svn/trunk/ pcap2msc-read-only; ln -s ~/src/pcap2msc-read-only/pcap2msc ~/bin/`

`cd <where yo' pcaps at!>/`

`pcap2msc <whatever.pcap> all`

This is ugly but it shows you what the individual packets are...

Then Pump the same thing into mscgen

`pcap2msc <whatever.pcap> all | mscgen -T png -o <whatever.png>
`
