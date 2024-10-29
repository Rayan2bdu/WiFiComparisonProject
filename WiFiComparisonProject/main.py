import matplotlib.pyplot as plt
import networkx as nx
from tcp_udp_test import tcp_test, udp_test


class Topology:
    def __init__(self, wifi):
        self.devices = []
        self.wifi = wifi  # Add this line to store the WiFi standard

    def add_device(self, device, range_value):
        self.devices.append((device, range_value))

    def plot_range(self):
        """Plot the range of devices in the topology."""
        device_names = [device[0] for device in self.devices]
        ranges = [device[1] for device in self.devices]

        plt.figure(figsize=(8, 6))
        plt.bar(device_names, ranges, color='lightgreen')
        plt.xlabel('Devices')
        plt.ylabel('Range (meters)')
        plt.title(f'Range of Devices in {self.wifi} Topology')
        plt.xticks(rotation=45)

        # Save the figure as a vector file (SVG or PDF)
        plt.savefig(f'range_plot_{self.wifi}.svg', format='svg')
        plt.show()

    def calculate_energy_consumption(self, time, power):
        """Calculate energy consumption in Joules."""
        return time * power  # Energy (Joules) = Power (Watts) * Time (seconds)

    def plot_energy_consumption(self, power_consumptions, time):
        """Plot the energy consumption of devices."""
        device_names = ["TCP", "UDP "]  # Extract device names
        energy_consumptions = [power * time for power in power_consumptions]  # Calculate energy consumption

        plt.figure(figsize=(8, 6))
        plt.bar(device_names, energy_consumptions, color='lightblue')
        plt.xlabel('Devices')
        plt.ylabel('Energy Consumption (Wh)')
        plt.title(f'Energy Consumption of Devices in {self.wifi} Topology')
        plt.xticks(rotation=45)
        plt.show()

def plot_topology(topology):
    plt.title(f"Topology for {topology.wifi}")
    G = nx.Graph()

    # Add nodes for client and server
    for device in topology.devices:
        G.add_node(device)

    # Add edges between client and server
    if len(topology.devices) == 2:
        G.add_edge(topology.devices[0], topology.devices[1])

    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')

    plt.show()


def plot_results(tcp_results, udp_results):
    labels = ['802.11b', '802.11bc']
    tcp_times = [tcp_results['802.11b'], tcp_results['802.11bc']]
    udp_times = [udp_results['802.11b'], udp_results['802.11bc']]

    x = range(len(labels))

    # Create histogram
    plt.bar(x, tcp_times, width=0.4, label='TCP Time', color='b', align='center')
    plt.bar([p + 0.4 for p in x], udp_times, width=0.4, label='UDP Time', color='r', align='center')

    plt.xlabel('Wi-Fi Standards')
    plt.ylabel('Time (seconds)')
    plt.title('TCP vs UDP Time Comparison')
    plt.xticks([p + 0.2 for p in x], labels)
    plt.legend()
    plt.show()

def calculate_mtbf(failures, total_time):
    """Calculate Mean Time Between Failures (MTBF)"""
    return total_time / failures

def calculate_mttr(repair_time, failures):
    """Calculate Mean Time To Repair (MTTR)"""
    return repair_time / failures


def plot_histogram(mttr_values, mtbf_values):
    """Plot a histogram for MTBF and MTTR for both Wi-Fi standards."""
    labels = list(mttr_values.keys())
    mttr = list(mttr_values.values())
    mtbf = list(mtbf_values.values())

    x = range(len(labels))

    plt.figure(figsize=(10, 6))

    # Plot MTTR
    plt.bar(x, mttr, width=0.4, label='MTTR', color='orange', align='center')
    # Plot MTBF
    plt.bar([p + 0.4 for p in x], mtbf, width=0.4, label='MTBF', color='blue', align='center')

    plt.xlabel('Wi-Fi Standards')
    plt.ylabel('Hours')
    plt.title('MTTR and MTBF Comparison for Wi-Fi Standards')
    plt.xticks([p + 0.2 for p in x], labels)
    plt.legend()
    plt.grid(axis='y')
    plt.show()


