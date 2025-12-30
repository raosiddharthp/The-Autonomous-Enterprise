from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import NaturalLanguageAPI
from diagrams.gcp.database import Firestore, Memorystore

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Data Arch: Semantic Enrichment", show=False, filename="contractguard_semantic_enrichment", direction="LR", graph_attr=graph_attr):
    doc_processing = NaturalLanguageAPI("Document AI\n(OCR/Extraction)")
    with Cluster("Vector Processing Layer"):
        embeddings = NaturalLanguageAPI("Vertex AI\nEmbeddings")
        v_search = Memorystore("Vector Search\n(FAISS)")
    meta = Firestore("Firestore\n(Metadata/State)")
    doc_processing >> Edge(label="Raw Text", color="darkblue") >> embeddings >> v_search >> Edge(label="Key-Value Map", color="darkgreen") >> meta