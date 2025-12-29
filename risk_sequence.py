from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.compute import Run
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.ml import NaturalLanguageAPI

# Filename: risk_sequence.png
with Diagram("Emergent Risk Propagation Sequence", show=False, filename="risk_sequence", direction="LR"):

    with Cluster("Detection"):
        detector = Run("FinRisk Sentinel\n(Anomally Detected)")

    with Cluster("Propagation"):
        analyzer = Monitoring("Real-Time Risk\n(Impact Analysis)")

    with Cluster("Mitigation"):
        mitigator = NaturalLanguageAPI("Omni CCAI\n(Automated Response)")

    # Sequence Flow
    detector >> Edge(label="1. Alert Trigger", color="firebrick", style="bold") >> analyzer
    analyzer >> Edge(label="2. Risk Scoring", color="firebrick") >> mitigator
    
    # Feedback loop representing the "Closed-Loop"
    mitigator >> Edge(label="3. Resolution Status", color="darkgreen", style="dashed") >> detector