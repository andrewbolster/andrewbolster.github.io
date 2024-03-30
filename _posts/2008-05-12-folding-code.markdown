---
author: admin
comments: false
date: 2008-05-12 19:51:00+00:00
layout: post
slug: folding-code
tags:
- Ubuntu
- folding
- linux
- bash
- scripting
- command-line
- text-to-speech
- C
- programming
title: Folding Code
---


I've been folding for a while now, and I'd previously written a really very cobbled together way of parsing my unitinfo.txt files, but, searching for something to do other than revise, I've written a similarly cobbled together but much shorter way of parsing my folding progress and telling me (as in speech) how far its going.  
  
Required: Espeak, basic bash knowledge to adjust.  
  
note: the espeak adjustments are just personal preference, so change them at will.  
  
Its kinda a cheat cus it calls itself but isnt recursive. I'm just lazy  
  
{% highlight bash %}
  #!/usr/bin/env bash  
  case "$1" in  
  "-v")  
   points | espeak --stdin -s200 -v en+f4  
   exit  
   ;;  
  "-w")  
   points | espeak --stdin -s200 -v en+f4 -w $2  
   exit  
   ;;  
  *)   
   echo "Folding Stats at "&& date +%H:%M  
   echo "CPU1:" && cat /var/folding/foldingathome/CPU1/unitinfo.txt | grep Progress | cut -d'[' -f1 | cut -d' ' -f2  
   echo "CPU2:" && cat /var/folding/foldingathome/CPU2/unitinfo.txt | grep Progress | cut -d'[' -f1 | cut -d' ' -f2  
   exit  
   ;;  
  esac  
{%endhighlight%}

it doesnt look very pretty on the console but i think it sounds alright.  
  
Better get some calculus done  
  
_Edited for new version of code with wavfile output_
