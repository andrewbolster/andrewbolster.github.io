---
author: admin
comments: false
date: 2008-10-27 19:15:00+00:00
layout: post
slug: my-conkyrc
title: My conkyrc
wordpress_id: 24
categories:
- Instructional
tags:
- conky
- lifehacker
- linux
- Ubuntu
---

Contents (what you get out of this)  
Weather, HDDtemp, UL/DL speed and cumulative meters, CPU load, Folding@Home status, Remote transmission download status (could be local, easy change), gmail status, RAM usage, Uptime, Date/Time, ToDo list  
  
These all automatically update dependant on the execi variable.  
  
Preface (What you need to get this all working)  
Linux OS (Ubuntu?)  
[Conky](http://conky.sourceforge.net/) (obv, see someone elses guide for how to get that *HINT* synaptic is ur friend)  
[Transmission](http://www.transmissionbt.com/) download manager (local or remote)  
Folding at home installed with [origami](https://help.ubuntu.com/community/FoldingAtHome/origami) (could be local or remote using the same logic as the Transmission manager)  
[Passwordless SSH authentication](http://penguinsandcoffee.blogspot.com/2008/10/links.html) (if your using this with any remote hosts)  
A todo list on the desktop called todo (strange that...)  
  
  
WARNING I'm lazy so im not telling you why or how this all works. Work it out yourself. I Got alot of the system monitoring stuff from a variety of places (lifehacker i think, my apologies to whoever i stole from).  
  
  
The Guts (The Guts)  
cat .conkyrc  
use_xft yes  
xftfont verdana:size=8  
alignment top_left  
xftalpha 0.8  
own_window yes  
own_window_type override  
own_window_transparent yes  
own_window_hints undecorated,sticky,skip_taskbar,skip_pager  
double_buffer yes  
draw_shades no  
draw_outline no  
draw_borders no  
stippled_borders 10  
border_margin 4  
border_width 1  
default_shade_color grey  
default_outline_color black  
default_color BADCDD  
use_spacer none  
no_buffers yes  
uppercase no  
text_buffer_size 512  
color1 F8DF58  
  
  
# ${color 6694B2}${font OpenLogos:size=45} u t  
  
#  ${color F8DF58}${font StyleBats:size=16}8${font}  Battery: ${battery_percent}% ${battery_bar}  
TEXT  
${color BADCDD}${font weather:size=82}${execi 600 ~/scripts/conditions.sh}${color}${font}${voffset -25}  ${execi 1200 ~/scripts/pogodynka.sh}  
 ${font weather:size=28}x ${font}HDD ${execi 1 ~/scripts/hddmonit.sh}�C   
 ${font PizzaDude Bullets:size=16}v${font}   Up: ${upspeed eth1} Kb/s  
 ${font PizzaDude Bullets:size=16}r${font}   Down: ${downspeed eth1} Kb/s  
 ${font PizzaDude Bullets:size=16}M${font}   Upload: ${totalup eth1}  
 ${font PizzaDude Bullets:size=16}S${font}   Download: ${totaldown eth1}  
 ${color ffffff}${font StyleBats:size=16}A${font}  CPU0: ${cpu cpu0}% ${cpubar cpu0}  
 ${font StyleBats:size=16}A${font}  CPU1: ${cpu cpu1}% ${cpubar cpu1}  
 ${font StyleBats:size=16}Y${font}  ${execi 10 origami monitor | awk '/Progress:/ {print $2}' | sed '/%$/N;s/\n/ /' }  
${execi 600 ssh REMOTEUSER@REMOTEHOST /opt/bin/transmission-remote -l |sed 's/  [ ]*/\t/g'| awk -F'\t' '/ing/ {print $3,"\t", $9}'| sort -rn}  
 ${color F8DF58}${font FreeSans:size=16}@${font}${execpi 300 python ~/scripts/gmail_parser.py GMAILUSER GMAILPASSWORD 3}  
 ${color C2E078}${font PizzaDude Bullets:size=16}J${font}   $mem / $memmax  
 ${font StyleBats:size=18}P${font}  Work:  ${uptime_short}  
${font Radio Space:size=14}${time %A %d %Y}  
    ${font Radio Space:size=55}${time %H:%M}  
${color F8DF58}${font FreeSans:size=10}${color0}TODO:${color1}  
${color F8DF58}${font FreeSans:size=10}${execi 30 cat /home/USERNAME/Desktop/todo}

Please at least pretend to click my ads. I know they're a joke, but still, it dont cost ya anything!
