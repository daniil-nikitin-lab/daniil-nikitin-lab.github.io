---
title: "Molecular biology through evolution: a video course"
permalink: /course/
wide: true
lead: >-
  Eight lectures from my 35-lecture molecular biology course (in Russian, 2017–2018),
  arranged as a sequence from population genetics through protein evolution and mutation
  to transposons and the arms race between transposable elements and the host genome.
---
{% assign track = site.data.lectures | where_exp: "l", "l.step" | sort: "step" %}
<div class="course">
  <nav class="course-toc" aria-label="Course contents">
    <strong>Contents</strong>
    <ol>
    {% for l in track %}<li><a href="#step-{{ l.step }}">{{ l.title_en }}</a></li>{% endfor %}
    </ol>
  </nav>
  <div class="course-lectures">
  {% for l in track %}
    {% assign prev = l.step | minus: 1 %}{% assign next = l.step | plus: 1 %}
    {% if prev < 1 %}{% assign prev = nil %}{% endif %}{% if next > 8 %}{% assign next = nil %}{% endif %}
    {% include lecture.html step=l.step id=l.id n=l.n title_ru=l.title_ru title_en=l.title_en summary=l.summary prev=prev next=next %}
  {% endfor %}
    <p>The remaining 27 lectures are in the <a href="https://www.youtube.com/playlist?list=PLNaLMqSph0LaBiFtJ9YD1FT-miq8L9cDk">full playlist</a>. Back to <a href="/education/">Educational projects</a>.</p>
  </div>
</div>
