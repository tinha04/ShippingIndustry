# Monitoring: Product and Technology

[Back to README](../../README.md) · [Product](product-and-tech.md) · [Market](market.md) · [Competition](competition.md) · [Risks](risks.md) · [Build plan](build-plan.md) · [Evidence](evidence.md) · [YC review](yc-review.md)

**Tier:** Exploring, rank 2. **YC lens:** 20/35 ([portfolio](../portfolio.md)). Numbers in brackets are [evidence](evidence.md) rows; L rows are in [landscape.md](../landscape.md).

## 1. One line

An independent, read only data box and software that keeps a signed record of a ship or floating reactor's radiation, status, location, seals and cyber alerts, and shares it by role with regulators, ports, class societies, insurers and the IAEA.

## 2. Is it doable and does it solve a pain?

| Question | Answer | Evidence |
|---|---|---|
| Real pain? | **Yes, ahead of demand** | Safeguards for moving reactors are unsolved [2, 3]; remote monitoring is being written into NRC rules [1]; ports need emergency and security data [L6]. No reactor runs at sea yet |
| Technically doable? | **Yes for the box; slow for approval** | Signing, offline storage and satellite sync are standard; radiation sensors are off the shelf [9]. Nuclear grade quality and cyber certification are the long poles (MN3) |
| Open gap? | **Narrow** | Reactor makers, Mirion and cyber firms each cover a part [9 to 11]; no independent cross vendor product found [15] |
| Who pays? | **Unproven** | Candidates: floating plant developers, ship operators, insurers; maybe required by regulators. Interviews decide |

## 3. Product (H)

| Part | What it does | Notes |
|---|---|---|
| **Sealed data box** | Reads radiation monitors, reactor status signals, GNSS position and tamper seals; signs every record with a hardware key; stores weeks offline; syncs over the ship's satellite link | Our hardware and embedded firmware skills |
| **One way link** | Data flows from reactor and ship networks into the box only; nothing flows back | Data diode design; never a control path |
| **Cyber watch** | Passive monitoring of traffic where ship systems meet reactor systems; alerts mapped to ship and reactor cyber rules [5, 6] | Partner with a cyber firm (Cydome, Xage) rather than build an engine |
| **Role based views** | Regulator, port, class society, insurer and IAEA each see what they are entitled to | Same record, different views |
| **Pre arrival packet** | Status summary sent to the port before each call, filed in the port's readiness record (idea 1) | Links stages 1 and 2 |
| **Operating record** | History per reactor for insurers and lenders (idea 3) | Links stages 2 and 3 |

**Pricing hypothesis (E):** $0.3M to $1M per reactor a year, hardware included.

## 4. Boundary

- Read only and one way. Never part of reactor control, protection or safety systems.
- Safeguards stay between states and the IAEA; we can supply tamper evident data if they ask, never replace their equipment.
- Controlled reactor data only under the developer's contract and export rules (risk MN9).

## 5. Why floating plants first

Barges and transportable plants are funded and moving now (Bluecore $60M in 2026 [L7]; Deployable Energy and Hornbeck [L8]; Prodigy by 2030 [L12]), sit at one port for long periods, and still face the same port, regulator and insurer questions as ships. Bluecore is testing monitoring and sensors on an unfueled prototype [L7], a natural first pilot.
