---
author: admin
categories:
- Instructional
comments: true
date: 2011-06-28 15:27:20+00:00
layout: post
slug: replace-unity-with-awn-and-gnome-do
tags:
- Ubuntu
- avant
- unity
- GUI customization
- gui
- Gnome-Do
- Desktop environment
- Avant Window Navigator
- gnome
- launcher
title: Replace Unity with AWN and Gnome-Do
---


Unity Sucks, and I don't like it. I prefer a combination of Avant Window Navigator, tilda, and Gnome-Do, to go from this

[caption id="attachment_633" align="aligncenter" width="300" caption="Unity, kinda, screen shots don't really work for launchers"][![Unity, kinda, screen shots don't really work for launchers]({{ BASE_PATH}}/uploads/2011/06/unity-300x225.png)]({{ BASE_PATH}}/uploads/2011/06/unity.png)[/caption]

to this
[caption id="attachment_634" align="aligncenter" width="300" caption="My Avant Setup"][![My Avant Setup]({{ BASE_PATH}}/uploads/2011/06/avant1-300x225.png)]({{ BASE_PATH}}/uploads/2011/06/avant1.png)[/caption]

Now, I haven't kept track of all of the changes I've made to my configuration files, so YMMV, but gnome-do and Avant have remarkably good GUI configuration tools, so customise to your hearts content!

Get rid of Unity

` sudo apt-get remove unity unity-asset-pool unity-place-applications unity-place-applications
`

Install the fun-stuff

`sudo apt-get install gnome-do gnome-do-plugins avant-window-navigator awn-settings tilda
`

(I personally prefer to get all the plugins aswell, but thats personal choice; just add in `awn-applets-all` to the above command)

At this point, it'll look like nothing has changed; just log out or log back in (Or reboot), and then unity will be gone (Woohoo!). The Gnome-Do Launcher should have come up, and if you've clicked out of it, it will come back to the foreground with a [windows\command]+Space press.

If everything has gone well, you can type 'Avant' in this launcher, and boom, there should be a window at the bottom. This is the avant launcher.
[caption id="attachment_632" align="alignleft" width="300" caption="Default Avant Window Navigator"][![Default Avant Window Navigator]({{ BASE_PATH}}/uploads/2011/06/avant0-300x225.png)]({{ BASE_PATH}}/uploads/2011/06/avant0.png)[/caption]

Now for some fun stuff.

Use gnome-do to start `tilda`. This is a quake-style terminal that pops down from the top of the screen with a quick [F1] click. Much better than the standard [alt+F2] command launcher.

As for the preferences, hack away at the Avant settings until you're happy. The screenshot above is how I like it (this time).
