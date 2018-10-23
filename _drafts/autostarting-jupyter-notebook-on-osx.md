---
layout: post
title: Autostarting Jupyter Notebook on OSX
tags: jupyter, python, osx
category: hotfix
---

So, I'm a Mac person now. Never expected to be here, and it's not by choice, but that's life. 

Either way, I've been trying to wrap my way around how things work in Mac World, and this was one that bugged me for a while; starting [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/) in the background at login. 

First off I started with [this](http://andykee.com/configuring-jupyter-to-automatically-start-in-the-background-on-osx.html) tutorial by Andy Kee, which didn't quite work. 

So, few things I learned; there's no globbing in plist files, so you'll have to modify this for your own user and python environment. 

Open up the LaunchAgent:

```zsh
vim Library/LaunchAgents/org.jupyter.notebook.plist
```

And add the below (with $USERNAME and $PYTHONPATH replacements, i.e. the `jupyter` executable should be under the `$PYTHONPATH/bin/` folder, check this with `which jupyter` from a terminal)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>KeepAlive</key>
    <true/>
    <key>Label</key>
    <string>org.jupyter.notebook</string>
    <key>ProgramArguments</key>
    <array>
      <string>$PYTHONPATH/bin/jupyter</string>
      <string>notebook</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardErrorPath</key>
    <string>/Users/$USERNAME/Library/LaunchAgents/org.jupyter.notebook.stderr</string>
    <key>StandardOutPath</key>
    <string>/Users/$USERNAME/Library/LaunchAgents/org.jupyter.notebook.stdout</string>
    <key>KeepAlive</key>
    <true/>
    <key>WorkingDirectory</key>
    <string>/Users/$USERNAME/</string>
  </dict>
</plist>
```

Then, similar to `systemd` in Linux, the startup service `launchd` needs to know about the file;

```zsh
launchctl load Library/LaunchAgents/org.jupyter.notebook.plist
```

You can manually start the service with `launchctl start org.jupyter.notebook` and it will automatically start up on whatever setup you've got  in your [jupyter profile](https://jupyter-notebook.readthedocs.io/en/stable/config_overview.html)
