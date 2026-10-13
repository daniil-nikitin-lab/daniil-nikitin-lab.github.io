# daniil-nikitin-lab.github.io

Source of the personal research website of Daniil Nikitin, served by GitHub Pages
at <https://daniil-nikitin-lab.github.io/>. Jekyll, no external theme.

## Update the publication list

```bash
python3 scripts/fetch_orcid.py > _data/publications.yml
```

The script reads the public ORCID record and Crossref/DataCite metadata. Rules:
a preprint is listed only when no peer-reviewed version exists; corrections are
attached as a note; author lists carry names only. Records can be excluded by DOI
(`DROP_DOI`) or ORCID put-code (`DROP_PUT_CODE`). An optional, git-ignored
`scripts/private_exclude.txt` (one term per line) drops any record whose title or
venue contains a listed term, without the term entering the repository.

## Change the video course

The 8 lectures on `/course/` are the entries of `_data/lectures.yml` that carry a
`step` field (1–8). Move the field to change the selection.

## Institutional details

Affiliation, address and institute phone live in `_data/affiliation.yml` and are
used by the header, footer and home page.

## Add a figure

1. Put the original in `pictures/` (git-ignored).
2. Add it to the allow-list in `scripts/prepare_images.sh` and run the script
   (needs Python 3 with Pillow). It resizes, strips metadata and keeps files
   under 300 KB.
3. Add an entry to `_data/figures.yml` (key, file, alt, caption, credit, float,
   width, height) and place it with `{% include figure.html key="..." %}`.

## Preview and deploy

```bash
bundle exec jekyll serve   # optional local preview, http://127.0.0.1:4000
```

Before every push, run the content check against the private exclusion list:

```bash
TERM=$(head -1 scripts/private_exclude.txt)
git ls-files -z | xargs -0 grep -l -i "$TERM" || echo "tracked files clean"
```

Push to `main`; GitHub Pages builds the site from the repository root.
