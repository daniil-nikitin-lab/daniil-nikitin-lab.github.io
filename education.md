---
title: Educational projects
permalink: /education/
---

## Molecular biology: a video course

In 2017–2018 I recorded a course of 35 lectures on molecular biology in Russian. It is built around evolutionary explanations: population genetics, neutral evolution, protein evolution and the arms race between transposons and the host genome. The course follows the structure of a university program, from biological macromolecules through genome maintenance and rearrangements to gene expression and its regulation.

**[Watch the 8-lecture evolutionary track →](/course/)**

The full course is available as a [YouTube playlist](https://www.youtube.com/playlist?list=PLNaLMqSph0LaBiFtJ9YD1FT-miq8L9cDk):

{% include youtube.html list="PLNaLMqSph0LaBiFtJ9YD1FT-miq8L9cDk" title="Molecular biology: lecture course by Daniil Nikitin (playlist)" %}

<details>
<summary>All 35 lectures</summary>
<div class="table-scroll">
<table>
  <thead><tr><th>No.</th><th>Block</th><th>Lecture</th><th>Original title</th></tr></thead>
  <tbody>
  {% for l in site.data.lectures %}
    <tr>
      <td>{{ l.n }}</td>
      <td>{{ l.block }}</td>
      <td><a href="https://www.youtube.com/watch?v={{ l.id }}&amp;list=PLNaLMqSph0LaBiFtJ9YD1FT-miq8L9cDk">{{ l.title_en }}</a>{% if l.step %} <span class="tag">track {{ l.step }}</span>{% endif %}</td>
      <td lang="ru">{{ l.title_ru }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
</div>
</details>
