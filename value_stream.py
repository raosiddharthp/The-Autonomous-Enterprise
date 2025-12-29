from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.analytics import Pubsub
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import NaturalLanguageAPI, VertexAI
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.security import KeyManagementService

# Filename: value_stream.png
with Diagram("SAFe Value Stream & Agentic Touchpoints", show=False, filename="value_stream", direction="LR"):
    
    with Cluster("1. Ingestion"):
        ingest_group = [Pubsub("Asset Inventory"),
                        Run("Doc Analyzer")]

    with Cluster("2. Processing"):
        proc_group = [Run("Contract Guard"),
                      NaturalLanguageAPI("Omni CCAI")]

    with Cluster("3. Recognition"):
        recog_group = [Run("RevRec-AI"),
                       VertexAI("GreenOps Sentinel")]

    with Cluster("4. Risk"):
        risk_group = [Run("FinRisk Sentinel"),
                      Monitoring("Real-Time Risk")]

    with Cluster("5. Steering"):
        steer_group = [Monitoring("Strategy Dashboard"),
                       KeyManagementService("DQ & Governance")]

    # Corrected Value Stream Flow (Connecting nodes to lists)
    # We use a simple loop or connect the first item to ensure the group link renders
    ingest_group >> proc_group[0]
    proc_group >> recog_group[0]
    recog_group >> risk_group[0]
    risk_group >> steer_group[0]

    # Agentic Overlay (Feedback Loops)
    orchestrator = NaturalLanguageAPI("Agentic Orchestrator")
    
    # Logic flow from Steering back to Orchestrator to Ingestion
    steer_group >> Edge(label="Feedback", color="firebrick", style="dashed") >> orchestrator
    orchestrator >> Edge(color="firebrick", style="dashed") >> ingest_group