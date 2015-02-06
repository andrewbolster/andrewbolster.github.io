---
layout: post
title: "Unattended Updates in Linux Mint"
description: ""
category: ""
tags: []
---
{% include JB/setup %}

There's several very valid tutorials and guides around about getting [Ubuntu](https://help.ubuntu.com/community/AutomaticSecurityUpdates), [Debian](https://wiki.debian.org/UnattendedUpgrades) and [Mint](http://community.linuxmint.com/tutorial/view/1217) to automatically update and upgrade, but they don't do much explaining/checking. 

This is a short post filling in the gaps I observed. 


## Get the package

`sudo apt-get install unattended-upgrades -y`

## *Enable* the package scheduler

*File Being Messed With*: 

`/etc/apt/apt.conf.d/20auto-upgrades`

*Log File Being Watched*: 

`/var/log/unattended-upgrades/unattended-upgrades.log` 

I've got no idea why this isn't automatic; possibly that in other environments, you *only* want security level upgrades to core system components rather than updating all regular applications. (Not doing this left me scratching my head for a while wondering why the logs kept saying `No packages found that can be upgraded unattended` when `apt` was telling me something completely different. Anyway, put the following into a new file named above. 

    APT::Periodic::Update-Package-Lists "1";
    APT::Periodic::Unattended-Upgrade "1";
    APT::Periodic::AutocleanInterval "21";

## Configure the Upgrade

*File Being Bessed With*: 

`/etc/apt/apt.conf.d/50unattended-upgrades`

*Log File Being Watched*: 

`/var/log/unattended-upgrades/unattended-upgrades.log` 

Not there yet, and this is where the weird changes come in (YMMV). Now that we've configured the scheduler to update, upgrade and autoclean, it needs to be told what packages it can mess with. Unfortunately this is where Mint starts to be a minor annoyance (or just my bad respository handling, either way). Most guides say to edit the above named file to uncomment the following lines in the `Unattended-Upgrade::Allowed-Origins` section.

    "${distro_id} stable";
    "${distro_id}:${distro_codename}-security";
    "${distro_id}:${distro_codename}-updates";

This isn't enough for me, and I'd still get packages stuck in `apt` limbo due having non-standard repos, eg using Ubuntu repos on Mint. So I also added:

    "Ubuntu stable";
    "Ubuntu trusty-security";
    "Ubuntu trusty-updates";

This also wasn't perfect, with packages like `google-chrome`, `python3.3`, and `ros-*` not being caught. So it looks like some of the 'third party' repositories are being missed. Easy fix; query the apt-list for what sources *should* be in there.

*Disclaimer* Do not under any circumstances do the below on a production or publically accessible system that you actually care about. No matter how awesome the OSS community is, things still break, and blindly trusting third party updates isn't safe.

Moving on; funnily enough, `unattended-upgrades` knows exactly what packages it doesn't look at; the operation is that for each entry in the `Allowed-Origins` section, each entry in the package cache is searched against that `origin:suite` pair. (i.e Ubuntu is the Origin and stable/trusty-whatever are the suites).

Using the following command, you can get a *rough* list of what's missing. 

    sudo unattended-upgrade --dry-run --debug | awk -F "\'" '/Origin component/{print $11,$9}' | sort | uniq 

For instance, I got a few really long lines that are useless, followed by this list;

    Canonical trusty
    Google, Inc. stable
    Heroku, Inc. stable
    isTrusted:True>])  site:
    linuxmint qiana
    LP-PPA-fkrull-deadsnakes trusty
    LP-PPA-stebbins-handbrake-snapshots trusty
    LP-PPA-webupd8team-java trusty
    now
    ROS trusty

We can realistically discard the "isTrusted" and "now" lines, but the rest look relatively accurate. 

With a little bit of escaping to deal with spaces and special characters in names (looking at you Google and Heroku...), the relevant `Allowed Origins` entries looks like this:


    "linuxmint qiana";
    "Canonical trusty";
    "jenkins-ci.org binary";
    "Google\, Inc.:stable";
    "Heroku\, Inc.:stable";
    "ROS trusty";
    "LP-PPA-fkrull-deadsnakes trusty";
    "LP-PPA-stebbins-handbrake-snapshots trusty";
    "LP-PPA-webupd8team-java trusty";

Annoyingly enough, the [Mendeley](http://www.mendeley.com) reference management software I use, doesn't declare an origin or suite field, leaving both blank. This is sure to be a massive security issue some time, but I manually added one more entry; `":";`

## The complete list
    "${distro_id} stable";
    "${distro_id}:${distro_codename}-security";
    "${distro_id}:${distro_codename}-updates";
    "Ubuntu stable";
    "Ubuntu trusty-security";
    "Ubuntu trusty-updates";
    "linuxmint qiana";
    "Canonical trusty";
    "jenkins-ci.org binary";
    "Google\, Inc.:stable";
    "Heroku\, Inc.:stable";
    "ROS trusty";
    "LP-PPA-fkrull-deadsnakes trusty";
    "LP-PPA-stebbins-handbrake-snapshots trusty";
    "LP-PPA-webupd8team-java trusty";
    ":"; //Mendeley

## Finally
Note: I *don't* want my machine to reboot 'if necessary' as I regularly run simulations over night and that would make me not a happy bunny. If you're in a different situation where that'd be useful; add the following line to the file

`Unattended-Upgrade::Automatic-Reboot "true";`

As always, if I've missed something, lemme know in the comments and I'll update.

