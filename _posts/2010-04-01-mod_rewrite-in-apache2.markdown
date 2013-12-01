---
author: admin
comments: true
date: 2010-04-01 16:51:01+00:00
layout: post
slug: mod_rewrite-in-apache2
title: Mod_Rewrite in Apache2
categories:
- Instructional
tags:
- 64-bit
- apache
- code
- linux
- networking
- programming
- server
- Ubuntu
- web
---

Just incase you forget how to fix this the easy way: Enable mod_rewrite for URL voodoo; (Or any module replacing the 
    
    rewrite

)

> 

>     
>     $sudo a2enmod rewrite
>     $sudo service apache2 restart
> 
> 

Remember to fiddle with 
    
    /etc/apache2/sites-available.*< \pre> and change "AllowOverride none" to "all" in any places that you're having trouble with rewritten URL's
