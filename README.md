# The joke about the demo

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/jinan86/the-joke-about-the-demo-20261121-0551/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/jinan86/the-joke-about-the-demo-20261121-0551/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)

A one-line joke about working beside AI coding agents, written by a
small program for the make.fun bounty of the same name.

> My AI agent ships code faster than I can review it, which is fine —
> by demo time, neither of us knows what it does.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the
joke to `entry.txt` in the output directory and checks the gate first:
1 to 280 characters, a single line, not only white space — failing hard
if it ever broke the rule. The output is fully deterministic: every run
writes the exact same bytes.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Competition

Entry for [The joke about the demo](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
on [make.fun](https://make.fun) — $35 in prizes, 20 places paid.

---

Built by [@jinan86](https://github.com/jinan86) for the make.fun bounty.
Join make.fun with referral code `95rs49se`.
