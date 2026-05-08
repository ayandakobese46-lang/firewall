import random 

blocked_ports = [21, 23, 25, 445]  # FTP, Telnet, SMTP, SMB
blocked_ips = ["192.168.1.100", "10.0.0.5"]

def generate_packet():
    """Simulate a random incoming packet with IP and port."""
    ip = f"192.168.1.{random.randint(1, 255)}"
    port = random.randint(1, 1024)
    return {"ip": ip, "port": port}

def firewall(packet):
    """Check if packet should be blocked or allowed."""
    if packet["ip"] in blocked_ips:
        return f"BLOCKED: Packet from {packet['ip']} on port {packet['port']}"
    elif packet["port"] in blocked_ports:
        return f"BLOCKED: Packet on blocked port {packet['port']} from {packet['ip']}"
    else:
        return f"ALLOWED: Packet from {packet['ip']} on port {packet['port']}"

  

for i in range(10):
    pkt = generate_packet()
    decision = firewall(pkt)
    print(decision)






