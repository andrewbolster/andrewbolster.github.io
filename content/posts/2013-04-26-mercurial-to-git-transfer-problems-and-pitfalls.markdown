---
categories:
- Instructional
comments: true
date: 2013-04-26 11:26:17+00:00
slug: mercurial-to-git-transfer-problems-and-pitfalls
tags:
- Bitbucket
- Git
- GitHub
- 'Version Control'
- 'version control'
title: Mercurial to Git transfer; problems, and pitfalls.
---


Finally decided to move my research work across to GitHub; seems the 'in' thing to do. Also I wanted to get more into the Git swing of things and using intermediary tools like hg-git seem a bit contrived for a 1 person project.

I've enjoyed using Bitbucket but it's just not quite as polished. That and GH has better integration to pretty much everything... Sorry.

Went through the process described [here](http://www.wordsinboxes.com/2012/02/migrating-repositories-from-bitbucket.html) but it's not really explained very well, so I'm adding my touch of idiot-proof magic.

Note: BB, Bitbucket, hg and mercurial are all talking about the same thing in different ways; hg is the command, mercurial is the protocol, Bitbucket is the hosting application, and BB is just my laziness. Likewise for GH, Github, git (and git, for completeness)

# 1. It's not cleaning, it's mapping

TL;DR usernames, emails, etc can be different between BB and GH, so we're going to make a file (`/dev/shm/users.txt`), based on the mercurial commit log, extracting the used usernames, and manually creating the mapping to the Github login.

First off, make sure that you have the following lines in your ~/.hgrc
`
[extensions]
hgext.convert=
`
Then, in your existing local mercurial repository (~/src/reponame), execute

`hg log | grep user: | sort | uniq | sed ’s/user: *//‘ > /dev/shm/users.txt`

This will generate the list of used credentials in the repo, so if your username was repoman, you'd have something like
`
repoman
repoman@localhost
Joe Bloggs <repoman@gmail.com>
`
Then pop into an existing GitHub repo of yours and find your credentials from the git log (In repoman's case it's "Joe Bloggs <repoman@gmail.com>")

Then in your editor of choice, change users.txt to:
`
repoman=Joe Bloggs <repoman@gmail.com>
repoman@localhost=Joe Bloggs <repoman@gmail.com>
Joe Bloggs <repoman@gmail.com>=Joe Bloggs <repoman@gmail.com>
`

The bottom line is fairly pointless but it's included for completeness.

Finally, you create a new empty (temporary) hg repo to copy the mapped repo to;
`
hg init /dev/shm/repo-hg-clean
hg convert --authors /dev/shm/users.txt ~/src/repo /dev/shm/repo-hg-clean
`
Boom, clean mercurial repo in /dev/shm/repo-hg-clean to migrate to git

# 2. Convert to Git

So we've made an intermediate mercurial repo, now to make an intermediate git repo, but FIRST; the tool.
`
cd /dev/shm/
git clone git://repo.or.cz/fast-export.git
git init repo-git
cd repo-git
fast-export/hg-fast-export.sh -r ../repo-hg-clean
git checkout HEAD
`

That was easy... hopefully...

If you come across this error (`Error: Branch [master] modified outside hg-fast-export:`) it means you didn't init into a clean repo. **The destination repo must be clean, we'll merge with any pre-existing repo next!**

# 3. "But I already made a repo using the web interface!"

I scratched my head at this one for a while (I'm still getting my head around git's version of informative error messages), but the method that works for me where I have an existing repo that is mergable with the contents of the previously mercurial repo.
`
cd /dev/shm/repo-git
git remote add origin <github URL from the repo page ending in .git!>
git push -u origin master
git pull origin master
git push
`
Then I move to my actual working directory (`~/src/`) and git clone the URL to see if it all works. If it works, I remove all the relevant temporary directories and relax!
