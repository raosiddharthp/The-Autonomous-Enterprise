from diagrams import Diagram, Edge
from diagrams.gcp.analytics import BigQuery
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Outcome: Cost Curve Transformation", show=False, filename="asset_cost_curve", direction="LR", graph_attr=graph_attr):
    reactive = Rack("Reactive Maintenance\n(High Volatility/Cost)")
    strategy = BigQuery("Intelligent Asset Inventory\n(Predictive Shift)")
    predictive = Rack("Predictive Maintenance\n(Lower TCO/Stability)")

    reactive >> Edge(label="Digital Pivot", color="darkred") >> strategy >> Edge(label="Cost Reduction", color="darkgreen", style="bold") >> predictive