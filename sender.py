import socket
import time

TARGET_IP = '192.168.1.100'  # <-- Change to your remote host
PORT = 9999
NUM_PACKETS = 5
TIMEOUT = 2  # seconds

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(TIMEOUT)

for i in range(NUM_PACKETS):
    msg = f"Tracer packet {i+1}"
    start = time.time()
    sock.sendto(msg.encode(), (TARGET_IP, PORT))
    print(f"[Sender] Sent: {msg}")
    
    try:
        data, addr = sock.recvfrom(1024)
        end = time.time()
        rtt = (end - start) * 1000  # ms
        print(f"[Sender] Echo from {addr}: {data.decode()} | RTT: {rtt:.2f} ms")
    except socket.timeout:
        print("[Sender] Timeout, no echo reply.")

    time.sleep(1)
