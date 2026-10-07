# Method

[Back to README](../README.md) · [Portfolio](portfolio.md) · [YC review](yc-review.md) · [Decisions](decisions.md) · [Sources](sources.md)

Same method as the Idea Lab, with one change: this repo scores with the YC lens only (section 1). The Idea Lab's 30 point lab score still has a "neuromorphic fit" criterion left from a dropped sensor idea, which does not apply to software and monitoring around reactors.

## 1. Scoring: the YC lens (1 to 5 each, total out of 35)

| Criterion | 1 means | 5 means |
|---|---|---|
| Problem | Anecdotal | Verified, costly, blocks the customer (regulation, losses, no cover) |
| Market | Under $10M a year reachable | $100M+ a year reachable |
| Insight | Common knowledge | A sourced reason others miss the gap |
| Differentiation | A funded leader already solves it | No one serves the gap we target |
| Founder fit | No relevant skills or access | Core skills and buyer access |
| Speed to proof | Over 12 months to first proof | Proof in weeks |
| Why now | Nothing changed | Rules, money and projects all moved this year |

**Overfitting warning:** scores are judgment until interviews and pilots replace them. Weights are equal on purpose so they cannot be tuned toward a favorite. With 0 interviews, a 1 point gap between ideas is noise.

## 2. Tiers

| Tier | Meaning |
|---|---|
| Lead | The company's first product; building after validation gates |
| Strong candidate | Evidence supports problem, market and a gap; validating with buyers |
| Exploring | Problem verified; gap or buyer unclear |
| Backup | Research only; revisit trigger recorded |
| Parked | Weak gap or small market; revisit trigger recorded |

**Promote** on evidence of pain plus budget (interviews, letters of intent, paid pilots). **Demote** when a competitor ships an equal product or a kill criterion hits.

## 3. Evidence tags

**V** verified source · **VC** vendor or company claim · **K** engineering or domain knowledge · **E** our estimate · **H** hypothesis.

Shared market facts are rows L1 onward in [landscape.md](landscape.md). Each idea's own facts are numbered rows in its `evidence.md`. Brackets in the text point to rows: [L6] is landscape row 6, [12] is row 12 of that idea's evidence file.

## 4. Update rules

1. New fact: add a row to the idea's `evidence.md` (or to [landscape.md](landscape.md) if it serves every idea) with tag, source and date checked.
2. Wrong fact: add it to the corrections log in that file, fix every file that used it, and re-score.
3. New risk: add it to the idea's `risks.md` with likelihood, impact, mitigation and test. Never delete a risk; close it with the evidence.
4. Score change: record it in [decisions.md](decisions.md) and the status table in [portfolio.md](portfolio.md), with the last 3 known scores for comparison.
