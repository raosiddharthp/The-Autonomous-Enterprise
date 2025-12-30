from diagrams import Diagram, Edge
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import VertexAI

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Audit Waterfall", show=False, filename="revrec_audit_waterfall", direction="LR", graph_attr=graph_attr):
    manual_baseline = Run("Manual Baseline\n(Audit Cycle: 3 Mos)")
    auto_evidence = VertexAI("Automated Evidence\nGathering")
    auto_testing = VertexAI("Automated Controls\nTesting")
    target_state = Run("Target State\n(Audit Cycle: 2 Weeks)")

    manual_baseline >> Edge(label="Eliminate Waste", color="darkred") >> auto_evidence >> auto_testing >> Edge(label="Finalized", color="darkgreen") >> target_state