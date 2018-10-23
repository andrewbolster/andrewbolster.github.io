/*
 * header-links.js
 * Copyright (C) 2018 andrew.bolster <andrew.bolster@AL-BEL-09993.local>
 * From https://ben.balter.com/2014/03/13/pages-anchor-links/
 * Distributed under terms of the MIT license.
 */
$(function() {
  return $("h1, h2, h3, h4, h5, h6").each(function(i, el) {
    var $el, icon, id;
    $el = $(el);
    id = $el.attr('id');
    icon = '<i class="fi-link small"></i>';
    if (id) {
      return $el.append($("<a />").addClass("header-link").attr("href", "#" + id).html(icon));
    }
  });
});

