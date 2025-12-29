from diagrams import Diagram, Edge
from diagrams.programming.language import Python
from diagrams.custom import Custom

# Using generic nodes to represent the iterative cycle stages
# Filename: delivery_lifecycle.png
with Diagram("TOGAF ADM: Agentic Delivery Lifecycle", show=False, filename="delivery_lifecycle", direction="TB"):

    # Defining the stages of the iteration cycle
    vision = Python("Architecture\nVision")
    business = Python("Business\nArchitecture")
    systems = Python("Information Systems\nArchitecture")
    tech = Python("Technology\nArchitecture")
    opportunities = Python("Opportunities\n& Solutions")
    migration = Python("Migration\nPlanning")
    implementation = Python("Implementation\nGovernance")
    change = Python("Architecture Change\nManagement")

    # Creating the circular iteration loop
    vision >> business >> systems >> tech >> opportunities >> migration >> implementation >> change >> vision

    # Central Requirements Hub
    requirements = Python("Requirements\nManagement")
    
    # Connecting all stages to the central hub to represent the TOGAF ADM core
    stages = [vision, business, systems, tech, opportunities, migration, implementation, change]
    for stage in stages:
        stage - Edge(style="dotted", color="grey") - requirements