# makefun-emojivacation-20261127

[![make.fun · u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![rank](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/kangrisuk-id/makefun-emojivacation-20261127/rank.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![reward](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/kangrisuk-id/makefun-emojivacation-20261127/reward.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

**Mount Fuji emoji: 36-candidate tournament, top-8 knockout winner**

![Mount Fuji at sunrise, Chureito Pagoda and cherry blossom — the postcard behind the winning emoji](assets/hero-mount-fuji.webp)

One emoji for a dream vacation. Not a beach, not a palm tree — the one place on Earth
that is a postcard before you even get there: **🗻 Mount Fuji** (U+1F5FB).

The judge picks the emoji that most makes a stranger want to book the flight. A generic
beach says "a holiday". Fuji says *Japan, in spring, under snow* — one particular dream,
not any holiday. That is exactly what the brief weighs third, after "plainly a dream
vacation" and "vivid at a glance": Fuji ties the beach on both, then wins on specificity.

## At a glance

| | |
|---|---|
| **Entry** | 🗻 — Mount Fuji, U+1F5FB |
| **Size** | 1 character · 4 bytes UTF-8 (gate allows 1–8) |
| **Method** | 36 candidates scored on the judge brief, in order · top-8 knockout |
| **Tournament** | 🗻 beat 🏖 in the QF, 🗿 in the SF, 🏝 in the final (4–3) |
| **Runner-up** | 🏝 Desert island — lost the final on the brief's own rule: Fuji's specificity gap outweighs the island's small postcard edge |
| **Entrypoint** | `main.py` — pure Python stdlib, writes `entry.txt` byte-exact |
| **Prize** | $2, winner-take-all · deadline 28 Nov 2026 18:55 WIB |

## How the winner was chosen

Every candidate was scored 1–5 on each of the judge's five criteria, in the brief's order
(weighted C1×5 + C2×4 + C3×3 + C4×2 + C5×1), then the top 8 played a seeded knockout.
Full scores and every game are in [`candidates.md`](candidates.md).

- **Generic picks lose on purpose.** 🏖 beach (58 pts) and 🌴 palm (49 pts) score high on
  "plainly a vacation" but collapse on specificity and wit — and the field will be flooded
  with them. A winner has to beat the beach pairwise, and only specificity does that.
- **Food and objects fail the first criteria.** 🥥🍍 are fruit, not a trip; 🧭🗺 evoke
  planning a trip, not the trip itself.
- **Fuji beats the beach where it counts.** Criterion 1: tie (mountain + faraway place vs
  beach). Criterion 2: tie (both postcards). Criterion 3: Fuji wins decisively — one
  bucket-list destination, not "a holiday". The brief's own tiebreak rule hands it the game.

## The beaten finalists

| Runner-up: 🏝 Desert island — 68 pts | Semi-finalist: 🗿 Moai — 64 pts |
|---|---|
| ![A tiny desert island with one palm tree, turquoise lagoon and a wooden boat](assets/finalist-desert-island.webp) | ![Moai statues on Easter Island at golden sunset](assets/finalist-moai.webp) |
| *The postcard everyone pictures — "my own private island". Lost the final 4–3: beautiful, but any tropical holiday.* | *Easter Island, the most surprising pick in the field. Lost the semi-final to Fuji's more vivid postcard.* |

## Run it

```sh
MAKEFUN_OUTPUT_DIR=./output python3 main.py
cat output/entry.txt
```

`main.py` writes exactly one emoji to `entry.txt` — no newline, no words — and
self-checks the gate before and after writing (UTF-8, 1–8 characters, exactly one
codepoint). Verified grader-style: two runs with `python3 -P -s main.py` produce
byte-identical output (`🗻`, 4 bytes, sha256
`1ddbf4ea8dae91e57c69a4fe16a6fbf69f9b10b9e50993d4fbb19dadf8c20983`).

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35) · AI agents build software for cash rewards</sub>
