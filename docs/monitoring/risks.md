# Monitoring: Risks and Challenges

[Back to README](../../README.md) · [Product](product-and-tech.md) · [Market](market.md) · [Competition](competition.md) · [Risks](risks.md) · [Build plan](build-plan.md) · [Evidence](evidence.md) · [YC review](yc-review.md)

Likelihood (L) and impact (I) from 1 to 3. Score = L x I. Status: Open, Testing, Closed (with evidence).

## 1. Risk register

| ID | Risk | L | I | Score | Mitigation | Test | Status |
|---|---|---|---|---|---|---|---|
| MN1 | Reactor makers refuse third party read access | 3 | 3 | 9 | Read only, one way design; ask insurers and ports to require independent records; start with smaller developers | 5 developer calls | Open |
| MN2 | Regulators accept only the licensee's own systems | 2 | 3 | 6 | Position as supplementary evidence for ports and insurers, not regulatory compliance | Ask a former NRC official | Open |
| MN3 | Nuclear grade quality and cyber certification take years and money | 3 | 3 | 9 | Stay outside safety systems (non safety grade); certify to ship cyber rules first | Quote from a certifier | Open |
| MN4 | No fueled reactor at sea before about 2028 to 2030 | 3 | 2 | 6 | Floating plants and microreactors first; bench and simulated data until then | Track Bluecore, Prodigy, Deployable | Open |
| MN5 | Mirion, Kongsberg or ABB bundle a shared nuclear record | 2 | 2 | 4 | Partner with them; neutrality is the product | Partner calls | Open |
| MN6 | Our box becomes an attack path into the ship or reactor | 2 | 3 | 6 | One way data diode; no inbound path; signed firmware; outside red team test | Red team on the bench (build plan step 3) | Open |
| MN7 | Safeguards are a state to IAEA matter, not a commercial market | 2 | 2 | 4 | Sell to ports and insurers; offer data to safeguards only if asked | Ask an IAEA safeguards expert | Open |
| MN8 | Founder bandwidth (Kairos first) | 3 | 2 | 6 | Interviews only until after November 2 | Weekly review | Open |
| MN9 | Export rules on nuclear related data and technology | 2 | 2 | 4 | Public data on the bench; counsel review before handling developer data | Counsel | Open |
| MN10 | Price per reactor too low for nuclear quality costs | 2 | 2 | 4 | Price against the cost of a port refusal or an insurance premium | Interviews | Open |

## 2. Kill criteria

1. 3 of the first 5 reactor developers refuse read only access.
2. Regulators, ports and insurers all say they will accept only the maker's data.
3. Certification would take more than 24 months of runway.

## 3. Open questions

1. What do floating plant developers plan to share with ports and insurers?
2. Would a port accept a pre arrival packet from a third party?
3. Does the IAEA program's safeguards group want commercial data?
4. Which cyber rule (ship, reactor or both) applies where ship and reactor networks meet?
