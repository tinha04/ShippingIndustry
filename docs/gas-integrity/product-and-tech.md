# Gas Detection Integrity: Product and Technology

[Back to README](../../README.md) · [Product](product-and-tech.md) · [Market](market.md) · [Competition](competition.md) · [Risks](risks.md) · [Build plan](build-plan.md) · [Evidence](evidence.md) · [YC review](yc-review.md)

**Tier:** Exploring; bridge for reactor monitoring and candidate future project (added 2026-10-07). **YC lens:** 23/35, the highest in this repo ([portfolio](../portfolio.md)). Numbers in brackets are [evidence](evidence.md) rows; M rows are in [monitoring evidence](../monitoring/evidence.md).

## 1. One line

A maker neutral add on that reads a ship's fixed gas detection system, guides and records every test, spots drifting or dead sensors between tests, and produces a signed record that port inspectors, class, vetting inspectors, insurers and ports accept. Gas fueled ships and gas carriers first; radiation monitors on nuclear ships later.

## 2. How it is done today

| Step | Today | What goes wrong |
|---|---|---|
| Design | The yard installs one maker's fixed system (Consilium, Autronica, Dräger, Hanla IMS and others) to class rules [26] | Each maker's tools only see its own system |
| Monthly function test | Crew apply span gas to each sensor and write results in a paper log or the planned maintenance system [7] | Wrong span gas, readings outside tolerance not caught, steps skipped [1, 3] |
| Calibration | Crew or a service engineer every 3 to 12 months [7] | Drift between visits goes unseen [1] |
| Inspection | Port state control, class, vetting and terminal inspectors witness tests and read the logs [1, 8] | Problems found at the inspection mean delays, deficiencies or detention [1, 3, 4] |
| New fuels | Ammonia adds ppm toxic alarms (25, 110, 220 ppm) and toxic safety zones [9, 20] | Electrochemical sensors age and drift; crews have little experience with them [6, 11] |

**What the evidence says:** drift and wrong test gas are the recurring findings [1, 3]; the record matters as much as the reading [7]; offshore data show fixed systems miss 40% to 48.5% of releases [5], though that is coverage as well as drift.

## 3. Is it doable and does it solve a pain?

| Question | Answer | Evidence |
|---|---|---|
| Real pain? | **Yes, verified but dated** | Coast Guard alert, P&I circular, flag warning, higher detention rate for gas carriers [1 to 4]. Newer data needed |
| Technically doable? | **Yes** | Panels expose alarms and readings over standard outputs (Modbus, 4 to 20 mA); remote calibration over HART or Modbus already exists on land [25]. Our box sits in a safe area and reads only, so the hazardous area rules stay with the maker's sensors (K) |
| Legally deployable? | **Likely, with class input** | Read only tap of a class approved safety system needs class acceptance; automatic test gas valves change the system and need approval (risk GI2) |
| Open gap? | **Yes, narrow** | Portable detector clouds exist [22 to 24]; fixed remote calibration exists inside single brands on land [25]; no maker neutral service for fixed systems on ships found [29] |
| Who pays? | **Unproven** | Ship managers and owners of gas fueled ships and gas carriers; maybe charterers and terminals through vetting |

## 4. Product (H)

| Part | What it does | Why it matters |
|---|---|---|
| **Read only data box** | Reads the fixed gas panel's output (Modbus RTU or TCP, or isolated 4 to 20 mA taps); stores and signs readings; works offline; syncs through the ship's link | Our hardware and embedded skills; no hazardous area certification because it sits in a safe area (K) |
| **Guided test app** | Walks the officer through each monthly test; checks the span gas against the sensor type before the test (catches the inert gas on catalytic sensor mistake [1]); records response time and reading per sensor | Turns the Coast Guard's top findings into checks that run before the inspector arrives |
| **Drift watch** | Tracks each sensor's zero, response and noise between tests; compares like sensors across the fleet; flags drift and near end of life sensors | Finds problems between tests instead of at the inspection |
| **Signed record and reports** | Tamper evident log of every test and calibration; one click report for port state control, class, vetting and terminals; export to the planned maintenance system | "An undocumented calibration is no calibration" [7] |
| **Fleet view** | Ship manager sees every ship's detector health in one place | Ship managers run many ships with many makers' systems |
| **Port and fuel supplier share (later)** | Detector health summary sent ahead of a bunkering or port call | Ports drawing toxic zones for ammonia [19, 20] |
| **Automatic test gas modules (later)** | Valve and small cylinder at critical points so tests run remotely | Needs class approval; phase 2 |
| **Radiation monitors (future)** | Same integrity layer for radiation monitors on floating plants and nuclear ships | The bridge to [reactor monitoring](../monitoring/product-and-tech.md) |

**Pricing hypothesis (E):** $8K to $20K per ship a year, hardware included; free 3 month pilot on one ship.

**Tech (K):** embedded Linux box, Modbus and isolated analog inputs, secure element signing (same as the [monitoring bench box](../monitoring/build-plan.md)), tablet app, fleet web view; tolerance rules from each maker's manual stored as data; drift detection with simple statistics first, machine learning only if needed.

## 5. Boundary

- Read only. Never silences, resets or changes alarm settings on the maker's system.
- Advisory. The maker's system stays the approved safety system; our record supports, not replaces, the crew's checks.
- No hazardous area equipment in phase 1.

## 6. Link to the rest of this repo

- **Monitoring:** same box, same signed record, same buyers (ports, class, insurers). Proves the product at sea years before reactors sail.
- **Readiness:** detector health is one line in a port's readiness file for new fuels.
- **Insurance:** an operating record of safety sensors is the data insurers say they lack for new fuels [12].
- **Idea Lab:** overlaps with the battery fire tag's gas sensing skills, but serves a different buyer (shipowners' fixed systems, not cargo boxes). Where it should live is a decision for Tin.
