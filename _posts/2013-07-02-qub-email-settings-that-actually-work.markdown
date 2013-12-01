---
author: admin
comments: true
date: 2013-07-02 11:17:16+00:00
layout: post
slug: qub-email-settings-that-actually-work
title: QUB Email Settings that Actually Work
categories:
- Instructional
tags:
- Email
- mail
- networking
- qub
- server
- settings
---

QUB Information Services can be a bit of a [mess](http://blogs.qub.ac.uk/cmc/2009/09/10/iphone-imap-settings-for-students/), so in the interest of saving time, here is what works for me.

In the below, the asterisks\* mean that the value may be called something different depending on your mail client.

Let me know in the comments if you find anything different and I'll try and keep this reasonably up to date.

# Incoming Mail (IMAP)

	
  * **Server**: imap.qub.ac.uk

	
  * **Port**:143

	
  * **Username**: `<Student Number>`

	
  * **Security**: TTLS / StartTTLS\*

	
  * **Authentication**: Normal\*

# Outgoing Mail (SMTP)

	
  * **Server**: smtp.qub.ac.uk

	
  * **Port**: 587

	
  * **Username**: `<Student Number>`

	
  * **Security**: TTLS/StartTTLS\*

	
  * **Authentication**: Normal\*

# Bi-Directional (Exchange Services for Mobile / Outlook)

	
  * **Server**: qmail.qub.ac.uk

	
  * **Port**:443

	
  * **Username**: ads/`<Student Number>`

	
  * **Security**: SSL

