# The Autonomous Enterprise

**A portfolio-grade AI Solutions Architecture for ClaraVis Medical Systems**
Built by [Siddharthan Rao](https://github.com/raosiddharthp) · TOGAF EA · Google MLE · Google Cloud Architect

---

## What this is

The Autonomous Enterprise is a complete enterprise AI architecture portfolio — nine design pages, eight module pages, an ADR index, a glossary, and a build specification — built around a single anchor client: ClaraVis Medical Systems, a €1.2B German MRI/CT imaging OEM with 12,000+ installed units across 34 countries.

It demonstrates how a production-grade AI platform is designed from first principles: starting from a client brief and regulatory obligations, through TOGAF ADM architecture phases, through SAFe delivery planning, through agent swarm design, ML engineering, infrastructure, and go-to-market strategy — and ending with eight fully specified AE modules, each with system context diagrams, GCP architecture, formal state machines, data flow sequences, HITL interfaces, ADRs, stakeholder rebuttals, and scripted demo pathways.

**Live site:** [raosiddharthp.github.io/The-Autonomous-Enterprise](https://raosiddharthp.github.io/The-Autonomous-Enterprise/)

---

## Navigation

### Portfolio Pages (01–09)

| Page | Title | What it covers |
|------|-------|----------------|
| [01](index.html) | The Autonomous Enterprise | Concept, positioning, the four-layer architecture |
| [02](page-02.html) | ClaraVis: Client Brief | Requirements, stakeholders, pain points, regulatory exposure |
| [03](page-03.html) | TOGAF ADM: Phases A–F | Architecture work products, migration horizons, ADRs 001–006 |
| [04](page-04.html) | Delivery & Product Design | SAFe ARTs, personas, FRD, 11 HITL checkpoints |
| [05](page-05.html) | Agent Swarm Architecture | ADK multi-agent design, A2A protocol, five agent specs, circuit breakers |
| [06](page-06.html) | ML Engineering & MLOps | Five model cards, Vertex AI Pipelines, SHAP, drift detection, MLE decisions |
| [07](page-07.html) | Infrastructure & GCP | Terraform IaC, VPC-SC, GKE, Cloud Run, CMEK, Chaos Engineering, runbook |
| [08](page-08.html) | Go-to-Market Strategy | Buyer map, horizon value, adoption risks, ADR-016 |
| [09](page-09.html) | AE Suite — Module Index | All 8 modules, dependency matrix, demo pathway index |

### Module Pages (M-01 through M-08)

| Module | Domain | Key architecture | HITL | Horizon |
|--------|--------|-----------------|------|---------|
| [M-01 CCAI Sales Agent](page-09-m01.html) | Commercial | ADK multi-agent · CCAI · Dialogflow CX · Salesforce | HITL-01 (turn-11 escalation) | H3 |
| [M-02 ContractGuard](page-09-m02.html) | Commercial | Document AI · Gemini 1.5 Pro 1M · XGBoost · Vector Store | HITL-02/03 | H2 |
| [M-03 RevRec AI](page-09-m03.html) | Financial | XGBoost · SHAP · Salesforce + SAP · Vertex AI | HITL-04/05/09 | H2 |
| [M-04 FinRisk Sentinel](page-09-m04.html) | Financial | Isolation Forest · BigQuery streaming · dual-reviewer | HITL-08 (dual) | H2 |
| [M-05 Asset IQ](page-09-m05.html) | Operations | RUL regression · Isolation Forest · 12K units · ISO 13485 | HITL-06/07 | H2 |
| [M-06 GreenOps Platform](page-09-m06.html) | Operations | Carbon Footprint API · GKE scheduling · CSRD Scope 3 | None | H3 |
| [M-07 Strategy Dashboard](page-09-m07.html) | Platform | BigQuery materialised views · Looker Studio · 5 panels | None | H3 |
| [M-08 Data Governance](page-09-m08.html) | Platform | TFX Validate · Feature Store lineage · quarantine | Steward (reinstatement) | H1 |

### Reference Documents

| Document | What it covers |
|----------|----------------|
| [ADR Index](adr-index.html) | All 16 architecture decisions + module-specific ADRs |
| [Glossary](glossary.html) | One-sentence definitions for all technical terms |
| [Changelog](changelog.html) | Version history and design evolution |

---

## The anchor client: ClaraVis Medical Systems

**Revenue:** €1.2B · **Employees:** 4,200 · **Installed base:** 12,000+ units · **Countries:** 34

**Three pain points that drive the entire architecture:**

1. **47-day CPQ cycle** across 9 manual silos — addressed by CCAI Sales Agent (M-01) and ContractGuard (M-02)
2. **3 ML models in production with no EU AI Act compliance posture** — addressed by the HITL framework, XAI layer, and Model Cards (Pages 04, 06)
3. **12,000 units across 6 disconnected regional telemetry systems with €40M warranty over-reserve** — addressed by Asset IQ (M-05) and Data Governance (M-08)

**Regulatory exposure:** EU AI Act Annex III · FDA 21 CFR 820 · ISO 13485 · ASC 606 · GDPR · ISO 27001 · EU CSRD

---

## Architecture overview

The AE is a four-layer platform:

```
┌─────────────────────────────────────────────────────┐
│  Presentation & Experience                          │
│  React · GitHub Pages · 8 app dashboards           │
│  HITL Approval UI · XAI Viewer · Audit Dashboard   │
├─────────────────────────────────────────────────────┤
│  Agent Orchestration                                │
│  Google ADK · CCAI · A2A · MCP · Firestore state   │
│  5 agents · 11 HITL checkpoints · circuit breakers │
├─────────────────────────────────────────────────────┤
│  Data & ML Platform                                 │
│  Vertex AI Pipelines · Feature Store · SHAP/XAI    │
│  Model Registry · Pub/Sub · BigQuery · MLOps        │
├─────────────────────────────────────────────────────┤
│  Infrastructure & Governance                        │
│  Terraform IaC · GKE · Cloud Run · VPC-SC · CMEK  │
│  BeyondCorp · IAM · Workload Identity · FinOps     │
└─────────────────────────────────────────────────────┘
```

All infrastructure is in GCP europe-west3. All data at rest is CMEK-encrypted. All inter-service authentication uses Workload Identity Federation. All consequential AI decisions have an immutable HITL audit record.

---

## The München narrative

A single account — Universitätsklinikum München — appears across five module demos, showing that the AE modules form a coherent workflow rather than independent tools:

1. **ContractGuard (M-02)** — analyses the MRI-7T purchase contract, flags the liability cap clause, Legal approves a counter-position
2. **RevRec AI (M-03)** — classifies the €2.84M contract as MULTI-ELEMENT, Finance Controller approves, SAP posts
3. **Asset IQ (M-05)** — monitors unit MRI-7T-MCH-0042 at that hospital, predicts 8.4 days RUL, Field Service Manager schedules maintenance
4. **FinRisk Sentinel (M-04)** — detects an anomalous payment from the same account, CFO and Finance Controller both notified
5. **Strategy Dashboard (M-07)** — MCH-0042 visible in the fleet panel, drill-through links back to the Asset IQ HITL queue

---

## Key design principles

1. **SHAP before HITL** — every SHAP explanation is written to BigQuery before the HITL checkpoint is created. The audit record cannot be retrospectively amended.
2. **SAP write guard** — the `sap.post_journal_entry()` function requires a `hitl_id` parameter. The SAP write is structurally unreachable without a committed human approval record.
3. **Quarantine-then-review** — schema-violating records are quarantined, not discarded. Data loss in a sensor system is irreversible.
4. **Hard-deadline bypass** — GreenOps never defers the daily RUL batch job or FinRisk model refresh. Only flexible weekly/monthly jobs are eligible for carbon deferral.
5. **Augmentation, not replacement** — ADR-002. Salesforce and SAP stay exactly where they are. The AE is the orchestration and intelligence layer above them.

---

## ADR summary (all 16 core decisions)

| ADR | Decision | Context |
|-----|----------|---------|
| ADR-001 | Salesforce Developer Edition REST API | Free, permanent, validates integration before production credentials |
| ADR-002 | GCP alongside Salesforce — augmentation not replacement | Architecture Principle: existing systems stay unchanged |
| ADR-003 | Cloud Run over GKE for stateless agent services | Per-request billing, no node pool management |
| ADR-004 | Firestore for agent state and HITL audit | Document model matches conversation state natively |
| ADR-005 | SHAP over LIME for XAI layer | Deterministic TreeExplainer vs approximation |
| ADR-006 | Pub/Sub as integration event bus | Decouples AE from Salesforce/SAP outages |
| ADR-007 | Google ADK over LangGraph/CrewAI | Native CCAI + Dialogflow CX + A2A integration |
| ADR-008 | A2A protocol over direct HTTP | Typed inter-agent contracts, agent replaceability |
| ADR-009 | Firestore over Redis for agent state | Persistence, immutability, BigQuery export |
| ADR-010 | XGBoost over neural network for RevRec/ContractGuard | Deterministic SHAP — EU AI Act Art. 13 requirement |
| ADR-011 | Isolation Forest over autoencoder for anomaly detection | TreeExplainer compatible, no labelled failures needed |
| ADR-012 | Vertex AI Pipelines over self-managed Kubeflow | Managed, versioned, GCP-native, ML Metadata store |
| ADR-013 | Shared VPC over separate VPCs per module | O(n²) peering avoided, centralised network management |
| ADR-014 | Cloud Armor over third-party WAF | VPC-SC data sovereignty, native SCC integration |
| ADR-015 | GKE Autopilot over GKE Standard for batch ML | Per-pod billing, GPU access, hardened by default |
| ADR-016 | Phased adoption over big-bang deployment | EU Act deadline forcing function, HITL trust-building |

Full ADR documentation with alternatives considered: [adr-index.html](adr-index.html)

---

## Deployment

This portfolio is deployed as a static GitHub Pages site. All HTML files are self-contained — no build step, no dependencies beyond Google Fonts.

**Local preview:**
```bash
git clone https://github.com/raosiddharthp/The-Autonomous-Enterprise.git
cd The-Autonomous-Enterprise
python -m http.server 8000
# Open http://localhost:8000
```

**GitHub Pages:** Enable in repository Settings → Pages → Source: main branch root.

All internal navigation uses relative paths (`href="page-02.html"`) — resolves correctly both locally and on GitHub Pages without any configuration.

---

## About

**Siddharthan Rao** — AI Solutions Architect · TOGAF EA Certified · Google MLE · Google Cloud Architect · SAFe SA + SPC

22 years in technology: 10 technical writing · 7 training/GSIs · 6 Salesforce solutions architecture · 15 years Salesforce CPQ/Q2C depth.

[GitHub](https://github.com/raosiddharthp) · [LinkedIn](#)

---

© 2026 Siddharthan Rao · The Autonomous Enterprise
