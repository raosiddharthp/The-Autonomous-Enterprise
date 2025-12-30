from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.iot import IotCore
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run
from diagrams.generic.database import SQL
from diagrams.generic.compute import Rack

# Value Stream: Sensor to ERP Booking
graph_attr = {
    "pad": "0.1",
    "nodesep": "1.0",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "Value Stream: Inference-to-Action", 
    show=False, 
    filename="asset_inference_sequence", 
    direction="LR", 
    graph_attr=graph_attr
):
    sensor = IotCore("Sensor Reading")
    
    with Cluster("Intelligent Core"):
        prediction = VertexAI("RUL Prediction")
        reasoning = VertexAI("Agentic Reasoning\n(Planner Agent)")

    with Cluster("Enterprise Systems"):
        # Using SQL icon as a reliable substitute for ERP/SAP
        erp = SQL("ERP Work-Order\n(SAP/ServiceNow)")
        technician = Run("Technician Dispatch")

    sensor >> prediction >> reasoning >> erp >> technician