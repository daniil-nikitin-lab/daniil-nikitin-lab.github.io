---
title: Ongoing projects
permalink: /projects/
---

{% include independence-note.html %}

<div class="card" markdown="1">

### Follicular lymphoma project (ComboBatch)

<p class="meta">Institute of Molecular Biology NAS RA, Group of Bioinformatics · since April 2026 · role: principal investigator (project lead)</p>

**Question.** Follicular lymphoma and diffuse large B-cell lymphoma both arise from germinal-center B cells. Can public transcriptomes from RNA sequencing and microarrays, from fresh-frozen and FFPE material, be combined without losing the differences between them?

**First output.** ComboBatch evaluates the full cross-product of 14 batch-removal strategies, 3 imputation methods, 33 harmonization algorithms and 2 post-removal conditions on 7,174 samples from 88 germinal-center B-cell lymphoma cohorts across four platforms. Across 2,234 harmonization approaches scored on 87 quality metrics, method choice (R² 0.36) and batch-removal strategy (0.26) determine harmonization quality, whereas imputation (0.016) and post-removal (< 0.01) are secondary. Feature Specific Quantile Normalization and Surrogate Variable Analysis were the top methods for multi-platform and RNA-seq-only compositions, respectively ([bioRxiv 2026, preprint](https://doi.org/10.64898/2026.09.15.751825); journal submission in preparation).

{% include figure.html key="combobatch-project" %}

**Code.** [ComboBatch](https://github.com/Nikit357/ComboBatch) (harmonization toolkit) · [FL_harmonization](https://github.com/Nikit357/FL_harmonization) (code and data annotation to reproduce the article).

</div>

<div class="card" markdown="1">

### TE–host arms race on the T2T-CHM13 assembly

<p class="meta">Independent research line · 2025–present</p>

**Question.** Which transposable element subfamilies are escaping host silencing now, and which genes and processes do they affect?

**Status.** Two single-author articles published in 2026 ([*G3*](https://doi.org/10.1093/g3journal/jkag250); [*R. Soc. Open Sci.*](https://doi.org/10.1098/rsos.260639)); follow-up analyses in progress.

**Code and data.** [T2T_transposons_genes](https://github.com/Nikit357/T2T_transposons_genes) · [T2T_transposons_evolution](https://github.com/Nikit357/T2T_transposons_evolution).

</div>

<div class="card" markdown="1">

### Retroelement-driven regulatory evolution: thesis manuscript

<p class="meta">Independent · 2026</p>

A manuscript that brings together the analyses of transcription factor binding and histone modification profiles linked to human retroelements ([Zenodo 2026](https://doi.org/10.5281/zenodo.19052415); [bioRxiv 2025, preprint](https://doi.org/10.1101/2025.09.24.677146)).

**Code.** [Retroelements_joint_analysis](https://github.com/Nikit357/Retroelements_joint_analysis) · [supplementary_RetroSpect](https://github.com/Nikit357/supplementary_RetroSpect).

</div>

## Research plan and computational needs

<div class="table-scroll" markdown="1">

| Project | Public data | Analyses |
|---|---|---|
| Follicular lymphoma (ComboBatch) | 7,174 bulk transcriptomes from 88 germinal-center B-cell lymphoma cohorts (RNA-seq and microarrays; fresh-frozen and FFPE) | Cross-product benchmark of 2,234 harmonization approaches, 87 quality metrics per approach; a five-scenario decision tree for choosing a harmonization method |
| TE–host arms race (T2T-CHM13) | 3.7 million TE annotations; ENCODE T2T-CHM13 tracks for seven epigenomic modalities in twelve cell lines; 28,738 gene annotations | Genome-wide co-mapping of TEs with genes and epigenomic tracks against permutation backgrounds; per-subfamily correlation with TE age; gene-set enrichment |
| Retroelement-driven regulatory evolution | ENCODE ChIP-seq profiles of transcription factors and six histone modifications; GTEx expression | Ranking of retroelement-linked regulatory impact across 25,075 genes; pathway enrichment |

</div>

All analyses are written in R, Python and Bash, and the code for each project is public on [GitHub](https://github.com/Nikit357).

## Independent research infrastructure

{% include figure.html key="camp" %}

The TE projects use only public data and need no wet laboratory; their code and supplementary data are in open repositories. The follicular lymphoma project is hosted by the Group of Bioinformatics at the Institute of Molecular Biology NAS RA.
