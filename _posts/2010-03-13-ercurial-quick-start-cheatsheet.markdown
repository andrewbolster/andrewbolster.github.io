---
author: admin
comments: true
date: 2010-03-13 12:24:47+00:00
layout: post
slug: ercurial-quick-start-cheatsheet
title: Mercurial Quick Start Cheatsheet
wordpress_id: 274
categories:
- Instructional
tags:
- code
- networking
- ns
- programming
- software
- Ubuntu
- version control
---

I hadn't used Mercurial before so I thought it might be a good idea to leave a reminder for me and anyone else who comes across it...

For tidyness, I do all of my dev-stuff ([Subversion](http://subversion.tigris.org/), [Mercurial](http://mercurial.selenic.com/), [CVS](http://www.nongnu.org/cvs/), [Git ](http://git-scm.com/)etc) under ~/src and only take root privileges when its needed; any good makefile should relocate the necessary files for you at the 'make install' or equivalent point.

**Update:**This article was picked up by the guys at [DevCheatSheet.com](http://www.andrewbolster.info/goto/http://devcheatsheet.com/cheatsheet/1589/) and I'm really honoured to be included in a site that I've been dipping into over the years, so if you need any kind of cheat sheet or quick reference, I highly recommend checking them out. _Anyway..._

<!-- more -->To start off, you should add some form of identification to your ~/.hgrc file


> 

>     
>     $ cat ~/.hgrc
>     [ui]
>     username = User Name
> 
> 



Now you can connect to <HOSTNAME> and grab a clone of <PROJECT> for you to work on


> 

>     
>     $ hg clone http://<HOSTNAME>/repo/<PROJECT>
>     $ cd <PROJECT>
> 
> 



Now you can work away, but if you add any files, remember before you commit back to the server to add the new files into the project manifest;


> 

>     
>     $ hg add <ADDFILES>
> 
> 



Once you've made your changes, commit and push them back to the host with an appropriate comment.


> 

>     
>     $ hg commit -m 'I added <ADDFILES> to extend/fix/etc'
>     $ hg push
> 
> 



If you dont want to make any changes, but you've clones a project (say to install something...) and 6 months later you want to update it, you don't have to delete and recreate the directory;


> 

>     
>     $ hg pull  http://<HOSTNAME>/repo/<PROJECT>
>     pulling from  http://<HOSTNAME>/repo/<PROJECT>
>     [...]
>     $ hg update
>     X files updated, X files merged, X files removed, X files unresolved
> 
> 



Of course, this assumed you haven't been tinkering with the code, in which case update will generally override your changes and reproduce whatever is currently sitting on the project server. If you want to merge, do so!


> 

>     
>     $ hg merge
> 
> 



For more interesting commands such as

    
    hg log; hg status


and more, consult the man pages... of if you're looking for serious detail, check out[ 'The Definitive Guide'](http://hgbook.red-bean.com/read/) by fellow island-man, [Bryan O'Sullivan](http://www.serpentine.com/blog/)
