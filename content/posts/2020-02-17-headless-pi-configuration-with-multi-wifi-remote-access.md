---
aliases:
- /2020/02/headless-pi-configuration-with-multi-wifi-remote-access/
- /2020/02/headless-pi-configuration-with-multi-wifi-remote-access.html
cover:
  image: img/headless-pi-configuration-with-multi-wifi-remote-access.generated.png
date: 2020-02-17 15:28:00+00:00
tags:
- Microcontrollers
- Raspberry Pi
title: Headless Pi Configuration with Multi-Wifi Remote Access
---
Raspberry Pi's are great, but often have a lot of baggage associated with them, and I keep forgetting all the clever things you can do to get them up and running without having a sea of cables attached...

# Results

Raspberry Pi that can be `ssh`d into from anywhere in the world* without poking any firewall rules or anything other than power connected to it, that works in a range of WiFi access points.

*(Requires access to an external domain or static IP server)

# Requirements

* Raspberry Pi with Wifi (Either onboard or dongle)
* Externally accessible `ssh`able server
* (Micro) SD Card reader and SD Card (>=8GB)
* Another machine to do all the magic with
* You to be sitting in a WiFi area that you know the key for...

# Setup

## OS Image

1. Install [Etcher](https://www.balena.io/etcher/) (Or similar, see [here](https://www.raspberrypi.org/documentation/installation/installing-images/) for other options)
2. Download Rasbian Lite from [here](https://www.raspberrypi.org/downloads/raspbian/)
3. Use Etcher (or whatever) to burn the downloaded image to the SD card
4. Once verified, eject, unplug, and replug the SD card into the machine.

## `Boot` Fiddling

### Enable SSH

When you plug the card back in, you should see a `boot` volume appear in your Finder/Explorer/File Manager, in it, create an empty file called `ssh`. e.g.

```bash
touch /Volumes/boot/ssh
```

## Pre-Configure Wifi

Then in your favourite text editor, create another file in the same directory called `wpa_supplicant.conf` that looks something like this, populated with the `ssid` and `psk` keys for your relevant networks.

```

country=GB #Or your ISO 3166 country code  
# https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes

ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
        ssid="TotallyMyWorkSSID"
        psk="supersecretandtotallyaccurate"
}

network={
        ssid="MyHomeWifi"
        psk="homesweethome"
}

network={
        ssid="farset-members"
        psk="probablytheworstkeptsecretinbelfast"
}
```

> If you have a 'weird' password with quotes or unescaped symbols, you can use `wpa_passphrase MY_SSID` to generate the relevant pre-encrypted `psk`'s that are acceptable by `wpa_supplicant.conf`, and you should be able to run this either on the pi directly later, any other pi, or any other linux-based wifi enabled machine... You can probably to it in a VM too but I haven't tested that...
> [Source](https://www.raspberrypi.org/forums/viewtopic.php?p=1472865&sid=0e9fd7545d8ce3e46ffaa9f212649697#p1472865)


## Squeaky Bum Time

At this point, eject and unplug the SD card from the machine, and plug it into the (unpowered) Pi, and then the moment of truth; power it on...

> At this point I recommend waiting at least 5 minutes, get a coffee or a [ClubMate](https://www.farsetlabs.org.uk/about/club_mate.html)

> While you're waiting, take some time to review the [Power/Startup](https://elinux.org/R-Pi_Troubleshooting#Power_.2F_Start-up) section of the Pi Troubleshooting Guide, just in case...

## First Login

### Easy Mode; mDNS

If you're lucky and have a nice router on your wifi network, you *might* be able to log in to your device using the default password `raspberry` using the below

```
ssh pi@raspberrypi
```
or

```
ssh pi@raspberrypi.local
```

### Hard Mode; Port Scan

Using a network scanner like `nmap`, scan for IP's that have the SSH port (22) open, and try a few. YMMV.

On basic networks this should be as simple as:

```
sudo nmap -sS -p 22 192.168.0.0/24
```

But you may also want to check out the [Fing](https://www.fing.com/products/fing-app) android network scanner which is great at identifying Raspberry Pi's based on their [Vendor MAC Address](https://www.macvendorlookup.com/)

Once you've identified the IP address of the Pi, you can connect to it like:

```
ssh pi@<IP-ADDRESS>
```

## Good Housekeeping

Now that we're in, there are a few steps that we should do just for good housekeeping;

1. Update the Pi with `sudo apt-get update; sudo apt-get upgrade -y`
2. Using [`sudo raspi-config`](https://www.raspberrypi.org/documentation/configuration/raspi-config.md), perform the following actions
	1. Change the `pi` user password to something custom
	2. Network Options > Set the Hostname to something memorable (We'll be referring to this in future as PI_HOST)
	3. Advanced Options > Update
3. Reboot with `sudo reboot`
4. Log back in with either `ssh pi@PIHOST`, or your previously found IP address (or return to the "Port Scan" section if that doesn't work)
5. Run `ssh-keygen` (without specifying a passphrase)
6. Print out and note the contents of the public key generated using `cat ~/.ssh/id_rsa.pub`

## Prepping `autossh`

We'll be using the `autossh` program to, well, automate ssh. This will be able to provide us with a "Reverse SSH Tunnel" to get into the Pi via an internet-accessible server, that we'll be calling `JUMPBOX`

### `JUMPBOX` Prep

Log into the `JUMPBOX`, and create a new `nologin` user

> **All the commands in this section should be executed on `JUMPBOX` as the `root` user (or add appropriate `sudo`s)**

```
useradd -m -s /sbin/nologin --disabled-password autotunnel
su - autotunnel -s /bin/bash
ssh-keygen
```
You'll be asked for a `passphrase` here, don't enter one, as this ensures we'll be able to securely setup the tunnel without manually entering passwords

Then we'll construct an `authorized_keys` file (note the Americanisation!) in the `.ssh` directory so our pi will be able to log into this account automatically.

```
mkdir ~/.ssh
vim ~/.ssh/authorized_keys
```
In this file, add the contents of the `cat ~/.ssh/id_rsa.pub` call that we performed on the Pi, and save it (with `<ESC>:wq`, incase you forgot...)

We need to make sure these files have the correct permissions, so...

```
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

### `PI_HOST` Prep

Autossh isn't installed by default

`sudo apt-get install autossh -y`

Similar to the setup of the `autotunnel` user on the `JUMPBOX`, we do the same on the `PI_HOST`

```
sudo useradd -m -s /sbin/nologin --disabled-password autotunnel
sudo su - autotunnel -s /bin/bash
ssh-keygen
ssh-copy-id JUMPBOX
ssh JUMPBOX
```
At this point you'll be asked to confirm things like accepting the SSH key of the JUMPBOX server, but you won't actually get a login shell and will be kicked off; this is because we setup the `autotunnel@jumpbox` user with `/sbin/nologin`, so it's fine.

Now, using <kbd>CTL</kbd> + <kbd>D</kbd> to "escape" from the `autotunnel` user back to the `pi` user

Finally, `sudo -sh` into the root user and execute the following to create a auto-starting services file

```sh
cat > /etc/systemd/system/autossh-JUMPBOX.service << EOF

[Unit]
Description=Keep a tunnel to 'JUMPBOX' open
After=network-online.target


[Service]
Type=forking
User=autotunnel
ExecStart=/usr/bin/autossh -f -M 0 -N -i /home/autotunnel/.ssh/id_rsa -o ServerAliveInterval=30 -o ServerAliveCountMax=3 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=false autotunnel@JUMPBOX -R 2222:127.0.0.1:22
ExecStop=/usr/bin/pkill -9 -u autotunnel
Restart=always

[Install]
WantedBy=multi-user.target
EOF

systemctl enable autossh-JUMPBOX.service
systemctl daemon-reload
reboot
```

And then wait a while and hope for the best!


# Persistent Connections

All-in-one command to test your JUMPBOX/PI_HOST connection;

```
ssh -J user@JUMPBOX pi@localhost -p 2222
```

Once you're happy that this is fairly stable, you can set up a 'shortcut' to this host in your local `~/.ssh/config` file with something like this

```
Host PI_HOST
        HostName localhost
        Port 2222
        ProxyJump user@JUMPBOX
        User pi
```

Then you can excute the following to set up passwordless pasthrough connection

```
ssh-copy-id PI_HOST
ssh PI_HOST
```

# Sources

* [Headless Raspberry Pi 4 SSH WiFi Setup](https://desertbot.io/blog/headless-raspberry-pi-4-ssh-wifi-setup)
* [Creating a user without a password](https://unix.stackexchange.com/questions/56765/creating-a-user-without-a-password)
* [Fun and Profit with Reverse SSH Tunnels and AutoSSH](https://hobo.house/2016/06/20/fun-and-profit-with-reverse-ssh-tunnels-and-autossh/)
* [Autossh.service](https://gist.github.com/thomasfr/9707568)
