---
aliases:
- /2014/07/ipython-websocket-failure-on-chrome.html
cover:
  image: img/ipython-websocket-failure-on-chrome.generated.png
date: 2014-07-25 00:00:00+00:00
tags:
- Chrome
- Jupyter
- Linux Mint
title: IPython Websocket Failure on Chrome
---
[IPython](http://ipython.org/) is an amazing tool, and in particular [IPython Notebook](http://nbviewer.ipython.org/github/ipython/ipython/blob/master/examples/Notebook/Index.ipynb), which is easily the best 'python scratch-pad' I've ever used.

However, a while ago something strange happened to my set up and I'm not entirely sure when or how but either way, here's how I 'fixed' it.

# The Problem

TL;DR Can't execute anything at all using Chrome, works fine in other browsers.

![WebSocket Fail]({{site.url}}/uploads/2014/websocketfail.png)

> WebSocket connection failed

> A WebSocket connection could not be established. You will NOT be able to run code. Check your network connection or notebook server configuration

This was accompanied by a JS console error (rightclick anywhere in Chrome and 'Inspect Element' will open up the dev tools)

> WebSocket connection to 'wss://localhost:8888/api/kernels/a893ce6e-3a3d-4a99-afc0-b02368245d32/stdin' failed: WebSocket is closed before the connection is established.

No unexpected error messages show up in the `ipython notebook --debug` log.

# The Setup

* Fully `pip` updated `ipython` (2.1.0) and `Tornado` (4.0)
* Latest [Chrome](https://www.google.com/intl/en_uk/chrome/browser/) (36.0)
* Fully updated [Linux Mint](http://www.linuxmint.com/) 17 Qiana
* Password protected notebooks configured. No change to configuration files since before 'issue'

# The Attempts

This is a surprisingly difficult thing to [Google](https://www.google.co.uk/search?q=chrome+WebSocket+connection+failed+websocket+is+closed+ipython&oq=chrom&aqs=chrome.1.69i59l3j69i57j69i60l2.1847j0j4&sourceid=chrome&es_sm=93&ie=UTF-8) and I got many 'that kinda looks like my problem but not quite', so here's a quick off the top of my head list of the things I tried.

* [Chromes proxy is screwed](http://stackoverflow.com/questions/19245200/ipython-notebook-websocket-connection-failed), use ip address instead of 'localhost' (also tried FQDN and a few other things), as well as clearing cache, etc  Interestingly, Chromes Proxy configuration defaults to the system setting which was all disabled anyway so this was a long shot.

* Maybe Chromes Websocket implementation is stuffed, or I'd played with a '[flag](chrome://flags)', so reset all to defaults. Nope.

* IPython install broken somehow? As per the [instructions](http://ipython.org/ipython-doc/dev/install/install.html) I'd launched a `iptest` and all came back within bounds (however, the `js/notebook` tests were disabled and I can't find any instruction anywhere as to enabling them, lemme know in the comments.

* Tornado conflict? Every so often Tornado does a 'breaking update' so maybe there's some update-race-condition. Also the [Quickstart](http://ipython.org/ipython-doc/dev/install/install.html#tornado) implies that Tornado 2.1 is the required version, so I tried it out, no joy.

* Another process occupying the same port? This was reported as a potential problem on some Mac machines but at this point I was getting desparate. Quick `lsof` stuffed that idea.

# The "Fix"

I'll be the first to admit, this 'fix' doesn't actually fix is so much as side-steps the breaking condition by wrapping the whole conversation into an SSL tunnel.

Long story short, **enable HTTPS and generate a self-signed cert**

`openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem`

And in either your customised profile or in the `ipython_notebook_config.py` file in `~/ipython/profile_nbdefault/`

```python
# The full path to an SSL/TLS certificate file.
c.NotebookApp.certfile = u'$WHEREVER_YOU_PUT/mycert.pem'
```
