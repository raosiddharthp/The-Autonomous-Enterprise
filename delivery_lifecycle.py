from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.devtools import GCR
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import VertexAI

# Gold Standard attributes: Horizontal span, high-fidelity spacing
graph_attr = {
    "pad": "0.1",
    "nodesep": "1.0",
    "ranksep": "1.5",
    "bgcolor": "transparent",
    "margin": "0"
}

with Diagram("Architectural Governance: Agile Delivery Loop", show=False, filename="delivery_lifecycle", direction="LR", graph_attr=graph_attr):

    # Representing the core ADM Phases with standard Technical/Management icons
    vision = VertexAI("Phase A:\nArchitecture Vision")
    business = Run("Phase B:\nBusiness Arch")
    info_sys = GCR("Phase C:\nInformation Systems")
    tech_arch = Monitoring("Phase D:\nTechnology Arch")
    
    with Cluster("Agile Implementation (Sprints)"):
        opps = Run("Phase E/F:\nOpportunities & Solutions")
        migration = VertexAI("Phase G:\nImplementation Governance")

    # Defining the Iterative Loop (Left to Right)
    vision >> Edge(label="Strategy", color="darkblue") >> business
    business >> Edge(label="Data/App", color="darkblue") >> info_sys
    info_sys >> Edge(label="Infra", color="darkblue") >> tech_arch
    
    # Connecting to the Agile Execution Cluster
    tech_arch >> Edge(label="Execution", color="darkgreen", style="bold") >> opps >> migration
    
    # The Return Feedback Loop (The 'Iteration' part of TOGAF)
    migration >> Edge(label="Lessons Learned", color="gray", style="dashed") >> vision