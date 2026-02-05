---
aliases:
- /2010/04/the-de-bill-or-how-i-learned-to-stop-worrying-and-love-tor.html
categories:
- Commentary
- Instructional
comments: true
date: 2010-04-09 11:11:35+00:00
slug: the-de-bill-or-how-i-learned-to-stop-worrying-and-love-tor
tags:
- Chrome
- Cybersecurity
- Desktop
- Firefox
- Linux
- Personal
- Privacy
- Ubuntu
title: The DE Bill, or, How I Learned to Stop Worrying and Love Tor
---
Folks, we're basically screwed; The Digital Economy Bill recieved Royal Accent on April 9th and is officially now Law.

So after barely three days of parliamentary 'debate' where only 20-ish MP's actually spoke on the subject (but somehow 189 MP's decided it was a good idea anyway), our civil rights have been sacrificed infront of the alter of copyright.

[Many](http://eu.techcrunch.com/2010/04/08/doublethink-the-digital-economy-bill-against-the-digital-economy/) sites have a much more indepth tretise on the subject than I could do so I'll keep this short.

Churchill said this about the rise of Socialism in Europe during WWII:

> “The stations of uncensored expression are closing down; the lights are going out; but there is still time for those to whom freedom and parliamentary government mean something, to consult together.”

Anyway, no point in whining, time to do something about it.

**How to use TOR to anonymise your internet traffic in Ubuntu**

[Tor aka The Onion Router](http://www.torproject.org/):

> Tor is free software and an open network that helps you defend against a form of network surveillance that threatens personal freedom and privacy, confidential business activities and relationships, and state security known as[ traffic analysis](http://www.torproject.org/overview.html.en).
Tor protects you by bouncing your communications around a distributed network of relays run by volunteers all around the world

Nice and easy, step 1, add the repository to your

/etc/apt/sources.list

`deb     http://deb.torproject.org/torproject.org $DISTRIBUTION main`

In my case, $Distribution  was karmic, for a full list of available distributions, [check here](http://deb.torproject.org/torproject.org/dists/)

Grab the gpg key and update the apt-cache, and install:

`gpg --keyserver keys.gnupg.net --recv 886DDD89
gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add -
sudo apt-get update
sudo apt-get install tor tor-geoipdb
`

So that's tor installed, and you can act as a tor node, sharing your bandwidth to protect the anonymity of others (To mess with this, [check out To﻿r's guide](http://www.torproject.org/docs/tor-doc-relay.html.en)). But to actually take advantage of it yourself, there's more steps;

1) [Polipo](http://www.pps.jussieu.fr/~jch/software/polipo/): A web caching proxy that should speed things up considerably while lightening the load on the Tor network. Normally just a simple `apt-get install polipo`, then grab the [Tor Project's polipo configuration](https://svn.torproject.org/svn/torbrowser/trunk/build-scripts/config/polipo.conf) and put it in either

/etc/polipi/config

or

~/.polipo

.
Finally, tidy everything up with a `sudo service polipo restart`

2) Use it: Either point your regular browser to HTTP proxy through

localhost:8118

(Polipo), or for SOCKS applications like IM and socket applications, go directly to the tor service at

localhost:9050

, Although depending on your system configuration, [this could be a bad idea](https://wiki.torproject.org/noreply/TheOnionRouter/TorFAQ#SOCKSAndDNS) if you're really paranoid.

3) [Test it.](https://check.torproject.org/) Heres how it looks when Tor is not configured properly.
[![Tor Failure](/uploads/2010/04/tor_fail-300x225.png)](/uploads/2010/04/tor_fail.png)

And heres how it is when it works!

[![Tor Success](/uploads/2010/04/tor_win-300x225.png)](/uploads/2010/04/tor_win.png)

There are a million and one ways of organising Tor, but Google and find the solution that works for you. For Firefox I recommend [FoxyProxy](http://foxyproxy.mozdev.org/), and [Proxy Switchy](https://chrome.google.com/extensions/detail/caehdcpeofiiigpdhbabniblemipncjj?hl=en-gb) for Chrome
