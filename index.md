---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

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
    <h2>News in the LBE</h2>
    <div class="feed">
      {% for post in site.data.feed_news %}
      <div class="feed-item">
        <!-- <div class="feed-date">{{ post.title }}</div> -->
        <p class="feed-content">{{ post.content }}<br><span class="feed-date">{{ post.date }}</span></p>
      </div>
      {% endfor %}
    </div>
  </div>
</div>

<hr>
<br>

<div class="meeting-feed">
    <h2>Lab meetings</h2>
    <div class="feed">
      {% for post in site.data.lab_meetings %}
      <div class="feed-item">
        <!-- <div class="feed-date">{{ post.title }}</div> -->
        <p class="feed-content">{{ post.speaker }} <span class="feed-title">{{post.title}}</span><br><span class="feed-date">{{ post.date }} {{post.type}} </span></p>
      </div>
      {% endfor %}
    </div>
</div>
<br>

<hr>
<br>

<h2>Research topics include:</h2>
<div class="gallery">
  {% for item in site.researchs %}
  <div class="research-card">
    <h3>{{ item.name }}</h3>
    <img src="{{ item.image }}" alt="{{ item.title }}" class="research-thumbnail">
    <div class="research-card-body">
      <p>{{ item.content }}</p>
    </div>
  </div>
  {% endfor %}
</div>

