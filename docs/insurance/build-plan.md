# Insurance: Build and Validation Plan

[Back to README](../../README.md) · [Product](product-and-tech.md) · [Market](market.md) · [Competition](competition.md) · [Risks](risks.md) · [Build plan](build-plan.md) · [Evidence](evidence.md) · [YC review](yc-review.md)

Owner split: the business co-founder runs insurer calls; the technical co-founder builds the risk model on top of the readiness data (idea 1). Validation only until after Kairos's YC application (November 2).

## 1. Interviews (6)

Targets, bets, script and call log: [playbook](../playbook.md#5-insurance-6-calls).

## 2. Build

| Step | Work | Pass condition |
|---|---|---|
| 1 | **Cover map:** for a nuclear ship and a floating plant, list every cover needed (hull, P&I, nuclear liability, cargo, port, crew), what is excluded where (CL370, RACE II, P&I reinsurance), what limits exist ($50M [2]) and who offers them [1 to 3, 11 to 15] | An underwriter confirms the map in one call |
| 2 | **Risk model v0:** transparent factor scores per ship, reactor and route; port readiness scores from idea 1 as inputs | An underwriter can explain every score from the factors |
| 3 | **Port refusal or delay cover sketch:** trigger (port refuses entry, or holds the ship beyond an agreed time), payout, data source for the trigger, price range from readiness scores | One capital partner and one shipowner say it is worth pricing |
| 4 | **Data room demo:** readiness evidence and a sample operating record (idea 2) with access logs | An insurer says it would use it in a quote |
| 5 | **Partner:** a data agreement with one of Northcourt, Markel and Willis, AXA XL or NorthStandard | Signed letter of intent |

## 3. Decision gate

After 6 calls and step 3: promote to Strong candidate if at least 2 insurers would pay for risk data or 1 capital partner would price port refusal cover. Otherwise keep insurance as a feature of readiness (risk data export) and stop building it as its own product.

## 4. Diligence log

| Date | Claim | Status | Finding |
|---|---|---|---|
| 2026-10-07 | Nuclear ships can buy normal marine cover | **No** | Excluded almost everywhere [1, 3]; $50M limit [2] |
| 2026-10-07 | A specialist nuclear underwriting agency exists | **Yes, for plants** | Northcourt since 2010 [12] |
| 2026-10-07 | Big insurers are entering | **Yes** | AXA XL in NEMO [10]; Markel and Willis facility [11]; Marsh for TerraPower [15] |
| 2026-10-07 | A liability treaty is coming | **Started, years away** | IMO legal group asked to begin (January 2026) [5] |
| 2026-10-07 | Port refusal cover exists | **Not found** | H; ask brokers |
