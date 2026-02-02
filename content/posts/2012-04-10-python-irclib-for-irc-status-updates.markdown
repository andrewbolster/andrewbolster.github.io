---
author: admin
categories:
- Instructional
comments: true
date: 2012-04-10 17:08:44+00:00
layout: post
slug: python-irclib-for-irc-status-updates
tags:
- 'Farset Labs'
- Hackerspace
- IRC
- Linux
- Programming
- Python
- Ubuntu
- irc
title: Python + irclib for IRC Status Updates
---


IRC, Python, Ubuntu linux. Simples!

Same as by [Twitter]({{ BASE_PATH }}/2012/04/python-oauth2-for-twitter-status-updates/) post, but for IRC.

Biggest problem with this one was working out that the IRC server needs to be kept alive with the `irclib.IRC.process_once()` command. This is wrapped in the while loop that assumes that there is other stuff going on for which you are waiting on a condition to be satisfied, but could easily be ignored if one is just sending out one message. Also, the PRIVMSG command can be used to broadcast to a channel, as is used here, or, as the name suggests, to communicate with a specific user.

All `$VARIABLES` should be replaces with your own stuff


    import irclib
    import time

    username="$USERNAME"
    irc_net="$NETWORK"
    irc_chan="$CHANNEL"
    irc_port=6667

    try:
        irc=irclib.IRC()
        irc_serv=irc.server()
        irc_serv.connect(irc_net,irc_port,username)
        irc_serv.join(irc_chan)
    except irclib.IRCError as err:
        print("Cannot Connect to IRC Service, Aborting:"+err)
        exit

    def post_irc(status):
        irc_serv.privmsg(irc_chan,status)

    while True:
        time.sleep(1)
        irc.process_once()
        if $CONDITION:
            post_irc($MESSAGE)
