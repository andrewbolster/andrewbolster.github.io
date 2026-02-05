---
categories:
- Commentary
comments: false
date: 2008-09-24 22:25:00+00:00
slug: primers-coming-up
tags:
- Bash
- Education
- Linux
- Perl
- Programming
- SSH
- Ubuntu
- XML
title: Primers Coming Up
---

Thru my work I'm thrown into alot of technologies that i dont nearly know enough about and as with alot of tech related things, the education scene is basic basic basic..GURU with little or no gradiation, so what I'm going to do is post what i learn when i learn it and where i learn it from and hopefully it'll be useful for someone else, and I'll also take the opportunity to rehash stuff I've already done.



ATM I'll probably be doing Bash scripting, Perl Scripting, XML, and whatever UNIX stuff comes up whenever I'm writing, but for now and for a relativly simple start; X display fowarding...



This is the setup: Linux/Unix based "client" and "server"; in my case I have headless systems that i fiddle with from time to time, but after a while vim just becomes a pain, and as for viewing html files etcetc copying things back and forth is a pain in the ass.



The solution is already there; From its beginning the X server has always been client server based on some level. Basically what were gonna do is tell the server to use the client as an X display; this is controlled thru an environment variable, strangly called DISPLAY

Lets assume were using SSH. \*nix SSHd has a simple system for fowarding and routing the relevent X ports (these wont show up in your "tunnels" tab if your using something like putty, but you shouldnt be using putty anyway)

Theres two versions of this fowarding ability, X and Y. in a nutshell, X is compressed and encrypted. Y isnt. On slow links, Y is probably your best bet, also some servers dont support the X flag. Also also, some sysadms disable this X fowarding.

Anyway, to the point. 

login to the server thusly

```bash
client# ssh user@server -X
```

then when you get a shell check to see if DISPLAY isnt already set (some servers are good enough to do this for you)

```bash
server# echo $DISPLAY
```

if your lucky it'll say localhost:10.0 otherwise it'll probably say :0.0 or something similar

If your in this unlucky situation, just enter

```bash
server# DISPLAY=localhost:10:0
```

then try it out, by running the clock and forking it into the background (&)

```bash
server# xclock &
```

Job done. Later
