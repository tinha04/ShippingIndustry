# Gas Detection Integrity: Build Guide (Bench Rig)

[Back to README](../../README.md) · [Startup plan](startup-plan.md) · [YC application](yc-application.md) · [Product](product-and-tech.md) · [Market](market.md) · [Competition](competition.md) · [Risks](risks.md) · [Build plan](build-plan.md) · [Build guide](build-guide.md) · [Evidence](evidence.md) · [YC review](yc-review.md)

Written 2026-10-07. Order parts on November 3, after Kairos's YC application. Prices are search snapshots [32 to 36]; check every price, lead time and outlet thread at checkout. Currency conversions are rough (E).

**Goal:** prove on the bench that the box and app catch the Coast Guard's findings (drift, out of tolerance readings, wrong span gas) [1] at least 9 times in 10, with no false "healthy", and that a monthly test is faster than paper ([build plan](build-plan.md#2-bench)).

**Shared hardware:** the data box below is the same box as the [reactor monitoring bench](../monitoring/build-plan.md). Monitoring adds a radiation sensor, GNSS, a tamper switch and a commercial data diode.

## 1. Tier 1: core bench (build first)

| Part | Example | Price (snapshot) | Backup | Evidence |
|---|---|---|---|---|
| Computer | Raspberry Pi 5, 8GB | About $150 list, $199 street | Industrial Pi gateway ($200 to $400, E) | [36] |
| RS485 (Modbus RTU) | Waveshare RS485 CAN HAT | $13.99 | Waveshare isolated 2 channel version (about A$36) | [36] |
| Isolated 4 to 20 mA inputs | Sequent Microsystems Industrial Automation HAT (4 inputs) | $120 | Sequent Multi IO HAT (2 inputs, $95) | [36] |
| Signing key | Adafruit ATECC608 breakout | $4.95 | SparkFun ATECC608A (about A$9) | [36] |
| Storage, power, enclosure | Industrial microSD or SSD; 24 V DIN supply; enclosure | $110 to $290 (E) | | E |
| Ammonia sensor (Modbus) | Seeed industrial Modbus RS485 NH3 sensor | About A$320 (about $210) | ACI CTS-M5220X, 4 to 20 mA or Modbus ($972) | [33] |
| Methane sensor (Modbus) | Renke RS-CH4-N01-2, 0 to 100% LEL | About ₹7,519 (about $90) | Unbranded 4 to 20 mA plus RS485 detector ($203); check sensing type | [34] |
| Panel emulator | A second Pi or a microcontroller serving a Modbus register map copied from a real panel manual (build plan step 1) | $10 to $80 (E) | | E |
| Test gas, methane | 50% LEL (2.5%) methane in air, 34 L | $75 to $325 | | [35] |
| Test gas, ammonia | 25 ppm ammonia in nitrogen, 34 L | From $263 plus $120 hazmat fee (special order, no returns) | 25 ppm ammonia in air ($325.50) | [35] |
| Seeded fault gas | Methane in nitrogen (no oxygen), for the wrong span gas case | $100 to $300 (E, not priced) | | E |
| Regulators | Fixed flow 0.5 L/min; stainless for ammonia; match each cylinder's outlet (C10 or CGA-600) | $145 to $164 each, 1 to 2 needed | BW REG-0.5 ($240) | [35] |
| Calibration cup and tubing | Fits the sensor heads | $20 to $50 (E) | | E |
| Tablet | Any recent Android tablet for the test app | $150 to $250 (E) | | E |
| Personal ammonia monitor | For the person running ammonia tests | $100 to $500 (E) | | E |
| **Tier 1 total** | | **About $1,700 to $3,300** | | |

## 2. Tier 2: real panel (only before a pilot, if a manager names a panel)

| Part | Example | Price (snapshot) | Evidence |
|---|---|---|---|
| Fixed gas controller with Modbus | MSA 9010/9020 | £1,586 (about $2,000) | [32] |
| or used controller | Honeywell Touchpoint Plus (confirm the Modbus option) | About $3,500 asking | [32] |
| Catalytic methane transmitter with Modbus | Engenuity Q8-CH4-100L (catalytic bead, so the wrong span gas fault is physical, not only a rule check) | $1,795 | [34] |
| 4 to 20 mA ammonia transmitter | ACI CTS-M5220X | $972 | [33] |
| **Tier 2 total** | | **About $4,800 to $6,300** | |

## 3. Steps

| Step | Work | Pass |
|---|---|---|
| 1 | Assemble the box: Pi 5, RS485 HAT, 4 to 20 mA HAT, ATECC608 on I2C; install the OS; lock it down (no inbound services) | Box boots and reads all inputs |
| 2 | Logger: read Modbus registers and 4 to 20 mA channels every second; append each reading to a hash chain; sign each block with the ATECC608 key; keep everything offline | 7 days offline with no gaps |
| 3 | Verifier on a laptop: re-checks the chain and signatures | Detects any edited, deleted or reordered record |
| 4 | Panel emulator: serve the register map of one real panel (readings, alarms, faults); the box reads it like a ship panel | Box decodes all points correctly |
| 5 | Baseline: 24 hours of zero readings; record noise per sensor | Noise known per sensor |
| 6 | Correct function tests: apply 50% LEL methane and 25 ppm ammonia at 0.5 L/min; record reading and response time (T90) | Results within the maker's tolerance |
| 7 | Seeded faults, 10 runs: zero offset (drift), slow response (restricted flow), dead or stuck sensor, out of tolerance reading, wrong span gas (methane in nitrogen on a catalytic sensor; a rule check in Tier 1), expired cylinder, skipped sensor | At least 9 of 10 flagged; 0 false "healthy" |
| 8 | Guided test app v0: steps per sensor, tolerance rules from the manual, cylinder label photo, one click report | Report a ship officer could hand to an inspector |
| 9 | Time trial: 10 sensor monthly test with the app against a paper log | App faster than paper |

## 4. Safety

- Certified low concentration test gases only: methane at 50% LEL (below the flammable range as delivered) and ammonia at 25 ppm. Never pure ammonia or pure methane on the bench.
- Ventilated room; vent the calibration cup exhaust away from people. Wear the personal ammonia monitor during ammonia tests.
- Secure cylinders upright; keep the safety data sheets on the bench; follow hazmat rules for shipping and storage.
- Stainless regulator for ammonia; never swap regulators between ammonia and other gases.
- The box is read only and lives in a safe area; it never writes to a panel or silences alarms.

## 5. Overfitting warning

Bench sensors are not marine type approved panels; the emulator copies one maker's register map; seeded faults are our guesses at real failures. A pass here proves the software and record, not performance on a ship. The ship pilot is the real test.
