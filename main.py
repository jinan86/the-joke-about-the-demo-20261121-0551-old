"""Entry for make.fun "The joke about the demo" (the-joke-about-the-demo-20261121-0551).

Writes one one-line joke about working beside AI coding agents to
entry.txt in the output directory (/output in the grading sandbox,
or $MAKEFUN_OUTPUT_DIR when set for a local run).

Standard library only, no network, fully deterministic: the same
text is written on every run.
"""

import os

JOKE = (
    "My AI agent ships code faster than I can review it, which is fine "
    "\u2014 by demo time, neither of us knows what it does."
)


def main() -> None:
    # Gate, same as the sealed scorer's: 1 to 280 Unicode code points,
    # and not only white space. Fail hard instead of writing bad output.
    if not 1 <= len(JOKE) <= 280:
        raise SystemExit(f"joke is {len(JOKE)} characters, must be 1-280")
    if not JOKE.strip():
        raise SystemExit("joke is only white space")
    if "\n" in JOKE:
        raise SystemExit("joke must be a single line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
