# Gas Detection Integrity: Competition

[Back to README](../../README.md) · [Startup plan](startup-plan.md) · [YC application](yc-application.md) · [Product](product-and-tech.md) · [Market](market.md) · [Competition](competition.md) · [Risks](risks.md) · [Build plan](build-plan.md) · [Build guide](build-guide.md) · [Evidence](evidence.md) · [YC review](yc-review.md)

Numbers in brackets are [evidence](evidence.md) rows.

## 1. Map

| Company | What they do | Pain point they solve | Pain point we solve | Different? |
|---|---|---|---|---|
| **Ship gas detection makers** (Consilium, Autronica, Dräger, Hanla IMS, CTI) [26] | Fixed systems and service for their own equipment | Detect gas; meet class rules | One view and record across all makers; drift between services | **Partly.** Biggest threat if they add cloud health; possible partners |
| **Industrial Scientific iNet** [22] | Cloud fleet management for portable detectors; automatic bump tests in docks | Portable detector upkeep and proof | Fixed systems built into the ship | **Yes for fixed.** Could expand; no marine case found |
| **Teledyne GDCloud, Blackline, MSA Safety io, WatchGas** [23] | Cloud records for portable detectors; Teledyne has marine docks | Portable fleets | Fixed systems | **Partly.** Teledyne is closest at sea |
| **Martek Marine** [24] | Portable detector with tamperproof calibration certificate; calibration gas supply | Portable proof at sea | Fixed systems; drift between tests | **Partly.** Channel for test gas |
| **Remote calibration on land** (MSA CalGard, General Monitors, SMC Sentry) [25] | Automatic tests for fixed detectors inside one brand | Less walking to sensors | Maker neutral, at sea, plus the record | **Partly.** Shows the tech works |
| **Ofiniti** (FuelBoss) [27] | Digital bunkering transactions for LNG, methanol and ammonia | Paperwork and fuel data for each delivery | Safety sensor health, not transactions | **Yes.** Partner: add a detector health summary to each bunkering record |
| **Danelec and other voyage data recorder makers** [28] | The ship's "black box", now with remote health checks | Accident investigation, compliance | Gas detector health and proof | **Partly.** Could add gas data; also a possible channel |
| **Planned maintenance software and service companies** (for example Lavastica [7]) | Logs and on board calibration visits | Scheduling and paperwork | Live drift between visits; signed proof | **Partly.** Integrate, don't replace |

## 2. Our gap

1. **Fixed systems, maker neutral, at sea:** portable tools are taken [22 to 24]; fixed remote calibration exists only inside single brands on land [25]; no neutral ship service found [29].
2. **Catch the known mistakes before the inspector does:** wrong span gas and out of tolerance readings are the Coast Guard's findings [1]; we check them at test time.
3. **Proof, not just readings:** a signed, inspector ready record [7, 8].
4. **A path to nuclear:** the same integrity layer later serves radiation monitors and reactor monitoring.

## 3. Where we lose

- A big maker (Consilium, Dräger) or Teledyne adds cloud health for fixed systems and bundles it.
- Panels are closed and makers refuse data access.
- Class requires a full approval before any connection.
- Ship managers see the planned maintenance system plus annual service as good enough.
- Detentions for gas detection are rarer today than the 2019 to 2020 alerts suggest.

## 4. Strategy

Start with ship managers that run several makers' systems, where neutrality matters most. Partner with Ofiniti (bunkering record) and a test gas supplier (Martek Fastcalgas). Offer makers a license instead of a fight. Keep phase 1 read only so class acceptance is light.

## 5. Stress test: new, or better? (2026-10-07)

**Improved, not new.** The idea (cloud proof of gas detector health) exists for portable detectors [22 to 24] and as single brand remote calibration on land [25]. What stays open: maker neutral health and proof for fixed systems on ships, which inspectors check and new fuels make more critical [1, 9]. **Value lever to test:** whether avoided delays and detentions, plus crew time saved, justify $8K to $20K per ship a year.
