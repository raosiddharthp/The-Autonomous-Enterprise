from diagrams import Diagram, Edge
from diagrams.gcp.ml import NaturalLanguageAPI
from diagrams.generic.device import Tablet

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Data View: Toxic Word Driver", show=False, filename="contractguard_feature_drivers", direction="LR", graph_attr=graph_attr):
    raw_doc = Tablet("Contract PDF")
    nlp = NaturalLanguageAPI("NLP Parser")
    toxic_words = Tablet("Toxic Tokens Identified:\n'Uncapped', 'Indemnity'")

    raw_doc >> nlp >> Edge(color="darkred", style="bold") >> toxic_words