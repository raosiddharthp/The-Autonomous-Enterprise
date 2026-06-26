> ### 🏛️ The Autonomous Enterprise Platform
> **Governance Layer** → [The Autonomous Enterprise](https://raosiddharthp.github.io/The-Autonomous-Enterprise/) &nbsp;|&nbsp; You are here: **Strategy Dashboard (M-07)**
>
> **Process Pillars:** [Quote-to-Cash](https://raosiddharthp.github.io/The-Autonomous-Quote-to-Cash/) · [Procure-to-Pay](https://raosiddharthp.github.io/The-Autonomous-Procure-to-Pay/) · [Finance Operations](https://raosiddharthp.github.io/The-Autonomous-Finance-Operations/) · [Supply Chain](https://raosiddharthp.github.io/The-Autonomous-Supply-Chain/)
> **Governance Crown:** [GreenOps](https://raosiddharthp.github.io/The-Autonomous-GreenOps/) · [Data Governance](https://raosiddharthp.github.io/The-Autonomous-Data-Governance/) · [Compliance Command Centre](https://raosiddharthp.github.io/The-Autonomous-Compliance/) · [FinRisk Sentinel](https://raosiddharthp.github.io/The-Autonomous-FinRisk/)

---

# Strategy Dashboard

**M-07 · Governance Layer · The Unified Intelligence View**

### All pillars. All signals. One screen.

The Strategy Dashboard is the platform-layer aggregation surface for **The Autonomous Enterprise Platform** — the single pane of glass where every process pillar's executive-relevant signal becomes visible at once. It is deliberately the dumbest module in the system: **it writes nothing, decides nothing, and infers nothing.** It is only meaningful because the data fabric beneath it — validated by Data Governance, scheduled by GreenOps — is running correctly.

---

## What It Does

Five panels, each fed by a materialised BigQuery view with a 15-minute refresh cycle:

| Panel | Reads From | Key Metric |
|---|---|---|
| Revenue Pipeline | Quote-to-Cash | Pipeline by stage, CPQ conversion rate, deal velocity |
| Fleet Health | Supply Chain | RUL distribution, HITL queue depth |
| Financial Risk | Finance Operations | Anomaly score distribution, open dual-reviewer cases |
| Carbon Emissions | GreenOps (all pillars) | Scope 1/2/3 actuals vs. CSRD target, deferred-job savings |
| Compliance Posture | All (via Data Governance, Compliance Command Centre) | HITL SLA breach rate, XAI coverage, model drift alerts |

**Every cell drills through.** Click a fleet health anomaly and you land in the Asset IQ HITL queue. Click a financial risk spike and you land in FinRisk Sentinel's anomaly detail view. The Strategy Dashboard is a navigation layer, not a destination.

---

## An Honest Scope Note

Current scope covers the **Quote-to-Cash** pillar and the platform-layer modules in full. **Procure-to-Pay and Supply Chain panels are on the roadmap** as those pillars mature into the same data-fabric contract Quote-to-Cash already satisfies. This dashboard does not pretend to show signals it doesn't yet have — a panel with no qualifying data source stays absent rather than getting populated with placeholder numbers.

This is a deliberate design stance, not an oversight: a unified executive view is only trustworthy if it's honest about what it doesn't yet cover.

---

## Architecture

**System Context (C4 Level 1):** every pillar's dataset in, one C-suite view out. The dashboard layer has no write path to any pillar — a one-way mirror, by design.

**Technical:** BigQuery materialised views → Looker Studio semantic layer → embedded dashboard panels. Refresh triggered by Pub/Sub topic `ae.governance.dashboard.refresh`. Sub-5-second render on cached views.

**Production readiness:** five views, five independent SLOs, one IAM boundary, zero silent failures. If a source pillar's data fabric goes stale, the corresponding panel shows a staleness flag — it does not show last week's number as if it were current.

---

## Architecture Decision Records

Three dashboard decisions, each chosen over a documented alternative with cost evidence:

- **Looker Studio over a custom React dashboard** — semantic layer reuse, no bespoke charting library to maintain, native BigQuery materialised-view binding
- **Materialised views over live query** — 15-minute refresh cadence is acceptable for executive consumption; live query cost at this read volume would be prohibitive
- **Pub/Sub-triggered refresh over polling** — refresh fires on actual upstream data change, not on a fixed clock that might run stale or redundant

---

## Where This Sits in the Platform

The Strategy Dashboard is the last platform service to close the loop — it depends on Data Governance (H1, validates everything it reads) and GreenOps (whose ESG feed is one of its five panels) being operational first. It is the screen a CFO, CRO, or CCO actually opens every morning; everything else in the platform exists, in part, to make this screen trustworthy.

[**← AE Platform Index**](https://raosiddharthp.github.io/The-Autonomous-Enterprise/page-09.html) · [**Compliance Command Centre →**](https://raosiddharthp.github.io/The-Autonomous-Compliance/)

---

*Part of [The Autonomous Enterprise Platform](https://raosiddharthp.github.io/The-Autonomous-Enterprise/) — a system of systems for AI-native enterprise governance, anchored on ClaraVis Medical Systems, a €1.2B German MRI/CT imaging OEM. ClaraVis is a fictional company; all metrics are illustrative of a plausible enterprise at the described scale.*

© 2026 Siddharth Rao Potukuchi
