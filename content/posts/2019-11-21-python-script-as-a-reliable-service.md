---
date: 2019-11-21T14:09:00+00:00
tags:
- Microcontrollers
- Python
- 'Raspberry Pi'
title: Python Script as a Reliable Service
---


> I was asked to help out a friend who had an installation in an art gallery that stopped booting properly, and was reminded that I keep forgetting to actually write this post.

Running a python script as a reliable, retryable service on a Raspberry Pi that waits for an 'up' network connection, because I'm an idiot who keeps changing his mind how to do it.

# Fail gracefully and with informative error messages:

`try: ... except:...` is your friend

Use the `logging` library by default

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')
```

OR

```python
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')
```

# Just use Systemd, don't get religious


`$EDITOR /lib/systemd/system/awesome.service`

```shell
[Unit]
Description=My Awesome Service
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/bin/python /home/pi/my_awesome_service.py
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```

`sudo chmod 644 /lib/systemd/system/awesome.service`

`chmod +x /home/pi/my_awesome_service.py`

`sudo systemctl daemon-reload`

`sudo systemctl enable awesome.service`

`sudo systemctl start awesome.service`

`sudo systemctl status awesome.service -l`

Then test it by rebooting repeatedly until you develop any kind of confidence in yourself.

Note: The `Restart=on-failure` will not restart the service if it cleanly exits, like `sys.exit(0)`, and `RestartSec=10` will wait for 10 seconds before relaunching the service, which will prevent the service being permanently killed if by the interval handler.


# Sources:

* [RPi Forums](https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=197513&sid=24f2e72c0eadcfcc089491479cfb7d1a)
* [SystemD Docs](https://www.freedesktop.org/software/systemd/man/systemd.service.html#)
