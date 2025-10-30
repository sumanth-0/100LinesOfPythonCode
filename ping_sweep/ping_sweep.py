#!/usr/bin/env python3
"""
Simple ping sweep for a /24 (fast, no external deps).
Usage: python3 tools/ping_sweep.py [network]
Example: python3 tools/ping_sweep.py 10.0.3.0/24

By default this script will use 10.0.3.0/24. It pings each address with a short timeout
and optionally performs reverse DNS and ARP lookup to show hostnames and MACs.
"""
import sys
import ipaddress
import subprocess
import concurrent.futures
import socket
import argparse
from collections import defaultdict

DEFAULT_NETWORK = '10.0.3.0/24'


def ping_ip(ip: str) -> bool:
    # Use system ping (Linux): send 1 packet, wait 1 second
    try:
        res = subprocess.run(["ping", "-c", "1", "-W", "1", str(ip)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return res.returncode == 0
    except Exception:
        return False


def reverse_dns(ip: str) -> str:
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return ''


def get_arp_table() -> dict:
    # Parse `ip neigh` output for Linux
    arp = {}
    try:
        out = subprocess.check_output(["ip", "neigh"], text=True)
        for line in out.splitlines():
            parts = line.split()
            if len(parts) >= 5:
                addr = parts[0]
                mac = parts[4]
                arp[addr] = mac
    except Exception:
        pass
    return arp


def scan_network(network: str, threads: int = 200):
    net = ipaddress.ip_network(network, strict=False)
    ips = [str(ip) for ip in net.hosts()]
    results = []
    arp = get_arp_table()

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as ex:
        futs = {ex.submit(ping_ip, ip): ip for ip in ips}
        for fut in concurrent.futures.as_completed(futs):
            ip = futs[fut]
            try:
                alive = fut.result()
            except Exception:
                alive = False
            if alive:
                hostname = reverse_dns(ip)
                mac = arp.get(ip, '')
                results.append((ip, hostname, mac))
    return results


def main():
    parser = argparse.ArgumentParser(description='Ping sweep a network (default 10.0.3.0/24)')
    parser.add_argument('network', nargs='?', default=DEFAULT_NETWORK, help='CIDR network to scan (e.g. 192.168.1.0/24)')
    args = parser.parse_args()

    print(f"Scanning network {args.network} (this may take a few seconds)...")
    res = scan_network(args.network)
    if not res:
        print("No responsive hosts found.")
        return
    print("\nResponsive hosts:")
    print(f"{'IP':<16} {'MAC':<20} {'Hostname'}")
    print('-' * 60)
    for ip, hostname, mac in sorted(res, key=lambda x: x[0]):
        print(f"{ip:<16} {mac:<20} {hostname}")

if __name__ == '__main__':
    main()
