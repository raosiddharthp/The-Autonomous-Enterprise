from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import VertexAI

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("FinRisk TRM Mapping", show=False, filename="finrisk_trm_mapping", direction="LR", graph_attr=graph_attr):
    with Cluster("Intelligence Layer"):
        ai = VertexAI("Vertex AI\n(Scoring)")
    
    with Cluster("Compute Layer"):
        compute = Run("Cloud Run\n(Orchestration)")
        
    with Cluster("Data Layer"):
        data = BigQuery("BigQuery\n(Risk Data Lake)")

    data >> Edge(color="gray") >> compute >> Edge(color="darkblue", style="bold") >> ai