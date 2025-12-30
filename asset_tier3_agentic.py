from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import NaturalLanguageAPI
from diagrams.generic.device import Tablet

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Tier 3: Agentic Swarm Logs", show=False, filename="asset_tier3_agentic", direction="LR", graph_attr=graph_attr):
    swarm = NaturalLanguageAPI("Maintenance Swarm\n(LLM Agents)")
    
    with Cluster("Operational Logs"):
        action = Tablet("Recommendation Log")
        technician = Tablet("Technician Mobile App")

    swarm >> Edge(label="Action Plan", color="darkorange") >> action >> technician