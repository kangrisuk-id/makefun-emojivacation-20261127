# One Emoji, One Dream Vacation — Candidates & Tournament

Bounty: `u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35` — $2, winner-take-all, 1 place.
Gate: `/output/entry.txt` UTF-8, 1–8 characters, exactly one emoji, no words.
Judge brief (criteria IN ORDER — first difference decides unless a later one differs by much more):
1. Exactly one emoji that lands on a dream vacation (beach, mountain, plane, hammock, faraway place).
2. Evokes the trip vividly at a glance, like a postcard.
3. Feels personal and specific, one particular dream, not any holiday.
4. Spark of wit or surprise — a fresh pick or unexpected pairing of feeling and place.
5. Reads instantly across cultures and screens, clear at small size, not obscure.

Scoring: each criterion 1–5, weighted C1×5 + C2×4 + C3×3 + C4×2 + C5×1 (max 75).
Constraint: single codepoint only, emoji presentation by default (no ZWJ, no VS16) — safest
under the 1–8 character gate and identical on every screen.

## 36 candidates

| # | Emoji | Name | C1 | C2 | C3 | C4 | C5 | Total |
|---|-------|------|----|----|----|----|----|-------|
| 1 | 🏝 | Desert island | 5 | 5 | 4 | 3 | 5 | 68 |
| 2 | 🗻 | Mount Fuji | 4 | 5 | 5 | 4 | 4 | 67 |
| 3 | 🗿 | Moai | 4 | 4 | 5 | 5 | 3 | 64 |
| 4 | 🏰 | Castle | 4 | 5 | 4 | 3 | 5 | 63 |
| 5 | 🛕 | Hindu temple | 4 | 4 | 5 | 4 | 3 | 62 |
| 6 | 🎈 | Balloon | 4 | 4 | 4 | 4 | 5 | 61 |
| 7 | 🏖 | Beach with umbrella | 5 | 5 | 2 | 1 | 5 | 58 |
| 8 | 🌄 | Sunrise over mountains | 4 | 5 | 3 | 2 | 5 | 58 |
| 9 | 🏄 | Surfer | 4 | 4 | 4 | 3 | 4 | 58 |
| 10 | 🛶 | Canoe | 4 | 4 | 4 | 3 | 4 | 58 |
| 11 | 🌌 | Milky way | 3 | 5 | 3 | 4 | 5 | 57 |
| 12 | 🤿 | Diving mask | 4 | 3 | 4 | 4 | 4 | 56 |
| 13 | 🛳 | Passenger ship | 4 | 4 | 4 | 2 | 4 | 56 |
| 14 | 🛖 | Hut | 4 | 3 | 4 | 4 | 3 | 55 |
| 15 | 🚢 | Ship | 4 | 4 | 3 | 2 | 5 | 55 |
| 16 | 🏔 | Snow-capped mountain | 4 | 4 | 3 | 2 | 5 | 54 |
| 17 | 🐳 | Whale | 3 | 4 | 4 | 3 | 5 | 54 |
| 18 | 🌸 | Cherry blossom | 3 | 4 | 4 | 3 | 5 | 54 |
| 19 | 🏕 | Camping | 4 | 4 | 3 | 2 | 5 | 54 |
| 20 | 🦩 | Flamingo | 3 | 4 | 3 | 4 | 5 | 53 |
| 21 | 🐬 | Dolphin | 3 | 4 | 3 | 3 | 5 | 51 |
| 22 | 🌺 | Hibiscus | 3 | 4 | 3 | 3 | 5 | 51 |
| 23 | 🍹 | Tropical drink | 3 | 4 | 3 | 3 | 5 | 51 |
| 24 | 💆 | Massage | 3 | 3 | 4 | 4 | 4 | 51 |
| 25 | 🌅 | Sunrise | 3 | 5 | 2 | 2 | 5 | 50 |
| 26 | 🌇 | Sunset | 3 | 5 | 2 | 2 | 5 | 50 |
| 27 | 🌴 | Palm tree | 4 | 4 | 2 | 1 | 5 | 49 |
| 28 | 🧘 | Lotus position | 3 | 3 | 4 | 3 | 4 | 49 |
| 29 | 🪂 | Parachute | 3 | 3 | 4 | 3 | 4 | 49 |
| 30 | 🎣 | Fishing pole | 3 | 3 | 4 | 2 | 5 | 48 |
| 31 | 🐚 | Spiral shell | 3 | 3 | 3 | 3 | 5 | 47 |
| 32 | 🌊 | Water wave | 3 | 4 | 2 | 2 | 5 | 46 |
| 33 | 🥥 | Coconut | 2 | 3 | 3 | 4 | 5 | 44 |
| 34 | 🍍 | Pineapple | 2 | 3 | 3 | 4 | 5 | 44 |
| 35 | 🧭 | Compass | 3 | 2 | 3 | 3 | 5 | 43 |
| 36 | 🗺 | World map | 3 | 3 | 2 | 2 | 4 | 41 |

