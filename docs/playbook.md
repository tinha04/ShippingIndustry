# Customer Discovery Playbook

[Back to README](../README.md) · [Portfolio](portfolio.md) · [Readiness build plan](readiness/build-plan.md) · [Monitoring build plan](monitoring/build-plan.md) · [Insurance build plan](insurance/build-plan.md) · [Gas detection build plan](gas-integrity/build-plan.md)

All ideas stay in validation until after Kairos's YC application (November 2): interviews only, no building. **Call order after November 2:** gas detection (lead, section 6) first, then readiness, monitoring and insurance. Proposed exception: one call with our industry contact before then ([decisions](decisions.md#2-waiting-on-tin)). **Owner:** the business co-founder runs calls; the technical co-founder takes notes. Log every answer as a row in that idea's `evidence.md` (tag H until several sources agree), then score the call (section 7).

## 1. Interview rules (all ideas)

1. Ask about past behavior and spending, not opinions.
2. No pitch until the last 5 minutes. Note what they raise unprompted.
3. Two people: one asks, one types quotes word for word.
4. End with an ask: an intro, a site visit, data, a letter of intent.
5. Public information only. Never accept controlled nuclear technical data, export controlled drawings or confidential safety files.
6. Do not name our industry contact or their company in this repo; it is public.

## 2. First call: our industry contact

**Goal:** learn what their project needs, test which of the three ideas helps it most, and get 3 introductions.

| Ask | Question | Serves |
|---|---|---|
| K1 | What are you building: ship type and size, reactor partner, flag, intended route, timeline? | All |
| K2 | Which approvals have you mapped so far, who did the work (class society, law firm, consultant), and what did it cost in time and money? | Readiness |
| K3 | Which ports must the ship call at? Has any port said yes, no or "not yet"? | Readiness, insurance |
| K4 | What is the single biggest blocker today: rules, ports, insurance, crew, fuel or financing? | All |
| K5 | Have you talked to insurers? What did they ask for, and what did they say? | Insurance |
| K6 | What data will ports, regulators or insurers ask from you, and who will hold it? | Monitoring |
| K7 | How much space and weight does shielding take in your design? Is that a problem you would pay to reduce? | Shielding (backup) |
| K8 | Would you test a free rule map and port scorecard for your route? Who else should we talk to? | Readiness; intros |
| K9 | Does your company run gas fueled ships or gas carriers today? Who manages gas detection tests and records, and has an inspector ever flagged them? | Gas detection integrity |

## 3. Readiness (10 calls)

**What every call must answer**

| Bet | Confirmed if they say | Killed if | Ask |
|---|---|---|---|
| **Pain:** port and route approvals are slow and redone per project | Months of advisor time, or a port that said no or "not yet" | They see no port problem before 2030 | P1, P2 |
| **Who pays** (RD3, biggest risk) | A budget or price for a scorecard or route map | Fewer than 3 of 10 would pay (kill 1) | P4 |
| **Free guidance leaves room** (RD1) | Guidance is too general for their ship or port | They will wait for NEMO or the IAEA | P5 |
| **Shared record** | Several parties ask for the same evidence | Each party wants its own files | P6 |

**Who to call**

| Target | Count | Main question |
|---|---|---|
| US and EU ports (planning, emergency, security leads; for example Corpus Christi, Long Beach, Rotterdam) | 3 | P3, P4 |
| Shipowners and operators studying nuclear ships (for example Hyundai Glovis, Liberty Global Logistics, Seaspan, Capital Maritime) | 2 | P1, P4 |
| Reactor and floating plant developers (for example Bluecore, Deployable Energy, Blossom, Prodigy) | 2 | P2, P6 |
| Class society nuclear team | 1 | P5 |
| Maritime or nuclear lawyer | 1 | P2, P5 |
| Former MARAD, Coast Guard or NRC official (advisor, not buyer) | 1 | P5: what would a regulator want to see? |

**Script**
- **P1.** Walk me through how you decided which ports your ship could use. Who did it, how long did it take?
- **P2.** What did your last regulatory or port study cost, and what did it miss?
- **P3.** (Ports) Has anyone asked to bring a nuclear ship or floating plant? What would you need before saying yes?
- **P4.** Who would pay for a port scorecard or a route map, and how much?
- **P5.** Lloyd's Register, NEMO and the IAEA publish guidance. What does it not answer for you?
- **P6.** Who else asks you for the same documents (class, regulator, port, insurer)?

## 4. Monitoring (8 calls)

**What every call must answer**

| Bet | Confirmed if they say | Killed if | Ask |
|---|---|---|---|
| **Read only access** (MN1, biggest risk) | They would share read only data with a third party | 3 of the first 5 refuse (kill 1) | M2 |
| **Someone requires independence** (MN2) | A port, insurer or regulator asked for independent records | Everyone accepts the maker's data (kill 2) | M3 |
| **Budget** | A price per reactor a year | No budget until fueled | M5 |
| **Certification is manageable** (MN3) | Non safety grade is acceptable for this use | Full nuclear grade required (kill 3 likely) | M4 |

