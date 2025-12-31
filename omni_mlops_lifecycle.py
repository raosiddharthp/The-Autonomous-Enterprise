from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.devtools import Build, GCR
from diagrams.gcp.ml import VertexAI
from diagrams.generic.device import Tablet

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("MLOps: CI/CD/CE Lifecycle", show=False, filename="omni_mlops_lifecycle", direction="LR", graph_attr=graph_attr):
    git = Build("Git Trigger\n(Prompt/Model)")
    
    with Cluster("Continuous Evaluation (CE)"):
        eval = VertexAI("Model Evaluation\n(Grounding Check)")
        hitl = Tablet("Human Review\n(Feedback Loop)")
        
    deploy = GCR("Model Registry\n(Promoted)")
    prod = VertexAI("Production Agent")

    git >> eval >> hitl >> deploy >> prod
    hitl >> Edge(color="darkorange", style="dashed", label="Re-Tune") >> git