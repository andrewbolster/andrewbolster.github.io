---
author: admin
categories:
- Instructional
comments: true
date: 2013-07-06 09:56:58+00:00
layout: post
slug: ssh-persistence-redux-multiple-sites-and-crontab-laziness
tags:
- Linux
- autossh
- ssh
- networking
- remote access
- cron
- service setup
- reverse shell
- persistent connection
- shell
- Raspberry Pi
- security
title: 'SSH Persistence Redux: Multiple sites and Crontab Laziness'
---


Inspired by a pretty good [write](http://www.reddit.com/r/linux/comments/1ho90h/a_simple_call_home_function_for_a_rasberry_pi/) up by Cynofield as to his setup for getting a Raspberry Pi to "phone home", I thought I'd set out how I do it.

I have a machine that lives behind a 'security' infrastructure that makes my life a living hell.

As a result, I set up automatic persistent reverse shells going back to other machines I use, so if I connect to _those_ machines, I can get into the secure environment, without anything nasty being able to get in with me.

Biggest pain in the ass is setting up the persistence of the connection. This is accomplished in two ways.

**Autossh** maintains the 'once up' persistence, so if the connection drops or is temporarily unavailable, it'll keep trying again.

Because I'm lazy, I wrapped autossh into a little lazy script I call `ssh_tunnel`


    #!/bin/sh
    # Example script to start up tunnel with autossh.
    # This script will tunnel 22 from the local host
    # to 11122 on the remote host.
    ID_FILE=$HOME/.ssh/id_rsa
    AUTOSSH_GATETIME=30
    AUTOSSH_DEBUG=yes
    AUTOSSH_PATH=/usr/bin/ssh
    export AUTOSSH_GATETIME AUTOSSH_DEBUG AUTOSSH_PATH
    autossh -2 -fN -i $ID_FILE -R '*':11122:localhost:22 -R '*':11188:localhost:8888 $*

To initiate the connection, (assuming you've already got [passwordless-login]({{ BASE_PATH }}/2011/12/guide-to-persistent-reverse-ssh-shells-and-port-forwards/) sorted to that particular host) it's just a case of `ssh_tunnel username@remote.host`

Now the connection is set up between the remote host machine and the "protected host", which we'll assume is not externally accessible normally. So to get back from the remote host to the protected host through whatever is in between, ssh into the remote host, and go

`$ ssh username@localhost -p 11122`

Ok, so how to set it up as a service that starts at boot? Easy...

**Cron **is a scheduler built into linux, and TL;DR, it's got more than just times, it can react to 'events'. Of particular interest is the **@reboot** [flag](http://team.macnn.com/drafts/crontab_defs.html).

To edit your per-user cron listing:

`$ crontab -e`

and add in

`@reboot path/to/ssh_tunnel user@host
`

Big benefit here is that it's easy as Pi(e) to set up multiple redundant hosts just by adding a new crontab line.

Simple as.
