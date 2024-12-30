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