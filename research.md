---
title: Research interests
permalink: /research/
---

<div class="summary-box" markdown="1">

**Research summary.** I study the evolutionary conflict between transposable elements (TEs) and the human genome, and its consequences for gene regulation and cancer. Using the telomere-to-telomere T2T-CHM13 assembly, I co-mapped 3.7 million TEs with 28,738 human genes and with seven epigenomic modalities from ENCODE in twelve cell lines. The analysis identified a 220 kb interferon-alpha domain enriched for young L1 copies, and showed that SVA elements and seven LTR subfamilies escape H3K9me3-mediated silencing while acquiring CTCF binding. In a second line of work, at the Institute of Molecular Biology NAS RA, I lead a follicular lymphoma project. Its first output benchmarks 2,234 harmonization approaches on 7,174 transcriptomes from 88 germinal-center B-cell lymphoma cohorts, to separate follicular lymphoma, diffuse large B-cell lymphoma and normal germinal-center B cells.

</div>

## Evolutionary genomics of transposable elements

{% include figure.html key="te-ga" %}

About 40 % of the human genome derives from retroelements. Many copies carry transcription factor binding sites and histone marks that the host genome has recruited into its own regulation. Between 2018 and 2019 my co-authors and I developed RetroSpect, a method that ranks genes and molecular processes by the density of retroelement-linked regulatory features near them ([Nikitin et al., 2019, book chapter](https://doi.org/10.1007/978-3-030-30363-1_5)). With it, we mapped retroelement-linked transcription factor binding sites ([*Front. Immunol.* 2018](https://doi.org/10.3389/fimmu.2018.00030); [*Cells* 2019](https://doi.org/10.3390/cells8020130)), enhancer marks H3K4me1 ([*Cells* 2019](https://doi.org/10.3390/cells8101219)) and five further histone modifications ([*Cells* 2019](https://doi.org/10.3390/cells8091034)) in ENCODE data. These analyses identified molecular pathways whose regulation was shaped most strongly by retroelements during human evolution.

{% include figure.html key="te-chord" %}

The complete T2T-CHM13 assembly made a genome-wide map possible. Using a 10 kb window around transcription start sites and a 500-permutation background, I mapped 3,709,429 TEs from 6 classes and 44 families to 28,738 genes ([*G3* 2026](https://doi.org/10.1093/g3journal/jkag250)). Each TE class is enriched near genes of specific functions: SVA elements near genes involved in transcription termination, Alu elements near RNA processing and splicing genes, MIR elements near zinc homeostasis and voltage-gated potassium channel genes, LINE elements near lipid metabolism and olfactory perception genes, and LTR elements near ion transport genes. The map is correlative; it provides a positional baseline for functional tests.

## The TE–host evolutionary arms race

Host genomes silence TEs, mainly through H3K9me3-dependent heterochromatin, and TEs that escape silencing can spread. In the T2T-CHM13 ENCODE data, I quantified the epigenetic state of 3.7 million TEs across seven epigenomic modalities in twelve cell lines and related it to TE age ([*R. Soc. Open Sci.* 2026](https://doi.org/10.1098/rsos.260639)). SVA elements show the strongest signatures of the arms race: younger copies progressively escape H3K9me3-mediated heterochromatinization while acquiring CTCF and enhancer marks. The AluYb8 and AluYb9 subfamilies accumulate CTCF binding. Seven LTR subfamilies (HERV16-int, MER11C, LTR43-int, HERVE-int, LTR22C, LTR5_Hs and HERVIP10FH-int) acquire both active and H3K9me3-enriched contexts together with CTCF binding. Across modalities, transposon-driven evolution is dominated by evasion of H3K9me3 and, secondarily, H3K27me3, together with invasion into CTCF-rich regions.

{% include figure.html key="te-arms-race" %}

The same conflict appears at the level of single loci. In the interferon-alpha domain, 77 of 175 TEs are young L1 copies from 36 subfamilies, with mean divergence of 135.7 against 188.2 genome-wide ([*G3* 2026](https://doi.org/10.1093/g3journal/jkag250)). This is consistent with recent L1 activity in a locus of innate immune genes, and could indicate an arms race affecting their regulation.

## Cancer as an evolutionary process

Tumours evolve under selection within the patient, and they often lose the silencing that keeps TEs inactive in normal tissues. Using six histone modifications from five ENCODE cell lines, I ranked the regulatory impact of retroelements across 25,075 human genes. Gene sets consistently enriched for retroelement-linked promoter and enhancer sites are associated with chronic myeloid leukemia and small cell lung cancer pathways, and with host defense against human T-cell lymphotropic virus type 1 ([bioRxiv 2025, preprint](https://doi.org/10.1101/2025.09.24.677146)).

My earlier work on transcriptomic biomarkers addressed how tumours differ from each other at the expression level, including RNA sequencing-based therapy prescription in colorectal cancer ([*BMC Cancer* 2022](https://doi.org/10.1186/s12885-022-10177-3)), prediction of sorafenib response in kidney cancer ([*Front. Mol. Biosci.* 2022](https://doi.org/10.3389/fmolb.2022.753318)) and microsatellite instability signatures ([*Front. Mol. Biosci.* 2021](https://doi.org/10.3389/fmolb.2021.737821)).

Since April 2026 I have led the follicular lymphoma project at the Institute of Molecular Biology NAS RA. Follicular lymphoma and diffuse large B-cell lymphoma both arise from germinal-center B cells and differ by subtle transcriptional changes, which batch effects between cohorts easily mask. The first output of the project, ComboBatch, identifies which harmonization methods preserve these differences ([bioRxiv 2026, preprint](https://doi.org/10.64898/2026.09.15.751825)); see [Ongoing projects](/projects/).
