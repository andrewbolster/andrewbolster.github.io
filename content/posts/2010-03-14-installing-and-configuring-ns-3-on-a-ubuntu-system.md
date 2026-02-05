---
aliases:
- /2010/03/installing-and-configuring-ns-3-on-a-ubuntu-system/
- /2010/03/installing-and-configuring-ns-3-on-a-ubuntu-system.html
categories:
- Instructional
comments: true
date: 2010-03-14 23:39:09+00:00
slug: installing-and-configuring-ns-3-on-a-ubuntu-system
tags:
- Linux
- Networking
- Programming
- Python
- Simulation
- Ubuntu
- Version Control
title: Installing and Configuring NS-3 on a Ubuntu System
---
[![](http://www.michele-mastrogiovanni.net/utilities/imgs/GraphViewer.jpg)](http://www.michele-mastrogiovanni.net/utilities/imgs/GraphViewer.jpg)
**

[NS-3](http://www.nsnam.org/) Appears to have a staggeringly steep learning curve so I hope these posts help out someone else (or me, when i forget all this in a month).

Running off a virtualised Ubuntu 9.10 system, the prerequisites I installed were all the ones [listed here](http://www.nsnam.org/wiki/index.php/Installation#Ubuntu.2FDebian). (And i removed some out of date packages)

> `sudo apt-get install bison bzr dia doxygen flex g++ gcc  gdb graphviz imagemagick libgoocanvas-dev libgtk2.0-0 libgtk2.0-dev libsqlite3-dev libxml2 libxml2-dev mercurial python python-dev python-kiwi python-pygoocanvas python-pygraphviz sqlite sqlite3 tcpdump texi2html texinfo texlive texlive-extra-utils valgrind`

That will take a while to install so go get coffee.

Once thats all finished, grab the source using [Mercurial](http://mercurial.selenic.com/) (it was installed in the command above). For tidyness, I do all of this under ~/src (If this was a multi-user system I would suggest working under /usr/src and performing the relevant steps as root or under [sudo](http://xkcd.com/149/))

If you havent used Mercurial before, [check my post on the subject](//2010/03/ercurial-quick-start-cheatsheet/).

>

>
>     $ hg clone <a href="http://code.nsnam.org/ns-3-allinone">http://code.nsnam.org/ns-3-allinone </a>
>
>

>
>     destination directory: ns-3-allinone
>     requesting all changes
>     adding changesets
>     adding manifests
>     adding file changes
>     added 31 changesets with 45 changes to 7 files
>     updating working directory
>     7 files updated, 0 files merged, 0 files removed, 0 files unresolved
>
>

Thats the easy bit done,  what you've downloaded is basically the instructions for downloading everything else about NS-3, all in python scripts.

For safety I am not using the dev branch; Check the latest version [here](http://code.nsnam.org/)

>

>
>     $ ./download.py -n ns-3.10
>
>

And that will output a whole pile of stuff that isnt too salient. Unless you're really bored...

After which there is a python script that looks after the actual build process, so fire it off with a simple;

>

>
>     $ ./build.py --enable-examples --enable-tests
>
>

And, again, lots of waiting (seriously, get coffee, on my VM it took just under 15 minutes) and lots of output.

It is not made clear on the project wiki but this script also fires off the python [WAF ](http://code.google.com/p/waf/) script so its a complete end to end builder. What isn't included in the build script is the (very tidy) automated regression test suite, so just for completeness...

>

>
>     $ cd ns-3.7
>     $./test.py
>     [...]
>     104 of 104 tests passed (104 passed, 0 skipped, 0 failed, 0 crashed, 0 valgrind errors)
>
>

UPDATE : This final stage is no longer needed as the tests were rolled into the ./build.py script after version 3.9

(please, if something goes wrong using these instructions at this stage, please comment or report it directly to [NSNAM.org's bugtracker](http://www.nsnam.org/bugzilla/))

Installer is all done and ns-3.7 is ready to rock an roll! Tutorials coming as soon as I work it out myself!
