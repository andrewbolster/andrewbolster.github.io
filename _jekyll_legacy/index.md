---
layout: page
title: Howdi, I'm Andrew, but most people call me Bolster
---
{% include JB/setup %}


* Senior R&D Manager (Data Science) at [Black Duck Software](https://blackduck.com/)
* Director, Treasurer @ [BSides Belfast](https://bsidesbelfast.org)
* among [other things](/about)

### Recent Writings

<ul class="posts">  
  {% for post in site.posts %}  
     <li>  
       <span>{{ post.date | date_to_string }}</span> &raquo;  
       <a href="{{ BASE_PATH }}{{ post.url }}">  
       {{ post.title }}</a>  
     </li>  
  {% endfor %}  
</ul>
