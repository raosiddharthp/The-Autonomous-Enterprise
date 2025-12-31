from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.compute import Run
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram(
    "Strategic View: Risk Heatmap", 
    show=False, 
    filename="risk_impact_heatmap", 
    direction="LR", 
    graph_attr=graph_attr
):
    source = BigQuery("Transaction Hub\n(Live Feed)")
    
    with Cluster("R Shiny Compute Layer"):
        engine = Run("Reactive Engine")
        viz = Run("Heatmap Generator")

    board_view = Rack("Proactive Risk Portal")

    source >> engine >> viz >> board_view