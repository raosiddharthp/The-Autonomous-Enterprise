from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Risk Architecture: Agentic Swarm", show=False, filename="risk_agentic_swarm", direction="LR", graph_attr=graph_attr):
    with Cluster("LangGraph + CrewAI Swarm"):
        researcher = VertexAI("Doc Researcher Agent")
        analyst = VertexAI("Risk Analyst Agent")
        narrator = VertexAI("SAR Narrative Agent")

    output = Rack("Suspicious Activity Report\n(Automated SAR)")
    
    researcher >> analyst >> narrator >> output