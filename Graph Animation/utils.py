import numpy as np

#--> Constants
NUM_NODES = 5
GRID_SIZE = 100
MAX_TIME = 20  # Maximum simulation time
ENERGY_CONSTANT = 0.01  # Energy dissipation constant
SINK_MOVE_DISTANCE = 5  # Distance the sink moves at each step

# Distance Calculation
def calculate_distance(node1, node2):
    return np.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)

# Simulate Data Transmission
def transmit_data(source, sink):
    if source.active:
        distance = calculate_distance(source, sink)
        energy_dissipation = ENERGY_CONSTANT * (distance ** 2)
        source.update_energy(energy_dissipation)
        return energy_dissipation, distance
    return 0, 0