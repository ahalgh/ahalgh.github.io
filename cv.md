---
layout: default
title: CV
extra_css: /styles/cv.css
---

<div class="cv-grid">

  <div class="cv-grid-header">
    <p class="name" style="font-size:26px;font-weight:700;margin:0 0 6px;">{{ site.data.personal.name }}</p>
    <p style="font-size:12px;color:#555;margin:0;">
      {{ site.data.personal.phone }} &bull;
      <a href="mailto:{{ site.data.personal.email }}">{{ site.data.personal.email }}</a> &bull;
      <a href="https://{{ site.data.personal.linkedin }}">{{ site.data.personal.linkedin }}</a> &bull;
      <a href="https://{{ site.data.personal.github }}">{{ site.data.personal.github }}</a>
    </p>
  </div>

  <h2 class="cv-section-title">Education</h2>
  <div class="cv-section-body">
    {% for edu in site.data.education %}
      {% include cv/education.html edu=edu %}
    {% endfor %}
  </div>

  <h2 class="cv-section-title">Honors &amp; Awards</h2>
  <div class="cv-section-body">
    {% for award in site.data.honors %}
      <div class="cv-entry">
        <div class="cv-left-date"></div>
        <div class="cv-right-content"><div>{{ award }}</div></div>
      </div>
    {% endfor %}
  </div>

  <h2 class="cv-section-title">Professional Experience</h2>
  <div class="cv-section-body">
    {% for exp in site.data.experience %}
      {% include cv/experience.html exp=exp %}
    {% endfor %}
  </div>

  <h2 class="cv-section-title">Projects</h2>
  <div class="cv-section-body">
    {% for proj in site.data.projects %}
      {% include cv/project.html proj=proj %}
    {% endfor %}
  </div>

  <h2 class="cv-section-title">Training</h2>
  <div class="cv-section-body">
    {% for t in site.data.training %}
      {% include cv/training.html t=t %}
    {% endfor %}
  </div>

  <h2 class="cv-section-title">Skills</h2>
  <div class="cv-section-body">
    <div class="cv-entry">
      <div class="cv-left-date"></div>
      <div class="cv-right-content">
        <div><strong>Languages &amp; Frameworks:</strong> {{ site.data.skills.languages }}</div>
        {% for s in site.data.skills.software %}<div>{{ s }}</div>{% endfor %}
      </div>
    </div>
  </div>

  <h2 class="cv-section-title">Publications</h2>
  <h3 class="cv-subsection-title">Journal Articles</h3>
  <div class="cv-section-body">
    {% for pub in site.data.publications %}
      {% if pub.type == "journal" %}
        {% include cv/publication.html pub=pub %}
      {% endif %}
    {% endfor %}
  </div>

  <h2 class="cv-section-title">Presentations</h2>
  <h3 class="cv-subsection-title">Oral</h3>
  <div class="cv-section-body">
    {% for p in site.data.presentations.oral %}
      {% include cv/presentation.html pres=p %}
    {% endfor %}
  </div>
  <h3 class="cv-subsection-title">Poster</h3>
  <div class="cv-section-body">
    {% for p in site.data.presentations.poster %}
      {% include cv/presentation.html pres=p %}
    {% endfor %}
  </div>

</div>
