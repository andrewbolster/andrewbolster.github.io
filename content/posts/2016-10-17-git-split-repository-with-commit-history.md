---
aliases:
- /2016/10/git-split-repository-with-commit-history/
- /2016/10/git-split-repository-with-commit-history.html
cover:
  image: img/git-split-repository-with-commit-history.generated.png
date: 2016-10-17 00:00:00+00:00
tags:
- Coding
- Development
- Git
- PhD
- Programming
- Version Control
title: Git Split Repository With Commit History
---
Thesis submitted, Viva cleared (with minor corrections) but this post isn't about all that...

Simple one; how do you go from one monolithic project repository to multiple respositories without losing all that tasty tasty commit history?

```shell
#! /bin/zsh
#
# git_split.sh Current_Repo username new_repo {list of files/folders you want to keep}
# Copyright (C) 2016 bolster <bolster@bolster.online>
#
# Distributed under terms of the MIT license.
#



BASEDIR=$1
INITDIR=`pwd`
NEWREPO="git@github.com:$2/$3.git"
shift 3
FILTER_ARGS=$@
TMPDIR=`mktemp -d -t ${BASEDIR}_XXXXXXXXX`
echo $BASEDIR $TMPDIR $FILTER_ARGS

cp -ra $BASEDIR/. $TMPDIR
cd $TMPDIR
git filter-branch --index-filter "git rm --cached -qr --ignore-unmatch -- . && git reset -q \$GIT_COMMIT -- $FILTER_ARGS" --prune-empty -- --all && git repack -a -d -f --depth=250 --window=250 && git remote set-url origin $NEWREPO && git gc && git push -u origin master
ls -latrh
cd $INITDIR
rm -rf $TMPDIR
```

YMMV, IANAGG, No refunds, Safety not guaranteed

(And I'd still like a better way of cleaning up the object history of the new repos... leave a comment if you've got a better idea!)
