from diagrams import Diagram, Edge
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Roadmap View: 3-Phase Evolution", show=False, filename="doc_roadmap_evolution", direction="LR", graph_attr=graph_attr):
    phase1 = Blank("Phase 1: POC\n(Free Tier)")
    phase2 = Blank("Phase 2: MVP\n(Regional Service)")
    phase3 = Blank("Phase 3: Enterprise\n(Global Scale)")

    phase1 >> Edge(label="Validate Value") >> phase2 >> Edge(label="Expand Scope") >> phase3