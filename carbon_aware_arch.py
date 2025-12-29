from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.devtools import GCR # Using GCR as a visual proxy for a registry/API if Billing is missing

# Filename: carbon_aware_arch.png
with Diagram("Carbon-Aware Architecture (Phase D)", show=False, filename="carbon_aware_arch", direction="TB"):

    with Cluster("Data Ingestion Layer"):
        # We use VertexAI icons for both to represent the "Agentic" nature of the APIs
        billing = VertexAI("Google Billing API")
        carbon_api = VertexAI("Carbon Footprint API") 
        
    with Cluster("Intelligence & Orchestration Layer"):
        agent_builder = VertexAI("Agent Builder\n(Decision Engine)")
        data_warehouse = BigQuery("Sustainability\nData Warehouse")

    with Cluster("Actionable Output"):
        optimization_agent = Run("Optimization Agent")

    # Layered Integration Flow
    billing >> Edge(label="Cost Data", color="darkblue") >> data_warehouse
    carbon_api >> Edge(label="Emissions Data", color="darkgreen") >> data_warehouse
    
    data_warehouse >> agent_builder
    agent_builder >> Edge(label="Orchestration", color="darkgreen", style="bold") >> optimization_agent