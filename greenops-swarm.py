from diagrams import Diagram, Cluster, Edge
from diagrams.programming.language import Python
from diagrams.gcp.ml import NaturalLanguageAPI
from diagrams.gcp.compute import Run

# This script generates 'greenops_swarm.png'
with Diagram("GreenOps Agentic Swarm Logic", show=False, filename="greenops_swarm", direction="TB"):
    
    trigger = NaturalLanguageAPI("Optimization Request")

    with Cluster("Multi-Agent Orchestration"):
        orchestrator = Python("Orchestrator Agent")
        
        with Cluster("Cognitive Specialists"):
            analyst = Python("Carbon Analyst")
            finops = Python("FinOps Strategist")
            
        executor = Run("Action Executor")

    # Swarm Communication Flow
    trigger >> orchestrator
    orchestrator >> Edge(label="Analyze Carbon") >> analyst
    orchestrator >> Edge(label="Verify Budget") >> finops
    
    # Inter-agent negotiation
    analyst >> Edge(color="darkgreen", style="dashed", label="Trade-off Data") >> finops
    
    finops >> orchestrator
    analyst >> orchestrator
    
    orchestrator >> Edge(label="Validated Action", color="darkgreen") >> executor