---
author: admin
comments: true
date: 2012-04-10 17:52:11+00:00
layout: post
slug: k8055-usb-python-twitter-irc-space-indicator-as-a-os-service
title: 'K8055 USB + Python + Twitter + IRC: Space Indicator as a OS Service'
categories:
- Instructional
tags:
- farsetlabs
- irc
- k8055
- python
- twitter
---

[caption id="attachment_768" align="alignright" width="231" caption="Big Red Button, Does what it says on the tin"][![]({{ BASE_PATH}}/uploads/2012/04/Emergency-stop-pushbutton-box-key-mushroom-switch.jpg)]({{ BASE_PATH}}/uploads/2012/04/Emergency-stop-pushbutton-box-key-mushroom-switch.jpg)[/caption]

After a long time in the oven, [Farset Labs is up and running](http://farsetlabs.org.uk/blog/2012/03/launch-day-hackathon/). Unforanately we don't have any of the crazy equipment yet, since we're broke.

As my first 'official' Farset Labs project, I've installed a 'Big Red Button' to notify the [@FarsetLabs](http://twitter.com/farsetlabs) twitter feed and #FarsetLabs on [Freenode](http://freenode.net) to the status of the space.

Basically, first person pushes the BRB down in the morning, then one of the directors key-unlocks the space to 'close' it.

This was accomplished using the  [Velleman K8055 USB interface board](http://www.velleman.eu/products/view/?country=be&lang=en&id=351346) and a lot of speaker wire.

Simple enough, but a process fruaght with stupid mistakes, such as:

	
  * Whoops, have to run as sudo to access the USB device

	
  * Whoops, [OAuth2](http://oauth.net/2/) is a pain in the ass

	
  * Whoops, have to change each message slightly or Twitter [thinks I'm spamming the joint](http://blog.tropo.com/2010/12/01/reminder-beware-of-duplicate-tweets-when-testing-twitter-apps-on-tropo/)

	
  * Whoops, have to do [PING/PONG responses](http://stackoverflow.com/questions/6853071/python-check-if-irc-connection-is-lost-ping-pong) to the IRC server (easier to use `irclib` since it manages that for you)

	
  * Whoops, need to keep talking to the IRC server otherwise it disconnects us (hence the `irc.process_once()` call in the main `while` loop)

	
  * Whoops, Ruby isn't any better than python at OAuth2

# Prerequisites

    
    sudo apt-get install build-essential libusb-dev python-dev python-setuptools python-irclib

    
    sudo easy_install oauth2

    
    sudo mkdir /opt/bin

# Actual Work

    
    cd /tmp/

    
    wget package from <a href="http://sourceforge.net/projects/python-k8055/">http://sourceforge.net/projects/python-k8055/</a>

    
    tar -xvjf python-k8055-0.2.tar.bz2

    
    cd python-k8055-0.2

    
    sudo python setup.py install

    
    cd /opt/bin/

    
    sudo wget <a href="http://pastebin.com/KqCKhKG6" target="_blank" title="Occupy Farset Python Script">occupy-farset.py</a>

    
    cd /etc/init/

    
    sudo wget <a href="http://pastebin.com/mzRZWP75" target="_blank" title="Occupy Farset Upstart Conf File">occupy-farset.conf</a>

    
    sudo initctl reload-configuration

    
    sudo service occupy-farset start

    
    sudo service occupy-farset status

# Explanation

	
  1. Download and install [python wrappers](http://python-k8055.sourceforge.net/) for the [Velleman K8055 USB interface board](http://www.velleman.eu/products/view/?country=be&lang=en&id=351346)

	
  2. Copy our customised (but highly customisable) python script that talks to IRC, [Twitter](http://www.andrewbolster.info/2012/04/python-oauth2-for-twitter-status-updates/), and the interface board

	
  3. Copy and install the Ubuntu Upstart conf file to use the script as a service

	
  4. Fire off the service and test that it's still up.

That's all folks!

