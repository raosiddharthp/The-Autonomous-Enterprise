from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.generic.device import Tablet
from diagrams.generic.compute import Rack

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.0",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase B: Strategic Reasoning Loop", 
    show=False, 
    filename="strat_reasoning_loop", 
    direction="LR", 
    graph_attr=graph_attr
):
    exec_user = Tablet("Board Member\n(Input)")
    
    with Cluster("Strategic Reasoning Loop"):
        agent = VertexAI("Strategy Agent\n(LangGraph)")
        kb = Rack("Strategy Knowledge Base")
        evaluator = VertexAI("ROI Evaluator")

    viz = Rack("Dashboard Update")

    exec_user >> Edge(label="Scenario Change") >> agent
    agent >> Edge(label="Lookup Context") >> kb
    agent >> Edge(label="Calculate Impact") >> evaluator
    evaluator >> Edge(label="Update View") >> viz