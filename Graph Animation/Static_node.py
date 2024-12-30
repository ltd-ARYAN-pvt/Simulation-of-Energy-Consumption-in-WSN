import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from node import Node
from utils import *

# Initialize Nodes and Sink
nodes = [
    Node(i, random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE), random.randint(50, 100))
    for i in range(NUM_NODES)
]
sink = Node('Sink', GRID_SIZE // 2, GRID_SIZE // 2, float('inf'))

# Visualization
def visualize(nodes, sink, ax, selected_node=None, message=""):
    ax.clear()
    ax.set_title("WSN Energy Simulation")
    ax.set_xlim(0, GRID_SIZE)
    ax.set_ylim(0, GRID_SIZE)
    
    # Plot nodes with IDs and energy levels
    for node in nodes:
        color = 'green' if node.active else 'red'
        ax.scatter(node.x, node.y, color=color, label=f'Node {node.node_id} (E: {node.energy:.2f})')
        ax.text(node.x, node.y - 3, f"{node.node_id}", fontsize=9, ha='center', color='black')  # Display Node ID
        ax.text(node.x, node.y + 3, f"{node.energy:.1f}", fontsize=8, ha='center', color='gray')  # Display Energy Level
    
    # Highlight selected node
    if selected_node:
        ax.scatter(selected_node.x, selected_node.y, color='orange', s=200, alpha=0.5, label="Selected Node")
    
    # Plot sink
    ax.scatter(sink.x, sink.y, color='blue', label='Sink', s=100)
    
    # Display failure message if any
    if message:
        ax.text(GRID_SIZE // 2, GRID_SIZE - 10, message, fontsize=12, ha='center', color='red')

    ax.legend(loc="upper right")
    ax.grid()

# Animation Function
def animate(time_step):
    global nodes, sink
    ax.clear()
    active_nodes = [node for node in nodes if node.active]
    
    if not active_nodes:
        print("All nodes depleted!")
        ani.event_source.stop()
        return
    
    # Sink requests data from a random node (may include depleted nodes)
    selected_node = random.choice(nodes)
    
    if not selected_node.active:
        message = f"Time {time_step}: Request to Node {selected_node.node_id} failed (Low Energy)."
        print(message)
        visualize(nodes, sink, ax, selected_node=selected_node, message="Request Failed: Low Energy")
        return
    
    # Transmit data and update energy
    energy_used, distance = transmit_data(selected_node, sink)
    message = (f"Time {time_step}: Sink requested data from Node {selected_node.node_id}. "
               f"Energy used: {energy_used:.2f}, Distance: {distance:.2f}")
    print(message)
    
    # Visualize nodes and energy flow
    visualize(nodes, sink, ax, selected_node=selected_node)
    
    # Draw an arrow to show energy flow
    ax.annotate(
        '', 
        xy=(sink.x, sink.y), 
        xytext=(selected_node.x, selected_node.y),
        arrowprops=dict(facecolor='yellow', edgecolor='black', width=2, headwidth=10, shrink=0.05)
    )

# Create Figure
fig, ax = plt.subplots(figsize=(8, 8))
time_step = 0

# Create Animation
ani = animation.FuncAnimation(
    fig, animate, frames=MAX_TIME, interval=1000, repeat=False
)
plt.show()