from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import Pubsub, Dataflow, BigQuery
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.database import Memorystore

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("FinRisk Systems Architecture", show=False, filename="finrisk_systems_arch", direction="LR", graph_attr=graph_attr):
    ingest = Pubsub("Streaming\nTransactions")
    
    with Cluster("Intelligence Warehouse"):
        stream_proc = Dataflow("Real-time ETL")
        warehouse = BigQuery("Risk Data Lake")
        embeddings = Memorystore("Vector Store\n(RAG Context)")

    agent_layer = VertexAI("Agentic Layer\n(Risk Inference)")

    ingest >> stream_proc >> warehouse
    warehouse >> Edge(label="Vectorized", color="darkblue") >> embeddings
    embeddings >> Edge(label="Contextual Retrieval", style="bold", color="darkgreen") >> agent_layer