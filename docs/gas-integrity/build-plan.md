# Gas Detection Integrity: Build and Validation Plan

[Back to README](../../README.md) · [Product](product-and-tech.md) · [Market](market.md) · [Competition](competition.md) · [Risks](risks.md) · [Build plan](build-plan.md) · [Evidence](evidence.md) · [YC review](yc-review.md)

Owner split: the business co-founder runs interviews; the technical co-founder builds the bench. Validation only until after Kairos's YC application (November 2). A full build guide (parts with checked prices, links and backups, wiring, safety) is not written yet; write it before ordering parts.

## 1. Interviews (8)

Targets, bets, script and call log: [playbook](../playbook.md#6-gas-detection-integrity-8-calls).

## 2. Bench

| Step | Work | Pass condition |
|---|---|---|
| 1 | **Panel data:** collect manuals and Modbus maps for 3 common ship gas panels (for example Consilium, Dräger, Autronica) [26]; list readable points (readings, alarms, faults) | At least 2 of 3 expose readings without the maker's help |
| 2 | **Bench rig:** a used fixed gas controller, 2 catalytic or infrared flammable sensors, 1 electrochemical ammonia sensor, test gas in air; reader on the same box as the [monitoring bench](../monitoring/build-plan.md) | Readings logged and signed every second for 7 days offline |
| 3 | **Seeded faults:** offset (drift), slow response, dead sensor, inert balanced span gas on a catalytic sensor (the Coast Guard's finding [1]) | At least 9 of 10 seeded faults flagged; 0 false "healthy" results |
| 4 | **Guided test app:** monthly test walk through with tolerance rules from the maker's manual; one click inspector report | A test of 10 sensors takes less time than the paper method |
| 5 | **Class check:** ask one class society whether a read only tap needs new approval | Written answer |
| 6 | **Ship pilot:** one gas fueled ship or gas carrier for 3 months, free | Record used in one inspection or vetting; at least one drift or test error caught |

**Indicative bench parts (E, prices to check before ordering):** used fixed gas controller $500 to $2,000; flammable and ammonia sensors $300 to $1,000; test gas cylinders and regulator $200 to $500; data box parts shared with the monitoring bench ($350 to $1,150). **Total about $1,350 to $4,650.**

**Safety:** use certified low concentration test gases (methane in air below the lower explosive limit, ammonia at ppm levels) in a ventilated space; never pure ammonia or flammable gas on the bench.

## 3. Decision gate

After 8 interviews and step 4: promote to Strong candidate if at least 3 managers or owners would pay $8K per ship a year and step 3 passes. Promote to lead (first product, ahead of the nuclear ideas) if a manager offers a paid pilot. Otherwise keep it as a feature of the monitoring box.

## 4. Diligence log

| Date | Claim | Status | Finding |
|---|---|---|---|
| 2026-10-07 | Ammonia alone is a big enough bridge | **No** | 5 ships in operation and 41 on order; 4 orders in 2026 [15] |
| 2026-10-07 | Fixed gas detection problems are real at sea | **Yes, dated** | Coast Guard alert, P&I circular, flag warning [1 to 3]; needs 2024 to 2026 data (GI5) |
| 2026-10-07 | Someone already sells maker neutral health for fixed ship systems | **Not found** | Portable clouds [22 to 24], single brand land remote calibration [25] [29] |
| 2026-10-07 | Digital bunkering covers safety data | **No** | Ofiniti covers transactions [27]; partner |
| 2026-10-07 | Hazardous area certification needed | **Not in phase 1** | Box sits in a safe area, read only (K); confirm with class (GI2) |
