---
category: ''
description: ''
layout: post
tags:
- timelapse creation
- community growth
- mencoder settings
- eventcam setup
- shiny eventcam setup
- web development
- Linux motion utility
title: The Making of a Timelapse
---

{% include JB/setup %}

Starting in May 2012 (a few weeks after we 'opened') I set up an eventcam in [Farset Labs](http://farsetlabs.org.uk), and I don't think I ever officially explained it...

Well, first off we were using a [Microsoft Lifecam](http://www.microsoft.com/hardware/en-gb/p/lifecam-cinema) that was kindly donated by [Josh Holmes](https://twitter.com/joshholmes). This was wired up to an even-then-ancient [Asus Eee 700](http://en.wikipedia.org/wiki/Asus_Eee_PC#Eee_700_series)[^1], wired with power and network, and left in the roof. That was about it.

The Linux `motion` utility was used to drive the camera and after fiddling with `motion`'s many many options, I settled on [this config file](https://gist.github.com/andrewbolster/8373019) to strike a balance between dropping boring frames when nothing was happening but to also maintain 'day night' cycle more or less realistically.

With a little bit of [magic scripting](https://gist.github.com/andrewbolster/8373242) that not only looked after the naming and sorting of the images taken each day, but also tarred-up the previous days images, generated a 'daily' timelapse, and uploading that timelapse to Youtube directly, making videos like this almost automatic.

<iframe width="560" height="315" src="//www.youtube.com/embed/Hc0PBWFCblQ" frameborder="0" allowfullscreen></iframe>

Aside from lots of storage problems since a busy day could generate over 2GB of full HD images (that meant that in the end, we 'lost' serveral weeks, had to move the backup server on several occasions), before eventcam was retired, we collected almost 350,000 individual images. That's 195 GB of images from 176 individual days between 17/05/2012 and 22/06/2013.

So, how the hell do you turn over a quarter of a million images into a timelapse? [`mencoder`](http://en.wikipedia.org/wiki/MEncoder)

I won't go through the long pain that was finding the right settings for the decimate option[^2], which drops similar consecutive frames, which cut down the first draft from 2 hours to 23 minutes. Thanks to Compn on #mplayer for help.

~~~~ shell
noglob mencoder mf://*.jpg \
-noskip -mf fps=25:type=jpg \
-ovc x264 -x264encopts bitrate=1200:threads=4 \
-vf decimate=0:524288:512:2 -o /dev/shm/decimated.mkv
~~~~

I've dropped the output file into `/dev/shm` which is a poor-man's ramdisk for speed things up a bit. But it still takes a looong time, although since I got a new machine in the office, this was as good an excuse as any for a 'burn in'.


If I'm back over Easter, the plan is to set up a new shiny eventcam setup in both the eventspace and the hopefully-finished-by-then workshop, which will be awesome.


[^1]: Funnily enough this little-laptop-that-could has since been adopted by the space, simply to continue to let the uptime counter clock up. It was nearly up to 500 days on the trot before some hateful individual (jk) rebooted it without knowing what it is. One of the joys of a growing community!

[^2]: the Decimate options are basically black magic, I just bounced through powers-of-two until I found ones that worked; mine say that you can have as many repeated frames as you like (0) that either don't vary by more than 524288 bits (not sure if this is just colour and/or luminosity), or if half (2) the frame changes by at least 512 (again, not entirely sure if that makes sense, but that's what the [man](http://www.mplayerhq.hu/DOCS/man/en/mplayer.1.html) pages say and that's what worked

