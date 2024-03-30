---
author: admin
categories:
- Instructional
comments: true
date: 2012-01-05 17:29:31+00:00
layout: post
slug: my-guide-to-my-own-favourite-ubuntu-setup
tags:
- Ubuntu
- Chrome Beta
- Dropbox
- TeXLive
- Etckeeper
- Vim
- Gnome Shell
title: My Guide To My Own Favourite Ubuntu Setup
---


This is my own self-indulgant reminder for how to do the things I like. I'll keep adding to this as I think of them.

# Basic Setup

![](http://troll.me/images/x-all-the-things/update-all-the-things.jpg)Install[ Ubuntu Latest](http://www.ubuntu.com/download/ubuntu/download) (currently 11.10), With the third party libraries and a home partition leaving at least 20GB for '/'.

Then Update everything, during which time you can plod along to download the relevant packages for [Chrome Beta](http://www.google.com/landing/chrome/beta/), [Dropbox](https://www.dropbox.com/install?os=lnx), etc

Once the update is done (I'd restart in most cases), additional packages I like to add are;

`vim  vim-latexsuite vim-vimoutliner vim-scripts vim-addon-manager synaptic gnome-do gnome-shell python-setuptools python3-setuptools python-distutils-extra python3-distutils-extra ipython terminator guake evolution openssh-server evolution-plugins-experimental libreoffice-evolution htop gnome-schedule nload perl-doc etherape zenmap gnuplot graphviz dot2tex latexmk cmus irssi etckeeper exuberant-ctags`.

# TeXLive

The Repo-bound texlive isn't complete, so I use the 'real' one.

I seem to be cursed that anywhere I need to install TeXlive, the internet sucks, so I do a full mirror and install locally.

`cd ~; mkdir -p src/tl; cd src/tl; rsync -va --delete rsync://ftp.heanet.ie/mirrors/ctan.org/tex/systems/texlive/tlnet/ .`

Let that run away in the background and get to something else.

Once it's done... `chmod+x install-tl`
`sudo ./install-tl
`
Select `<I>` (Full install)

Coffee.

You'll want to put something like this in your `~/.profile` to put texlive in your `PATH`.

`# set PATH so it includes TexLive
if [ -d "/usr/local/texlive/2011/bin/i386-linux" ] ; then
PATH="/usr/local/texlive/2011/bin/i386-linux:$PATH"
fi`

To enable the `tlmgr` package manager, you'll need to configure with your friendly neighbourhood [CTAN mirror](http://dante.ctan.org/mirmon/); in my case, Heanet.

`sudo tlmgr option repository http://ftp.heanet.ie/mirrors/ctan.org/tex/systems/texlive/tlnet/`

sudo tlmgr update --all

# Dropbox Integration

I use Dropbox to hold a lot of configuration data. Specifically 'dotfiles'. As such, in my Dropbox folder, I have a folder (dotfiles) full of the kind of files you expect to see; .bashrc, .vimrc, .vim/, etc etc etc.

In order to make things simple (ish) remove  the default .bashrc, and Symbolically link (ln-s) this to my custom one in Dropbox.

`cd ~; rm .bashrc; ln -s ~/Dropbox/dotfiles/.bashrc ~/.bashrc`

This [bashrc ](http://pastebin.com/TsnSvjfd)is common to all my machines and is pretty basic.

The .[profile ](http://pastebin.com/qtRqZfJ1)file is where I do most of the work; it has the stuff that I always need, like 'Add Dropbox/bin to the path' and 'add ~/bin to the path', but also says 'source ~/.bashrc_local' for the times I need to have differences between machines (think 32 vs64, etc).

`cd Dropbox/dotfiles; `

`for entry in .profile .vim* .bashrc .vim .config .cmus .irssi .xchat2 ".ssh/config"; do rm $HOME/$entry; ln -s $HOME/Dropbox/dotfiles/$entry $HOME/$entry; done`

# Fixing Gnome-shell

Gnome shell is not perfect, but these help.

Bring back minimise buttons: ` gconftool-2 -s -t string /desktop/gnome/shell/windows/button_layout ":minimize,maximize,close"`

# Other Fixes

### Vim

Funnily enough, installing `vim-addons` and `vim-latexsuite` doesn't actually install `vim-latexsuite`. Package managers are funny that way. Here's the plugins I like to enable.

` sudo vim-addons install python-indent latex-suite taglist markdown-syntax detectindent doxygen-toolkit info justify nerd-commenter utl vimoutliner xmledit`

### `Etckeeper`

Don't forget to init etckeeper; `cd /etc; sudo etckeeper init`

