from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run
from diagrams.gcp.network import PrivateServiceConnect
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.operations import Monitoring
from diagrams.generic.device import Tablet

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Phase D: Multi-Agent Orchestration", show=False, filename="strat_langgraph_orchestration", direction="LR", graph_attr=graph_attr):
    lpm_user = Tablet("LPM Reviewer\n(HITL Signature)")
    with Cluster("VPC Service Perimeter"):
        with Cluster("LangGraph (Cloud Run)"):
            planner = Run("Planner Agent\n(Task Orchestrator)")
            analyst = Run("Financial Analyst\n(ROI Calc)")
            summarizer = Run("Executive Summarizer")
        vpc_sc = PrivateServiceConnect("VPC Service Controls")
        model = VertexAI("Gemini 1.5 Pro\n(Reasoning Core)")
        tracking = Monitoring("Cloud Trace\n(Audit Trail)")
    planner >> Edge(label="Sub-Task") >> analyst
    analyst >> Edge(label="ROI Results") >> summarizer
    summarizer >> Edge(label="Review (> $1M)", color="red", style="bold") >> lpm_user
    [planner, analyst, summarizer] >> vpc_sc >> model
    summarizer >> tracking