# Monitoring: Build and Validation Plan

[Back to README](../../README.md) · [Product](product-and-tech.md) · [Market](market.md) · [Competition](competition.md) · [Risks](risks.md) · [Build plan](build-plan.md) · [Evidence](evidence.md) · [YC review](yc-review.md)

Owner split: the business co-founder runs interviews; the technical co-founder builds the bench box. Validation only until after Kairos's YC application (November 2). A full build guide (parts with checked prices, links and backups, wiring, safety) is not written yet; write it before ordering parts.

## 1. Interviews (8)

Targets, bets, script and call log: [playbook](../playbook.md#4-monitoring-8-calls).

## 2. Bench

| Step | Work | Pass condition |
|---|---|---|
| 1 | **Data model:** list what each reader needs (regulator, port, class society, insurer, IAEA) from NRC proposed Part 57, safeguards papers, Lloyd's Register guidance and the Rotterdam study [1 to 3, 8, L6] | One page per reader, checked in 2 calls |
| 2 | **Bench data box:** single board computer, radiation sensor, GNSS, hardware signing key, tamper switch, offline storage. Feed it synthetic reactor status data (power, temperatures, flows, alarms) from a simple simulator we write | 7 days offline; every record signed; a verifier on a laptop detects any edited, missing or reordered record |
| 3 | **One way link and red team:** data enters the box through a one way link only; an outside tester tries to reach the source network through the box | No inbound path found |
| 4 | **Role based views and pre arrival packet:** port, insurer and regulator views of the same record; packet filed in the readiness record (idea 1) | A port contact says the packet answers its pre arrival questions |
| 5 | **Pilot:** an unfueled floating plant prototype (Bluecore is testing monitoring and sensors on one [L7]) | Box runs alongside their sensors for 30 days |

**Indicative bench parts (E, prices to check before ordering):**

| Part | Example | About |
|---|---|---|
| Computer | Raspberry Pi 5, or an industrial gateway | $80 to $400 |
| Radiation sensor | Scintillation spectrometer (for example Radiacode 103) or a USB Geiger counter | $100 to $400 |
| Position | u-blox GNSS module | $50 to $70 |
| Signing key | Microchip ATECC608 secure element board | $10 to $20 |
| Tamper | Enclosure with lid switch and light sensor | $50 to $150 |
| One way link | Two microcontrollers with a transmit only serial or fiber link | About $30 |
| Storage | Industrial SD card or SSD | $30 to $80 |
| **Total** | | **About $350 to $1,150** |

**Safety:** background radiation and recorded datasets only. No radioactive sources on the bench.

## 3. Decision gate

After 8 interviews and step 3: promote to Strong candidate if at least 2 developers would share read only data and 1 port or insurer would require or pay for independent records. Otherwise move to Partner or license (offer the record to a detector or remote operations company).

## 4. Diligence log

| Date | Claim | Status | Finding |
|---|---|---|---|
| 2026-10-07 | An independent monitoring product for ship reactors exists | **Not found** | Makers, Mirion, cyber firms and plant AI each cover parts [9 to 14, 15] |
| 2026-10-07 | Rules allow remote monitoring | **Proposed** | NRC Part 57, final expected January 2027 [1] |
| 2026-10-07 | Safeguards for moving reactors are solved | **No** | Still being studied [2, 3] |
| 2026-10-07 | A floating plant developer tests monitoring before fuel | **Yes** | Bluecore's unfueled prototype [L7] |
