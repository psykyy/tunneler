import socket

PORT = 9999
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))
print(f"[Echo Responder] Listening on UDP port {PORT}...")

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print(f"[Echo Responder] Received from {addr}: {data.decode()}")
    sock.sendto(data, addr)
