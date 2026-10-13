---
title: Publications
permalink: /publications/
---
{% assign pubs = site.data.publications %}
{% assign n_articles = pubs | where: "type", "journal-article" | size %}
{% assign n_preprints = pubs | where: "preprint", true | size %}
{% assign n_single = pubs | where: "sole_author", true | size %}

{{ n_articles }} journal articles, {{ n_preprints }} preprints and {{ n_single }} single-author works. Preprints are listed only when no peer-reviewed version exists. Full records: [ORCID](https://orcid.org/0000-0003-1029-1174) · [Scopus](https://www.scopus.com/authid/detail.uri?authorId=57200544585).

{% assign groups = pubs | map: "group" | uniq %}
{% for g in groups %}
<h2>{{ g }}</h2>
{% if forloop.first %}{% include figure.html key="te-ga-pubs" %}{% endif %}
<ol class="pubs" reversed>
{% assign items = pubs | where: "group", g %}
{% for p in items %}
  <li>
    {%- assign n = p.authors | size -%}
    {%- assign last = n | minus: 1 -%}
    {%- assign own = -1 -%}
    {%- for a in p.authors -%}{%- if a contains "Nikitin" and a contains "D." -%}{%- assign own = forloop.index0 -%}{%- endif -%}{%- endfor -%}
    {%- assign shown = 0 -%}
    {%- for a in p.authors -%}
      {%- assign i = forloop.index0 -%}
      {%- assign keep = true -%}
      {%- if n > 10 and i >= 6 and i != own -%}{%- assign keep = false -%}{%- endif -%}
      {%- if keep -%}
        {%- if shown > 0 -%}, {% endif -%}
        {%- if n > 10 and i == own and own >= 6 -%}… {% endif -%}
        {%- if i == own -%}<strong>{{ a }}</strong>{%- else -%}{{ a }}{%- endif -%}
        {%- assign shown = shown | plus: 1 -%}
      {%- endif -%}
    {%- endfor -%}
    {%- if n > 10 and own < last -%}, et al.{%- endif %}
    ({{ p.year }}). <span class="pub-title">{{ p.title }}</span>. <em>{{ p.journal }}</em>.
    {% if p.doi %}<a href="{{ p.url }}">doi:{{ p.doi }}</a>{% endif %}
    {% if p.preprint %}<span class="tag">preprint</span>{% endif %}
    {% if p.note %}<br><span class="meta">{{ p.note }}</span>{% endif %}
  </li>
{% endfor %}
</ol>
{% endfor %}
