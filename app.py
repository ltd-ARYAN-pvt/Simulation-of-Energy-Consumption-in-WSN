import streamlit as st
import subprocess
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import os

# Constants
GRID_SIZE = 100
ENERGY_CONSTANT = 0.01
SINK_MOVE_DISTANCE = 5

# Node Class
class Node:
    def __init__(self, node_id, x, y, energy):
        self.node_id = node_id
        self.x = x
        self.y = y
        self.energy = energy
        self.active = True

    def update_energy(self, energy_dissipation):
        if self.energy >= energy_dissipation:
            self.energy -= energy_dissipation
        else:
            self.energy = 0
            self.active = False

# Distance Calculation
def calculate_distance(node1, node2):
    return np.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)

# Visualization
def visualize(nodes, sink, ax, selected_node=None, message=""):
    ax.clear()
    ax.set_title("WSN Energy Simulation")
    ax.set_xlim(0, GRID_SIZE)
    ax.set_ylim(0, GRID_SIZE)

    for node in nodes:
        color = 'green' if node.active else 'red'
        ax.scatter(node.x, node.y, color=color)
        ax.text(node.x, node.y - 3, f"{node.node_id}", fontsize=9, ha='center', color='black')
        ax.text(node.x, node.y + 3, f"{node.energy:.1f}", fontsize=8, ha='center', color='gray')

    if selected_node:
        ax.scatter(selected_node.x, selected_node.y, color='orange', s=200, alpha=0.5)

    ax.scatter(sink.x, sink.y, color='blue', s=100)

    if message:
        ax.text(GRID_SIZE // 2, GRID_SIZE - 10, message, fontsize=12, ha='center', color='red')

    # Draw arrow to show data flow
    if selected_node and selected_node.active:
        ax.annotate('', xy=(sink.x, sink.y), xytext=(selected_node.x, selected_node.y),
                    arrowprops=dict(facecolor='yellow', edgecolor='black', width=2, headwidth=10, shrink=0.05))

    ax.grid()

# Sidebar Log
if "log" not in st.session_state:
    st.session_state.log = []

def log_message(message):
    st.session_state.log.append(message)
    if len(st.session_state.log) > 20:
        st.session_state.log.pop(0)

# Streamlit App
st.title("WSN Energy Simulation App")
st.markdown("""
### Wireless Sensor Network Simulation
This app lets you simulate energy consumption in a WSN with:
1. **Static Sink Node**: The sink is fixed at the center of the grid.
2. **Mobile Sink Node**: The sink moves randomly in the grid.

Use the sliders below to configure the simulation parameters.
""")

# Interactive Controls
num_nodes = st.slider("Number of Nodes", min_value=5, max_value=50, value=10)
max_time = st.slider("Simulation Time (Steps)", min_value=10, max_value=100, value=20)
grid_size = st.slider("Grid Size", min_value=50, max_value=200, value=100)

# Update Global Variables
GRID_SIZE = grid_size

# Buttons for simulation
if "ani" not in st.session_state:
    st.session_state.ani = None

def display_energy_table(nodes):
    energy_data = {"Node ID": [node.node_id for node in nodes],
                   "Energy": [node.energy for node in nodes],
                   "Status": ["Active" if node.active else "Depleted" for node in nodes]}
    st.sidebar.table(energy_data)

if st.button("Simulate Static Sink Node"):
    st.write("Running simulation for Static Sink Node...")
    nodes = [
        Node(i, random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE), random.randint(50, 100))
        for i in range(num_nodes)
    ]
    sink = Node('Sink', GRID_SIZE // 2, GRID_SIZE // 2, float('inf'))

    fig, ax = plt.subplots(figsize=(8, 8))

    def animate_static(time_step):
        active_nodes = [node for node in nodes if node.active]

        if not active_nodes:
            log_message("All nodes depleted!")
            st.warning("All nodes depleted!")
            return

        selected_node = random.choice(nodes)
        if selected_node.active:
            distance = calculate_distance(selected_node, sink)
            energy_dissipation = ENERGY_CONSTANT * (distance ** 2)
            selected_node.update_energy(energy_dissipation)
            log_message(f"Step {time_step}: Node {selected_node.node_id} sent data. Energy used: {energy_dissipation:.2f}")

        visualize(nodes, sink, ax, selected_node=selected_node)
        display_energy_table(nodes)

    ani = animation.FuncAnimation(fig, animate_static, frames=max_time, interval=1000, repeat=False)
    video_path = "static_sink_simulation.mp4"
    ani.save(video_path, writer="ffmpeg")

    st.video(video_path)

if st.button("Simulate Mobile Sink Node"):
    st.write("Running simulation for Mobile Sink Node...")
    nodes = [
        Node(i, random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE), random.randint(50, 100))
        for i in range(num_nodes)
    ]
    sink = Node('Sink', GRID_SIZE // 2, GRID_SIZE // 2, float('inf'))

    fig, ax = plt.subplots(figsize=(8, 8))

    def move_sink(sink):
        sink.x = (sink.x + random.randint(-SINK_MOVE_DISTANCE, SINK_MOVE_DISTANCE)) % GRID_SIZE
        sink.y = (sink.y + random.randint(-SINK_MOVE_DISTANCE, SINK_MOVE_DISTANCE)) % GRID_SIZE

    def animate_mobile(time_step):
        active_nodes = [node for node in nodes if node.active]

        if not active_nodes:
            log_message("All nodes depleted!")
            st.warning("All nodes depleted!")
            return

        move_sink(sink)

        selected_node = random.choice(nodes)
        if selected_node.active:
            distance = calculate_distance(selected_node, sink)
            energy_dissipation = ENERGY_CONSTANT * (distance ** 2)
            selected_node.update_energy(energy_dissipation)
            log_message(f"Step {time_step}: Node {selected_node.node_id} sent data. Energy used: {energy_dissipation:.2f}")

        visualize(nodes, sink, ax, selected_node=selected_node)
        display_energy_table(nodes)

    ani = animation.FuncAnimation(fig, animate_mobile, frames=max_time, interval=1000, repeat=False)
    video_path = "mobile_sink_simulation.mp4"
    ani.save(video_path, writer="ffmpeg")

    st.video(video_path)

# Sidebar Log
st.sidebar.title("Simulation Logs")
st.sidebar.markdown("""Logs of recent actions during the simulation will appear here.""")
for log in st.session_state.log:
    st.sidebar.text(log)

st.markdown("---\nDeveloped using **Streamlit** for interactive and dynamic WSN simulations.")
