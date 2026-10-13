"""Build _data/publications.yml from the public ORCID record.

Fetches the works list from the ORCID public API, enriches each DOI with
bibliographic metadata from the Crossref API (DataCite API for Zenodo and other
DataCite DOIs), applies the site's citation rules and prints YAML to stdout.

Citation rules:
  * a preprint is listed only when no peer-reviewed version exists;
  * corrections are attached as a note to the corrected article;
  * author lists carry names only, never affiliations.

Usage:
    python3 scripts/fetch_orcid.py > _data/publications.yml
"""

import html
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ORCID = "0000-0003-1029-1174"
OWN_FAMILY = "Nikitin"

# Preprints whose peer-reviewed version is published (preprint -> article).
DROP_DOI = {
    "10.32942/x2fm2m",  # -> 10.1093/g3journal/jkag250
    "10.64898/2026.03.19.712972",  # -> 10.1098/rsos.260639
    "10.2139/ssrn.4529648",  # -> 10.1016/j.xcrm.2025.102029
}
# ORCID records without a DOI that are not shown (excluded conference abstract).
DROP_PUT_CODE = {210748652}

CORRECTION_OF = {"10.3390/cells8080832": "10.3390/cells8020130"}
JOURNAL_FIX = {"10.14740/jh412w": "Journal of Hematology"}

SINGLE = "Single-author work"
PREPRINTS = "Preprints"
TE = "Transposable elements and regulatory evolution, 2018–2019"
CANCER = "Cancer genomics and transcriptomic biomarkers"
GROUP_ORDER = [SINGLE, PREPRINTS, TE, CANCER, "Other"]
GROUP = {
    "10.1093/g3journal/jkag250": SINGLE,
    "10.1098/rsos.260639": SINGLE,
    "10.1101/2025.09.24.677146": SINGLE,
    "10.5281/zenodo.19052415": SINGLE,
    "10.64898/2026.09.15.751825": PREPRINTS,
    "10.3389/fimmu.2018.00030": TE,
    "10.3390/cells8020130": TE,
    "10.3390/cells8091034": TE,
    "10.3390/cells8101219": TE,
    "10.1007/978-3-030-30363-1_5": TE,
    "10.1016/j.xcrm.2025.102029": CANCER,
    "10.3389/fmolb.2022.753318": CANCER,
    "10.1186/s12885-022-10177-3": CANCER,
    "10.1016/j.heliyon.2021.e06408": CANCER,
    "10.3389/fmolb.2021.737821": CANCER,
    "10.1016/j.jmig.2021.03.011": CANCER,
    "10.3390/ijms21228491": CANCER,
    "10.3390/biomedicines8060142": CANCER,
    "10.3390/cancers11081060": CANCER,
    "10.1007/s10549-018-5043-0": CANCER,
    "10.14740/jh412w": CANCER,
}
PREPRINT_SERVERS = {"10.1101": "bioRxiv", "10.64898": "bioRxiv"}


def warn(msg):
    print(f"warning: {msg}", file=sys.stderr)


