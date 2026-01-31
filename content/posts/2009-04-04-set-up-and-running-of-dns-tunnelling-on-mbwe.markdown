---
author: admin
categories:
- Instructional
comments: false
date: 2009-04-04 23:14:32+00:00
layout: post
slug: set-up-and-running-of-dns-tunnelling-on-mbwe
tags:
- code
- coding
- MyBook
- SSH
- hardware
- security
- DNS
- networking
- Embedded
- Perl
- traffic encryption
- DNS2TCP
- network setup
- software
- linux
- port forwarding
- SOCKS proxy
- eee
- desktop
- programming
title: Set up and running of DNS tunnelling on MBWE
---


Last week or there abouts, there was a big buzz around the interwebs revisiting [Dan Kaminski's OzymanDNS tool](http://www.doxpara.com/?p=51), a perl based toolkit for tunnelling TCP traffic over DNS requests (technically its TCP over SSL over DNS but whos counting) That was originally released mid-2004.

I never really found the true source of the new hype surrounding a "old" project (it may have been HAK5's[ episode 504](http://www.hak5.org/episodes/episode-504) that demonstrated the tool, mubix has put the [write up](http://www.room362.com/archives/456-ozymandns-tunneling-ssh-over-dns.html) in at [room362](http://www.room362.com/))

I then found that it had since been reengineered by[ Andreas Gohr](http://www.splitbrain.org/blog) and wrote a brilliant[ write up ](http://www.splitbrain.org/blog/2008-11/02-dns_tunneling_made_simple)on its setup and use and i think is the best example for any skill level.

Long story short, i gave it a go redirecting dns requests from my andrewbolster.info domain using my main development box at home as a "server" and tested it using my Asus EEEpc from a guest wireless access point in work, and it works. Its VERY slow, but it works.

But that left me with a problem; I turn off my dev box as often as I can (Dual core CPU, 3 internal HDDs, Cooling systems, 6GB ram, Fatty graphics card, etc, kinda draw a bit of juice) and i definatly dont want to leave it on if i'm going to be away from the house for weeks. So i turned to my brilliant Western Digital MyBook World edition.

Problem was the Perl in optware aswell as the one that ships with the device, had no compiled threads support, and on a less technical point, running cpan would max our CPU and memory on this tiny box, all taken up by the perl processes. Long story short, perl was not the way to go ( I would have recompiled Perl as per the write up on [mybookworld.wikidot.com](http://mybookworld.wikidot.com/perl-5-8-8), but with perl performing as badly as it was with relativly simple "one time" processes, i didnt want to have that running 24/7/356 ).

Tracing back through the history led me to [dns2tcp](http://www.hsc.fr/ressources/outils/dns2tcp/index.html.en), originally written by Olivier Dembour in C, my favourite language for small systems (duh) and i found it to be hurrendously under-documented. So below is a quick blow by blow of what i did to get dns2tcp installed, running and client configured

If you do not have access to a hosted or internet assessible DNS server / BIND system, you are screwed; Some people will let you use theirs, and if you ask really nicely I'll put in a redirect on mine, but i probably wont.


  1. (Assuming you have a web interface to a internet facing DNS server) Add a "NS" name listing in your DNS settings that redirects to a server that DOES NOT RUN DNS. Example:
I have the domain andrewbolster.info that has its own DNS settings, so when you go to blog.andrewbolster.info, it goes to a different machine than going to www.andrewbolster.info does.
I have a [DynDNS](http://www.dyndns.com/services/dns/dyndns/) entry for my home network, eg iwant2gohomenow.dyndns.net that i use for accessing the MBWE from anywhere, i do not host a DNS server at home. So if im running my dns2tcp server at iwant2gohomenow.dyndns.net the entry I put in my andrewbolster.info ([Dreamhost](http://www.dreamhost.com/hosting.html) ) DNS configuration is this:

> Name: [ tunnel ].andrewbolster.info
Type : [ NS ]
Value: [ iwant2gohomenow.dyndns.org ]

If i was going it command line style in BIND I'd add

> tunnel.andrewbolster.info      IN        NS        iwant2gohomenow.dyndns.net

This basically mean that when you ask "What ip address does tunnel.andrewbolster.info have?", the andrewbolster.info server says "pfft , i dunno, ask the guy at iwant2gohomenow.dyndns.org".

Unfortunatly, Theres nobody he can talk to there.


  2. PORT FOWARDING IS A PAIN There, i said it, but fact is its good security. DNS operates on UDP port 53. In my case, the internal IP address of my MBWE is 192.168.1.3, and if your reading this far down then I assume you can port foward on a router. If not, [this is a good guide ](http://lmgtfy.com/?q=port+fowarding).


  3. If you havent already hacked your MBWE to shreds,[ this ](http://mybookworld.wikidot.com/first-steps-with-mbwe)is a great place to start. For the below to work, the "server" to host the dns tunnel MUST have a ssh box (you can get it to redirect using multiple ressources below, but I leave that as an exercise for the reader)


  4. Log on to the device that is going to be your server and make sure you have the build packages for your environment: in my case it was simply a case of

> ipkg install gcc

For debian based, its

> apt-get install build-essential


  5. Download the dns2tcp tarfile from  [dns2tcp](http://www.hsc.fr/ressources/outils/dns2tcp/index.html.en) and untar it  in a sensible place like /opt/src or /usr/src ({%highlight bash%}tar -xvzf <tarfile> or gunzip -c <tarfile> | tar xvf - {%endhighlight%} depending on your environment)


  6. READ THE INSTALL AND README DOCUMENTS, I know they both suck, just read them.


  7. This bit is (hopefully) easy; [ ./configure && make && make install ]  answer the questions it asks if it asks, and if it craps out and google cant help, and forums dont help, [twitterme](http://www.twitter.com/bolster)!


  8. cd back to your home directory and replace the values entered with those that are appropriate to you:

> cat > ~/.dtf2tcpdrc << EOF
listen = 192.168.1.3
port = 53
domain = tunnel.andrewbolster.info
ressources = ssh:127.0.0.1:22
EOF

Yes, i know, resources is spelt wrong, but it works, ok?


  9. Now test it with

> dns2tcpd -F -d2

The -F keeps it in the foreground instead of daemonising it, and the -d2 is a debug flag to give just a bit more info.
If it doesnt crap out, your good to move on to the client.


  10. Do steps 4,5,and 7 on whatever client you are using


  11. Same idea with the home directory file

> cat > ~/.dtf2tcprc << EOF
domain = tunnel.andrewbolster.info
ressource = ssh
local_port = 2222
debug_level = 1
server = bolster.homelinux.net
EOF

The local_port is completly arbitrary but 2222 is my default for remove shells


  12. Now for the test! Start dns2tcpc with

> dns2tcpc -d2

And you should get no errors
Now go to a different terminal and log into the server like this

> ssh testUser@localhost -p 2222

Whats that you say? localhost? dns2tcp has opened up a port on your client system that connected to port 22 on the server, so your logging into the server, but my going thru the client port first.


  13. If all goes well, you should have your normal user shell on the server, but if you fire up wireshark or some other traffic sniffer, you'll see that there is only DNS traffic (assuming you done have FF or anything else running at the time)


  14. Waaay, shell, fun, and everyone loves [Lynx](http://en.wikipedia.org/wiki/Lynx_(web_browser)), but were not done yet. If your "server" ssh server has been updated in the past decade, it can also operate as a [SOCKS](http://en.wikipedia.org/wiki/SOCKS) proxy, so we can route "real" web surfing fun through DNS without any of that pesky deep packet inspection stuff because its all wrapped up in SSL.
To fire up a SOCKS connection, execute

> ssh testUser@localhost -p 2222 -D 8888

As with 2222, 8888 is arbitrary, but i use it for proxies.


  15. At this point we have an arrangement where everything that gets sent to port 8888, gets sent on thru port 2222 on the client, that then gets encrypted and sent off as an obsfucated DNS query, and while that sounds interesting, its not really useful; Until you change your firefox proxy settings to localhost:8888 (dont forget to checkbox the socks)

ITS SLOW, I know, but then next time you miss a bus or a train or a plane and you are stuck in some god foresaken hell hole of a transit hub with only the expensive [starbucks](http://www.starbucks.com/retail/wireless.asp) wifi to serve you, it is on your own conscious wether you use this too to accidentally[ GET AROUND PAYING FOR IT](http://revision3.com/forum/showthread.php?t=26856). Its illegal, how could you ever think about doing something like GETTING FREE INTERNET. I'm ashamed of you for even thinking about USING FREE TOOLS TO GET AROUND PROPRIATORY RESTRICTIONS TO THE FREE INTERNET. Go sit in the corner, the corner with the[ T-Mobile wireless access.](https://selfcare.hotspot.t-mobile.com/locations/viewLocationMap.do)

And, if you find this write-up useful or interesting, please a) repost it with credit b) comment
Also, big thanks to all the people whos tools I've used to demonstrate this, be sure to visit their websited and subscribe to their feeds.
