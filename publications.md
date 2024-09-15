---
layout: default
title: "Publications"
---

# Publications

{% assign papers_by_year = site.data.references | group_by: "year" | sort: "year" | reverse %}
{% for year_group in papers_by_year %}
  <h2>{{ year_group.name }}</h2> <!-- Display the year as a heading -->
  <hr>
{% for paper in year_group.items %}
  <div class="paper">
    <!-- Title on the first line, italicized and with custom gray color -->
    {{ paper.title }}<br>

    <p>
    <!-- Authors on the second line, bolded and with a lighter gray color -->
    {% if paper.authors %}
      <em style="color: #888;">{{ paper.authors | join: ", " }}</em><br>
    {% endif %}

    <!-- Journal and year on the third line, with a DOI link if available -->
    {{ paper.citation }}
    {% if paper.year %}
      ({{ paper.year }})
    {% endif %}
    </p>
    </div>
{% endfor %}
{% endfor %}
