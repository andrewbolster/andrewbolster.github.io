---
date: 2020-06-23T14:32:00+01:00
tags:
- Bash
- Git
- 'version-control'
title: Merging Git Repos for Archival Purposes
---


# TL;DR

I had reason to want to combine git repos into one big repo consisting of repos in their own folders, while ideally maintaining the histories of all those repos for archaeological purposes.

There are many reasons why someone would *want* to do this, and my specific use case isn't relevant. Good luck.

<script src="https://gist.github.com/andrewbolster/2ed60be3592c41c9123b5c0b764dea4c.js"></script>



## Why so complicated?

* 'Hidden' files (dotfiles) suck
* Shell Wildcards suck
* Wildcards with selective exclusions (i.e. `.git`) suck
* File names with spaces suck
* Trailing Slashes suck
* Rewriting History sucks

### Raw version because I don't trust GIST and embeds and such....

```bash
#!/bin/bash

usage() {
	cat << EOF
This script imports a git repo (accessible from https://\$origin/\$user/\$repo) and all its history as subdirectory of a destination (available locally at \$dest)
It is designed for non-production, archival processes and may destroy everything you've ever loved because you looked at it funny. You have been warned.
The structure of the destination will end up something like this:
~/src
- \$dest
  - origins
    - \$origin
      - \$user
        - \$repo
Required Arguments:
	-u|--user: The user that owns the repo to be imported
	-r|--repo: The name of the repository to be imported
	-d|--dest: The local name of the destination repository (assumed to be under ~/src)
	-o|--origin: The git server that is the origin of the repo to be imported
EOF
}
if [  $# -le 6 ]; then
    usage
    exit 1
fi

while [[ "$#" -gt 0 ]]; do
    case $1 in
        -u|--user) user="$2"; shift ;;
        -r|--repo) repo="$2"; shift ;;
    	-d|--dest) dest="$2"; shift ;;
	    -o|--origin) origin="$2"; shift ;;
    	*) echo "Unknown parameter passed: $1"; usage; exit 1 ;;
    esac
    shift
done

tmp="/tmp/_${dest}_tmp"

echo "Importing $origin/$user/$repo into $dest"

rm -rf ~/src/$repo
cd ~/src
git clone https://$origin/$user/$repo
cd $repo
git filter-branch \
	--tree-filter "mkdir -p $tmp/origin; git ls-files | cpio -pdumB $tmp/origin; git ls-files | xargs  -d '\n' rm -r; find . -type d -empty -delete; mkdir -p origins/$origin/$user; mv $tmp/origin origins/$origin/$user/$repo/"\
	--tag-name-filter cat --prune-empty -- --all
if [ $? -eq 0 ]; then
	## WAIT PATIENTLY
	cd ../$dest
	git remote add $repo ../$repo
	git fetch $repo --tags
	git merge --allow-unrelated-histories $repo/master #Youre on your own if you want a different / multiple branch(es)...
	git remote remove $repo
else
	echo failed for $user/$repo
fi
```
