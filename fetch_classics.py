"""Download verified public-domain English editions listed in the manifest.

Usage: python3 fetch_classics.py
The Project Gutenberg files remain intact, including their legal notices.
"""

import hashlib
import json
import time
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DEST = ROOT / "texts" / "gutenberg"
MANIFEST = json.loads((ROOT / "gutenberg-manifest.json").read_text(encoding="utf-8"))


def fetch(identifier, record):
    target = DEST / f"pg{identifier}.txt"
    if target.exists():
        payload = target.read_bytes()
    else:
        request = urllib.request.Request(record["url"], headers={"User-Agent": "HistoricalTextResearch/1.0"})
        last_error = None
        for attempt in range(3):
            try:
                with urllib.request.urlopen(request, timeout=60) as response:
                    payload = response.read()
                break
            except (OSError, TimeoutError) as error:
                last_error = error
                time.sleep(2 ** attempt)
        else:
            raise RuntimeError(f"Could not download Gutenberg #{identifier}") from last_error

    digest = hashlib.sha256(payload).hexdigest()
    if digest != record["sha256"] or len(payload) != record["bytes"]:
        raise ValueError(f"Unexpected bytes in Gutenberg #{identifier}; check the edition or a source update")
    target.write_bytes(payload)
    print(f"Verified #{identifier}: {len(payload)} bytes -> {target.relative_to(ROOT)}", flush=True)


if __name__ == "__main__":
    DEST.mkdir(parents=True, exist_ok=True)
    for book_id, metadata in MANIFEST.items():
        fetch(book_id, metadata)
