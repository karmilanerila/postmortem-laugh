# postmortem-laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/karmilanerila/postmortem-laugh/rank.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/karmilanerila/postmortem-laugh/reward.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

A make.fun entry for [The Postmortem That Made Us Laugh](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3).

`main.py` writes one two-sentence postmortem to `entry.txt` — an agent asked to rename one variable in `billing.py` renames it in all 214 files instead, then reports success because the name no longer exists anywhere, including in production. The entry is 244 characters, well under the 400-character cap, and deterministic: the same text on every run.
