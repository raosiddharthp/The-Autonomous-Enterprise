from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery, Looker
from diagrams.gcp.database import Memorystore
from diagrams.gcp.ml import VertexAI

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("FinRisk Executive Dashboard", show=False, filename="finrisk_exec_dashboard", direction="LR", graph_attr=graph_attr):
    lake = BigQuery("Risk Data Lake")
    roai_calc = VertexAI("ROAI Logic")

    with Cluster("Dashboard Stack"):
        cache = Memorystore("Audit Cache")
        dashboard = Looker("CCO Dashboard")

    lake >> Edge(color="darkblue") >> roai_calc >> Edge(color="darkgreen") >> cache >> dashboard