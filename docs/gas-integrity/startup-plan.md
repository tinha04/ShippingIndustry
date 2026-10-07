# Gas Detection Integrity: Startup Plan (YC Path)

[Back to README](../../README.md) · [Startup plan](startup-plan.md) · [YC application](yc-application.md) · [Product](product-and-tech.md) · [Market](market.md) · [Competition](competition.md) · [Risks](risks.md) · [Build plan](build-plan.md) · [Build guide](build-guide.md) · [Evidence](evidence.md) · [YC review](yc-review.md)

**Status:** Lead product and YC pitch (Tin's decision, 2026-10-07). YC lens 23/35. Validation only until after Kairos's YC application (November 2); building starts November 3. Numbers in brackets are [evidence](evidence.md) rows.

## 1. The company in one page

| Item | Plan |
|---|---|
| One line | Proof that ship gas detectors work |
| Problem | Fixed gas sensors on gas fueled ships and gas carriers drift and get tested with the wrong gas; inspectors find it, and ships face delays and detention [1 to 4]. New fuels (ammonia) make it a toxic safety issue [9, 10] |
| Product | A read only box on any maker's gas panel, a guided test app, drift warnings, and a signed record inspectors accept ([product](product-and-tech.md)) |
| First customer | A ship manager running gas carriers or LNG fueled ships with systems from 2 or more makers |
| Offer | Free 3 month pilot on one ship, then $8K to $20K per ship a year (E) |
| Why now | About 1,100 gas capable ships in service and 1,000 on order; first ammonia ships in 2026; fuel records going digital [13 to 21] |
| Moat | Maker neutral fleet data on how sensors drift (more ships, better warnings); a record inspectors and insurers learn to trust; the same box and record carry into reactor monitoring |
| Vision | Every safety sensor on every ship has a record that ports, class and insurers trust: gas detectors now, radiation monitors and ship reactors next ([monitoring](../monitoring/product-and-tech.md)) |

## 2. Beachhead

| Segment | Ships (V or E) | Why first | Why not first |
|---|---|---|---|
| **LNG carriers and LNG fueled ships run by third party managers** | About 730 LNG carriers [17]; 942 LNG capable ships [13] | Most fixed detection, most inspections, the Coast Guard findings came from LNG carriers [1] | Big managers move slowly |
| Methanol and ammonia fueled ships | 159 plus 5 in service [14, 15] | Newest systems, least crew experience, toxic alarms [9] | Few ships |
| LPG carriers | Over 1,000 (K, unverified) | Similar systems | Unverified count |
| Tankers and chemical carriers | Several thousand (K) | Large fleet | Different detection setups; later |

## 3. Minimum product (what the pilot ship gets)

1. One data box reading the panel's existing output (Modbus or isolated 4 to 20 mA), read only.
2. The guided monthly test on a tablet, with span gas checks.
3. A weekly drift report to the technical superintendent.
4. A one click inspector report.

Not in the minimum product: automatic test gas valves, port sharing, fleet benchmarks, radiation monitors.

## 4. Timing against Kairos

YC takes one application per batch. Kairos uses Winter 2027 (deadline November 2; decisions about December 11). Spring and Summer 2027 deadlines are not announced; past cycles and projections point to about February and May 2027; YC's application also offers early decision for "a batch after Winter 2027" (V, third party sources; check ycombinator.com/apply).

| If Kairos... | Then this company |
|---|---|
| Is accepted for Winter 2027 | Founders are full time on Kairos; this stays in validation, or moves to a separate team. Q10 (full time) cannot be answered yes for both |
| Is not accepted, or the founders choose this | Apply for Spring 2027 (about February) with interviews, bench results and a signed pilot, or Summer 2027 (about May) with pilot data |

**Entity (Tin's decision):** form the company when applying (YC application or a DOE GAIN voucher, whichever comes first). A Delaware C corporation is the usual choice for US venture backed startups (K); confirm with counsel.

## 5. Milestones to the application

| By | Milestone | Metric | Feeds YC question |
|---|---|---|---|
| November 2026 | Industry contact call; 8 ship manager interviews; 2024 to 2026 inspection data on gas detection; one class society answer on read only taps | 8 calls logged; 3 managers name a price; recent finding rate known | Q25, Q27, Q37, Q38 |
| December 2026 | Bench rig built ([build guide](build-guide.md)); seeded fault test; guided test app v0 | 9 of 10 faults caught; 0 false "healthy"; test time vs paper | Q14, Q15, Q18 |
| January 2027 | Pilot ship signed (letter of intent); advisor from ship management or port state control | 1 LOI; 1 advisor | Q18, Q21, Q37 |
| February 2027 | Spring 2027 application, if the founders choose this company | Video of bench catching faults; pilot LOI; interview quotes | All |
| March to May 2027 | Pilot running; first paid conversion | First faults caught at sea; first paid ship | Q21, Q22 |

## 6. Demo Day targets (about 3 months after acceptance)

1. 5 ships under paid contract, about $40K to $100K annual run rate at $8K to $20K per ship (E).
2. At least one inspection or vetting passed using our record.
3. Drift caught before a test on at least one ship.
4. A second manager in a paid pilot.
5. Nuclear path started: data dictionary v0 shared with a NEMO working group ([prepare now](../monitoring/prepare-now.md)).

## 7. What partners will attack, and our answer

| Attack | Answer | Risk left |
|---|---|---|
| "Is this a venture scale company?" | Gas detection alone is tens of millions a year; the same record extends to tankers, then radiation monitors and ship reactors, where independent records will be required | **High** |
| "Your evidence is from 2020" | We bring 2024 to 2026 inspection data and manager quotes before applying (GI5) | **High until done** |
| "Consilium will build this" | For its own panels; managers run several makers (GI1) | Medium |
| "Class won't let you connect" | Read only through existing outputs; written class answer before the pilot (GI2) | Medium |
| "Why you?" | Hardware, embedded firmware, gas sensing; an industry contact; an advisor from ship management before applying | Medium |

## 8. Kill or pivot

Kill criteria are in [risks](risks.md#2-kill-criteria). If managers will not pay but class and insurers want the record, pivot to selling the record to insurers or makers as a license. If gas detection findings turn out rare, fold the box back into reactor monitoring and keep readiness as the near term product.

## 9. Overfitting warning

0 interviews, 0 users. Prices, adoption, YC dates and the Demo Day revenue target are estimates. The 23/35 score is one research pass.
