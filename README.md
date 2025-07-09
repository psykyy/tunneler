# Remote Packet Tracer

Simple remote UDP packet tracer in Python.

## Files

- `receiver.py`: Logs incoming UDP packets.
- `echo_responder.py`: Replies to packets (for RTT).
- `sender.py`: Sends packets, optionally measures RTT.
- `tracer.py`: Traces network hops using `scapy`.

## Usage

1. Run `receiver.py` or `echo_responder.py` on remote machine.
2. Edit `sender.py` to point to that IP, then run it.
3. Use `tracer.py` for hop-by-hop trace.
4. `log.txt` will record incoming packets automatically.

## Dependencies

- Python 3+
- `pip install scapy` (for `tracer.py`)