**Who to call**

| Target | Count | Main question |
|---|---|---|
| Floating plant and microreactor developers | 3 | M1, M2 |
| Reactor makers' instrumentation teams | 1 | M2, M4 |
| Port emergency planner | 1 | M3 |
| Marine insurer | 1 | M3, M5 |
| Ship cyber firm (for example Cydome) | 1 | M4 |
| Former NRC or IAEA safeguards official (advisor) | 1 | M3, M4 |

**Script**
- **M1.** What will you monitor on your reactor, and who sees that data today?
- **M2.** Would you let a third party read a one way copy? What would stop you?
- **M3.** Has a port, insurer or regulator asked for data you don't want to give them directly?
- **M4.** What quality and cyber standard would a read only box outside your safety systems need?
- **M5.** What would you pay per reactor a year for a record ports and insurers accept?
- **M6.** (Added 2026-10-07) Which data points would you expose read only, and what names do you use for them today?
- **M7.** Would you co-author an open data dictionary for marine reactors through NEMO ([prepare now](monitoring/prepare-now.md))?

## 5. Insurance (6 calls)

**What every call must answer**

| Bet | Confirmed if they say | Killed if | Ask |
|---|---|---|---|
| **Data has value now** | They would pay for ship and route risk data | No one in 3 of 5 calls (kill 1) | I2 |
| **Capital partner** (IN1, biggest risk) | They would back or co-design a cover with us | No partner within 12 months (kill 2) | I4 |
| **Port refusal is a real cost** (IN8) | Owners name what a refused or delayed call costs | Owners shrug | I3 |

**Who to call**

| Target | Count | Main question |
|---|---|---|
| Nuclear underwriters (for example Northcourt, a nuclear pool) | 2 | I1, I2, I4 |
| Marine P&I insurer (for example NorthStandard) | 1 | I1, I3 |
| Specialty insurer or facility (for example AXA XL, Markel) | 1 | I4 |
| Broker (for example Marsh, Willis) | 1 | I2, I3 |
| Shipowner studying nuclear | 1 | I3 |

**Script**
- **I1.** What would you need to quote a nuclear ship or floating plant today?
- **I2.** Would you pay for port readiness and operating data per ship? How much?
- **I3.** What does a refused or delayed port call cost an owner? Would anyone insure it?
- **I4.** Would you provide capacity for a narrow cover designed with a data partner?

## 6. Gas detection integrity (8 calls)

Added 2026-10-07 as the bridge for reactor monitoring ([full review](gas-integrity/product-and-tech.md)).

**What every call must answer**

| Bet | Confirmed if they say | Killed if | Ask |
|---|---|---|---|
| **Pain:** tests, drift and records cause findings, delays or crew time | A recent finding, delay or detention, or hours per month on tests | Never flagged and tests take little time (GI4) | G1, G2 |
| **Who pays** (GI4, biggest risk) | A price per ship a year | Fewer than 3 of 8 would pay $8K per ship (kill 1) | G5 |
| **Mixed makers** (GI1) | Their fleet runs systems from 2 or more makers | One maker everywhere with a service deal they like | G3 |
| **Data access** (GI3) | Panels have Modbus or analog outputs they would let us read | Makers or class block it (kills 2 and 3) | G4, C2 |

**Who to call**

| Target | Count | Main question |
|---|---|---|
| Technical superintendents at ship managers running gas carriers or LNG fueled ships | 3 | G1, G3, G5 |
| Owners of methanol or ammonia fueled ships (for example the first ammonia ship operators) | 1 | G2, G5 |
| Port state control or vetting inspector (current or former) | 1 | G1: how often is gas detection cited today? |
| Class society machinery or automation surveyor | 1 | C2 |
| Gas detection maker or service company | 1 | G4 |
| Bunkering platform or test gas supplier (Ofiniti, Martek) | 1 | Partnership |

**Script**
- **G1.** When was gas detection last raised in an inspection or vetting? What happened next?
- **G2.** Walk me through a monthly gas detection test. Who does it, how long does it take, where is it recorded?
- **G3.** Which makers' gas detection systems run across your fleet?
- **G4.** Does your panel send readings to the ship's alarm system? Over what output?
- **G5.** What would you pay per ship a year for drift warnings and an inspector ready record?
- **C2.** (Class) Would a read only connection to a gas panel's existing output need new approval?

## 7. Scoring a call

| Score | Meaning |
|---|---|
| 3 | Named a price or budget, or offered data, an intro or a pilot |
| 2 | Confirmed the pain with a past example |
| 1 | Interested, no example |
| 0 | Said the pain does not exist or is solved |

Re-score the idea after every 5 calls ([method §4](method.md#4-update-rules)).

## 8. Call log

| Date | Idea | Who (role, not name) | Score | Key quote | Next step |
|---|---|---|---|---|---|
| | | | | | |
