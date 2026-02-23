---
layout: default
title: CV
---

<div style="text-align:center;padding-bottom:12px;border-bottom:2px solid #222;margin-bottom:4px;">
  <p class="name" style="font-size:26px;font-weight:700;margin-bottom:6px;">{{ site.data.personal.name }}</p>
  <p style="font-size:12px;color:#555;">
    {{ site.data.personal.phone }} &bull;
    <a href="mailto:{{ site.data.personal.email }}">{{ site.data.personal.email }}</a> &bull;
    <a href="https://{{ site.data.personal.linkedin }}">{{ site.data.personal.linkedin }}</a> &bull;
    <a href="https://{{ site.data.personal.github }}">{{ site.data.personal.github }}</a>
  </p>
</div>

<div class="cv-section">
  <h2>Educational Background</h2>
  {% for edu in site.data.education %}
    {% include cv/education.html edu=edu %}
  {% endfor %}
</div>

<div class="cv-section">
  <h2>Honors and Awards</h2>
  <ul>
    {% for award in site.data.honors %}<li>{{ award }}</li>{% endfor %}
  </ul>
</div>

<div class="cv-section">
  <h2>Professional Experience</h2>
  {% for exp in site.data.experience %}
    {% include cv/experience.html exp=exp %}
  {% endfor %}
</div>

<div class="cv-section">
  <h2>Projects</h2>
  {% for proj in site.data.projects %}
    {% include cv/project.html proj=proj %}
  {% endfor %}
</div>

<div class="cv-section">
  <h2>Training</h2>
  {% for t in site.data.training %}
    {% include cv/training.html t=t %}
  {% endfor %}
</div>

<div class="cv-section">
  <h2>Skills</h2>
  <div class="cv-skill-row"><strong>Languages &amp; Software:</strong> {{ site.data.skills.languages }}</div>
  {% for s in site.data.skills.software %}
    <div class="cv-skill-row">{{ s }}</div>
  {% endfor %}
</div>

<div class="cv-section">
  <h2>Publications</h2>
  <h3 style="font-size:13px;font-weight:700;margin:8px 0 4px;">Journal Articles</h3>
  {% for pub in site.data.publications %}
    {% if pub.type == "journal" %}
      {% include cv/publication.html pub=pub %}
    {% endif %}
  {% endfor %}
</div>

<div class="cv-section">
  <h2>Presentations</h2>
  <h3 style="font-size:13px;font-weight:700;margin:8px 0 4px;">Oral</h3>
  {% for p in site.data.presentations.oral %}
    {% include cv/presentation.html pres=p %}
  {% endfor %}
  <h3 style="font-size:13px;font-weight:700;margin:8px 0 4px;">Poster</h3>
  {% for p in site.data.presentations.poster %}
    {% include cv/presentation.html pres=p %}
  {% endfor %}
</div>
