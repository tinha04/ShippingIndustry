# Portfolio

[Back to README](../README.md) · [Method](method.md) · [YC review](yc-review.md) · [Landscape](landscape.md) · [Decisions](decisions.md) · [Sources](sources.md)

Three ideas for the layer around ship reactors, plus one backup, tested after Kairos. Scores follow the YC lens in [method.md](method.md).

## 1. Status

| Idea | YC score (35) | Tier | Verdict | Next step |
|---|---|---|---|---|
| [Port and route readiness](readiness/product-and-tech.md) | **21, rank 1** | Exploring | Improved, not new. Strongest why now; most likely to earn revenue before ships exist. Lloyd's Register consortium, NEMO, IAEA and Core Power cover the work as studies and free guidance; no software product found | Industry contact call, then 10 buyer calls |
| [Independent reactor monitoring](monitoring/product-and-tech.md) | **20, rank 2** | Exploring | Improved, not new. Best founder fit; demand waits for fueled reactors; makers hold the data | 5 developer calls on read only access; floating plants first |
| [Insurance for nuclear ships](insurance/product-and-tech.md) | **18, rank 3** | Exploring | Strongest problem, weakest position: no license, capital or ships yet; Northcourt, Markel and Willis, AXA XL and NorthStandard are moving | 6 insurer calls: will anyone pay for risk data now? |
| [Shielding and layout optimizer](shielding/research.md) | 18 | Backup | Research only; yards and makers do it in house | One question in every call |

**Overfitting warning:** 0 interviews. Gaps of 1 to 3 points are within judgment error. The order reflects speed to proof and why now more than size.

## 2. How the three ideas fit (proposal)

```mermaid
flowchart LR
    R["Readiness<br/>port and route records"] --> M["Monitoring<br/>operating records"]
    M --> I["Insurance<br/>risk data and cover"]
    R --> I
```

- **One record, three products:** the port and ship evidence from readiness is what the monitoring box files before each call, and both are what insurers need to price.
- **Revenue in order of arrival:** readiness sells now (studies), monitoring when floating plants fuel (about 2028), insurance when ships trade (about 2030).
- **Why one company (H):** each alone is tens of millions a year at most ([readiness](readiness/market.md#5-read-on-venture-scale), [monitoring](monitoring/market.md#5-read-on-venture-scale), [insurance](insurance/market.md#5-read-on-venture-scale)); together they share customers, data and trust. Waiting on Tin ([decisions](decisions.md#2-waiting-on-tin)).
- **Risk of one company:** three hard things at once with two founders. Mitigation: build only readiness until a kill or promote decision; keep the others in interviews.

## 3. Score cards (round 1, 2026-10-07)

| Criterion | Readiness | Monitoring | Insurance | Shielding (backup) |
|---|---|---|---|---|
| Problem | 4 | 3 | **5** | 3 |
| Market | 2 | **3** | **3** | 2 |
| Insight | 3 | 3 | 3 | 3 |
| Differentiation | **2** | **2** | 1 | **2** |
| Founder fit | 2 | **3** | 1 | 2 |
| Speed to proof | **3** | 2 | 1 | **3** |
| Why now | **5** | 4 | 4 | 3 |
| **Total** | **21** | 20 | 18 | 18 |

**Score history:** first round; no earlier scores to compare. From the next round, show the last 3 known scores per idea here.

## 4. Options considered and not chosen (2026-10-07)

| Option | Why not now | Revisit if |
|---|---|---|
| Nuclear crew training and staffing (ex Navy reactor operators into merchant crews) | Not chosen by Tin; NEMO's training task force and maritime academies are working on it [L19, L20] | A shipowner names crew as its biggest blocker |
| Reactor leasing or energy as a service | Capital heavy; Core Power's model with about $500M raised [L2, L3] | Never as a startup without a reactor partner |
| Building a reactor | Out of scope | n/a |

## 5. Lessons carried from the Idea Lab

| Lesson | How we applied it here |
|---|---|
| Check what incumbents already do before claiming a gap | Searched class societies, consortia, insurers and consultants, not only startups ([stress test](yc-review.md#5-stress-test-new-or-better-2026-10-07)) |
| Search logistics firms and integrators, not only product makers | Found the Lloyd's Register consortium, Core Power's port studies and Northcourt |
| A better product alone is not a company when funded players cover the need | Positioned all three on neutrality and a shared record, not on technology |
| Check the adoption bottleneck before building | The bottleneck is ports, rules and insurance, so we build there and not in reactors |
