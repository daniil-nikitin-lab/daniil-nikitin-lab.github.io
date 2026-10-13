#!/bin/bash
# Resize and re-export the pictures used on the site into assets/img/.
# Only files on the allow-list below are processed; everything else in pictures/
# stays private, so a photo cannot reach the public repository by accident.
#
# Requires python3 with Pillow.
# Usage: scripts/prepare_images.sh [path/to/cv/media/image1.png]
set -euo pipefail
cd "$(dirname "$0")/.."

SRC=pictures
OUT=assets/img

# source file | output path | max long edge (px)
ALLOW=(
  "me_medieval_clothes_with_laptop.jpeg|independent-work.jpg|1600"
  "graphical_abstract_transposons.jpeg|papers/te-epigenetic-impact-ga.jpg|1400"
  "transposable_elements_figure.jpeg|papers/te-tss-chord.jpg|1400"
  "first_transposons_figure.jpeg|papers/te-arms-race-epigenomics.jpg|1400"
  "graphical_abstract_FL_harmonization.jpeg|papers/combobatch-ga.jpg|1400"
  "international_biology_olympiad.jpeg|awards/ibo-2013-bern.jpg|1600"
  "certificate.jpeg|awards/iso-lead-auditor-2026.jpg|1400"
  "gclp_certificate.jpeg|awards/gclp-2025.jpg|1400"
  "historical_battle_armor.jpeg|hobbies/reenactment-1.jpg|1600"
  "another_medieval_battle.jpeg|hobbies/reenactment-2.jpg|1600"
  "me_working_in_camp.jpeg|projects/remote-work-camp.jpg|1600"
  "me_my_team_skiing.jpeg|hobbies/skiing.jpg|1600"
  "my_family.jpeg|hobbies/family.jpg|1600"
)

export_jpeg() {  # src dst maxedge
  # PIL re-encodes without copying EXIF/XMP, which strips metadata, and lowers
  # JPEG quality step by step until the file fits the 300 KB budget.
  mkdir -p "$(dirname "$2")"
  python3 - "$1" "$2" "$3" <<'PY'
import io, sys
from PIL import Image, ImageOps

src, dst, max_edge = sys.argv[1], sys.argv[2], int(sys.argv[3])
img = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
img.thumbnail((max_edge, max_edge), Image.LANCZOS)  # never upscales
for q in range(82, 54, -4):
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=q, optimize=True, progressive=True)
    if buf.tell() <= 300_000:
        break
open(dst, "wb").write(buf.getvalue())
PY
}

for row in "${ALLOW[@]}"; do
  IFS='|' read -r src dst max <<<"$row"
  export_jpeg "$SRC/$src" "$OUT/$dst" "$max"
  echo "$OUT/$dst"
done

if [[ -n "${1:-}" ]]; then
  export_jpeg "$1" "$OUT/portrait.jpg" 600
  echo "$OUT/portrait.jpg"
fi
