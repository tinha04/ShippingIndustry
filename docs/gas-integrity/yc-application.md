# Gas Detection Integrity: YC Application Draft

[Back to README](../../README.md) · [Startup plan](startup-plan.md) · [YC application](yc-application.md) · [Product](product-and-tech.md) · [Market](market.md) · [Competition](competition.md) · [Risks](risks.md) · [Build plan](build-plan.md) · [Build guide](build-guide.md) · [Evidence](evidence.md) · [YC review](yc-review.md)

Draft 1, 2026-10-07. Questions follow the order of YC's form ([all 40](../yc-review.md#3-the-40-questions)); YC edits the form each batch, so check the live form. Grades and gaps per answer are in the [YC review](yc-review.md). **Founders write their own answers to the founder questions;** this file only lists what each needs. Replace every "[to do]" with real results before submitting. Numbers in brackets are [evidence](evidence.md) rows, for our use only; strip them before pasting.

## Founders (Q1 to Q11): founders write

| # | Question | What the answer needs |
|---|---|---|
| 1 | Profiles | Education, work, links |
| 2 | Technical founder? | Yes: hardware, embedded firmware |
| 3 | Most impressive thing built | A concrete hardware or firmware story; Kairos counts |
| 4 | Hacked a non computer system | A specific story |
| 6 | Who builds | All design and firmware by founders; contractors only with IP assigned |
| 8 | How the founders met | Specific and short |
| 9, 10 | Full time? | A clear plan; note the conflict with Kairos ([startup plan §4](startup-plan.md#4-timing-against-kairos)) |
| 11 | Video | Record after interviews so it can quote ship managers |

## Company (Q12 to Q17)

**Q12. Company name:** [to do, founders choose]

**Q13. What your company does (50 characters):** Proof that ship gas detectors work (34)

**Q14. Demo:** [to do: bench video of the box catching drift and the wrong test gas]

**Q15. What is your company going to make?**
> Ships that run on LNG, methanol or ammonia, and ships that carry gas, depend on fixed gas detectors. Those sensors drift, and crews test them with the wrong gas; port inspectors find it, and the ship is delayed or detained. We make a small read only box that connects to any maker's gas detection panel, a tablet app that guides and checks each monthly test, and software that spots drifting sensors between tests. Every test becomes a signed record the ship can hand to inspectors, class and charterers. The same box and record will later serve radiation monitors and ship reactors, where independent records will be required.

**Q16, Q17. Location:** [to do] Near the first customer's technical office (Houston, Singapore or Rotterdam are the gas shipping hubs). Decide after interviews.

## Progress (Q18 to Q24)

**Q18. How far along are you?**
> [to do, update at submission] Research and stress test done (October 2026). By submission: 8 ship manager interviews, a bench rig that caught [x] of 10 planted faults, and [a pilot letter of intent].

**Q19. Time on this:** [to do]

**Q20. Tech stack:**
> Embedded Linux data box (Raspberry Pi class) with Modbus RTU and TCP and isolated 4 to 20 mA inputs; hardware secure element signing each record into a hash chain; offline first with sync over the ship's link; tablet app for guided tests; fleet web view; tolerance rules from each maker's manual stored as data; simple statistics for drift before any machine learning.

**Q21, Q22. Users, revenue:** [to do] None yet. Target by submission: one free pilot ship.

**Q23. Previous application:** [to do] Kairos applied for Winter 2027; explain the relationship.

**Q24. Accelerators:** [to do]

## Idea (Q25 to Q29)

**Q25. Why this idea? Domain expertise? How do you know people need it?**
> The US Coast Guard found fixed gas sensors reading outside tolerance, failed calibrations and the wrong test gas on LNG carriers, which delayed cargo work; a major shipowners' insurer warned members about the "alarming trends" [1, 2]. One Coast Guard sector detained gas carriers at more than three times the national rate [4]. Inspectors treat an undocumented calibration as no calibration [7]. Meanwhile about 1,100 gas capable ships are in service and 1,000 more are on order, and the first ammonia ships arrived in 2026 with toxic alarms at 25 ppm [9, 13 to 15, 18]. We build low power sensing hardware and firmware. [to do: add quotes from 8 ship manager interviews and 2024 to 2026 inspection data]

**Q26. Competitors, and what you understand that they don't:**
> Gas detection makers (Consilium, Autronica, Dräger, Hanla IMS) service their own fixed systems. Industrial Scientific, Teledyne, Blackline and MSA keep cloud records for portable detectors, about 475,000 on Industrial Scientific alone. MSA and General Monitors sell remote calibration for their own fixed detectors on land. What we understand: inspectors judge the record, ship managers run several makers' systems, and the most common findings (drift, wrong test gas) can be caught at test time. No one keeps a maker neutral, signed health record for fixed systems at sea [22 to 29].

**Q27. How will you make money, and how much could you make?**
> A yearly fee per ship, about $8K to $20K including hardware, after a free 3 month pilot. Gas fueled ships and gas carriers alone are about $12M to $33M a year at modest adoption; tankers and chemical carriers add more; radiation monitors on floating plants and ship reactors are the long term expansion. [to do: replace with prices named in interviews]

**Q28. Category:** Industrials, maritime, climate, hard tech.

**Q29. Other ideas considered:** Port readiness for nuclear ships, independent monitoring for ship reactors, nuclear ship insurance (this repo); Kairos; drone production test stations and battery fire early warning (Idea Lab).

## Equity and curious (Q30 to Q35): founders write

Entity: formed when applying (Tin's decision); Delaware C corporation is usual (K, confirm with counsel).

## Interview questions (Q36 to Q40)

**Q36. Insight and why now:** Inspectors judge the record, not just the sensor, and the top findings can be caught at test time by software on any maker's panel. Why now: gas fueled fleets are growing fast, ammonia brings toxic alarms, and fuel records are going digital in Singapore and Rotterdam [13 to 21].

**Q37. First customer and price:** A ship manager running LNG carriers or LNG fueled ships with mixed makers; free 3 month pilot on one ship, then $8K to $20K per ship a year. [to do: name the manager after interviews]

**Q38. Biggest risk and how you will know in 3 months:** Managers may see maintenance logs plus the maker's annual service as enough (GI4). We will know from 8 interviews and one pilot.

**Q39. Why won't a big company or the customer do this?** Each maker sees only its own panels; managers run several; a neutral record has to come from outside the makers. Crews already do the tests but cannot see drift between them.

**Q40. By Demo Day:** 5 ships under paid contract, one inspection passed with our record, drift caught before a test on at least one ship, a second manager in a paid pilot ([startup plan §6](startup-plan.md#6-demo-day-targets-about-3-months-after-acceptance)).
