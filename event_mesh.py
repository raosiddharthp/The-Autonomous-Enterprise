from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.analytics import Pubsub
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import NaturalLanguageAPI
from diagrams.gcp.operations import Monitoring

# Filename: event_mesh.png
with Diagram("Pub/Sub Event Mesh Decoupling", show=False, filename="event_mesh", direction="LR"):

    source = Run("Contract Guard\n(Publisher)")
    
    with Cluster("GCP Event Mesh"):
        topic = Pubsub("Contract_Events_Topic")
        
    with Cluster("Downstream Subscribers (Fan-out)"):
        subscribers = [
            Run("Doc Analyzer"),
            NaturalLanguageAPI("Omni CCAI"),
            Run("RevRec-AI"),
            Monitoring("Real-Time Risk")
        ]

    # Asynchronous Fan-out Pattern
    source >> Edge(label="Publish Event", color="darkblue") >> topic
    topic >> Edge(color="darkblue", style="dashed") >> subscribers