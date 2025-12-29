from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.analytics import BigQuery, Dataflow, Pubsub
from diagrams.gcp.compute import GKE, Run
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.devtools import Build

with Diagram("GreenOps Platform Architecture", show=False, filename="greenops_arch", direction="LR"):
    
    with Cluster("Data Ingestion & Ingress"):
        sources = [Pubsub("GCP Billing"), 
                   Pubsub("Carbon Intensity")]
        pipeline = Dataflow("Stream Processor")

    with Cluster("Intelligence Layer (Vertex AI)"):
        model = VertexAI("TimesFM Forecast")
        registry = VertexAI("Model Registry")
        monitoring = VertexAI("Drift Defense")
        
        pipeline >> Edge(label="Feature Store") >> model
        model >> registry
        registry >> monitoring

    with Cluster("Autonomous Execution"):
        actions = [GKE("Workload Shifter"),
                   Run("Scale Regulator")]

    with Cluster("MLOps & CI/CD"):
        cicd = Build("Cloud Build / CT")
        cicd >> Edge(color="firebrick", style="dashed") >> registry

    # Main Flow
    sources >> pipeline >> model
    monitoring >> Edge(label="Trigger Action", color="darkgreen") >> actions