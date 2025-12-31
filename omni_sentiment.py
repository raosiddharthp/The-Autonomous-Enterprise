from diagrams import Diagram, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.2", "bgcolor": "transparent"}

with Diagram("CSAT: Sentiment Correlation Map", show=False, filename="omni_sentiment_map", direction="TB", graph_attr=graph_attr):
    sentiment_engine = VertexAI("Natural Language API\n(Sentiment/Tone)")
    interaction = Blank("Agentic Interaction\n(Resolution)")
    nps_lift = Blank("NPS Growth\n(+15 Points)")

    sentiment_engine >> Edge(label="Analyze Tone") >> interaction >> Edge(color="darkblue", style="bold") >> nps_lift