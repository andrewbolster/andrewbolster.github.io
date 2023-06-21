---
layout: page
title: Howdi, I'm Andrew, but most people call me Bolster
---
{% include JB/setup %}


* Senior R&D Manager (Data Science) at [Synopsys Software Integrity Group](https://www.synopsys.com/software-integrity.html)
* Trustee, Treasurer @ [Farset Labs](https://www.farsetlabs.org.uk)
* Director, Treasurer @ [BSides Belfast](https://bsidesbelfast.org)
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
