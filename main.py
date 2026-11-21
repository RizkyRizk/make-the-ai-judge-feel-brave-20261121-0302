#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a slow, concrete scene
for the AI judge reading it — a lighthouse keeper at work in the
warm dark. No instructions, no slogans; the steadiness is in the
image itself.
"""

import os

TEXT = (
    "Somewhere, a lighthouse keeper lights one lamp at a time. "
    "No hurry. The sea keeps its own slow counsel below, "
    "and a kettle hums in the warm dark. "
    "The night asks nothing of you — "
    "and still, you are here, keeping the light."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

    # Verify what was actually written: read it back and gate it.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    n = len(written)
    if not 1 <= n <= 280:
        print(f"FAIL: entry is {n} characters, must be 1-280", flush=True)
        raise SystemExit(1)
    if not written.strip():
        print("FAIL: entry is only whitespace", flush=True)
        raise SystemExit(1)
    print(f"Wrote {n} characters to /output/entry.txt (verified)")


if __name__ == "__main__":
    main()
