---
author: admin
comments: true
date: 2010-06-01 12:31:11+00:00
layout: post
slug: customised-user-directories-in-ubuntu
title: Customised User Directories in Ubuntu
categories:
- Instructional
tags:
- bash
- desktop
- dropbox
- linux
- shell
- Ubuntu
- workstation
---

I've been doing alot of messing around in Ubuntu recently and there are lots of tweaks I like to make. One of them being to show the contents of my home folder as my desktop; I don't need any more pointless folders....

Dead easy, there is a .config directory under your $HOME dir, containing several files. The one we need is user-dirs.dirs , and it looks something like this.

{%highlight bash%}
# This file is written by xdg-user-dirs-update
# If you want to change or add directories, just edit the line you're
# interested in. All local changes will be retained on the next run
# Format is XDG_xxx_DIR="$HOME/yyy", where yyy is a shell-escaped
# homedir-relative path, or XDG_xxx_DIR="/yyy", where /yyy is an
# absolute path. No other format is supported.
#
XDG_DESKTOP_DIR="$HOME/Desktop"
XDG_DOWNLOAD_DIR="$HOME/Downloads"
XDG_TEMPLATES_DIR="$HOME/Templates"
XDG_PUBLICSHARE_DIR="$HOME/Public"
XDG_DOCUMENTS_DIR="$HOME/Documents"
XDG_MUSIC_DIR="$HOME/Music"
XDG_PICTURES_DIR="$HOME/Pictures"
XDG_VIDEOS_DIR="$HOME/Videos"
{%endhighlight%}

And this is what I changed mine to

{%highlight bash%}
# This file is written by xdg-user-dirs-update
# If you want to change or add directories, just edit the line you're
# interested in. All local changes will be retained on the next run
# Format is XDG_xxx_DIR="$HOME/yyy", where yyy is a shell-escaped
# homedir-relative path, or XDG_xxx_DIR="/yyy", where /yyy is an
# absolute path. No other format is supported.
#
XDG_DESKTOP_DIR="$HOME"
XDG_DOWNLOAD_DIR="$HOME/Downloads"
XDG_TEMPLATES_DIR="$HOME/Templates"
XDG_PUBLICSHARE_DIR="$HOME/Public"
XDG_DOCUMENTS_DIR="$HOME/Dropbox/Documents"
XDG_MUSIC_DIR="$HOME/Music"
XDG_PICTURES_DIR="$HOME/Dropbox/Photos"
XDG_VIDEOS_DIR="$HOME/Videos"
{%endhighlight%}

Changed desktop directory to home
Made the Documents and Pictures directories reference the relevent [Dropbox](http://www.andrewbolster.info/2010/01/ubuntu-windows-sharing-a-dropbox-folder-on-ntfs/) folders
