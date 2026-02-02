---
categories:
- Instructional
comments: false
date: 2008-11-06 19:20:00+00:00
slug: mbwe-fuel-gauge-speedometer-conversion
tags:
- Bash
- Linux
- Programming
- Storage
title: MBWE Fuel Gauge -> Speedometer conversion
---


The Fuel gauge on the front of my MBWE is fairly useless, noone cares, so why not repurpose it as a speedometer?

first, stop it displaying the "fuel" Stolen from [http://kyyhkynen.net/stuff/mybook/reduce_disk_usage.php](http://kyyhkynen.net/stuff/mybook/reduce_disk_usage.php)

****

> **Disable the service that displays the disk usage** with the leds in the front panel of your MBWE. Admit it, the feature is pretty much useless and because the service has to check the amount of free space on the disk(s), it is causing disk access.

In order to prevent the service from starting during boot, edit /etc/init.d/S15wdc-fuel-gauge. Comment out this line:

>
>     $FGD &
>
>
Then stop the service:

>
>     # /etc/init.d/S15wdc-fuel-gauge stop
>
>


    <span style="font-size:130%;"><span style="font-family:Georgia,serif;">Once all thats done, this is my script (The ultimate in lazy)</span></span>
    <blockquote>#!/bin/bashINITIAL_RX=`cat /sys/class/net/eth0/device/net:eth0/statistics/rx_bytes`sleep 10FINAL_RX=`cat /sys/class/net/eth0/device/net:eth0/statistics/rx_bytes`DELTA_RX=`expr $FINAL_RX - $INITIAL_RX`KBPS_RX=`expr $DELTA_RX / 10240 `

    let "RESULT = $KBPS_RX / 3"echo $RESULT > "/sys/devices/platform/wdc-leds/leds:wdc-leds:fuel-gauge/brightness"</blockquote>
    <span style="font-size:130%;"><span style="font-family:arial;">The 3 in there is the scaling factor between the kbps download and the number of lights on. </span><span style="font-family:arial;">Since I'm not often downloading any faster than about 400kbps, and when i am im not really worried about i</span></span>

    <span style="font-size:130%;"><span style="font-family: arial;">0 to 100: lights one led (5 o’clock)</span>

    <span style="font-family: arial;">100 to 150: lights two leds (5 and 7 o’clock)</span>

    <span style="font-family: arial;">150 to 200: lights three leds (5, 7 and 9 o’clock)</span>

    <span style="font-family: arial;">200 to 250: lights four leds (5, 7, 9 and 11 o’clock)</span>

    <span style="font-family: arial;">250 to 280ish: lights five leds (5, 7, 9, 11 and 1 o’clock)</span>

    <span style="font-family: arial;">280ish and more: lights all leds.</span></span>

    <span style="font-size:130%;"><span style="font-family: arial;">I have the whole thing running as a cronjob every 5 minutes</span></span>,<span style="font-size:130%;"><span style="font-family: arial;"> <a href="http://unixhelp.ed.ac.uk/CGI/man-cgi?crontab+5">do that urself</a></span></span>

\*[MBWE]: Western Digital My Book World Edition
