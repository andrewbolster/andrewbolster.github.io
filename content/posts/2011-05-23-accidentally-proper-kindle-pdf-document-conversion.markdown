---
categories:
- Instructional
comments: true
date: 2011-05-23 13:25:13+00:00
slug: accidentally-proper-kindle-pdf-document-conversion
tags:
- Books
- Shell
- Tutorial
title: Accidentally Proper Kindle PDF Document Conversion
---


![Example of standard PDF 'conversion'](/uploads/2011/05/IMG_20110523_140017-225x300.jpg)

I've discovered a strange undocumented\* 'feature' of the Amazon Kindle document Delivery system. As it stands, if you send a document to username@free.kindle.com or @kindle.com, the document is sent onto your device at its convenience. Generally this is fine, but for most documents that people actually use (PDFs) this can be a pain as the service says it does not support PDF reflow, and on a smaller than A4/Letter screen, lovely documents end up looking like this...

That, well, sucks. The only useful way to use it without serious eyestrain (seriously? thats why I bought the damned thing) is to zoom into the top half of the page and work in landscape. Not useful.

\***UPDATE: As Tanya points out below, this _is_ documented, and the only thing that needs done to perform this style of conversion is the 'Convert' subject line, but I quite like the command line style... :P**

This has carried on for months now and as I find myself sitting on the command line more and more often I was getting irked by always having to pop over to chrome and drag some files to send myself a document, so I did what any geek would do; replace it with a small shell script. There are lots of tutorials out there for how to do this so I'm gonna try not to repeat them too much.

`sudo apt-get install sendemail`

`sudo vim /usr/bin/sendkindle`

```bash
#!/bin/bash
# Depends on package sendemail
$FROMEMAIL=#An email address connected to your kindle account
$USERNAME=#Your kindle username
$USER=#Gmail username in this case, but if you are an apps user, remember to include the full email address, or just $FROMEMAIL
$PASSWORD=#I dont think I have to explain this`

sendemail -f $FROMEMAIL -t $USERNAME@free.kindle.com -u "Convert" -m "Sent automatically by sendemail." -s smtp.gmail.com:587 -xu $USER -xp $PASSWORD -a "$1" -o tls=yes
```

The `-otls=yes` is important as most tutorials that talk about using Gmail either neglect to mention it or deal with much more advanced configurations than this.

Anyway, back to the matter at hand; you want to send a pdf.

`sendkindle myawesomedocument.pdf`

Give it a bit to upload the file, then check your kindle.

Note: This is the same document as was shown before, the formatting is not perfect but is a hell of a lot easier on the eyes, AND supports the full range of kindle text features (fonts, text to speech, etc).

[![](/uploads/2011/05/IMG_20110523_142231-225x300.jpg)](/uploads/2011/05/IMG_20110523_142231.jpg)

I've tested this with a few PDF's aswell as a few power point files (absolutly garbled layout but the text is still picked up), and I suspect this is all due to the much simpler way that sendemail deals with MIME-types. But I don't want to question the magic too much...
