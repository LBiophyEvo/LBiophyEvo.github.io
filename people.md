---
layout: default
title: "Team"
---
<div class="bandeau-croc-bottom" style="background-image: url('./assets/images/people/lab_photo.jpg');"></div>

{% assign grouped_members = site.members | group_by: "type" | sort: "type" | reverse %}

<div class="people-gallery">
  {% for group in grouped_members %}
    <h2>{{ group.name }}</h2>
    <div class="topic-group">
      <div class="people-gallery-row">
        {% assign sorted_members = group.items | sort: "name" | reverse %}
        {% for member in sorted_members %}
          <div class="people-gallery-item">
          <div class="gallery-info">
            <a class="research-link" href="{{ member.url | relative_url }}">
            <img src="{{ member.image }}" alt="{{ member.title }}" class="people-gallery-photo">
              <h3>{{ member.name | escape }}</h3>
            </a>
            <p>{{ member.description }}</p>
          </div>
          </div>
        {% endfor %}
      </div>
    </div>
  {% endfor %}
</div>
