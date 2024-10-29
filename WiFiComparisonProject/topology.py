# topology.py

class Topology:
    def __init__(self, standard):
        self.standard = standard  # e.g., '802.11b' or '802.11bc'
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def show_topology(self):
        print(f"Topology with Wi-Fi Standard: {self.standard}")
        for device in self.devices:
            print(f"Device: {device}")