---
categories:
- Instructional
comments: true
cover:
  image: uploads/2010/07/CRlogo.jpg
date: 2010-07-24 16:55:38+00:00
slug: citrix-web-client-with-ubuntu
tags:
- Cybersecurity
- Firefox
- Google Chrome
- Linux
- Networking
- Remote Access
- Ubuntu
title: Citrix Web Client with Ubuntu
---

[![Citrix Reciever Logo](/uploads/2010/07/CRlogo.jpg)](/uploads/2010/07/CRlogo.jpg)Ubuntu is one of those polarising technologies; Its really easy to use on a recreational basis, or as part of a institution/business wide rollout, but heartbreakingly awkward to use 'alone' within an entrenched business setting.

One such setting is that of Queen's University; the only form of secure remote access that is made (quietly) availiable is through a [Citrix XenApp gateway](https://offcampus.qub.ac.uk/). Great in theory; everyone can take a slice of a virtualized desktop, do whatever they need to do, and that processing power and memory can be easially reappropriated when they're done. Unfortunately, in an effort to be 'secure', you HAVE to use Windows, and you HAVE to have Internet Explorer installed, and you HAVE to install the propitiatory XenApp client.

Since I don't have my completly legal [MSDNAA](http://msdn62.e-academy.com/elms/Storefront/Home.aspx?campus=quob_compsci)-provided Windows 7 ISO handy, I couldn't fire up a virtual machine to handle it, so I'm left with jerry rigging a solution using Citrix's crippled linux client.

It all appears to be simple enough, even simpler than [UbuntuGuide](http://ubuntuguide.org/wiki/Ubuntu:Feisty/CommercialApplications#How_to_Install_Citrix_ICAClient_10); [download](https://www.citrix.com/English/ss/downloads/index.asp) and extract the client called Citrix Reciever (and the additional USB support package, ctxusb), download and install the '.deb' for ubuntu, or .rpm for RH/Fedora, or alternatively .tar.gz (YMMV), in which case you'll need to run the installer.

`sudo ./setupwfc`

NOTE: only 32 bit clients are released, and in the case of Debian/RH based systems, you can force package installation to accept a 32 bit client on a 64 bit system. See [Here](//2011/09/force-32-bit-installs-on-64-bit-systems-debrpm/) for details.

Now, in an ideal world, that SHOULD be it, but Queen's uses a CA (Certificate Authority) SSL Cert that isn't shipped by default with Ubuntu (Specifically [DigiCert High Assurance EV Root CA](https://www.digicert.com/digicert-root-certificates.htm)), so if you try and open up the Student Desktop link (that actually generates a launch.ica file) will crap out with "You have not chosen to trust the issuer of the server's security certificate."

Easy if obscure fix; grab the certificate ([DigiCert](https://www.digicert.com/digicert-root-certificates.htm) or otherwise) and copy it to your keystore.

`sudo cp ~/Downloads/*.crt /usr/lib/ICAClient/keystore/cacerts/`

For newer versions of the client, this path has moved to...

` /usr/lib/ICAClient/linuxx86/keystore/cacerts/`

Thanks to Rudolf for pointing that out to me!

And again, newer (12.1) appears in

`/opt/Citrix/ICAClient/keystore/cacerts/`

Now, even with all this setup, [Google Chrome](http://www.google.com/chrome) doesn't like the arrangement, but Firefox copes handily.

**UPDATE 2011/11/09 **QUB appear to have changed their certificate authority (probably don't want to pay for it...) So [here](https://www.instantssl.com/ssl-certificate-support/cert_installation/UTN-USERFirst-Hardware.crt) is the new certificate to use (UTN-USERFirst-Hardware)

**UPDATE 2012/05/08 **Citrix keep moving the goalposts in terms of download locations... Update link to go to downloads listing. Find it yourself. Added info about USB support package. The Cert file disappeared again. [Try this.](http://bit.ly/IAcS63)

UPDATE: 2012/07/17 If you get an install error on the 64 bit version of the latest debs, check out this forum [post](http://forums.citrix.com/thread.jspa?threadID=306353&tstart=0)
