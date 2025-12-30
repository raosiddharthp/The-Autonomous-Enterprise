from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run
from diagrams.gcp.analytics import BigQuery
from diagrams.generic.compute import Rack
from diagrams.generic.blank import Blank

# TOGAF Phase D: Technology Architecture - Strategy Alignment
graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "Strategy Alignment: Hierarchical Sunburst", 
    show=False, 
    filename="strat_alignment_sunburst", 
    direction="TB", 
    graph_attr=graph_attr
):
    # The Center: Strategic Themes
    core_strategy = Blank("Enterprise\nStrategic Themes")

    with Cluster("Reactive Compute Layer (Cloud Run)"):
        api_engine = Run("R/Shiny API\n(observeEvent)")
    
    with Cluster("Data Sovereignty (BigQuery RLS)"):
        finance_data = BigQuery("Financial Rows")
        ops_data = BigQuery("Ops Metrics")

    # The Rim: Real-Time Execution
    dashboard = Rack("Executive Command Hub")

    # Logic Flow
    [finance_data, ops_data] >> Edge(label="Secure Stream") >> api_engine
    api_engine >> Edge(label="Reactive Update") >> dashboard
    dashboard >> Edge(label="Scenario Toggle", style="dashed") >> core_strategy