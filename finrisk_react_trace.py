from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.database import Spanner
from diagrams.gcp.security import KeyManagementService

# Using KMS to represent DLP/Security logic for PII redaction
graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.5", "bgcolor": "transparent"}

with Diagram("FinRisk ReAct Trace", show=False, filename="finrisk_react_trace", direction="LR", graph_attr=graph_attr):
    agent = VertexAI("Researcher Agent\n(ReAct Loop)")

    with Cluster("GCP Action Space"):
        ledger = Spanner("Spanner\n(Transaction Ledger)")
        pii_sec = KeyManagementService("DLP API\n(PII Redaction)")

    agent >> Edge(label="1. Thought: Need History") >> agent
    agent >> Edge(label="2. Tool: Query Spanner", color="darkblue") >> ledger
    ledger >> Edge(label="3. Obs: Patterns Found") >> agent
    agent >> Edge(label="4. Thought: Redact PII") >> agent
    agent >> Edge(label="5. Tool: Call DLP", color="darkred") >> pii_sec
    pii_sec >> Edge(label="6. Obs: Data Clean") >> agent