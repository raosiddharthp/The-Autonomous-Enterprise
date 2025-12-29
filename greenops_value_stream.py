from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.analytics import Pubsub, BigQuery
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import NaturalLanguageAPI, VertexAI
from diagrams.gcp.iot import IotCore

# Filename: greenops_value_stream.png
with Diagram("ESG Value Stream: Telemetry to Narrative", show=False, filename="greenops_value_stream", direction="LR"):

    with Cluster("1. Ingestion"):
        telemetry = IotCore("Carbon Telemetry")
        stream = Pubsub("Data Stream")

    with Cluster("2. Processing & Analysis"):
        warehouse = BigQuery("Carbon Data Lake")
        analyst = Run("Carbon Analyst Agent")

    with Cluster("3. Narrative Generation"):
        llm = VertexAI("Gemini 1.5 Pro\n(Contextual Synthesis)")
        report_gen = NaturalLanguageAPI("ESG Narrative Engine")

    # Flow: Ingestion -> Processing -> Generation
    telemetry >> stream >> warehouse >> analyst
    analyst >> Edge(label="Insights", color="darkgreen") >> llm
    llm >> Edge(label="Drafting", color="darkgreen") >> report_gen