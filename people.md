---
layout: default
title: "Our Team"
---

{% assign grouped_members = site.members | group_by: "type" | sort: "type" | reverse %}

<div class="people-gallery">
  {% for group in grouped_members %}
    <h2>{{ group.name }}</h2>
    <div class="position-group">
      <div class="people-gallery-row">
        {% assign sorted_members = group.items | sort: "name" | reverse %}
        {% for member in sorted_members %}
          <div class="people-gallery-item">
            <img src="{{ member.image }}" alt="{{ member.title }}" class="people-gallery-photo">
            <div class="people-gallery-info">
              <h3>{{ member.name }}</h3>
              <!-- <p>{{ member.email }}</p> -->
              <p>{{ member.content }}</p>
            </div>
          </div>
        {% endfor %}
      </div>
    </div>
  {% endfor %}
</div>