def main():
    # Create topologies for both standards
    topology_b = Topology('802.11b')
    topology_bc = Topology('802.11bc')

    # Add devices with their respective ranges (in meters)
    topology_b.add_device("Client 802.11b", 100)
    topology_b.add_device("Server 802.11b", 150)
    topology_bc.add_device("Client 802.11bc", 200)
    topology_bc.add_device("Server 802.11bc", 250)

    # Plot range for both topologies
    topology_b.plot_range()
    topology_bc.plot_range()

    # Define identical power consumption values (in Watts)
    identical_power_consumption = 5  # Example value for both standards
    power_consumptions_b = [identical_power_consumption, identical_power_consumption]  # For 802.11b
    power_consumptions_bc = [identical_power_consumption, identical_power_consumption]  # For 802.11bc

    time = 3600  # Example time in seconds (1 hour)

    # Plot energy consumption for both topologies
    topology_b.plot_energy_consumption(power_consumptions_b, time)
    topology_bc.plot_energy_consumption(power_consumptions_bc, time)

    # Show topologies
    plot_topology(topology_b)
    plot_topology(topology_bc)

    # Använd exempelvärden för MTTR och MTBF

    # Definiera MTTR och MTBF
    failures = 5
    total_time = 1000  # i timmar
    repair_time = 10  # i timmar

    mtbf = calculate_mtbf(failures, total_time)
    mttr = calculate_mttr(repair_time, failures)

    # Skriv ut MTBF och MTTR
    print(f"MTBF: {mtbf} hours")
    print(f"MTTR: {mttr} hours")

    mttr_values = {
        '802.11b': 10,  # Exempelvärde för MTTR i timmar
        '802.11bc': 8  # Exempelvärde för MTTR i timmar
    }

    mtbf_values = {
        '802.11b': 100,  # Exempelvärde för MTBF i timmar
        '802.11bc': 120  # Exempelvärde för MTBF i timmar
    }

    # Anropa histogramfunktionen
    plot_histogram(mttr_values, mtbf_values)

    # Perform tests (replace '127.0.0.1' with actual server IP)
    tcp_time_b, tcp_data_b = tcp_test('127.0.0.1', 7006)
    udp_time_b, udp_data_b = udp_test('127.0.0.1', 7007)

    tcp_time_bc, tcp_data_bc = tcp_test('127.0.0.1', 7009)
    udp_time_bc, udp_data_bc = udp_test('127.0.0.1', 7010)

    # Store results
    tcp_results = {
        '802.11b': tcp_time_b,
        '802.11bc': tcp_time_bc
    }
    udp_results = {
        '802.11b': udp_time_b,
        '802.11bc': udp_time_bc
    }

    # Print results
    print(f"TCP Time (802.11b): {tcp_time_b}")
    print(f"UDP Time (802.11b): {udp_time_b}")
    print(f"TCP Time (802.11bc): {tcp_time_bc}")
    print(f"UDP Time (802.11bc): {udp_time_bc}")

    # Calculate energy consumption for TCP and UDP
    energy_b_tcp = topology_b.calculate_energy_consumption(tcp_time_b, identical_power_consumption)
    energy_b_udp = topology_b.calculate_energy_consumption(udp_time_b, identical_power_consumption)
    energy_bc_tcp = topology_bc.calculate_energy_consumption(tcp_time_bc, identical_power_consumption)
    energy_bc_udp = topology_bc.calculate_energy_consumption(udp_time_bc, identical_power_consumption)

    # Print energy consumption results
    print(f"Energy Consumption (TCP): {energy_b_tcp} Joules")
    print(f"Energy Consumption (UDP): {energy_b_udp} Joules")
    print(f"Energy Consumption (TCP): {energy_bc_tcp} Joules")
    print(f"Energy Consumption (UDP): {energy_bc_udp} Joules")

    # Plot results
    plot_results(tcp_results, udp_results)


if __name__ == "__main__":
    main()