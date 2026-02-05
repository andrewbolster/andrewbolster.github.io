---
cover:
  image: img/installing-ubuntu-touch-on-the-nexus-7.generated.png
date: 2013-12-20 00:00:00+00:00
tags:
- Android
- Ubuntu
- mobile
title: Installing Ubuntu Touch on the Nexus 7
---

I'm always amazed by Canonical. Particularly their documentation.

[Ubuntu Touch](https://wiki.ubuntu.com/Touch/) is the grand movement to bring Ubuntu into the mobile domain, and it's developing fast.

Can't say the same about the [documentation](https://wiki.ubuntu.com/Touch/Install); too long and doesn't really make sense. And for what is actually a fantastically simple process, it deserves better. The `phablet-flash` folks have done an amazing job.

So without further ado, the assumption: If you're thinking of putting Ubuntu on your device, I'd say it's reasonable to assume that:

1. You've already [rooted](http://www.androidcentral.com/root) your device to put something different on it
2. You've already enabled [USB debugging](http://www.makeuseof.com/tag/what-is-usb-debugging-mode-on-android-makeuseof-explains/)
3. You already know how to / if you care to [backup](http://www.pcmag.com/article2/0,2817,2423270,00.asp) the device.

Once that's all wrapped up, onto the meat.

```bash
sudo add-apt-repository ppa:phablet-team/tools
sudo apt-get update
sudo aptitude -y install phablet-tools android-tools-adb android-tools-fastboot
phablet-flash ubuntu-system --channel devel --bootstrap
```

Job done! Hopefully Cyanogenmod can take some inspiration for this.
