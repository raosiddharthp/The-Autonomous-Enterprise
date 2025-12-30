from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery, DataCatalog
from diagrams.gcp.ml import NaturalLanguageAPI
from diagrams.gcp.database import Memorystore

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Phase C: Information Architecture", show=False, filename="contractguard_phase_c_info", direction="LR", graph_attr=graph_attr):
    contracts = BigQuery("Contract Data Fabric")
    
    with Cluster("Semantic Layer"):
        vectors = Memorystore("Vector Embeddings\n(Rights vs. Liabilities)")
        search = NaturalLanguageAPI("Semantic Query Engine")

    contracts >> Edge(label="Index") >> vectors
    vectors >> Edge(label="RAG Context") >> search