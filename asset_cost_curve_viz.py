from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import Looker
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Strategic View: Predictive ROI", show=False, filename="asset_cost_curve_viz", direction="LR", graph_attr=graph_attr):
    dashboard = Looker("CFO Executive View")
    
    with Cluster("ROI Drivers"):
        downtime = Rack("Downtime Reduction")
        parts = Rack("Parts Optimization")
        labor = Rack("Labor Efficiency")

    [downtime, parts, labor] >> Edge(color="darkblue") >> dashboard