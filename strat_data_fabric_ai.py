from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import VertexAI
from diagrams.generic.compute import Rack

# TOGAF Phase C: Information Systems Architecture
graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase C: Strategy AI Data Fabric", 
    show=False, 
    filename="strat_data_fabric_ai", 
    direction="LR", 
    graph_attr=graph_attr
):
    source = BigQuery("Strategic Data Fabric\n(Financials/OKRs)")

    with Cluster("AI Integration Plane"):
        orchestrator = Run("LangGraph Agent\n(Orchestrator)")
        model = VertexAI("Gemini 1.5 Pro\n(Reasoning Engine)")
        prediction = VertexAI("Health Scoring\n(Endpoint)")

    dashboard = Rack("Executive Dashboard")

    source >> Edge(label="Query Metrics") >> orchestrator
    orchestrator >> Edge(label="Contextualize") >> model
    model >> Edge(label="Synthesize Narrative") >> dashboard
    source >> prediction >> Edge(label="Real-time Health") >> dashboard