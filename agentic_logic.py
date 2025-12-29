from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
from diagrams.gcp.ml import VertexAI
from diagrams.programming.language import Python

# Filename: agentic_logic.png
with Diagram("Agentic Reasoning Logic (Gemini & LangGraph)", show=False, filename="agentic_logic", direction="TB"):

    with Cluster("LangGraph Orchestration Layer"):
        orchestrator = VertexAI("Orchestrator Agent\n(Gemini 1.5 Pro)")
        
        with Cluster("Specialist Swarm"):
            specialists = [
                Python("Legal specialist"),
                Python("FinOps specialist"),
                Python("Data specialist")
            ]
        
        critic = VertexAI("Critic Agent\n(Validation)")

    # The Loop Logic
    orchestrator >> Edge(label="Task Delegation", color="darkblue") >> specialists
    specialists >> Edge(label="Draft Output", color="darkblue") >> critic
    
    # Feedback Loop (The "Logic" part)
    critic >> Edge(label="Refinement / Rejection", color="firebrick", style="dashed") >> orchestrator
    
    # Final Output
    critic >> Edge(label="Validated Result", color="darkgreen", style="bold") >> orchestrator