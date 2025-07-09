from scapy.all import IP, ICMP, sr1

target = "8.8.8.8"  # <-- Change this to your target
max_hops = 20

print(f"[Tracer] Tracing route to {target}")

for ttl in range(1, max_hops + 1):
    pkt = IP(dst=target, ttl=ttl) / ICMP()
    reply = sr1(pkt, timeout=2, verbose=0)
    if reply is None:
        print(f"{ttl}\t*")
    elif reply.type == 0:
        print(f"{ttl}\t{reply.src} (Destination reached!)")
        break
    else:
        print(f"{ttl}\t{reply.src}")
