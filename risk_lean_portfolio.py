from diagrams import Diagram, Cluster, Edge
from diagrams.generic.blank import Blank
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("SAFe: Risk Epic Funnel", show=False, filename="risk_lean_portfolio", direction="TB", graph_attr=graph_attr):
    with Cluster("Strategic Themes"):
        growth = Blank("Global Expansion")
        safety = Blank("Sanction Compliance")

    with Cluster("Epic Funnel (LPM)"):
        monitoring = Rack("Risk Monitoring Epic")
        guardrails = Rack("Budget Guardrails")

    [growth, safety] >> monitoring >> guardrails