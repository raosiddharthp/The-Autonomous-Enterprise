from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import Pubsub, Dataflow, BigQuery
from diagrams.gcp.network import PrivateServiceConnect
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

# TOGAF Phase C: Information Systems Architecture
graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase C: Secure Data Lineage", 
    show=False, 
    filename="risk_data_lineage", 
    direction="LR", 
    graph_attr=graph_attr
):
    source = Pubsub("Real-Time Risk Events")
    
    with Cluster("VPC Service Controls Perimeter"):
        pipeline = Dataflow("Pre-Processing Pipeline")
        warehouse = BigQuery("Risk Data Warehouse")
        agent_context = Run("Agent Contextualization\n(LangChain)")
        llm = VertexAI("Gemini 1.5 Pro\n(Reasoning Core)")

    insights = Run("Risk Insights Dashboard")

    source >> pipeline >> warehouse
    warehouse >> agent_context >> llm >> insights
    pipeline >> PrivateServiceConnect("VPC-SC") << llm # Illustrate VPC-SC protecting LLM