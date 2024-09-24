---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

<div class="bandeau-croc-top" style="background-image: url('./assets/images/banner/Scaffold1_12.jpg');"></div>

<div class="content-wrapper">
  <div class="main-content">
    <div class="lab-description-box">
      <h2> About The LBE </h2>
      <p>The Laboratory of Biophysics and Evolution (LBE) studies major evolutionary
      transitions and develops innovative technologies to study biological organisms.
      Created in 2021, the lab is part of UMR CNRS-ESPCI 8231 Chemistry, Biology and
      Innovation.</p>

      <p> LBE comprises two teams:
      -team Nghe: origins of life, (bio)chemical reaction networks, evolution of gene
      networks, microfluidic technologies

      -team Rainey: fraternal transitions and the evolution of life cycles,
      egalitarian transitions and the evolution of heredity, eco-evolution dynamics of
      bacterial communities, millifluidic technologies</p>
  </div>
</div>

<div class="news-feed">
    <h2 class="feed-title">News in the LBE</h2>
    <div class="feed">
      {% for post in site.data.feed_news %}
      <div class="feed-item">
        <span class="feed-title">{{ post.title }}</span>
        <p class="feed-text">{{ post.content }}<br><span class="feed-date">{{ post.date }}</span></p>
      </div>
      {% endfor %}
    </div>
  </div>
</div>

<hr class="custom-hr">
<br>

<h2 class="feed-title">Lab meetings</h2>
<div class="meeting-feed">
    <div class="feed">
      {% for post in site.data.lab_meetings %}
      <div class="feed-item">
        <!-- <div class="feed-date">{{ post.title }}</div> -->
        <p class="feed-content"><strong>{{ post.speaker }}</strong> <span class="feed-title">{{post.title}}</span><br><span class="feed-date">{{ post.date }} {{post.type}} </span></p>
      </div>
      {% endfor %}
    </div>
</div>

<br>
<hr class="custom-hr">
<br>

<h2 class="feed-title">Research topics</h2>
<div>
  <!-- {% assign projects_by_topic = site.projects | group_by: "topic" %} -->
  
  {% for topic in projects_by_topic %}
    <!-- <h3>{{ topic.name | capitalize }}</h3> -->
    <div class="gallery">
      {% for project in topic.items %}
        <div class="research-card">
          <div class="gallery-info">
            <a class="research-link" href="{{ project.url | relative_url }}">
            <img src="{{ project.image }}" alt="{{ project.name }}" class="research-thumbnail">
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
