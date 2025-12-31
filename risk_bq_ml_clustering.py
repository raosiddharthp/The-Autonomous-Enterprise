from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Risk Architecture: BQML K-Means", show=False, filename="risk_bq_ml_clustering", direction="LR", graph_attr=graph_attr):
    with Cluster("BigQuery ML In-Warehouse"):
        data = BigQuery("Transaction Fabric")
        model = BigQuery("K-Means Cluster Model\n(Anomalies)")
    
    anomalies = Rack("Silent Risk Detected")
    
    data >> model >> anomalies