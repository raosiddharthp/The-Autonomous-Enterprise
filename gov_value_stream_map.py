from diagrams import Diagram, Edge
from diagrams.gcp.storage import GCS
from diagrams.gcp.analytics import Dataflow
from diagrams.gcp.compute import Run
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Outcome: Value Stream Realization", show=False, filename="gov_value_stream_map", direction="LR", graph_attr=graph_attr):
    raw = GCS("Raw Event\n(Low Trust)")
    val = Dataflow("Automated Validation")
    agent = Run("Agentic Quality Score")
    golden = Rack("Golden Record\n(Trusted Asset)")

    raw >> Edge(label="Fast Flow", color="blue") >> val >> agent >> Edge(color="darkgreen", style="bold") >> golden