# Readiness: Product and Technology

[Back to README](../../README.md) · [Product](product-and-tech.md) · [Market](market.md) · [Competition](competition.md) · [Risks](risks.md) · [Build plan](build-plan.md) · [Evidence](evidence.md) · [YC review](yc-review.md)

**Tier:** Exploring, rank 2. **YC lens:** 21/35 ([portfolio](../portfolio.md)). Numbers in brackets are [evidence](evidence.md) rows; L rows are in [landscape.md](../landscape.md).

## 1. One line

Software that maps every rule a nuclear ship call triggers, scores each port's readiness, shows which routes a ship can trade, and keeps one evidence record that owners, ports, class societies, regulators and insurers can all check.

## 2. Is it doable and does it solve a pain?

| Question | Answer | Evidence |
|---|---|---|
| Real pain? | **Yes, but early** | Port access is the barrier named by the Rotterdam study and by MARAD [L6, L1]; Otto Hahn reached about 33 ports [L23]. No nuclear ship trades yet, so the pain is felt in planning budgets, not lost revenue |
| Technically doable? | **Yes, from public sources** | The rules are public (IMO code, SOLAS VIII, ABS and Lloyd's Register rules, NRC and Coast Guard MOU, IAEA program) [L13 to L18]; the Rotterdam and Corpus Christi studies publish the questions ports must answer [L5, L6, 1] |
| Open gap? | **Narrow** | No software product found [13]; the work is done as one off studies and free guidance by the Lloyd's Register consortium, NEMO, the IAEA and Core Power [L5, L6, L14, L18, L19] |
| Who pays? | **Unproven** | Candidates: ship and floating plant projects, ports (some grant funded [5]), MARAD. Interviews decide |

## 3. Product (H)

| Module | What it does | Built from |
|---|---|---|
| **Rule map** | Every requirement for a nuclear ship call by port, flag, class society, reactor type and voyage stage (approach, berth, cargo work, emergency), each with its source and owner | IMO, IAEA, NRC, Coast Guard, class rules [L13 to L18] |
| **Port scorecard** | About 30 questions in 6 areas: emergency plans, berths and exclusion zones, radiation monitoring, security, local law and bans, public acceptance. Scored 0 to 3 with evidence links | Rotterdam and Corpus Christi study scopes [L5, L6, 1, 2] |
| **Route view** | For a ship and route: each port's score, canals, national bans (for example New Zealand [L25]), and the list of what is missing | Rule map plus scorecards |
| **Evidence record** | One file per ship and per port: documents, approvals, open items; each party sees its own view; exports in each party's format | Owner, port and class inputs |
| **Cited search** | Answers rule questions with the exact clause cited; says "not covered" when no source exists | Public documents only |

**Pricing hypothesis (E):** free first map for a design partner; port scorecard $50K to $250K; project readiness file $150K to $500K; yearly shared record $100K to $300K per ship and $50K to $150K per port.

**Tech (K):** Python; document store of public rules with clause level IDs; retrieval with citations and a refusal when no source supports an answer; scorecard as structured data so scores can be compared across ports; role based access for the evidence record.

## 4. Boundary

- We advise and document. Class societies, flag states and regulators keep every approval; nothing we produce is a certificate.
- Public information only, unless a customer shares its own files under contract. No controlled technical data.
- Possible US export rule on helping foreign nuclear projects (10 CFR Part 810): check with counsel before work for a non US reactor project (risk RD7).

## 5. What it is not

- Not a reactor design or licensing tool for the reactor itself (Everstar and Atomic Canyon serve land reactor licensing [6 to 8]).
- Not a class society. Not a law firm; legal opinions stay with counsel.
