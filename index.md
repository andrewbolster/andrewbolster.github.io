---
layout: page
title: Howdi, I'm Andrew, but most people call me Bolster
---
{% include JB/setup %}


* Data Science Engineering Manager @ [NTT Application Security](https://www.whitehatsec.com)
* Trustee @ [Farset Labs](https://www.farsetlabs.org.uk)
* among [other things](/about)

### Recent Writings

<ul class="posts">  
  {% for post in site.posts limit:30 %}  
     <li>  
       <span>{{ post.date | date_to_string }}</span> &raquo;  
       <a href="{{ BASE_PATH }}{{ post.url }}">  
       {{ post.title }}</a>  
     </li>  
  {% endfor %}  
</ul>
