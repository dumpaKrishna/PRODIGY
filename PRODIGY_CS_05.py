from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        else:
            protocol = "Other"
            src_port = "N/A"
            dst_port = "N/A"

        print(f"[+] {protocol} Packet: {ip_src}:{src_port} -> {ip_dst}:{dst_port}")
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            print(f"Payload: {packet[protocol].payload}")

print("Starting packet sniffer...")
sniff(prn=packet_callback, store=0, count=10)
