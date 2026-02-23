#!/usr/bin/env python3
"""
Generate cv.html (and optionally CV_AG.pdf) from cv_data.yaml + cv_template.html.

Usage:
    python generate_cv.py           # generates cv.html
    python generate_cv.py --pdf     # also generates CV_AG.pdf via WeasyPrint

Dependencies (install once):
    pip install pyyaml jinja2
    pip install weasyprint          # optional, for --pdf flag
"""

import sys
import yaml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

ROOT = Path(__file__).parent


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

    # ── Load data ──────────────────────────────────────────────────────────
    data_path = ROOT / "cv_data.yaml"
    with open(data_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)

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
