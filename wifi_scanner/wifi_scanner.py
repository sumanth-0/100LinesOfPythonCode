#!/usr/bin/env python3
"""Simple Wi-Fi scanner
Provides a small CLI that scan nearby Wi-Fi networks using
nmcli, iw, or iwlist and parsers for their outputs.
"""
from subprocess import PIPE, Popen
import shutil

def run(cmd):
    try:
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, text=True)
        out,err = p.communicate(timeout=8)
        return out
    except Exception:
        return ""
def parse_nmcli(out):
    rows = []
    for line in out.splitlines()[1:]:
        parts = [p.strip() for p in line.split()]
        if not parts: continue
        # nmcli aligns columns; fallback simple split: last cols are SIGNAL CHAN SECURITY
        ssid = line[:40].strip()
        rest = line[40:].split()
        if len(rest) >= 3:
            bssid = rest[0]
            signal = rest[1]
        else:
            bssid = ''
            signal = rest[0] if rest else ''
        rows.append((ssid,bssid,signal))
    return rows
def parse_iw(out):
    rows = []
    ssid = bssid = signal = None
    for l in out.splitlines():
        l = l.strip()
        if l.startswith('BSS '):
            if ssid:
                rows.append((ssid,bssid,signal))
            bssid = l.split()[1]
            ssid = signal = None
        elif l.startswith('SSID:'):
            ssid = l.split(':',1)[1].strip()
        elif 'signal:' in l:
            signal = l.split('signal:')[1].split()[0]
    if ssid:
        rows.append((ssid,bssid,signal))
    return rows
def parse_iwlist(out):
    rows=[]
    ssid=bssid=signal=None
    for l in out.splitlines():
        l=l.strip()
        if l.startswith('Cell '):
            if ssid: rows.append((ssid,bssid,signal))
            parts=l.split()
            bssid=parts[4] if len(parts)>=5 else ''
            ssid=signal=None
        elif 'ESSID:' in l:
            ssid=l.split('ESSID:')[1].strip('"')
        elif 'Signal level=' in l:
            signal=l.split('Signal level=')[1].split()[0]
    if ssid: rows.append((ssid,bssid,signal))
    return rows
def pretty_print(rows):
    if not rows:
        print('No networks found or scanning tools not available.')
        return
    print(f"{'SSID':40} {'BSSID':20} SIGNAL")
    for s,b,sg in rows:
        print(f"{s[:40]:40} {b:20} {sg}")
def main():
    if shutil.which('nmcli'):
        out = run(['nmcli','-f','SSID,BSSID,SIGNAL,CHAN,SECURITY','device','wifi','list'])
        rows = parse_nmcli(out)
        pretty_print(rows)
        return
    if shutil.which('iw'):
        # find iface
        out = run(['iw','dev'])
        iface = None
        for l in out.splitlines():
            l=l.strip()
            if l.startswith('Interface '):
                iface = l.split()[1]; break
        if iface:
            out = run(['sudo','iw','dev',iface,'scan'])
            rows = parse_iw(out)
            pretty_print(rows)
            return
    if shutil.which('iwlist'):
        iface = 'wlan0'
        out = run(['sudo','iwlist',iface,'scanning'])
        rows = parse_iwlist(out)
        pretty_print(rows)
        return
    print('No scanning tools (nmcli/iw/iwlist) found. Please run on a Linux host with Wi‑Fi tools installed.')
if __name__=='__main__':
    main()