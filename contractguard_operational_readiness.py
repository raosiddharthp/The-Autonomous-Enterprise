from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import NaturalLanguageAPI
from diagrams.gcp.operations import Monitoring
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Operational Readiness Heatmap", show=False, filename="contractguard_operational_readiness", direction="LR", graph_attr=graph_attr):
    with Cluster("Nuance Extraction Accuracy"):
        standard = NaturalLanguageAPI("Standard Clauses\n(99% Accuracy)")
        complex_cl = NaturalLanguageAPI("Complex Indemnity\n(95% Accuracy)")
        high_risk = NaturalLanguageAPI("Liabilities\n(96% Accuracy)")

    monitor = Monitoring("Accuracy Thresholds")
    ready_signal = Rack("Production Readiness")

    [standard, complex_cl, high_risk] >> monitor >> Edge(label="95%+ Met") >> ready_signal