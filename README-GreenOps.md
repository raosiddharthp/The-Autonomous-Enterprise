> ### 🏛️ The Autonomous Enterprise Platform
> **Governance Layer** → [The Autonomous Enterprise](https://raosiddharthp.github.io/The-Autonomous-Enterprise/) &nbsp;|&nbsp; You are here: **GreenOps Platform (M-06)**
>
> **Process Pillars:** [Quote-to-Cash](https://raosiddharthp.github.io/The-Autonomous-Quote-to-Cash/) · [Procure-to-Pay](https://raosiddharthp.github.io/The-Autonomous-Procure-to-Pay/) · [Finance Operations](https://raosiddharthp.github.io/The-Autonomous-Finance-Operations/) · [Supply Chain](https://raosiddharthp.github.io/The-Autonomous-Supply-Chain/)
> **Governance Crown:** [Strategy Dashboard](https://raosiddharthp.github.io/The-Autonomous-Strategy-Dashboard/) · [Data Governance](https://raosiddharthp.github.io/The-Autonomous-Data-Governance/) · [Compliance Command Centre](https://raosiddharthp.github.io/The-Autonomous-Compliance/) · [FinRisk Sentinel](https://raosiddharthp.github.io/The-Autonomous-FinRisk/)

---

# GreenOps Platform

**M-06 · Governance Layer · Carbon-Aware Scheduling**

### Defer when the grid is dirty. Dispatch when it's clean.

GreenOps is one of five governance modules in **The Autonomous Enterprise Platform** — a system of systems spanning four end-to-end business process pillars and a governing crown layer. GreenOps itself is the only fully autonomous service in that crown — no HITL checkpoint, no human decision path, no ML inference. It is a deterministic scheduling decision engine that shifts every flexible batch workload across all four process pillars to low-carbon grid windows, without touching a single line of domain logic in any pillar.

Hard-deadline jobs are never deferred. That constraint is enforced at the GKE Autopilot admission-controller level — not as an application-layer check that a misconfigured flag could bypass.

---

## What It Does

GreenOps re-evaluates every deferred job against the latest grid carbon intensity forecast on a 30-minute loop. A job deferred 90 minutes ago because the grid was running at 142 gCO₂eq/kWh gets re-checked the moment a low-carbon window opens — and dispatches automatically. No human approves this. No human needs to.

| | |
|---|---|
| **Deferral window** | ±6 hours from submission (flexible jobs only) |
| **Re-evaluation cadence** | Every 30 minutes |
| **Hard-deadline jobs** | Never deferred — enforced at GKE admission controller |
| **HITL checkpoints** | None — the only AE Platform service with zero human decision path |
| **Horizon** | H3 · PI-7 · Minimal Risk classification |

**The five-state job lifecycle has no dead end.** Every job reaches `COMPLETE`. Window-expired jobs force-dispatch at whatever the current grid intensity is — the ESG record reports `saving_pct: 0%` honestly in the worst case, rather than hiding the miss.

---

## What Gets Deferred — and What Never Does

| Job | Pillar / Module | Deadline Type | Deferral |
|---|---|---|---|
| Weekly model retraining (RevRec AI) | Quote-to-Cash · M-03 | Soft | ✓ ±6h |
| Weekly model retraining (Asset IQ RUL) | Quote-to-Cash · M-05 | Soft | ✓ ±6h |
| Weekly model retraining (ContractGuard) | Quote-to-Cash · M-02 | Soft | ✓ ±6h |
| Daily feature pipeline backfill | Platform · M-08 | Soft | ✓ ±3h |
| **Daily RUL batch prediction** | Quote-to-Cash · M-05 | **Hard** — Field Service queue same day | ✗ Never |
| **FinRisk anomaly model refresh** | Quote-to-Cash · M-04 | **Hard** — streaming model currency | ✗ Never |
| ContractGuard vector store reindex | Quote-to-Cash · M-02 | Soft | ✓ ±12h |

This is the precedent the GreenOps design generalises to every pillar: anything that feeds a same-day human decision is hard. Anything that just needs to be fresh by next week is flexible.

---

## Architecture

**Four deployable containers, one scheduling boundary**, inside a single VPC-SC perimeter (`europe-west3`):

1. **Cloud Scheduler** — external trigger, submits `job_id · suite_id · deadline · flexibility_window`
2. **GreenOps Agent** (Cloud Run, always-on, `min-instances:1`) — carbon intensity forecaster, scheduling decision engine, job dispatcher
3. **Firestore** — `deferred_jobs` collection, TTL on `window_expiry`
4. **BigQuery** — `ae_greenops.job_metrics`: actual intensity, estimated kWh, metered kWh, carbon saved, CSRD eligibility flag — written per dispatch, audit-traceable

A circuit breaker wraps every Carbon Footprint API call. On timeout or 5xx, GreenOps enters degraded mode: all queued jobs dispatch immediately with `api_fallback:true` flagged in the ESG record. Scheduling resumes automatically on the next successful API response. The system fails safe, not silent.

**Service account:** `greenops-sa@` — scoped to `roles/run.invoker`, `roles/datastore.user`, `roles/bigquery.dataEditor`, `roles/monitoring.viewer`. Nothing broader.

---

## Compliance Output

GreenOps exists for one regulatory reason beyond cost: **EU CSRD Scope 3, Category 11** reporting. Every dispatch decision writes an immutable, queryable ESG record — `kgCO₂eq saved`, `metered_kwh`, `csrd_eligible` — that rolls up into the platform-wide sustainability disclosure ClaraVis Medical Systems is obligated to file under EU Taxonomy rules.

The constraint that makes this trustworthy: **Hard-Deadline Bypass is enforced at the infrastructure layer.** GreenOps cannot defer the daily Asset IQ RUL batch or the FinRisk model refresh, no matter what the carbon forecast says — because deferring either one risks a missed maintenance window or a stale fraud model, and no carbon saving is worth that trade. The GKE admission controller — not application code — makes this true.

---

## Where This Sits in the Platform

GreenOps serves every process pillar equally and every future pillar by default — it has no domain-specific logic to update when a fifth pillar joins the platform. It reads job metadata; it doesn't care what the job does.

It is the second of three platform services to deploy, after Data Governance (M-08, the H1 foundation every pillar depends on) and alongside the Strategy Dashboard (M-07), which reads the GreenOps ESG feed as one of its five executive panels.

[**← AE Platform Index**](https://raosiddharthp.github.io/The-Autonomous-Enterprise/page-09.html) · [**Strategy Dashboard →**](https://raosiddharthp.github.io/The-Autonomous-Strategy-Dashboard/)

---

*Part of [The Autonomous Enterprise Platform](https://raosiddharthp.github.io/The-Autonomous-Enterprise/) — a system of systems for AI-native enterprise governance, anchored on ClaraVis Medical Systems, a €1.2B German MRI/CT imaging OEM. ClaraVis is a fictional company; all metrics are illustrative of a plausible enterprise at the described scale.*

© 2026 Siddharth Rao Potukuchi
