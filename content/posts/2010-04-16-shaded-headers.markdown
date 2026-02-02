---
author: admin
categories:
- Instructional
comments: true
date: 2010-04-16 16:25:46+00:00
layout: post
slug: shaded-headers
tags:
- CSS
- HTML
- Tutorial
- WordPress
- jQuery
- 'web-design'
title: Shaded Headers in Thematic
---


So, as you can see the blog is sporting a new, cleaner look. Nothing better than experimenting!  One of the nicer aspects of the new setup is the shaded headers (ie. `<h1>`/`<h2>` tags).

I started off my experimentation by going through [WebDesignerWall's walkthrough](http://www.webdesignerwall.com/tutorials/css-gradient-text-effect/) on the subject of text effects, but the limitation that I came across was that if you use their implimentation, any links (`<a\>`) in the header are lost 'under' the span.

Going from top to tail, this is how i have my gradients set up.  Download the gradient files ([white background]({{ BASE_PATH }}/wp-content/themes/penguincafe/img/gradient-white.png) / [black background]({{ BASE_PATH }}/wp-content/themes/penguincafe/img/gradient-dark.png)) and place them in whatever accessible image directory you are using. (If you get lost, [bloggingtips.com do a great overview](http://www.bloggingtips.com/2007/12/21/file-paths-in-your-wordpress-css-and-theme-files/))

Basically, the operation is to layer the gradient image over the text _inside_ the `<a>` tag's that are children of `<h1>`/`<h2>` ([hence the '>' in the CSS selector](http://www.w3.org/TR/css3-selectors/#child-combinators)), so that the gradient image itself is still a link. Don't worry about how the `<span>` tag gets there yet...  In whichever css file you are using add the following block of css.

```css


     h1 > a,h2 > a {
     position:relative;
     }
     h1 > a span, h2 > a span {
     background:url(path/to/gradient-whichever.png);
     position:absolute;
     display:block;
     width:100%;
     height:31px;
     }

```

If you are using a [thematic child theme](http://op111.net/53), the css file should be:


>   wp-content/themes/`<childname>`/style.css

The relative position is important as it is what allows the gradient image to overlay the text.  Next thing to worry about is getting the `<span>` tag inside the `<a>` tag without lots of legwork.

Welcome to [JQuery](http://docs.jquery.com/How_jQuery_Works) gentlefolk; it can do magic for your bloodpressure.  To keep it simple, add this function into your 'functions.php' (if you know you already have a JQuery script declaration, then you know enough to remove the relevant bit from below, if you don't, ask in the comments)

```javascript
     function shaded_headers() {
     echo <<<END
     <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3/jquery.min.js"></script>
     <script type="text/javascript">
     $(document).ready(function(){
     //prepend span tag to H1 and H2
     $("h1 > a").prepend("<span></span>");
     $("h2 > a").prepend("<span></span>");
     });
     </script>
     END;
     }
     add_filter('thematic_head_scripts','shaded_headers');
```



And your done! This doesn't work for headers that aren't links, but I'm working on that (IANA JQuery Guru, help is you like!)

If I've missed anything out, please point it out in the comments or tweet me @bolster
