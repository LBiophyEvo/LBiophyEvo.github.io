---
layout: default
title: "Software"
---

<!-- <div class="gallery"> -->
<!--   {% for elem in site.softwares %} -->
<!--   <a href="{{ elem.site }}"> -->
<!--     <div class="research-card"> -->
<!--       <img src="{{ elem.image }}" alt="{{ elem.name }}" class="research-thumbnail"> -->
<!--       <div class="gallery-info"> -->
<!--         <h3>{{ elem.name }}</h3> -->
<!--         <p>{{ elem.description }}</p> -->
<!--       </div> -->
<!--     </div> -->
<!--     </a> -->
<!--   {% endfor %} -->
<!-- </div> -->

<div class="gallery">
  {% for item in site.softwares %}
  <div class="research-card">
    <a href="{{ item.site }}">
    <h3>{{ item.name }}</h3>
    </a>
    <div class="research-card-body">
        <img src="{{ item.image }}" alt="{{ item.title }}" class="research-thumbnail">
      <p>{{ item.content }}</p>
    </div>
  </div>
  {% endfor %}
</div>
