from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run
from diagrams.custom import Custom

# graph_attr for the "Gold Standard": Wide span, no white space, transparent background
graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent",
    "margin": "0"
}

with Diagram("Multi-Agent Orchestration: Cognitive Loop", show=False, filename="agentic_logic", direction="LR", graph_attr=graph_attr):
    
    # Using VertexAI as the industry standard for the Orchestrator
    orchestrator = VertexAI("Orchestrator Agent\n(Gemini 1.5 Pro)")

    with Cluster("Specialist Swarm (Task Execution)"):
        # Using Google Cloud Run icons or generic Bot icons for specialists
        legal = Run("Legal Specialist")
        finops = Run("FinOps Specialist")
        data = Run("Data Specialist")
        specialists = [legal, finops, data]

    # Using a VertexAI icon with a different label for the Critic (Industry standard for ML validation)
    critic = VertexAI("Critic Agent\n(Validation/Refinement)")

    # Logical Horizontal Flow
    orchestrator >> Edge(label="Task Delegation", color="darkblue") >> legal
    orchestrator >> Edge(color="darkblue") >> finops
    orchestrator >> Edge(color="darkblue") >> data

    # Collective output to Critic
    legal >> Edge(label="Draft Output", color="purple", style="dashed") >> critic
    finops >> Edge(color="purple", style="dashed") >> critic
    data >> Edge(color="purple", style="dashed") >> critic

    # Feedback Loop back to Orchestrator or Validation
    critic >> Edge(label="Validated Result", color="darkgreen", style="bold") >> orchestrator
    critic >> Edge(label="Refinement Req", color="red", style="dotted") >> orchestrator