# Gas Detection Integrity: YC Review

[Back to README](../../README.md) · [Startup plan](startup-plan.md) · [YC application](yc-application.md) · [Product](product-and-tech.md) · [Market](market.md) · [Competition](competition.md) · [Risks](risks.md) · [Build plan](build-plan.md) · [Build guide](build-guide.md) · [Evidence](evidence.md) · [YC review](yc-review.md) · [All areas](../yc-review.md)

**Lead product and YC pitch (Tin's decision). YC lens 23/35, the highest in this repo (first round, 2026-10-07).** Draft answers: [YC application](yc-application.md). Ships need it today, it fits our hardware skills, and it proves the record that reactor monitoring needs later. Held back by a mid size market, dated problem data and maker or class gatekeeping. Numbers in brackets are [evidence](evidence.md) rows.

## 1. YC lens

| Criterion | Score | Why |
|---|---|---|
| Problem | 4 | Coast Guard alert, P&I circular, flag warning; delays and detentions [1 to 4]; ammonia toxic alarms from 25 ppm [9]. Not 5: data are from 2019 to 2020 and no loss tied directly to drift found |
| Market | 3 | About $12M to $33M a year at modest adoption, more with tankers and the nuclear step ([market](market.md#3-bottom-up-e)) |
| Insight | 3 | Inspectors judge the record, not the sensor [7]; the top findings (drift, wrong span gas [1]) can be caught at test time; one neutral layer serves gas now and radiation later |
| Differentiation | 3 | Portable clouds and single brand land tools exist [22 to 25]; no neutral fixed system service at sea found [29] |
| Founder fit | 3 | Hardware, embedded firmware, gas sensing work in the Idea Lab; no shipping network beyond our contact |
| Speed to proof | 3 | Bench with seeded faults in weeks; a ship pilot needs an owner and a class answer (months) |
| Why now | 4 | LNG, methanol and ammonia fleets growing; first ammonia ships and refueling trials in 2026; fuel records going digital [13 to 21] |

## 2. The idea questions

| # | Draft answer | Grade | Gap |
|---|---|---|---|
| 12 | Name not chosen | Missing | |
| 13 | "Proof that ship gas detectors work" (34 characters) | **Strong** | |
| 14 | None | Missing | Bench video: drift and wrong test gas caught |
| 15 | A maker neutral add on that reads a ship's fixed gas detection system, guides and records each test, spots drifting sensors, and produces a signed record inspectors accept | OK | No demo |
| 16, 17 | Near a gas carrier or LNG fueled fleet manager (Houston, Singapore, Rotterdam) | Weak | Choose after interviews |
| 18 | Research done; build plan ready; 0 interviews | **Weak** | 8 interviews, bench faults test |
| 20 | Embedded Linux, Modbus and isolated analog inputs, secure element signing, tablet app, fleet web view | **Strong** | |
| 21, 22 | No users, no revenue | Missing | |
| 25 | Coast Guard found out of tolerance sensors and wrong span gas on LNG carriers, delaying cargo work [1]; gas carriers detained more often in one sector [4]; ammonia ships arriving [18]. Domain: gas sensing hardware | OK | Recent data, buyer quotes |
| 26 | Consilium, Dräger, Autronica (own systems); iNet, Teledyne, Blackline (portables); MSA, General Monitors (single brand remote calibration on land); Ofiniti (bunkering). **Insight:** no one keeps a neutral, signed health record for fixed systems at sea, where inspectors look | OK | Confirm no maker offers it |
| 27 | $8K to $20K per ship a year; $12M to $33M a year at modest adoption (E) | Weak | Price unproven (GI4) |
| 28 | Hard tech, maritime, climate, industrial safety | Strong | |
| 29 | Port readiness, reactor monitoring, nuclear insurance; Kairos; the Idea Lab ideas | Strong | |
| 36 | Insight as Q26; why now: new fuel fleets and ammonia in 2026 | **Strong** | |
| 37 | A ship manager running gas carriers or LNG fueled ships with mixed makers; free 3 month pilot, then per ship | OK | No conversation yet |
| 38 | Managers find maintenance logs and annual service good enough (GI4). Know within 3 months from 8 interviews | **Strong** | |
| 39 | Makers serve their own systems; managers run several makers; a neutral record must come from outside | OK | GI1 |
| 40 | 5 ships under contract; seeded fault results; one inspection passed using our record | Weak | |

**Count:** 6 Strong, 5 OK, 4 Weak, 3 Missing (18 rows; some rows cover two questions).

## 3. Partner interview stress test

| Attack | Answer | Risk left |
|---|---|---|
| "Consilium or Dräger will just add this" | For their own systems. Managers run several makers; neutrality is the product | Medium (GI1) |
| "Is this a big company?" | Gas detection alone is tens of millions a year; the same record serves tankers, then radiation monitors and reactor monitoring | **High** |
| "Those alerts are from 2020" | Correct; we will bring 2024 to 2026 inspection data | **High (GI5)** |
| "Class won't let you connect" | Read only through existing outputs; we ask class before the pilot | Medium (GI2) |
| "Crews hate new tools" | It has to make the monthly test faster than paper or it fails | Medium (GI8) |

## 4. What moves the rank

| Milestone | Grade change |
|---|---|
| 3 managers name a price | Q27, Q37 to OK or Strong; market and problem confirmed |
| Bench catches 9 of 10 seeded faults | Q14, Q15 to Strong |
| Recent inspection data show gas detection findings are common | Problem to 5 |
| A paid ship pilot | Progress no longer empty; could become the lead product |
