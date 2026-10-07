# CLAUDE.md: session handoff for the Nuclear Shipping Lab

Read this first in every session. Then read [README.md](README.md) (public page), [docs/portfolio.md](docs/portfolio.md) (scores and tiers), [docs/method.md](docs/method.md) and [docs/landscape.md](docs/landscape.md). At the end of any session that changes a score, tier or plan: update the idea's files in `docs/`, [docs/decisions.md](docs/decisions.md), the evidence tables (then regenerate [docs/sources.md](docs/sources.md) with `python3 tools/gen_sources.py .`), the status table in [docs/portfolio.md](docs/portfolio.md), the README if the public picture changed, and this file.

## 1. Mission

- This repo holds due diligence on startup ideas for the layer around ship reactors, tested after Kairos, Tin's lead startup ([tinha04/Kairos](https://github.com/tinha04/Kairos)). Format and habits mirror the Idea Lab ([tinha04/IdeaLab](https://github.com/tinha04/IdeaLab), private).
- **Ideas (Tin's decision, 2026-10-07):** port and route readiness (rank 1), independent reactor monitoring (rank 2), insurance for nuclear ships (rank 3); shielding and layout optimizer as backup research.
- **Bridge idea (added 2026-10-07):** gas detection integrity, proof that ship gas detectors work, YC lens 23 (highest here). Same box and signed record as reactor monitoring; earns from gas fueled ships and gas carriers now. Proposal: make it the first product and the YC pitch, with nuclear as the long term vision ([decisions](docs/decisions.md#2-waiting-on-tin)).
- **Origin:** an industry contact in shipping who works on modular nuclear power for ships. Do not name them or their company in this public repo.
- **Scope:** readiness, monitoring and risk tools around ship reactors. Never reactor design, fuel handling, weapons or naval propulsion. Monitoring is read only, one way, and never part of reactor control or safety systems.

## 2. Status (October 7, 2026)

| Idea | YC score (35) | Tier | Biggest open question |
|---|---|---|---|
| Gas detection integrity (bridge) | 23 | Exploring | Will ship managers pay per ship beyond maintenance logs and the maker's service (GI4)? Are 2019 to 2020 inspection findings still common (GI5)? |
| Port and route readiness | 21 | Exploring | Will ports and owners pay for readiness work now, or wait for free guidance (RD1, RD3)? |
| Independent reactor monitoring | 20 | Exploring | Will reactor makers share read only data, and will anyone require independent records (MN1, MN2)? |
| Insurance for nuclear ships | 18 | Exploring | Will an insurer pay for risk data before ships exist; who provides capital (IN1)? |
| Shielding and layout optimizer | 18 | Backup | Is shielding a bottleneck anyone would pay to fix (K7)? |

- **Proof so far:** research and stress test only. 0 interviews, 0 users, 0 revenue.
- **Team:** technical co-founder (hardware, embedded firmware, product) and business co-founder (customers, partners, grants). **Gaps:** nuclear regulation, maritime law, insurance underwriting, class approval for ship equipment.
- **Timing:** interviews only until after Kairos's YC application on November 2; proposed exception: one call with the industry contact (waiting on Tin).
- **Branch:** work on `claude/hopeful-goldberg-rbahec`. Do not push elsewhere without permission. No PR unless asked.
- **Visibility:** this repo is public; proposal to make it private before interview notes go in.

## 3. Goals

| Idea | Metric | Target |
|---|---|---|
| All | Industry contact call | Done, with 3 introductions |
| Gas detection | Ship manager interviews | 8 ([playbook](docs/playbook.md#6-gas-detection-integrity-8-calls)) |
| Gas detection | Bench rig | At least 9 of 10 planted faults caught (drift, slow response, dead sensor, wrong test gas); 0 false "healthy" |
| Gas detection | Decision gate | At least 3 managers would pay $8K per ship a year; a paid pilot makes it the lead product |
| Readiness | Buyer interviews | 10 ([playbook](docs/playbook.md#3-readiness-10-calls)) |
| Readiness | Rule map and scorecards | 100+ cited requirements; 3 ports scored; contact agrees with the route view |
| Readiness | Decision gate | At least 3 buyers would pay |
| Monitoring | Developer interviews | 8 ([playbook](docs/playbook.md#4-monitoring-8-calls)) |
| Monitoring | Bench box | 7 days offline, every record signed, tampering detected, no inbound path in a red team test |
| Monitoring | Decision gate | 2 developers share read only data and 1 port or insurer would require it |
| Insurance | Insurer interviews | 6 ([playbook](docs/playbook.md#5-insurance-6-calls)) |
| Insurance | Decision gate | 2 insurers pay for data or 1 capital partner prices port refusal cover |
| All | Advisors | Former NRC or Coast Guard official, nuclear lawyer, nuclear underwriter |

## 4. Risks to watch

Full registers: [readiness](docs/readiness/risks.md), [monitoring](docs/monitoring/risks.md), [insurance](docs/insurance/risks.md).
1. **Free guidance (RD1):** the Lloyd's Register consortium, NEMO (port and insurability guide by 2027) and the IAEA could make readiness work unpaid.
2. **Ships slip (RD2, MN4, IN2):** first deliveries 2030 to 2033 at the earliest; floating plants come first.
3. **Data access (MN1):** reactor makers may refuse a third party.
4. **Capital and license (IN1, IN4):** insurance cannot start as an insurer.
5. **Founder fit (RD6, IN10):** no regulatory or insurance expert; fix with advisors.
6. **Export rules (RD7, MN9):** US rules on helping foreign nuclear projects; public information only until counsel reviews.
7. **Founder bandwidth (MN8, GI10):** Kairos first; the gas bridge overlaps the Idea Lab's battery fire gas sensing.
8. **Gas bridge (GI1, GI2, GI4, GI5):** makers or class gatekeep panel data; managers may see logs plus service as enough; problem data are dated.
9. **Approvals cost before revenue (MN12):** certify only after a paying pilot ([prepare now](docs/monitoring/prepare-now.md)).

## 5. How to continue

1. Prepare and run the industry contact call with [playbook §2](docs/playbook.md#2-first-call-our-industry-contact) once Tin approves. Log answers in the evidence files (tag H).
2. After November 2: build one data box for both the [gas detection bench](docs/gas-integrity/build-plan.md) and the [monitoring bench](docs/monitoring/build-plan.md); build the readiness rule map and three port scorecards with the [readiness build plan](docs/readiness/build-plan.md).
3. Get 2024 to 2026 port state control and vetting data on gas detection findings (GI5) before pitching the bridge.
4. Follow the [monitoring prepare now](docs/monitoring/prepare-now.md) timeline; GAIN needs a legal entity.
5. Run the interviews; re-score with [docs/method.md](docs/method.md) after every 5 calls; record changes in [docs/decisions.md](docs/decisions.md) and [docs/portfolio.md](docs/portfolio.md) with the last 3 known scores.
6. Watch: the IMO carbon vote (October 2026), the NRC maritime white paper (Fall 2026), NRC Part 57 final rule (January 2027), NEMO's port and insurability guide (2027), IAEA ATLAS expert groups, the IMO legal committee on a nuclear liability regime, MARAD's next steps after its request for information.
7. Confirm key search based rows against the original documents before quoting them to customers (see the overfitting warning in [docs/yc-review.md](docs/yc-review.md#5-stress-test-new-or-better-2026-10-07)).
8. Never delete a risk; close it with evidence. Keep a corrections log in each evidence file.

## 6. Working conventions (founder preferences)

- Concise, direct, metrics driven. Use periods and commas. **No dashes** (no em or en dashes) in prose.
- **No changes without explicit instruction.** Re-read files before editing. Confirm understanding when a request is nuanced.
- Research first, stress test second. Note challenges, goals and edge cases.
- Give **overfitting warnings proactively** (scores, vendor numbers, single studies, small samples).
- **Converge slowly.** Never drop an idea without evidence; move it between tiers.
- Tag every claim (V, VC, K, E, H) and cite sources.
- Keep the README public, short and free of jargon. Put detail in `docs/`. Validate links, anchors and dashes before committing: `python3 tools/check_docs.py .`
- Commit messages end with the attribution lines required by the session.

## 7. Repository map

| Path | Contents |
|---|---|
| `README.md` | Public page: all ideas in plain language |
| `CLAUDE.md` | This handoff |
| `docs/portfolio.md` | Status, how the ideas fit, score cards, options not chosen, lessons |
| `docs/method.md` | YC lens scoring, tiers, evidence tags, update rules |
| `docs/landscape.md` | Shared evidence rows L1 to L31: programs, rules, history, economics |
| `docs/yc-review.md` | The 40 YC questions, ranking, stress test; each idea also has its own `yc-review.md` |
| `docs/playbook.md` | Interview rules, the industry contact call, targets and scripts per idea, call log |
| `docs/decisions.md` | Decisions in force and proposals waiting on Tin |
| `docs/sources.md` | All sources by area, generated from the evidence tables |
| `docs/readiness/`, `docs/monitoring/`, `docs/insurance/`, `docs/gas-integrity/` | `product-and-tech.md`, `market.md`, `competition.md`, `risks.md`, `build-plan.md`, `evidence.md`, `yc-review.md` |
| `docs/monitoring/prepare-now.md`, `docs/monitoring/niches.md` | Seven moves before 2030 and a timeline; eight niches scored (gas detection wins) |
| `docs/shielding/research.md` | Backup idea: problem, evidence, rivals, score, revisit triggers |
| `tools/` | `gen_sources.py` (rebuilds `docs/sources.md` from evidence links), `check_docs.py` (links, anchors, no em or en dashes) |

Evidence tags: **V** verified source, **VC** vendor or company claim, **K** engineering or domain knowledge, **E** our estimate, **H** hypothesis.
