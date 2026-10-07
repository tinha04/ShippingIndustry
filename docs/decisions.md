# Decision Log

[Back to README](../README.md) · [Portfolio](portfolio.md) · [Method](method.md)

Decisions in force, newest first.

## 1. In force

| Date | Decision | Why | Revisit when |
|---|---|---|---|
| 2026-10-07 | **Gas detection integrity is the lead product and the YC pitch,** with reactor monitoring as the long term vision (Tin's decision) | Highest score (23); a customer who can pay this year; best speed to proof and founder fit | Gate after 8 interviews and the bench fault test ([build plan §3](gas-integrity/build-plan.md#3-decision-gate)) |
| 2026-10-07 | **It lives in this repo,** not the Idea Lab (Tin's decision) | It is the bridge to reactor monitoring; buyers differ from the battery fire tag | n/a |
| 2026-10-07 | **Form the legal entity when applying** (YC or a GAIN voucher, whichever comes first) (Tin's decision) | Needed for GAIN and YC; no cost before then | Before the FY2027 GAIN deadline, if GAIN comes first |
| 2026-10-07 | **One data box for gas detection and reactor monitoring** (Tin's decision) | Shared hardware, firmware and signing ([build guide](gas-integrity/build-guide.md)) | If ship requirements split them |
| 2026-10-07 | **Make this repo private** (Tin's decision). Not done by Claude: no tool access to repo settings; Tin to switch it in GitHub settings | The repo holds strategy and will hold interview notes | Done when GitHub shows Private |
| 2026-10-07 | YC planning docs added: [startup plan](gas-integrity/startup-plan.md), [application draft](gas-integrity/yc-application.md), [build guide](gas-integrity/build-guide.md) | Organize the repo for YC planning and building (Tin's instruction) | Each milestone |
| 2026-10-07 | **Monitoring prepare now plan and niche scoring written** (Tin's instruction): seven moves before 2030 ([prepare now](monitoring/prepare-now.md)), eight niches scored ([niches](monitoring/niches.md)) | Approvals and integration are the slow parts; most can be done once, early | At each monitoring gate |
| 2026-10-07 | **Gas detection integrity added as a bridge idea and candidate future project,** full scope review in `docs/gas-integrity/`; YC lens 23, the highest in this repo | Ships need it now; same box and record as reactor monitoring; no maker neutral fixed system service at sea found | After 8 ship manager interviews |
| 2026-10-07 | **Ammonia only bridge rejected:** too small (5 in service, 41 on order); folded into gas detection across all gas fuels | Fleet count ([gas evidence](gas-integrity/evidence.md)) | If ammonia orders pick up sharply |
| 2026-10-07 | No score changes for readiness, monitoring, insurance or shielding this round | Prepare now work shortens later steps but adds no buyer evidence | After interviews |
| 2026-10-07 | **Continue three ideas:** port and route readiness, independent reactor monitoring, insurance for nuclear ships. **Keep the shielding and layout optimizer as backup research** to see if it can grow (Tin's decision) | Chosen from six wedges in the first brainstorm; the reactor and the leasing model are out of reach for a startup | After the first 5 interviews per idea |
| 2026-10-07 | First YC lens scores: readiness 21, monitoring 20, insurance 18, shielding backup 18 | Research and stress test ([yc review](yc-review.md)) | After interviews |
| 2026-10-07 | Scope: readiness, monitoring and risk tools around ship reactors. Never reactor design, fuel handling, weapons or naval propulsion. Monitoring is read only and never part of reactor control or safety systems | Keeps us outside nuclear safety licensing and export controlled design work | If a customer asks for more |
| 2026-10-07 | Parked: crew training and staffing, reactor leasing ([portfolio §4](portfolio.md#4-options-considered-and-not-chosen-2026-10-07)) | Not chosen; capital or incumbents | Triggers recorded |
| 2026-10-07 | Scoring: the YC lens only; no 30 point lab score in this repo | The lab score's "neuromorphic fit" criterion does not apply here | If the Idea Lab method changes |
| 2026-10-07 | Repo format mirrors the Idea Lab: short public README, handoff in CLAUDE.md, detail in `docs/` per idea, evidence tags on every claim | Same founders, same review habits | n/a |

## 2. Waiting on Tin

| Proposal | Why |
|---|---|
| **One company in stages:** gas detection now (decided as lead), readiness now, monitoring when floating plants fuel, insurance when ships trade, on one shared record ([portfolio §2](portfolio.md#2-how-the-three-ideas-fit-proposal)) | Each alone is tens of millions a year at most; together they share customers, data and trust |
| **Call our industry contact before November 2** (one call, script K1 to K9 in the [playbook](playbook.md#2-first-call-our-industry-contact)) | Low bandwidth; tests the lead product (K9) and opens introductions |
| **Insurance starts as a data supplier,** with port refusal or delay cover as the first product, not as an underwriting agency | No license, capital or loss data; port refusal needs no nuclear capacity |
| **Monitoring starts with floating plants,** not ships | Funded and earlier (Bluecore, Deployable Energy, Prodigy) |
| **Recruit advisors:** first a ship manager or port state control inspector (lead product); then a former NRC or Coast Guard official, a nuclear lawyer, a nuclear underwriter | Founder fit is 3 on the lead and 1 to 2 on readiness and insurance |
| Timing: interviews only until after Kairos's YC application (November 2), same as the Idea Lab; this company applies for Spring or Summer 2027 only if the founders are not full time on Kairos ([startup plan §4](gas-integrity/startup-plan.md#4-timing-against-kairos)) | Founder bandwidth; YC asks whether all founders work full time |
| Nuclear vs fuel cost model (payback, fuel price and carbon price sensitivity) as a free tool for owners, part of the readiness pitch | Proposed in the first brainstorm; not built |