def get_json(url, accept="application/json"):
    req = urllib.request.Request(
        url, headers={"Accept": accept, "User-Agent": "fetch_orcid/1.0 (mailto:none)"}
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def norm_title(t):
    return re.sub(r"[^a-z0-9]", "", t.lower())


def clean(text):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", text or ""))).strip()


def private_terms():
    # Kept outside version control so the excluded terms never enter the repository.
    path = Path(__file__).with_name("private_exclude.txt")
    if not path.exists():
        return []
    return [ln.strip().lower() for ln in path.read_text().splitlines() if ln.strip()]


def author_name(given, family):
    initials = " ".join(p[0] + "." for p in re.split(r"[\s-]+", given or "") if p)
    return f"{initials} {family or ''}".strip()


def metadata(doi):
    """Return title, author names, container, publisher, year and subtype for a DOI."""
    try:
        m = get_json(f"https://api.crossref.org/works/{doi}")["message"]
        return dict(
            title=(m.get("title") or [""])[0],
            authors=[author_name(a.get("given"), a.get("family") or a.get("name"))
                     for a in m.get("author", [])],
            container=(m.get("container-title") or [""])[0],
            publisher=m.get("institution", [{}])[0].get("name") or m.get("publisher", ""),
            year=(m.get("issued", {}).get("date-parts") or [[None]])[0][0],
            subtype=m.get("subtype") or m.get("type"),
        )
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise
    a = get_json(f"https://api.datacite.org/dois/{doi}")["data"]["attributes"]
    return dict(
        title=(a.get("titles") or [{}])[0].get("title", ""),
        authors=[author_name(c.get("givenName"), c.get("familyName") or c.get("name"))
                 for c in a.get("creators", [])],
        container="",
        publisher=a.get("publisher", ""),
        year=a.get("publicationYear"),
        subtype=(a.get("types") or {}).get("resourceTypeGeneral"),
    )


def main():
    works = get_json(f"https://pub.orcid.org/v3.0/{ORCID}/works")
    terms = private_terms()
    entries, corrections = {}, {}

    for group in works["group"]:
        s = group["work-summary"][0]
        title = s["title"]["title"]["value"]
        ids = (s.get("external-ids") or {}).get("external-id", [])
        doi = next((i["external-id-value"].lower() for i in ids
                    if i["external-id-type"] == "doi"), None)
        year = ((s.get("publication-date") or {}).get("year") or {}).get("value")
        venue = (s.get("journal-title") or {}).get("value") or ""

        if s["put-code"] in DROP_PUT_CODE or doi in DROP_DOI:
            continue
        if any(t in (title + " " + venue).lower() for t in terms):
            warn(f"dropped by private exclusion list: put-code {s['put-code']}")
            continue
        if doi is None:
            # A record without a DOI is shown only if it is not a duplicate title.
            entries.setdefault(("nodoi", norm_title(title)), dict(
                title=title, authors=[], journal=venue, year=year, doi=None,
                url=None, type=s["type"], put_code=s["put-code"]))
            continue

        meta = metadata(doi)
        authors = meta["authors"]
        journal = JOURNAL_FIX.get(doi) or clean(meta["container"]) or venue
        preprint = s["type"] == "preprint" or meta["subtype"] == "posted-content"
        if preprint and not journal:
            journal = PREPRINT_SERVERS.get(doi.split("/")[0], meta["publisher"])
        if s["type"] == "dissertation-thesis":
            journal = "Zenodo (thesis manuscript)"
        if not year:
            year = meta["year"]

        entry = dict(
            title=clean(meta["title"] or title),
            authors=authors,
            journal=journal,
            year=int(year) if year else None,
            doi=doi,
            url=f"https://doi.org/{doi}",
            type=s["type"],
            preprint=preprint,
            sole_author=len(authors) == 1,
        )
        if doi in CORRECTION_OF:
            corrections[CORRECTION_OF[doi]] = doi
            continue
        entries[doi] = entry

    # Drop no-DOI duplicates (e.g. a data-set record titled like a paper).
    kept_titles = {norm_title(e["title"]) for k, e in entries.items() if e["doi"]}
    for k in [k for k in entries if isinstance(k, tuple)]:
        if k[1] in kept_titles:
            del entries[k]
        else:
            warn(f"record without DOI kept: put-code {entries[k]['put_code']}")

    # Drop preprints whose journal version is now in ORCID.
    journal_titles = {norm_title(e["title"]) for e in entries.values()
                      if e["doi"] and not e.get("preprint")}
    for k in [k for k, e in entries.items() if e.get("preprint")]:
        if norm_title(entries[k]["title"]) in journal_titles:
            warn(f"preprint dropped, journal version exists: {k}")
            del entries[k]

    out = []
    for k, e in entries.items():
        if e["doi"] in corrections:
            e["note"] = f"Correction published: doi:{corrections[e['doi']]}"
        e["group"] = GROUP.get(e["doi"], "Other")
        if e["group"] == "Other":
            warn(f"no group assigned: {e['doi'] or e.get('put_code')}")
        e.pop("put_code", None)
        out.append(e)

    out.sort(key=lambda e: (GROUP_ORDER.index(e["group"]), -(e["year"] or 0), e["title"]))
    yaml.safe_dump(out, sys.stdout, sort_keys=False, allow_unicode=True, width=1000)
    print(f"{len(out)} entries", file=sys.stderr)


if __name__ == "__main__":
    main()
