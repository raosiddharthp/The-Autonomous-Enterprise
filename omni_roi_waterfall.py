from diagrams import Diagram, Cluster, Edge
from diagrams.generic.blank import Blank
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("ROI Waterfall: Cumulative Impact", show=False, filename="omni_roi_waterfall", direction="LR", graph_attr=graph_attr):
    baseline = Rack("Baseline Costs")
    
    with Cluster("Value Drivers"):
        deflection = Blank("AI Deflection\n(65% Reduction)")
        aht = Blank("AHT Optimization\n(20% Gain)")
        revenue = Blank("Upsell Conversion\n(15% Lift)")
        
    outcome = Rack("Optimized Value State")

    baseline >> Edge(label="AI Transformation", color="darkgreen") >> deflection >> aht >> revenue >> outcome