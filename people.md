---
layout: default
title: "Our Team"
---

<div class="bandeau">
  <img src="./assets/images/people/lab_photo.jpg" class="patchwork-img" alt="Image 1">
  <!-- You can add more images or repeat the same ones multiple times -->
</div>

{% assign grouped_members = site.members | group_by: "type" | sort: "type" | reverse %}

<!-- <div class="people-gallery"> -->
<!--   {% for group in grouped_members %} -->
<!--     <h2>{{ group.name }}</h2> -->
<!--     <div class="position-group"> -->
<!--       <div class="people-gallery-row"> -->
<!--         {% assign sorted_members = group.items | sort: "name" | reverse %} -->
<!--         {% for member in sorted_members %} -->
<!--           <div class="people-gallery-item"> -->
<!--             <img src="{{ member.image }}" alt="{{ member.title }}" class="people-gallery-photo"> -->
<!--             <div class="people-gallery-info"> -->
<!--               <h3>{{ member.name }}</h3> -->
<!--               <\!-- <p>{{ member.email }}</p> -\-> -->
<!--               <p>{{ member.content }}</p> -->
<!--             </div> -->
<!--           </div> -->
<!--         {% endfor %} -->
<!--       </div> -->
<!--     </div> -->
<!--   {% endfor %} -->
<!-- </div> -->

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
