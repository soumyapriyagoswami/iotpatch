import socket
import subprocess

DEFAULT_PORTS = [22, 23, 80, 1883, 8883]  # SSH, Telnet, HTTP, MQTT

def scan_open_ports(ip, ports=DEFAULT_PORTS):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.4)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports


def check_tls_support(url):
    # naive HTTPS check
    return url.startswith("https://")


def scan_device(ip):
    """
    Basic vulnerability audit for an IoT device.
    """
    report = {
        "device": ip,
        "open_ports": [],
        "score": 100,
        "issues": [],
        "recommendations": []
    }

    # Port Scan
    open_ports = scan_open_ports(ip)
    if open_ports:
        report["open_ports"] = open_ports
        report["issues"].append("Open critical ports detected")
        report["recommendations"].append("Close unused ports")
        report["score"] -= len(open_ports) * 5

    return report
