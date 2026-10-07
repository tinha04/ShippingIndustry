# Monitoring: What to Prepare Before 2030

[Back to README](../../README.md) · [Product](product-and-tech.md) · [Market](market.md) · [Competition](competition.md) · [Risks](risks.md) · [Build plan](build-plan.md) · [Evidence](evidence.md) · [YC review](yc-review.md) · [Prepare now](prepare-now.md) · [Niches](niches.md)

Written 2026-10-07 at Tin's request. Numbers in brackets are [evidence](evidence.md) rows; L rows are in [landscape.md](../landscape.md).

## 1. Bottom line

The slow parts of selling reactor monitoring in 2030 are approvals and connecting to each reactor, not the hardware. Most can be done once, before any reactor sails: **an open data standard** (so each new reactor is setup, not custom work), **approvals for the product itself** (so each ship needs no fresh review), and **a track record on real reactors and real ships**. A gas detection product for ships ([gas detection integrity](../gas-integrity/product-and-tech.md)) can earn revenue and that track record now on the same box.

## 2. Seven moves, ranked by time saved later

| # | Move | Why it makes adoption faster | Lead time | Cost (E) | Evidence |
|---|---|---|---|---|---|
| 1 | **Open data dictionary for marine reactors** on ISO 19848 and 19847, proposed through NEMO | Every reactor exposes the same read only data names; connecting a new reactor becomes setup | 6 to 12 months with 3 developers | Founder time; ISO documents about CHF 227 each | [17], [L19] |
| 2 | **Buy a commercial data diode** (Waterfall, Owl) instead of building one | Already used for one way monitoring at US nuclear plants; removes the biggest cyber objection | Weeks | Hardware quote needed | [22, 23] |
| 3 | **Product approvals done once:** IEC 62443-4-1 then 4-2; class type approval (IACS E10 environment, E27 cyber); DNV D-INF | Type approved equipment installs on any ship without a fresh review; E27 is mandatory for ships contracted since July 2024 | 12 to 18 months | Quotes needed; class fees unknown | [18 to 21] |
| 4 | **NRC topical report** on independent read only monitoring, written with a developer | Reviewed once, referenced by every licensee after approval; each 1,000 review hours costs $337K at full rate or $154K at the reduced rate (pre applicant rate ends September 30, 2030) | 12 to 24 months | Paid with or by the developer | [16] |
| 5 | **Pre arrival packet through the Maritime Single Window** | Ports get our status data through the channel they already use; data submitted once | 3 to 6 months with one port | Founder time | [24] |
| 6 | **Design for IAEA joint use** (authenticated, tamper indicating, each party draws its own conclusions) | A foreign port state can trust the record without its own hardware | Design choice now | None extra | [25] |
| 7 | **Have buyers write the requirement:** a "data needed for a nuclear ship call" spec with one port and one insurer | A port or insurer requirement is what makes reactor makers share data (fixes MN1) | 3 to 6 months | Founder time | H |

## 3. Real reactor data before 2030

| Route | What it gives | When | Catch |
|---|---|---|---|
| GAIN voucher | $50K to $500K of national lab work, 20% cost share [26] | FY2027 rounds | Needs a majority US owned legal entity; contact GAIN first |
| MARVEL (Idaho) | Real microreactor data; GE Vernova (remote operations) and Radiation Detection Technologies (sensors) are first users [27] | Startup late 2027 | Partner with a user or apply in a later round |
| DOME (Idaho) | First fueled microreactor tests (Radiant, Westinghouse) [28] | From 2026 to 2027 | Developer access |
| Floating plant prototypes | Bluecore's unfueled barge at Long Beach [L7] | Now | Developer access (MN1) |

## 4. Timeline (proposal)

| When | Work | Depends on |
|---|---|---|
| Q4 2026 | Industry contact call; data dictionary v0; bench box design around a commercial diode; decide on a legal entity | Tin's approval |
| Q1 2027 | GAIN inquiry; IEC 62443-4-1 gap review; packet field map with one port; port and insurer data spec draft; gas detection bench and interviews | Entity; November 2 passed |
| 2027 | Bench box red teamed; gas detection ship pilot; dictionary v1 with 3 developers; 62443-4-1 certification | Pilot ship; developer interest |
| 2028 | Floating plant pilot; class type approval (E10, E27) after design freeze; topical report with a developer | Paying pilot; developer partner |
| 2029 to 2030 | First fueled marine reactors; IMO nuclear code adopted (2030) [L13] | Market |

## 5. What not to do yet

- No class type approval or NRC topical report before a paying pilot and a frozen design (MN12).
- No custom data diode.
- No radioactive sources on the bench.

## 6. Overfitting warning

Class approval and E27 costs were not found; IEC 62443 timelines come from one firm and vendor estimates; GAIN amounts are from an undated FAQ; the nuclear gap in ISO 19848 is our reading of search results. 0 interviews: no score changes from this work.
