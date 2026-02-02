---
category: ''
description: ''
tags:
- Linux
title: SNMP Monitoring and Configuration for Networks and Linux Host Monitoring
---


*TL:DR*: Setting up Observium to perform autodiscovery with dynamic DNS, and sample snmp configs to manage Linux servers

This week I've taken a 'break' from the academics since I nearly killed myself sorting out some research for [TrustCom](https://research.comnet.aalto.fi/Trustcom2015/) (Fingers crossed), and I've been engrossed in redoing the network here in our [University of Liverpool](http://liv.ac.uk) research lab.

Good network and system monitoring tools are hard to come by, especially for free and with decent OSS tendencies.

[Observium](http://www.observium.org/) definitly qualifies on both, with really clear [installation instructions](http://www.observium.org/wiki/Installation) that I won't even pretend to be able to extend.

One thing that is missing however is true auto-discovery of systems in networks; Observium has an extremely powerful SNMP service discovery and polling system that, again, I can't fault. Host discovery is another matter.

Earlier this week I did battle with Dynamic DNS updates (DHCP telling DNS who appeared so, myrandomhostname.domain.com actually resolves to that device if they're in the lab and doesn't if they're not. I'm not quite done licking my wounds from that particular battle so I'll maybe write that up some other time.

But, it means that we have and expect to have devices flowing in and out of the lab fairly regularly, and it'd be nice to keep track of things dynamically.

## End Goals

* Automated host discovery from nameserver
* Sensible SNMP configuration for linux hosts

(These solution files look like crap on smaller browsers, but they're cleanly copy/pastable)

## Solution 1:


### server:/etc/cron.d/observium_discoverer
```bash
13   *    * * *    root    host -t axfr anrg.liv.ac.uk  | awk '$4 ~ "^A$" {print $1}' > /dev/shm/devices 2> /dev/null; /opt/observium/add_device.php /dev/shm/devices >> /dev/null 2>&1
```

## Solution 2:
Required Packages:

```bash
sudo aptitude install snmpd lm-sensors snmp-mibs-downloader
```

### clients:/etc/default/snmpd
```bash
# This file controls the activity of snmpd and snmptrapd

# Don't load any MIBs by default.
# You might comment this lines once you have the MIBs downloaded.
export MIBS=/usr/share/snmp/mibs

# snmpd control (yes means start daemon).
SNMPDRUN=yes

# snmpd options (use syslog, close stdin/out/err).
SNMPDOPTS='-Lsd -Lf /dev/null -u snmp -g snmp -I -smux,mteTrigger,mteTriggerConf -p /var/run/snmpd.pid'
#SNMPDOPTS='-Lsd -Lf /dev/null -u snmp -I -smux -p /var/run/snmpd.pid -c /etc/snmp/snmpd.conf'

# snmptrapd control (yes means start daemon).  As of net-snmp version
# 5.0, master agentx support must be enabled in snmpd before snmptrapd
# can be run.  See snmpd.conf(5) for how to do this.
TRAPDRUN=yes

# snmptrapd options (use syslog).
TRAPDOPTS='-Lsd -p /var/run/snmptrapd.pid'
```

### clients:/etc/snmp/snmpd.conf
```bash
agentAddress  udp:161
view   systemonly  included   .1.3.6.1.2.1.1
view   systemonly  included   .1.3.6.1.2.1.25.1
rocommunity public  default
rouser   authOnlyUser

sysLocation    Back of the World
sysContact     bolster@liv.ac.uk
sysServices    72

trapsink     localhost public

iquerySecName   internalUser
rouser          internalUser

master          agentx
```

## Problems Experienced following other instructions (AKA Google Search Foo)

Lots of these while trying to get the SNMP client to respond sensibly

* `/etc/snmp/snmpd.conf: line XXX: Error: Unknown payload OID`
* `trigger OID: fileErrorFlag`
* `/etc/snmp/snmpd.conf: line 88: Error: Already have an entry for this process.`
* `duplicate table data attempted to be entered. row exists`
* `Error opening specified endpoint "udp:161"`
