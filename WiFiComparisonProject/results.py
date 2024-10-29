# results.py

import csv


def save_results(results, filename='results.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Protocol', 'Wi-Fi Standard', 'Throughput (Mbps)', 'Latency (ms)', 'Packet Loss (%)',
                         'Power Consumption (W)'])

        # Write the results
        for result in results:
            writer.writerow(result)


# Example of how to call this function
if __name__ == "__main__":
    # Sample results data
    results_data = [
        ['TCP', '802.11b', 54, 10, 0, 2],
        ['UDP', '802.11b', 30, 15, 5, 2],
        ['TCP', '802.11bc', 100, 5, 0, 1.5],
        ['UDP', '802.11bc', 80, 7, 2, 1.5]
    ]

    save_results(results_data)