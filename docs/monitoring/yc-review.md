# Monitoring: YC Review

[Back to README](../../README.md) · [Product](product-and-tech.md) · [Market](market.md) · [Competition](competition.md) · [Risks](risks.md) · [Build plan](build-plan.md) · [Evidence](evidence.md) · [YC review](yc-review.md) · [Prepare now](prepare-now.md) · [Niches](niches.md) · [All areas](../yc-review.md)

**Rank 3 of 4. YC lens 20/35 (first round).** Best founder fit of the three (hardware and embedded firmware), but demand starts only when reactors are fueled, and reactor makers hold the data. Numbers in brackets are [evidence](evidence.md) rows; L rows are in [landscape.md](../landscape.md).

## 1. YC lens

| Criterion | Score | Why |
|---|---|---|
| Problem | 3 | Safeguards for moving reactors unsolved [2, 3]; ports and insurers need data [L6]; but no reactor runs at sea yet |
| Market | 3 | About $20M to $60M a year from 50 ships and 20 floating plants; more with larger fleets or land microreactors ([market](market.md#3-bottom-up-e)) |
| Insight | 3 | A moving reactor needs one record that foreign ports, insurers and the IAEA all trust, so independence is the product |
| Differentiation | 2 | No independent product found [15], but makers, Mirion, ship remote operations and cyber firms each cover parts [9 to 14] |
| Founder fit | 3 | Hardware, embedded firmware, signed data and low power design fit; no nuclear quality experience |
| Speed to proof | 2 | Bench box in weeks; proof on a real reactor takes years (MN4) |
| Why now | 4 | NRC Part 57 [1]; IAEA safeguards group [L14]; ship cyber rules [5]; floating plant funding [L7, L8] |

## 2. The idea questions

| # | Draft answer | Grade | Gap |
|---|---|---|---|
| 12 | Name not chosen | Missing | |
| 13 | "Independent monitoring for ship reactors" (40 characters) | **Strong** | |
| 14 | None | Missing | Bench video of a tamper detected record |
| 15 | A sealed, read only data box and software that signs a reactor's radiation, status, location, seals and cyber alerts, and shares it by role with regulators, ports, insurers and the IAEA | OK | No demo |
| 16, 17 | Near our first floating plant pilot (Long Beach) | Weak | Choose after interviews |
| 18 | Research done; build plan ready; 0 interviews | **Weak** | 8 interviews, bench box |
| 20 | Embedded Linux, secure element signing, one way link, GNSS, radiation sensor, role based web views | OK | |
| 21, 22 | No users, no revenue | Missing | |
| 25 | Safeguards "still being studied" [3]; NRC remote monitoring rule [1]; ports need security and emergency data [L6]. Domain: hardware and embedded | OK | Developer quotes |
| 26 | Reactor makers, Mirion, ABB and Kongsberg, Cydome and Xage, Nuclearn. **Insight:** each serves one owner; no one keeps a record that foreign parties trust | OK | MN1 |
| 27 | $0.3M to $1M per reactor a year; $20M to $60M a year from 50 ships and 20 floating plants (E) | Weak | Price unproven (MN10) |
| 28 | Hard tech, energy, security | Strong | |
| 29 | Readiness, insurance, shielding optimizer; Kairos | Strong | |
| 36 | Insight as Q26; why now as section 1 | OK | Depends on fueled reactors |
| 37 | A floating plant developer with an unfueled prototype [L7] | OK | No conversation yet |
| 38 | Makers refuse data access (MN1). Know within 3 months from 5 developer calls | **Strong** | |
| 39 | A maker's own monitoring can't be independent; ports and insurers abroad need a neutral record | OK | MN1, MN2 |
| 40 | Bench box red teamed; one 30 day pilot on a floating plant prototype | Weak | |

**Count:** 4 Strong, 7 OK, 4 Weak, 3 Missing (18 rows; some rows cover two questions).

## 3. Partner interview stress test

| Attack | Answer | Risk left |
|---|---|---|
| "The reactor maker already monitors everything" | For itself. A foreign port and an insurer need a record the maker doesn't control | **High (MN1)** |
| "No reactors at sea for years" | Floating plants first; Bluecore tests monitoring now [L7] | **High (MN4)** |
| "Nuclear certification will kill you" | Stay outside safety systems; certify to ship cyber rules first | High (MN3) |
| "You're an attack path" | One way link, no inbound path, outside red team | Medium (MN6) |
| "Safeguards is the IAEA's job" | We sell to ports and insurers; safeguards can use our data if asked | Medium (MN7) |

## 4. What moves the rank

| Milestone | Grade change |
|---|---|
| 2 developers agree to share read only data | Differentiation to 3; Q26, Q39 to Strong |
| Bench box passes the red team test | Q14, Q15 to Strong |
| An insurer or port says it would require independent records | Problem to 4 |
| 30 day pilot on a floating plant prototype | Progress no longer empty; speed to proof to 3 |
