---
layout: default
---
{% include JB/setup %}

{% for post in site.posts limit: 10 %}
<div class="row-fluid">
  <div class="span12">
    <a href="{{ post.url}}"><h2>{{ post.title }}</h2></a>
    <h4>{{ post.date | date_to_long_string }}</h4>
    <p>
      {{ post.content | strip_html | truncatewords:75}}
      <br/>
      <a href="{{ post.url }}">Read Post</a>
    </p>
  </div>
</div>
{% endfor %}

