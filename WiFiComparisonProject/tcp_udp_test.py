# tcp_udp_test.py

import socket
import time

def tcp_test(server_ip, port):
    # TCP Test
    start_time = time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, port))
        s.sendall(b"Hello, TCP!")
        data = s.recv(1024)
    end_time = time.time()
    return end_time - start_time, data

def udp_test(server_ip, port):
    # UDP Test
    start_time = time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"Hello, UDP!", (server_ip, port))
        data, _ = s.recvfrom(1024)  # Wait for response
    end_time = time.time()
    return end_time - start_time, data
