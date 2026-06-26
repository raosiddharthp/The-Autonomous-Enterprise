# The Autonomous Enterprise
## Governance Layer · Autonomous Enterprise Platform

**A production-grade, TOGAF-aligned AI Solutions Architecture for ClaraVis Medical Systems**  
Built by [Siddharthan Rao](https://github.com/raosiddharthp) · TOGAF EA · Google MLE · Google Cloud Architect · SAFe SA + SPC

---

[![Live Site](https://img.shields.io/badge/Live%20Site-GitHub%20Pages-blue)](https://raosiddharthp.github.io/The-Autonomous-Enterprise/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GCP](https://img.shields.io/badge/Cloud-Google%20Cloud%20Platform-4285F4)](https://cloud.google.com)
[![EU AI Act](https://img.shields.io/badge/Compliance-EU%20AI%20Act%20%C2%B7%20ISO%2013485-green)](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
[![Version](https://img.shields.io/badge/Version-2.0.0-informational)](changelog.html)

---

## Table of Contents

1. [What Is the Autonomous Enterprise Platform](#1-what-is-the-autonomous-enterprise-platform)
2. [The Four Pillars](#2-the-four-pillars)
3. [The Governance Platform — The Autonomous Enterprise](#3-the-governance-platform--the-autonomous-enterprise)
4. [Anchor Client: ClaraVis Medical Systems](#4-anchor-client-claravis-medical-systems)
5. [Architecture Overview](#5-architecture-overview)
6. [Governance Layer Dashboards](#6-governance-layer-dashboards)
7. [Module Index — AE Platform](#7-module-index--ae-platform)
8. [Portfolio Navigation](#8-portfolio-navigation)
9. [Architecture Decision Records](#9-architecture-decision-records)
10. [Key Design Principles](#10-key-design-principles)
11. [Regulatory & Compliance Posture](#11-regulatory--compliance-posture)
12. [The München Narrative — Cross-Module Thread](#12-the-münchen-narrative--cross-module-thread)
13. [Infrastructure & Deployment](#13-infrastructure--deployment)
14. [About](#14-about)

---

## 1. What Is the Autonomous Enterprise Platform

**The Autonomous Enterprise Platform** is a system of systems — four end-to-end business-process pillars and a governing crown layer, each architected as a complete, production-grade system: from regulatory obligations and business requirements through TOGAF ADM architecture phases, agent swarm design, ML engineering, GCP infrastructure, and go-to-market strategy.

The Platform is unified by:

- A **shared anchor client** — ClaraVis Medical Systems, a €1.2B German MRI/CT imaging OEM — whose pain points drive every architectural decision across all four platforms.
- A **shared GCP data fabric** — BigQuery, Vertex AI Feature Store, Pub/Sub, Firestore — that the four pillars write to and read from, enabling cross-domain intelligence.
- A **shared governance layer** — The Autonomous Enterprise platform — that provides the Strategy Dashboard, Data Governance framework, GreenOps carbon management, and FinRisk Sentinel that sit above all four pillars.
- A **shared compliance posture** — EU AI Act Annex III, ISO 13485, ASC 606, GDPR, EU CSRD — enforced as write-path constraints, not post-hoc reports.

The Autonomous Enterprise (this repository) is the **governance platform** of the Autonomous Enterprise Platform — the layer that orchestrates, monitors, and provides cross-domain visibility across the Quote-to-Cash, Finance Operations, Procure-to-Pay, and Supply Chain pillars.

---

## 2. The Four Pillars

| Pillar | Domain | Live Site | Core Capability |
|--------|--------|-----------|-----------------|
| **The Autonomous Quote-to-Cash** | Commercial · Q2C | [raosiddharthp.github.io/The-Autonomous-Quote-to-Cash](https://raosiddharthp.github.io/The-Autonomous-Quote-to-Cash/) | Collapses 47-day CPQ cycle to under 9 days via ADK multi-agent orchestration, CCAI Sales Agent, and ContractGuard AI. |
| **The Autonomous Finance Operations** | Financial · RevRec · Risk | [raosiddharthp.github.io/The-Autonomous-Finance-Operations](https://raosiddharthp.github.io/The-Autonomous-Finance-Operations/) | EU AI Act-compliant revenue recognition (ASC 606), anomaly detection, and dual-reviewer financial risk governance. |
| **The Autonomous Procure-to-Pay** | Procurement · Sourcing | [raosiddharthp.github.io/The-Autonomous-Procure-to-Pay](https://raosiddharthp.github.io/The-Autonomous-Procure-to-Pay/) | AI-assisted supplier evaluation, contract negotiation, and procurement cycle compression via Gemini 1.5 Pro and Document AI. |
| **The Autonomous Supply Chain** | Operations · Logistics | [raosiddharthp.github.io/The-Autonomous-Supply-Chain](https://raosiddharthp.github.io/The-Autonomous-Supply-Chain/) | Predictive asset maintenance across 12,000+ installed MRI/CT units, IoT telemetry unification, and warranty reserve optimisation. |

> **Governance Layer** → The Autonomous Enterprise (this repository) provides the cross-cutting Strategy Dashboard (M-07), Data Governance (M-08), GreenOps (M-06), and FinRisk Sentinel (M-04) that span all four pillars.

---

## 3. The Governance Platform — The Autonomous Enterprise

The **Autonomous Enterprise** is not a fifth pillar — it is the platform layer that the four pillars run on. It provides:

| Capability | Module | What It Governs |
|------------|--------|-----------------|
| **Strategy Dashboard** | M-07 | Unified KPI visibility across all four pillars: revenue pipeline, fleet health, carbon emissions, financial risk — in a single Looker Studio–backed executive interface. |
| **Data Governance** | M-08 | TFX schema validation, Feature Store lineage, quarantine-then-review pipeline for all pillar data feeds. The H1 foundation that must be in place before any ML model can reach production. |
| **GreenOps Platform** | M-06 | CSRD Scope 1/2/3 carbon accounting across all pillar workloads; GKE intelligent job scheduling; Carbon Footprint API integration. |
| **FinRisk Sentinel** | M-04 | Real-time anomaly detection on payment and financial event streams across the Quote-to-Cash, Finance Operations, and Procure-to-Pay pillars. Dual-reviewer HITL (HITL-08). |
| **HITL Framework** | Platform | 11 named human oversight checkpoints (HITL-01 through HITL-11) spanning all eight modules, satisfying EU AI Act Article 14 as a structural property of the system. |
| **XAI / SHAP Layer** | Platform | SHAP explanations written to BigQuery before every HITL checkpoint. Immutable audit record. EU AI Act Article 13 transparency by design. |

---

## 4. Anchor Client: ClaraVis Medical Systems

The Autonomous Enterprise Platform is designed around a single, realistic anchor client. Every architectural decision is traceable to a ClaraVis business requirement or regulatory obligation.

| Attribute | Value |
|-----------|-------|
| **Headquarters** | Munich, Germany |
| **Revenue** | €1.2B |
| **Employees** | 4,200 |
| **Product Portfolio** | MRI & CT Imaging Systems |
| **Installed Base** | 12,000+ units across 34 countries |
| **Regulatory Exposure** | EU AI Act Annex III · FDA 21 CFR 820 · ISO 13485 · ASC 606 · GDPR · ISO 27001 · EU CSRD |

### The Three Pain Points

**Pain 01 — 47-Day CPQ Cycle Across 9 Manual Silos**  
Every MRI configuration requires sequential handoffs between Sales, Applications Engineering, Legal, Service, Finance, Revenue Recognition, Logistics, and Post-Sales. Target with the Autonomous Enterprise Platform: CPQ cycle under 9 days.  
→ *Addressed by: The Autonomous Quote-to-Cash (M-01, M-02)*

**Pain 02 — EU AI Act Exposure on Every ML Inference**  
Three existing predictive models classified as high-risk under EU AI Act Annex III, none producing human-reviewable explanations or documented oversight checkpoints.  
→ *Addressed by: HITL Framework (all modules), XAI/SHAP layer (M-03, M-04, M-05), Data Governance (M-08)*

**Pain 03 — 12,000 Units Across 6 Disconnected Telemetry Systems; €40M Warranty Over-Reserve**  
No unified asset event schema. Predictive maintenance impossible. Finance provisions worst-case every quarter.  
→ *Addressed by: The Autonomous Supply Chain (M-05), Data Governance (M-08), Strategy Dashboard (M-07)*

---

## 5. Architecture Overview

The Autonomous Enterprise implements a four-layer architecture. All four pillars of the Platform share this stack.

```
┌─────────────────────────────────────────────────────────────────────┐
│  PRESENTATION & EXPERIENCE LAYER                                    │
│  React · GitHub Pages · 8 AE module dashboards · 4 Pillar UIs     │
│  HITL Approval UI · XAI Viewer · Strategy Dashboard · Audit View   │
├─────────────────────────────────────────────────────────────────────┤
│  AGENT ORCHESTRATION LAYER                                          │
│  Google ADK · CCAI · A2A Protocol · MCP · Firestore state          │
│  5 specialist agents · 11 HITL checkpoints · circuit breakers      │
├─────────────────────────────────────────────────────────────────────┤
│  DATA & ML PLATFORM LAYER                                           │
│  Vertex AI Pipelines · Feature Store · SHAP/XAI · Model Registry   │
│  Pub/Sub event bus · BigQuery · MLOps CI/CD · Drift detection       │
├─────────────────────────────────────────────────────────────────────┤
│  INFRASTRUCTURE & GOVERNANCE LAYER                                  │
│  Terraform IaC · GKE Autopilot · Cloud Run · VPC-SC · CMEK        │
│  BeyondCorp · IAM · Workload Identity Federation · FinOps           │
└─────────────────────────────────────────────────────────────────────┘
```

**Infrastructure constraints (non-negotiable):**
- All workloads in `europe-west3` (Frankfurt) — data residency, GDPR, EU AI Act enforcement jurisdiction.
- All data at rest: CMEK-encrypted (Cloud KMS, customer-managed keys).
- All inter-service authentication: Workload Identity Federation — no long-lived service account keys.
- All consequential AI decisions: immutable HITL audit record in Firestore before any write operation proceeds.

---

## 6. Governance Layer Dashboards

The three governance dashboards are the cross-cutting intelligence layer of the Platform. They consume event streams from all four pillars and surface unified, executive-level visibility.

### M-07 — Strategy Dashboard

The unified command interface for the ClaraVis enterprise. Five panels, each fed by a materialised BigQuery view with a 15-minute refresh cycle.

| Panel | Data Source Pillars | Key Metric |
|-------|---------------------|------------|
| Revenue Pipeline | Autonomous Quote-to-Cash | Pipeline by stage, CPQ conversion rate, deal velocity |
| Fleet Health | Autonomous Supply Chain | RUL distribution across 12,000+ units, HITL queue depth |
| Financial Risk | Autonomous Finance Operations | Anomaly score distribution, open HITL-08 cases |
| Carbon Emissions | All (GreenOps) | Scope 1/2/3 actuals vs CSRD target, deferred job savings |
| Compliance Posture | All | HITL SLA breach rate, XAI coverage, model drift alerts |

**Drill-through:** Every cell in the dashboard links to the source module's HITL queue or model explanation viewer. The Strategy Dashboard is a navigation layer, not a destination.

**Technical:** BigQuery materialised views → Looker Studio semantic layer → embedded dashboard panels. Refresh triggered by Pub/Sub topic `ae.governance.dashboard.refresh`.

### M-08 — Data Governance Dashboard

The H1 foundation. Must be operational before any ML model reaches a production scoring endpoint.

| View | Purpose |
|------|---------|
| Schema Validation | TFX `ExampleValidator` pass/fail rate by pillar feed, quarantine queue depth |
| Feature Lineage | Vertex AI Feature Store — feature-to-model dependency graph, staleness alerts |
| Data Quality SLA | Record arrival latency, null rate, schema drift by source system |
| Quarantine Review | Steward interface: inspect quarantined records, approve reinstatement or permanent discard |

**Design principle — Quarantine, Never Discard:** Schema-violating records are written to `bq.ae_governance.quarantine` with full provenance metadata. Sensor data loss in a 12,000-unit field deployment is operationally irreversible. The steward reinstatement HITL (HITL-11) is the only path to either restoring or retiring a quarantined record.

### M-06 — GreenOps Platform Dashboard

CSRD EU Taxonomy–aligned carbon accounting. Scope 1 (direct), Scope 2 (energy), and Scope 3 (supply chain, asset lifecycle) tracked against ClaraVis's 2030 net-zero commitment.

| Panel | Data Source | Granularity |
|-------|-------------|-------------|
| Carbon Budget | Carbon Footprint API · GCP Billing | Per-project, per-module, per-quarter |
| GKE Scheduler | GKE Autopilot workload metadata | Per-batch-job, estimated deferral saving (kg CO₂e) |
| Scope 3 Attribution | Autonomous Supply Chain (M-05) | Per installed-unit lifecycle stage |
| CSRD Report Preview | All | Downloadable EU CSRD §29a compliant disclosure |

**Hard constraint — Hard-Deadline Bypass:** GreenOps never defers the daily RUL batch job (M-05) or the FinRisk model refresh (M-04). Only flexible weekly/monthly batch workloads are eligible for carbon-aware scheduling. This constraint is enforced at the GKE scheduler admission controller level, not as an application-layer check.

---

## 7. Module Index — AE Platform

| Module | Domain | Pillar | Key Architecture | HITL | Horizon |
|--------|--------|--------|-----------------|------|---------|
| [M-01 CCAI Sales Agent](page-09-m01.html) | Commercial | Autonomous Quote-to-Cash | ADK · CCAI · Dialogflow CX · Salesforce | HITL-01 (turn-11) | H3 |
| [M-02 ContractGuard](page-09-m02.html) | Commercial | Autonomous Quote-to-Cash | Document AI · Gemini 1.5 Pro 1M · XGBoost · Vector Store | HITL-02/03 | H2 |
| [M-03 RevRec AI](page-09-m03.html) | Financial | Autonomous Quote-to-Cash | XGBoost · SHAP · Salesforce + SAP · Vertex AI | HITL-04/05/09 | H2 |
| [M-04 FinRisk Sentinel](page-09-m04.html) | Financial | Autonomous Enterprise (Governance) | Isolation Forest · BigQuery streaming · dual-reviewer | HITL-08 (dual) | H2 |
| [M-05 Asset IQ](page-09-m05.html) | Operations | Autonomous Supply Chain | RUL regression · Isolation Forest · 12K units · ISO 13485 | HITL-06/07 | H2 |
| [M-06 GreenOps](page-09-m06.html) | Operations | Autonomous Enterprise (Governance) | Carbon Footprint API · GKE scheduling · CSRD Scope 3 | None | H3 |
| [M-07 Strategy Dashboard](page-09-m07.html) | Platform | Autonomous Enterprise (Governance) | BigQuery mat. views · Looker Studio · 5 panels | None | H3 |
| [M-08 Data Governance](page-09-m08.html) | Platform | Autonomous Enterprise (Governance) | TFX Validate · Feature Store lineage · quarantine | HITL-11 (steward) | H1 |

**Delivery Horizons:**
- **H1** — Compliance foundation. Must ship before EU AI Act enforcement deadline. Data Governance (M-08) is the sole H1 module because no ML model can reach production without it.
- **H2** — Intelligence layer. Revenue recognition, financial risk, contract analysis, predictive maintenance. ROI demonstrable within 2 quarters of deployment.
- **H3** — Autonomous operations. Sales agent, GreenOps, Strategy Dashboard. Built on H1/H2 foundation; delivers compound value as pillar data matures.

---

## 8. Portfolio Navigation

### Autonomous Enterprise — Design Pages (01–09)

| Page | Title | Coverage |
|------|-------|----------|
| [01](index.html) | The Autonomous Enterprise | Concept, Platform positioning, four-layer architecture |
| [02](page-02.html) | ClaraVis: Client Brief | Requirements, stakeholders, pain points, regulatory obligations |
| [03](page-03.html) | TOGAF ADM: Phases A–F | Architecture work products, migration horizons, ADRs 001–006 |
| [04](page-04.html) | Delivery & Product Design | SAFe ARTs, personas, FRD, 11 HITL checkpoints |
| [05](page-05.html) | Agent Swarm Architecture | ADK multi-agent, A2A protocol, 5 agent specs, circuit breakers |
| [06](page-06.html) | ML Engineering & MLOps | 5 model cards, Vertex AI Pipelines, SHAP, drift detection |
| [07](page-07.html) | Infrastructure & GCP | Terraform IaC, VPC-SC, GKE, Cloud Run, CMEK, chaos engineering |
| [08](page-08.html) | Go-to-Market Strategy | EU Act as forcing function, buyer map, horizon value, adoption risks |
| [09](page-09.html) | AE Platform — Module Index | All 8 modules, dependency matrix, demo pathways |

### Reference Documents

| Document | Coverage |
|----------|----------|
| [ADR Index](adr-index.html) | All 16 architecture decision records + module-specific ADRs |
| [Glossary](glossary.html) | Authoritative one-sentence definitions for every technical term |
| [Changelog](changelog.html) | Full version history with design rationale |

---

## 9. Architecture Decision Records

All 16 core ADRs are documented in [adr-index.html](adr-index.html). Key decisions relevant to the governance layer:

| ADR | Decision | Governance Relevance |
|-----|----------|----------------------|
| ADR-004 | Firestore for agent state and HITL audit | Immutable audit trail, BigQuery export for governance reporting |
| ADR-005 | SHAP over LIME for XAI layer | Deterministic TreeExplainer — audit record cannot vary between runs |
| ADR-006 | Pub/Sub as integration event bus | Governance dashboards subscribe to all pillar event streams without coupling |
| ADR-010 | XGBoost over neural network for RevRec/ContractGuard | EU AI Act Art. 13 — SHAP TreeExplainer requires tree-based model |
| ADR-011 | Isolation Forest for anomaly detection | TreeExplainer compatible — FinRisk Sentinel HITL-08 can surface feature contributions |
| ADR-012 | Vertex AI Pipelines for MLOps | ML Metadata store — Data Governance (M-08) queries pipeline lineage directly |
| ADR-013 | Shared VPC over separate VPCs per module | Governance layer has network-level visibility across all pillar workloads |
| ADR-015 | GKE Autopilot for batch ML | GreenOps can schedule and defer any Autopilot workload via the node pool API |
| ADR-016 | Phased adoption (H1→H2→H3) | Data Governance (H1) is the contractual gate for all H2 ML modules |

---

## 10. Key Design Principles

These are architectural constraints, not guidelines. Every component of the Autonomous Enterprise Platform satisfies all five.

**1. SHAP Before HITL**  
Every SHAP explanation is written to BigQuery (`ae_governance.xai_audit`) before the HITL checkpoint record is created in Firestore. The audit record structurally cannot reference an explanation that doesn't exist. Retrospective amendment is architecturally impossible.

**2. SAP Write Guard**  
The `sap.post_journal_entry()` function signature requires a `hitl_id` parameter. The SAP GL write is unreachable without a committed human approval record. This is a code-level constraint, not a process-level one.

**3. Quarantine, Never Discard**  
Schema-violating records are written to the quarantine table with full provenance. Data loss in a field sensor deployment is operationally irreversible. The steward HITL (HITL-11) is the only legal exit from quarantine.

**4. Hard-Deadline Bypass**  
GreenOps never defers the daily RUL batch job or FinRisk model refresh. Only flexible weekly/monthly jobs are carbon-deferral eligible. Enforced at the GKE admission controller, not application code.

**5. Augmentation, Not Replacement**  
ADR-002. Salesforce and SAP remain unchanged. The Autonomous Enterprise Platform is the orchestration and intelligence layer above them. No existing system is deprecated in H1 or H2.

---

## 11. Regulatory & Compliance Posture

| Regulation | Scope | How the Platform Satisfies It |
|-----------|-------|---------------------------|
| **EU AI Act Annex III** | All high-risk ML modules (M-02, M-03, M-04, M-05) | HITL checkpoints (Art. 14), SHAP explanations (Art. 13), Model Cards (Art. 11), Data Governance (Art. 10) |
| **EU AI Act Article 14** | Human oversight on all high-risk decisions | HITL-01 through HITL-11: each a formal state machine node with named actor, SLA, and immutable audit record |
| **ISO 13485** | Medical device quality management | Asset IQ (M-05) maintenance records, HITL-06/07 sign-off, Device History Record integration |
| **FDA 21 CFR 820** | Design controls for medical devices | Asset IQ model validation, HITL approval chain, immutable Firestore audit records |
| **ASC 606 / IFRS 15** | Revenue recognition | RevRec AI (M-03) classification with SHAP justification, HITL-04/05 Finance Controller approval, SAP write guard |
| **GDPR** | Personal data processing | VPC-SC data residency (`europe-west3`), CMEK, BeyondCorp access control, Data Governance lineage |
| **ISO 27001** | Information security | Cloud Armor WAF, Binary Authorization, Workload Identity Federation, Secret Manager rotation |
| **EU CSRD** | Sustainability reporting | GreenOps (M-06) Scope 1/2/3 accounting, automated CSRD §29a disclosure generation |

---

## 12. The München Narrative — Cross-Module Thread

A single account — **Universitätsklinikum München** — appears across five module demos, proving that the AE Platform modules form a coherent workflow, not independent tools.

```
ContractGuard (M-02)        RevRec AI (M-03)           Asset IQ (M-05)
Analyses MRI-7T             Classifies €2.84M          Monitors unit
purchase contract →         contract as                 MRI-7T-MCH-0042 →
flags liability cap →       MULTI-ELEMENT →             predicts 8.4d RUL →
Legal approves              Finance approves,           Field Service
counter-position            SAP posts                   schedules maintenance
        ↓                          ↓                           ↓
FinRisk Sentinel (M-04)                          Strategy Dashboard (M-07)
Detects anomalous payment                        MCH-0042 visible in
from same account →                              fleet panel; drill-through
CFO + Controller notified                        links to Asset IQ HITL queue
```

This narrative is the portfolio's proof-of-concept for the governance platform: the Strategy Dashboard (M-07) is the single pane of glass where all five thread events are visible simultaneously.

---

## 13. Infrastructure & Deployment

### GCP Infrastructure

All workloads are deployed to `europe-west3` (Frankfurt).

```hcl
# infrastructure/main.tf (representative)
module "ae_shared_vpc" {
  source       = "./modules/shared-vpc"
  region       = "europe-west3"
  project_id   = var.project_id
  cmek_key_id  = google_kms_crypto_key.ae_cmek.id
}

module "ae_governance_layer" {
  source        = "./modules/governance"
  vpc_id        = module.ae_shared_vpc.network_id
  bq_dataset    = "ae_governance"
  pubsub_topics = ["dashboard.refresh", "xai_audit", "hitl.events"]
}
```

Key infrastructure decisions: GKE Autopilot (batch ML, ADR-015), Cloud Run (stateless agent services, ADR-003), Shared VPC (ADR-013), Terraform remote state in GCS with CMEK, VPC-SC perimeter isolating all data plane services.

### Portfolio Deployment

This portfolio is a static GitHub Pages site. No build step. No framework. No backend.

```bash
git clone https://github.com/raosiddharthp/The-Autonomous-Enterprise.git
cd The-Autonomous-Enterprise
python -m http.server 8000
# Open http://localhost:8000
```

All internal navigation uses relative paths (`href="page-02.html"`) — resolves correctly locally and on GitHub Pages without configuration.

**GitHub Pages:** Settings → Pages → Source: `main` branch root.

---

## 14. About

**Siddharthan Rao** — AI Solutions Architect · TOGAF EA Certified · Google MLE · Google Cloud Architect · SAFe SA + SPC

22 years in technology: 10 technical writing · 7 training/GSIs · 6 Salesforce solutions architecture · 15 years Salesforce CPQ/Q2C depth.

[GitHub](https://github.com/raosiddharthp) · [LinkedIn](#) · [The Autonomous Quote-to-Cash](https://raosiddharthp.github.io/The-Autonomous-Quote-to-Cash/) · [The Autonomous Finance Operations](https://raosiddharthp.github.io/The-Autonomous-Finance-Operations/) · [The Autonomous Procure-to-Pay](https://raosiddharthp.github.io/The-Autonomous-Procure-to-Pay/) · [The Autonomous Supply Chain](https://raosiddharthp.github.io/The-Autonomous-Supply-Chain/)

---

*The Autonomous Enterprise Platform and ClaraVis Medical Systems are portfolio artefacts. ClaraVis is a fictional company; all metrics are illustrative of a plausible enterprise at the described scale.*

© 2026 Siddharthan Rao · The Autonomous Enterprise
