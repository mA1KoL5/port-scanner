#!/usr/bin/env python3
import socket

target = input("Enter target IP or hostname: ").strip()

ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    587: "SMTP (TLS)",
    993: "IMAPS",
    995: "POP3S",
    3306: "MySQL",
    3389: "RDP",
    5900: "VNC",
    8080: "HTTP-alt",
}

print(f"\nScanning {target} for common ports...\n")

for port, name in ports.items():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} ({name}) is OPEN")

print("\nScan complete.")
