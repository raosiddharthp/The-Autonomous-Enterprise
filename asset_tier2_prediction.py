from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.iot import IotCore
from diagrams.generic.device import Tablet

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Tier 2: Prediction Architecture", show=False, filename="asset_tier2_prediction", direction="LR", graph_attr=graph_attr):
    sensors = IotCore("Asset Sensor Stream")
    
    with Cluster("Predictive Analytics"):
        model = VertexAI("RUL Estimation Model")
        profile = Tablet("Degradation Profile")

    sensors >> model >> Edge(label="p(Failure)", color="blue") >> profile