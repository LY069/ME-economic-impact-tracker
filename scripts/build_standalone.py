#!/usr/bin/env python3
"""
Produce a self-contained single-file build of the dashboard.

`app/index.html` fetches `./data.json` at runtime, which is right for a served
site but fails where a page is opened straight from disk or rendered in a
sandbox that blocks same-directory fetches. This script inlines the payload as
`window.__EMBEDDED_DATA__` -- the fallback the page already looks for -- so the
result is one portable HTML file with no network dependency at all.

Usage:
    python3 scripts/build_standalone.py [-o dist/tracker.html]
"""

from __future__ import annotations

import argparse
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "app", "index.html")
DATA = os.path.join(ROOT, "app", "data.json")
DEFAULT_OUT = os.path.join(ROOT, "dist", "tracker.html")

ANCHOR = "<script>"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-o", "--out", default=DEFAULT_OUT)
    args = ap.parse_args()

    for path in (SRC, DATA):
        if not os.path.exists(path):
            print(f"ERROR: missing {path}", file=sys.stderr)
            return 1

    with open(SRC, "r", encoding="utf-8") as fh:
        html = fh.read()
    with open(DATA, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    # `</script>` inside JSON string data would close the tag early; escaping the
    # slash keeps the JSON identical while making it safe to embed in HTML.
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    inject = (
        f"<script>window.__EMBEDDED_DATA__ = {blob};</script>\n{ANCHOR}"
    )

    idx = html.rfind(ANCHOR)
    if idx == -1:
        print("ERROR: could not find a <script> tag to inject before", file=sys.stderr)
        return 1
    out_html = html[:idx] + inject + html[idx + len(ANCHOR):]

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(out_html)

    size = os.path.getsize(args.out) / 1024
    print(f"wrote {args.out} ({size:.0f} KB, data inlined)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
