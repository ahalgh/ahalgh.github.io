#!/usr/bin/env python3
"""
Generate cv.html (and optionally CV_AG.pdf) from data/*.yaml + cv_template.html.

Usage:
    python generate_cv.py           # generates cv.html
    python generate_cv.py --pdf     # also generates CV_AG.pdf via WeasyPrint

Dependencies (install once):
    pip install pyyaml jinja2
    pip install weasyprint          # optional, for --pdf flag

To update the CV, edit the relevant file in data/ and re-run this script
(or just push — GitHub Actions will run it automatically):

    data/personal.yaml      — name, contact info
    data/education.yaml     — degrees
    data/honors.yaml        — awards and honors
    data/experience.yaml    — jobs and research positions
    data/projects.yaml      — course/personal projects
    data/training.yaml      — courses and certifications
    data/skills.yaml        — languages and software
    data/publications.yaml  — journal articles
    data/presentations.yaml — oral and poster presentations
"""

import sys
import yaml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data"

SECTIONS = [
    "personal",
    "education",
    "honors",
    "experience",
    "projects",
    "training",
    "skills",
    "publications",
    "presentations",
]


def bold_name(text: str) -> str:
    """Bold every variant of the author's name that appears in author lists."""
    variants = [
        "Greenhalgh, A.D.",
        "Greenhalgh, A.",
        "Alex Greenhalgh",
    ]
    for v in variants:
        text = text.replace(v, f"<strong>{v}</strong>")
    return text


def main():
    want_pdf = "--pdf" in sys.argv

    # ── Load each section from its own file ───────────────────────────────
    data = {}
    for section in SECTIONS:
        path = DATA / f"{section}.yaml"
        with open(path, encoding="utf-8") as f:
            data[section] = yaml.safe_load(f)

    # ── Render HTML ────────────────────────────────────────────────────────
    env = Environment(loader=FileSystemLoader(str(ROOT)))
    env.filters["bold_name"] = bold_name
    template = env.get_template("cv_template.html")
    html = template.render(**data)

    out_html = ROOT / "cv.html"
    out_html.write_text(html, encoding="utf-8")
    print(f"[OK] Generated {out_html}")

    # ── Optionally generate PDF ────────────────────────────────────────────
    if want_pdf:
        try:
            import weasyprint
            out_pdf = ROOT / "CV_AG.pdf"
            weasyprint.HTML(string=html, base_url=str(ROOT)).write_pdf(str(out_pdf))
            print(f"[OK] Generated {out_pdf}")
        except ImportError:
            print(
                "[!] WeasyPrint not installed. Run: pip install weasyprint\n"
                "    Or open cv.html in your browser and use File > Print > Save as PDF."
            )
    else:
        print(
            "    Tip: open cv.html in your browser and File > Print > Save as PDF\n"
            "    Or run: python generate_cv.py --pdf   (requires: pip install weasyprint)"
        )


if __name__ == "__main__":
    main()
