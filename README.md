# Simulation of Energy Consumption in Wireless Sensor Networks Using Static and Mobile Sink Nodes
**Author :- Aryan Pandey and Prathviraj Gawali** 

This project simulates energy consumption in a Wireless Sensor Network (WSN) using both static and mobile sink nodes. The simulation showcases how sensor nodes communicate with the sink node and demonstrates the energy efficiency trade-offs between static and mobile sinks.

---

## Table of Contents
- [Simulation of Energy Consumption in Wireless Sensor Networks Using Static and Mobile Sink Nodes](#simulation-of-energy-consumption-in-wireless-sensor-networks-using-static-and-mobile-sink-nodes)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Theory Behind the Code](#theory-behind-the-code)
    - [Wireless Sensor Networks (WSNs):](#wireless-sensor-networks-wsns)
    - [Energy Consumption:](#energy-consumption)
    - [Static vs. Mobile Sink Nodes:](#static-vs-mobile-sink-nodes)
  - [Features](#features)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [Usage](#usage)
    - [Simulating with Static Sink Node](#simulating-with-static-sink-node)
    - [Simulating with Mobile Sink Node](#simulating-with-mobile-sink-node)
  - [Graphical Animation](#graphical-animation)
    - [Running Animations](#running-animations)
  - [Directory Structure](#directory-structure)
  - [Contributing](#contributing)
  - [License](#license)

---

## Introduction
Wireless Sensor Networks (WSNs) are integral in applications like environmental monitoring, smart cities, and healthcare. This project models energy consumption in WSNs by comparing static and mobile sink nodes. Using Python and Streamlit for interactivity, the project also includes dynamic visualizations created with Matplotlib to illustrate energy consumption patterns.

---

## Theory Behind the Code

### Wireless Sensor Networks (WSNs):
WSNs are networks of spatially distributed sensors that monitor physical or environmental conditions (e.g., temperature, pressure).

- **Sensor Nodes**: Collect data and transmit it to a central node (sink).
- **Sink Node**: Processes and aggregates data from the sensor nodes.

### Energy Consumption:
Energy efficiency is a critical aspect of WSNs since nodes are typically battery-powered. Energy consumption occurs during:
- **Sensing**: Gathering environmental data.
- **Processing**: Performing computations on the data.
- **Communication**: Transmitting and receiving data.

Communication energy is heavily influenced by the distance between the transmitter and receiver due to path loss.

### Static vs. Mobile Sink Nodes:
- **Static Sink**: Fixed in one position, leading to uneven energy usage. Nodes closer to the sink tend to deplete their energy faster.
- **Mobile Sink**: Moves within the network, balancing energy consumption and prolonging the network’s lifetime.

---

## Features
- Interactive simulation using **Streamlit**.
- Visual comparison of energy consumption with static vs. mobile sink nodes.
- Dynamic animations using **Matplotlib**.
- Clear insights into energy usage patterns in WSNs.

---

## Installation

### Prerequisites
1. Python 3.8 or higher
2. pip (Python package installer)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/ltd-ARYAN-pvt/Simulation-of-Energy-Consumption-in-WSN.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
Run the Streamlit app to interact with the simulation.

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Choose between **Static Sink Node** or **Mobile Sink Node** simulations in the app interface.
3. Observe energy consumption patterns and node activity in real-time.

### Simulating with Static Sink Node
1. Select **Static Sink Node** from the interface.
2. View the energy usage and depletion patterns around the fixed sink node.

### Simulating with Mobile Sink Node
1. Select **Mobile Sink Node** from the interface.
2. Observe how the mobile sink’s movement balances energy consumption across the network.

---

## Graphical Animation
Dynamic visualizations for both static and mobile sink nodes are included in the **Graph Animation** directory. These are implemented using Matplotlib.

### Running Animations
1. Navigate to the `Graph Animation` directory:
   ```bash
   cd Graph Animation
   ```
2. For static sink node animation:
   ```bash
   python static_node.py
   ```
3. For mobile sink node animation:
   ```bash
   python mobile_node.py
   ```
4. Watch as the energy consumption and sink node activity are visualized dynamically.

---

## Directory Structure
```
wsn-energy-simulation/
├── app.py                # Streamlit app for interactive simulation
├── Graph Animation/      # Directory for graphical animations
│   ├── mobile_node.py    # Animation for mobile sink node
│   └── static_node.py    # Animation for static sink node
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
```

---

## Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

