---
date: 2020-02-18T16:40:00+00:00
layout: post
tags:
- pi
- networking
- iot
- emon
- farset
- mosquitto
- mqtt
- raspberry pi
title: Mosquitto (MQTT) Emon Pi (Open Energy Monitor) Forwarding Bridge
---

Super quick one this time; I've been experimenting with [MQTT](http://mqtt.org/) to act as a central messaging broker for "Farset In-Space Related Stuff" as part of the near continuous [renovations and expansions](https://blog.farsetlabs.org.uk/2019/09/farset-labs-2-0-nearly-ready-to-go/).

We previously had a well configured [EMonPi](https://wiki.openenergymonitor.org/index.php/EmonPi) set up with nice dashboards and things, but that died a death at some point during the move, who knows.

Anyway, EmonPi has a built in [mosquitto](https://mosquitto.org/) broker, which it uses to keep 'state' across several parts of the emonpi ecosystem.

On the other side, I had a relatively easy job getting [Mosquitto set up via Docker on our Synology NAS](https://hub.docker.com/_/eclipse-mosquitto) (also [NodeRed](https://nodered.org/), but that's for another day), however I had no idea how to connect the two.

I was expecting the kind of intricate surgery to 'replace' a core part of emonpi's architecture with an 'off-device' broker, and all the failure that that would entail, but helpfully, the MQTT protocol has a concept of "bridging", where you can effectively make one Broker 'publish' all it's topics on another broker. [Super Easy, Barely an Inconvenience](http://www.steves-internet-guide.com/mosquitto-bridge-configuration/).

TL;DR
Create a file called `bridge_over_the_river_que.conf`\* in the mosquitto/config/conf.d/ folder on the *source* device (in this case the emon pi), with the following contents \*
```
#connection farset

connection bridge-fsl
address 192.168.1.222:1883

topic # out 0
```

If you want to make the 'bridge' bi directional, you can add `topic # in 0` to also grab everthing from the 'destination' broker, but in this case, we don't want that.

If we wanted to be pedantic and to only forward `emon` sensor [topic values](https://guide.openenergymonitor.org/technical/mqtt/), or values from a particular device, you can replace the `#` with the appropriate [topic wildcard](https://subscription.packtpub.com/book/application_development/9781787287815/1/ch01lvl1sec18/understanding-wildcards) (you knew that you could do wildcards in MQTT right? Cus I didn't!)

\* Naturally, adjust the values to something that makes sense in your setup....
