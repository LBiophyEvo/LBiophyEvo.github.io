---
layout: default
title: "Research"
---

<div>
  {% assign projects_by_topic = site.projects | group_by: "topic" %}
  
  {% for topic in projects_by_topic %}
    <h2>{{ topic.name | capitalize }}</h2>
    <div class="gallery">
      {% for project in topic.items %}
        <div class="research-card">
          <div class="gallery-info">
            <a class="research-link" href="{{ project.url | relative_url }}">
            <img src="{{ project.image }}" alt="{{ project.name }}">
            <br>
              {{ project.name | escape }}
            </a>
            <p>{{ project.description }}</p>
          </div>
        </div>
      {% endfor %}
    </div>
  {% endfor %}
</div>
