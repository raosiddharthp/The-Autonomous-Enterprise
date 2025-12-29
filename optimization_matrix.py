from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import VertexAI

# graph_attr: "pad": "0" removes margins
# "nodesep": "2.0" stretches the distance between nodes horizontally
# "ranksep": "2.0" stretches the distance between the logic engine and regions
graph_attr = {
    "pad": "0.1",
    "nodesep": "2.0", 
    "ranksep": "2.0",
    "bgcolor": "transparent",
    "margin": "0"
}

with Diagram("Carbon-Cost Optimization Matrix", show=False, filename="optimization_matrix", direction="LR", graph_attr=graph_attr):
    
    # Intelligence Layer
    optimizer = VertexAI("Cost/Carbon\nDecision Engine")

    with Cluster("Execution Regions (Global Reach)"):
        high_perf = Run("Primary Region\n(Performance Focused)")
        green_perf = Run("Secondary Region\n(Carbon-Aware Schedule)")

    # Horizontal Flow
    optimizer >> Edge(label="Low Carbon Priority", color="darkgreen", style="bold") >> green_perf
    optimizer >> Edge(label="Low Latency Priority", color="darkblue", style="bold") >> high_perf