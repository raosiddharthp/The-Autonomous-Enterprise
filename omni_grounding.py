from diagrams import Diagram, Cluster, Edge
from diagrams.generic.blank import Blank
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.ml import VertexAI

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.2", "bgcolor": "transparent"}

with Diagram("Grounding Evaluation Logic", show=False, filename="omni_grounding_dashboard", direction="TB", graph_attr=graph_attr):
    source_docs = BigQuery("Enterprise Knowledge\n(Source of Truth)")
    agent_output = VertexAI("Agent Response")
    
    with Cluster("Evaluation Metrics (DeepEval/Ragas)"):
        faithfulness = Blank("Faithfulness\n(No Hallucination)")
        relevancy = Blank("Answer Relevancy")
        context = Blank("Context Precision")

    source_docs >> faithfulness
    agent_output >> [faithfulness, relevancy]
    faithfulness >> Edge(color="darkgreen") >> Blank("Executive Scorecard")