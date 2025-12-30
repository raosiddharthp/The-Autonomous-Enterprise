from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.operations import Monitoring
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Tier 1: Vitality Strategy", show=False, filename="asset_tier1_vitality", direction="LR", graph_attr=graph_attr):
    with Cluster("Fleet Health Aggregation"):
        metrics = BigQuery("Health Score Lake")
        targets = Monitoring("MTBF Targets")
    
    executive_view = Rack("Executive Dashboard\n(Vitality)")

    metrics >> Edge(label="Aggregate", color="darkgreen") >> targets >> executive_view