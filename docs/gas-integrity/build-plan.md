# Gas Detection Integrity: Build and Validation Plan

[Back to README](../../README.md) · [Startup plan](startup-plan.md) · [YC application](yc-application.md) · [Product](product-and-tech.md) · [Market](market.md) · [Competition](competition.md) · [Risks](risks.md) · [Build plan](build-plan.md) · [Build guide](build-guide.md) · [Evidence](evidence.md) · [YC review](yc-review.md)

Owner split: the business co-founder runs interviews; the technical co-founder builds the bench. Validation only until after Kairos's YC application (November 2). Parts, prices, links, backups, steps and safety: [build guide](build-guide.md).

## 1. Interviews (8)

Targets, bets, script and call log: [playbook](../playbook.md#6-gas-detection-integrity-8-calls).

## 2. Bench

| Step | Work | Pass condition |
|---|---|---|
| 1 | **Panel data:** collect manuals and Modbus maps for 3 common ship gas panels (for example Consilium, Dräger, Autronica) [26]; list readable points (readings, alarms, faults) | At least 2 of 3 expose readings without the maker's help |
| 2 | **Bench rig:** Tier 1 uses Modbus methane and ammonia sensors plus a panel emulator; Tier 2 adds a real fixed controller only before a pilot ([build guide](build-guide.md)); the reader is the same box as the [monitoring bench](../monitoring/build-plan.md) | Readings logged and signed every second for 7 days offline |
| 3 | **Seeded faults:** offset (drift), slow response, dead sensor, inert balanced span gas on a catalytic sensor (the Coast Guard's finding [1]) | At least 9 of 10 seeded faults flagged; 0 false "healthy" results |
| 4 | **Guided test app:** monthly test walk through with tolerance rules from the maker's manual; one click inspector report | A test of 10 sensors takes less time than the paper method |
| 5 | **Class check:** ask one class society whether a read only tap needs new approval | Written answer |
| 6 | **Ship pilot:** one gas fueled ship or gas carrier for 3 months, free | Record used in one inspection or vetting; at least one drift or test error caught |

**Bench cost:** Tier 1 core bench about $1,700 to $3,300; Tier 2 real panel about $4,800 to $6,300, only before a pilot ([build guide](build-guide.md)).

**Safety:** use certified low concentration test gases (methane in air below the lower explosive limit, ammonia at ppm levels) in a ventilated space; never pure ammonia or flammable gas on the bench.

## 3. Decision gate

Lead product by Tin's decision (2026-10-07). After 8 interviews and step 4: stays lead if at least 3 managers or owners would pay $8K per ship a year and step 3 passes. If not, demote to a feature of the monitoring box and make readiness the near term product ([startup plan §8](startup-plan.md#8-kill-or-pivot)).

## 4. Diligence log

| Date | Claim | Status | Finding |
|---|---|---|---|
| 2026-10-07 | Ammonia alone is a big enough bridge | **No** | 5 ships in operation and 41 on order; 4 orders in 2026 [15] |
| 2026-10-07 | Fixed gas detection problems are real at sea | **Yes, dated** | Coast Guard alert, P&I circular, flag warning [1 to 3]; needs 2024 to 2026 data (GI5) |
| 2026-10-07 | Someone already sells maker neutral health for fixed ship systems | **Not found** | Portable clouds [22 to 24], single brand land remote calibration [25] [29] |
| 2026-10-07 | Digital bunkering covers safety data | **No** | Ofiniti covers transactions [27]; partner |
| 2026-10-07 | Hazardous area certification needed | **Not in phase 1** | Box sits in a safe area, read only (K); confirm with class (GI2) |
