---
aliases:
- /2014/01/unicode-madness-in-jekyll.html
cover:
  image: img/unicode-madness-in-jekyll.generated.png
date: 2014-01-20 00:00:00+00:00
tags:
- Jekyll
- blogging
- irc
title: Unicode Madness in Jekyll
---
Ok so this was a weird one.

I've been lurking on [#jekyll](irc://freenote.net/#jekyll) for a while, trying to 'give back' with slightly-more-than-noob-knowledge. Mostly it's simple mistakes or misunderstandings that I went through myself, so easy enough.

Then there was [kaffeebohne](http://blog.koffeingeladen.de/) and the infernal BOM.

To make a long story short (And to index the Googles), the symptoms were that [this source file](https://paste.xinu.at/JEZpi/) in German (i.e. lots of tasty unicode ü's etc) was garbling the unicode, not activating the template layouts, and basically not doing anything, while Jekyll was perfectly happy with no errors what so ever.

First port of call was fiddling with the file itself. Long story short, even with NOTHING in the file, it still wasn't rendering correctly. Wether I had it in their source file or my own, whatever the title.

So a file with no contents and a completly different title was still screwing things up? WTF?

So what's the difference between it and any other file?

```bash
➜  _posts git:(master) ✗ file 2014-01-20-schreibdochmal_19_01_14.md
2014-01-20-schreibdochmal_19_01_14.md: exported SGML document, UTF-8 Unicode (with BOM) text, with very long lines
➜  _posts git:(master) ✗ file 2014-01-11-the-making-of-a-timelapse.md
2014-01-11-the-making-of-a-timelapse.md: ASCII text, with very long lines
```

Wut?...

Funnily enough this is hinted as a problem in [this stack overflow post](http://stackoverflow.com/questions/12467632/jekyll-regeneration-failed-with-unicode-posts) but doesn't propose a solution. (Although `chcp 650001` didn't work for me), but it mentioned the [BOM](http://en.wikipedia.org/wiki/Byte_order_mark), or Byte Order Mark, an invisible endiness indicator that sits at the front of a text stream waiting to spoil your day.

Long story short, can be fixed by [this answer](http://stackoverflow.com/questions/1068650/using-awk-to-remove-the-byte-order-mark)

```bash
awk '{if(NR==1)sub(/^\xef\xbb\xbf/,"");print}' INFILE > OUTFILE
```

Hopefully this helps someone along later on.
