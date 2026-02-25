---
layout: default
title: CV
extra_css: /styles/cv.css
fa: true
---

<div class="cv-grid">

  <div class="cv-grid-header">
    <p class="name" style="font-size:26px;font-weight:700;margin:0 0 10px;">{{ site.data.personal.name }}</p>
    <div class="cv-social-links">
      <div class="cv-social-col">
        <div class="cv-social-link">
          <i class="fas fa-envelope"></i>
          <a href="mailto:{{ site.data.personal.email }}">{{ site.data.personal.email }}</a>
        </div>
        <div class="cv-social-link">
          <i class="fas fa-globe"></i>
          <a href="https://{{ site.data.personal.homepage }}">{{ site.data.personal.homepage }}</a>
        </div>
        <div class="cv-social-link">
          <i class="fas fa-file-pdf"></i>
          <a href="javascript:void(0)" onclick="downloadCV()">CV PDF</a>
        </div>
      </div>
      <div class="cv-social-col">
        <div class="cv-social-link">
          <i class="fab fa-github"></i>
          <a href="https://{{ site.data.personal.github }}">{{ site.data.personal.github }}</a>
        </div>
        <div class="cv-social-link">
          <i class="fab fa-linkedin"></i>
          <a href="https://{{ site.data.personal.linkedin }}">LinkedIn</a>
        </div>
        <div class="cv-social-link">
          <i class="fas fa-graduation-cap"></i>
          <a href="{{ site.data.personal.scholar }}">Google Scholar</a>
        </div>
      </div>
    </div>
    <p class="cv-statement" style="margin:12px 0 0;font-style:italic;">Machine Learning, Scientific Computing, and Operations Research</p>
    <p class="cv-statement" style="margin:6px 0 0;">I apply modern ML methods&mdash;including deep learning, optimization, and large language models&mdash;to problems in materials informatics, autonomous systems, and decision support. I have worked with researchers and engineers at Georgia Tech, Army Futures Command, and New Mexico State University.</p>
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
      {% assign parts = award | split: ", " %}
      {% assign date = parts | last %}
      {% assign name_size = parts | size | minus: 1 %}
      {% assign name_parts = parts | slice: 0, name_size %}
      {% assign name = name_parts | join: ", " %}
      <div class="cv-entry">
        <div class="cv-left-date">{{ date }}</div>
        <div class="cv-right-content"><div>{{ name }}</div></div>
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

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
<script>
function downloadCV() {
  html2pdf().set({
    margin:      0.5,
    filename:    'Greenhalgh_CV.pdf',
    image:       { type: 'jpeg', quality: 0.98 },
    html2canvas: { scale: 2, useCORS: true, logging: false },
    jsPDF:       { unit: 'in', format: 'letter', orientation: 'portrait' },
    pagebreak:   { mode: 'avoid-all' }
  }).from(document.querySelector('.cv-grid')).save();
}
</script>
