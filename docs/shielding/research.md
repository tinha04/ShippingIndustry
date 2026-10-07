# Shielding and Layout Optimizer: Backup Research

[Back to README](../../README.md) · [Portfolio](../portfolio.md) · [YC review](../yc-review.md) · [Landscape](../landscape.md)

**Tier:** Backup (Tin's decision, 2026-10-07): research only, kept to check whether it can grow into something more. **YC lens:** 18/35 (first round). All rows checked October 7, 2026 through web search results; L rows are in [landscape.md](../landscape.md).

## 1. One line

Software that cuts the weight of a ship reactor's radiation shield and finds the best place for the reactor on the hull, so the ship loses less cargo space and weight.

## 2. Why it matters

- **"More cargo space" is the weakest part of the nuclear pitch:** removing fuel tanks frees only about 5% more container space in Lloyd's Register's 15,000 TEU case [L27]; the real gain there is speed and more trips a year.
- **Shields are heavy:** Korean studies optimized a ship shield from about 12,051 to about 10,507 tonnes [1].
- **Layout is a design constraint from day one:** ABS's "nuclear ready" notation reserves space and structure for shielding and weight [3]; the ABS and Blossom LNG carrier moved the reactor to the stern and reinforced the hull [L28].

## 3. Evidence

| # | Claim | Value | Tag | Source |
|---|---|---|---|---|
| 1 | Korean ship shielding study | Concrete between steel, 36% lighter than land plant shielding; further optimization from about 12,051 t to 10,507 t; reactor and plant placed in former fuel tank areas to limit container loss | V (1 conference paper) | [KNS](https://kns.org/files/pre_paper/31/281길영미.pdf) |
| 2 | MIT retrofit study | 12,000 TEU Neo-Panamax ship with a microreactor; CAD and finite element checks; judged technically and economically viable | V | [MIT DSpace](https://dspace.mit.edu/handle/1721.1/162806) |
| 3 | ABS nuclear ready notation | Space allocation, structural arrangements for shielding and weight, system interfaces | V | [NEI Magazine](https://www.neimagazine.com/news/abs-sets-nuclear-ready-ship-standard/) |
| 4 | Retrofits | Technically feasible, economically impractical | V | [Seatrade](https://www.seatrade-maritime.com/sustainability/nuclear-retrofits-technically-feasible-economically-impractical) |
| 5 | PhysicsX | $300M Series C (June 2026) at about $2.4B; AI models that replace parts of engineering simulation; backed by Siemens and NVIDIA | V | [PhysicsX](https://www.physicsx.ai/newsroom/physicsx-announces-300m-series-c-to-accelerate-physics-ai-for-industrial-engineering) |
| 6 | TopMC | Neutronics and shielding code with an AI surrogate module for faster design | V | [KIT](https://indico.kit.edu/event/5433/contributions/22893/) |
| 7 | ML assisted shielding | Neural network trained on 200 MCNP runs ranks 1,000 shield configurations; top 20 checked in MCNP | V (research) | [arXiv](https://arxiv.org/abs/2504.17319) |
| 8 | OpenMC | Free Monte Carlo radiation transport code led by Argonne and MIT | V | [ALCF](https://alcf.anl.gov/news/open-source-code-driving-innovation-nuclear-and-fusion-energy-research) |
| 9 | Ship design software | NAPA covers early design through statutory calculations; Cadmatic offers an AI structural design recommender | V | [NAPA](https://www.napa.fi/ja/ship-design/), [Cadmatic](https://cadmatic.com/en/articles/optimized-structural-design-recommender-system-a-two-step-solution-for-ai-based-ship-design-optimization/) |

## 4. Competitors

| Company | What they do | Pain point they solve | Pain point we would solve | Different? |
|---|---|---|---|---|
| **Reactor makers and shipyards** (HD KSOE, Samsung Heavy, Blossom, Core Power's partners) | In house shielding and layout design | Their own design | A tool across reactors and hulls | **Partly.** Biggest threat: they do it themselves |
| **PhysicsX** | AI engineering simulation across industries [5] | Faster simulation | Shielding plus hull layout, nuclear specific | **Partly.** Could enter with far more money |
| **TopMC, OpenMC, MCNP** | Radiation transport codes, some with AI modules [6 to 8] | Accurate dose and shielding physics | Coupling shielding to hull, weight and cargo | **Partly.** Our engine, not our product |
| **NAPA, Cadmatic, AVEVA** | Ship design software [9] | Hull, structure, stability | Radiation shielding inside the same loop | **Partly.** Partner or acquirer |

## 5. YC lens

| Criterion | Score | Why |
|---|---|---|
| Problem | 3 | Shield weight and layout are real constraints [1, 3], but yards and makers handle them in house |
| Market | 2 | About 20 to 40 design teams x $100K to $500K a year, about $2M to $20M (E) |
| Insight | 3 | Fast surrogate models of radiation codes [6, 7] can sit inside hull design loops |
| Differentiation | 2 | PhysicsX, codes with AI modules and ship design suites each cover a part [5 to 9] |
| Founder fit | 2 | Software skills; no radiation transport or naval architecture expertise |
| Speed to proof | 3 | A demo on a public reference design with OpenMC in weeks; credibility needs a yard's data |
| Why now | 3 | Design approvals since June 2026 [L11]; nuclear ready notation [3] |
| **Total** | **18** | |

## 6. Revisit if

1. Our industry contact, a shipyard or a reactor maker says shield weight or layout is a bottleneck they would pay to fix (question K7 in the [playbook](../playbook.md#2-first-call-our-industry-contact)).
2. A yard offers design data for a joint study.
3. Readiness work (idea 1) shows that cargo space or weight decides whether owners order nuclear ships.

## 7. Corrections log

None yet.
