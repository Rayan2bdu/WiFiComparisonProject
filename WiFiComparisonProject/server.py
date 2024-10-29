import socket
from threading import Thread

def tcp_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', port))
        s.listen()
        print(f"TCP server listening on port {port}...")
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)  # Echo back the received data

def udp_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(('127.0.0.1', port))
        print(f"UDP server listening on port {port}...")  # Removed listen()
        while True:
            data, addr = s.recvfrom(1024)  # Use recvfrom for UDP
            print('Received from', addr, 'Data:', data)
            s.sendto(data, addr)  # Echo back the received data

if __name__ == "__main__":
    # Create threads for TCP and UDP servers
    Thread(target=tcp_server, args=(7006,)).start()  # TCP for 802.11b
    Thread(target=udp_server, args=(7007,)).start()  # UDP for 802.11b
    Thread(target=tcp_server, args=(7009,)).start()  # TCP for 802.11bc
    Thread(target=udp_server, args=(7010,)).start()  # UDP for 802.11bc
