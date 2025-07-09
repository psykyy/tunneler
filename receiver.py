import socket
import time

PORT = 9999
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))
print(f"[Receiver] Listening on UDP port {PORT}...")

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    msg = data.decode()
    log_line = f"[{timestamp}] From {addr}: {msg}\n"
    print(log_line.strip())
    with open('log.txt', 'a') as f:
        f.write(log_line)
