---
aliases:
- /2010/03/any-port-in-a-storm.html
categories:
- Instructional
comments: true
date: 2010-03-06 12:19:10+00:00
slug: any-port-in-a-storm
tags:
- Cybersecurity
- Linux
- Network Security
- Networking
- port forwarding
title: Any Port in a Storm
---
While working on an IDS Solution for a client, I came across [Untangle](http://www.untangle.com), and I loved it so much that I pulled out an old box and loaded it up as my office firewall.

One thing that is lacking, from my perspective (at least in the 'free' edition) is the firewall interface; Untangle uses an IpTables based firewall, but doesn't replicate the usual INPUT FOWARD OUTPUT rulebase. I think that in 90% of usecases for Untangle, this isnt a problem, but I found it a little bit alien to have portfowarding hidden in the Networking config pane, and firewall separatly.

Anyway, It's been a few years since I cared that much about firewalls, and came up against a few issues of simply not remembering what ports to open up in which direction; Untangle's firewall ships with a default-pass configuration, which is fairly pointless from a security stance.

To make matters more confusing, I set up Untangle in a transparent configuration so that I wouldnt have to reconfigure my office IP addresses to a new subnet, and so avoid dealing with the portforwarding twice (external router, and internal firewall).

So, with that in mind, I set up the following rule.

Allow any > any from 192.168.1.1/24 to 192.168.1.1/24

And that dealt with any internal traffic, but still logged the traffic in the unlikely event anything local is compromised.

Anyway, biggest issue I came across was what traffic to allow out from the Internal network, So I'm leaving myself a list for next time... (Lots of mail ones because I use thunderbird)

DNS - port 53

SSH - port 22

FTP - port 21

HTTP - port 80, 8080

HTTPS  - port 443

POP3 - port 110

IMAP - port 143

SMTP - port 25

Secure SMTP (SSMTP) - port 465

Secure IMAP (IMAP4-SSL) - port 585

IMAP4 over SSL (IMAPS) - port 993

Secure POP3 (SSL-POP) - port 995

So each of those rules are, "Allow Internal > External:$ports", going the other way is a bad idea!!!
