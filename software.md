---
layout: default
title: "Software"
---

<div class="gallery">
  {% for elem in site.softwares %}
  <a href="{{ elem.site }}">
    <div class="gallery-item">
      <img src="{{ elem.image }}" alt="{{ elem.name }}" class="project-image">
      <div class="gallery-info">
        <h3>{{ elem.name }}</h3>
        <p>{{ elem.description }}</p>
      </div>
    </div>
    </a>
  {% endfor %}
</div>
