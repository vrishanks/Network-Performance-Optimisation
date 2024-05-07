import csv
import random
import socket
import struct
import time

def random_ip():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

def random_protocol():
    protocols = ['TCP', 'UDP']
    return random.choice(protocols)

def random_port():
    return random.randint(1, 65535)

def random_bytes():
    return random.randint(100, 10000)

def random_packets():
    return random.randint(1, 100)

def random_duration():
    return random.randint(10, 300)

data = []
for _ in range(1000):
    source_ip = random_ip()
    destination_ip = random_ip()
    protocol = random_protocol()
    port = random_port()
    bytes_ = random_bytes()
    packets = random_packets()
    duration = random_duration()
    data.append([source_ip, destination_ip, protocol, port, bytes_, packets, duration])

with open('network_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['SourceIP', 'DestinationIP', 'Protocol', 'Port', 'Bytes', 'Packets', 'Duration'])
    writer.writerows(data)

print("CSV data generated successfully.")
