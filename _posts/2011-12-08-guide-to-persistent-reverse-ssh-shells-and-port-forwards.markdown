---
author: admin
categories:
- Instructional
comments: true
date: 2011-12-08 13:41:41+00:00
layout: post
slug: guide-to-persistent-reverse-ssh-shells-and-port-forwards
tags:
- code
- tunnel
- linux
- Ubuntu
- bash
- ssh
- port forwarding
- nix
- unix
- Unix
- networking
- forwarding
- port
- reverse shell
- ssh tunnel
title: Guide to Persistent Reverse SSH Shells and Port Forwards
---


Idiot proof setup for persistent reverse shells / port forwards (same thing) under a Ubuntu VM remote and my Dreamhost server, but should apply to nearly\* all \*nix's

First off, some terms to keep this easy. I want to be able to access my in-office VM, `xavier` from my server `magneto` (not my names, but they conveniently complement). `xavier` is **not** publicly accessible, but `magneto` is. I'll be replacing all of the [FQN's](http://en.wikipedia.org/wiki/Fully_qualified_name) with these terms so expand on your own. In generic terms, `xavier `is the remote machine (i.e the one behind some NAT firewall or such that you want to get access to) and `magneto `is the local machine. Its a bit confusing since all of the work is done on `xavier`, but it makes sense in the long run. Just trust me and get on with it.

	
  1. Make sure that `xavier `can access `magneto `without a password by testing with ssh from `xavier `to `magneto `i.e. `[bolster@xavier]:~ $ ssh magneto`. (general solution to this **not** working is `[bolster@xavier]:~$ ssh-keygen; ssh-copy-id magneto` but [YMMV](http://www.urbandictionary.com/define.php?term=YMMV))

	
  2. Also make sure that `xavier `has an ssh server running (test with `[bolster@xavier]:~ $ ssh localhost`, fix with `sudo apt-get install openssh-server -y` )

	
  3. Save the [`ssh-persist` script](http://pastebin.com/5Xj9vMm5) to somewhere useful and make it executable ( `chmod +x path/to/ssh-persist` )

	
  4. Make `ssh-persist` start at startup (I like just adding it to Ubuntu's 'Startup Applications' dialog, again YMMV)

	
  5. Logout and log back in again! (or just start `ssh-persist` manually)

	
  6. Test with by sshing into magneto, then `ssh localhost -p 2222` (or whatever you set it to). Note that you will still be asked for the password for `xavier `(unless you do the same as step 1 in reverse)

	
  7. Done

Wasn't that easy?

\*Nearly because not all \*nix's have` ssh-copy-id`. See this great [post ](http://blogs.translucentcode.org/mick/archives/000230.html)for a work around.