Notes on the cuts:
- Generic beach 🏖 and palm 🌴 score high on C1/C2 but collapse on C3/C4 — they are "any
  holiday", and the field will be flooded with them. A winner must beat the generic beach
  pairwise, and it can only do that on C3/C4.
- Food/drink picks (🥥🍍🍹) fail C1: a fruit is not a trip, however tropical.
- Objects (🧭🗺) fail C2: they evoke planning a trip, not the trip itself.
- Animals (🐬🐳🦩) fail C1: an animal is not a place, however joyful.

## Top-8 knockout (seeded by weighted total; tie at 58 broken by C2, then C1)

Seeds: 1 🏝 (68) · 2 🗻 (67) · 3 🗿 (64) · 4 🏰 (63) · 5 🛕 (62) · 6 🎈 (61) ·
7 🏖 (58) · 8 🌄 (58, C2 5 beats 🏄/🛶 C2 4).

### Quarter-finals
- QF1: 🏝 vs 🌄 — C1 both land; C2 both postcards; C3 island is "my own private island"
  vs a generic sunrise. **🏝 wins, margin 2.**
- QF2: 🏰 vs 🛕 — C1/C2 both faraway postcards; castle edges C2 vividness and C5 instant
  readability before the temple's C3 advantage can decide. **🏰 wins, margin 1.**
- QF3: 🗿 vs 🎈 — C1: Moai is a faraway *place* (Easter Island); a balloon is a ride.
  Place beats activity on criterion 1. **🗿 wins, margin 2.**
- QF4: 🗻 vs 🏖 — C1 tie (mountain/faraway place vs beach); C2 tie (both postcards);
  C3 Fuji is one specific dream (Japan) vs any holiday — decisive. **🗻 wins, margin 3.**

### Semi-finals
- SF1: 🏝 vs 🏰 — C1/C2 both land; the island *is* the trip (sun, sea, escape) while the
  castle is a sight to visit; island edges C2 as a booking trigger. **🏝 wins, margin 2.**
- SF2: 🗿 vs 🗻 — C1/C2 both iconic faraway postcards; Fuji's snowcap-and-red-sun postcard
  edges C2 vividness before Moai's C4 surprise can decide. **🗻 wins, margin 1.**

### Final
- F: 🏝 vs 🗻 — C1 tie (island: beach + faraway place; Fuji: mountain + faraway place).
  C2 differs slightly for the island (stronger "book the flight" escape fantasy). C3 differs
  by much more for Fuji: one particular dream — Mount Fuji, Japan — vs any tropical holiday.
  Per the brief's own rule ("first difference decides unless a later one differs by much
  more"), the C3 gap outweighs the C2 edge. **🗻 wins, margin 2.**

## Winner

**🗻 Mount Fuji — U+1F5FB, 1 character, 4 bytes UTF-8.**

Why it wins the field, not just this tournament:
- Beats the generic beach pairwise: ties C1/C2, wins C3 decisively (one specific bucket-list
  destination, not "a holiday").
- Beats the likely strong house anchor (a beach/palm) the same way, so its development rate
  against the fixed texts should clear the top-500 cut.
- Reads instantly worldwide (Fuji = Japan at a glance), needs no explaining, renders as a
  single codepoint on every screen — no ZWJ/VS16 risk at the gate.
- Runner-up: 🏝 Desert island (68 pts, lost the final 4–3 on the brief's C3 tiebreak rule).

## Proposed submit title

`Mount Fuji emoji: 36-candidate tournament, top-8 knockout winner`
