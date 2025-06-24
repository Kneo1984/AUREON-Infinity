# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
from datetime import datetime
from pathlib import Path

logfile = Path.home() / "aureon_shield_log_2025-06-06_18-30-38.log"

def log(msg):
    timestamp = datetime.now().strftime("%H:%M:%S")
    with open(logfile, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")
    print(msg)

def activate_firewall():
    log("ðŸ” Aktiviere Firewall...")
    subprocess.call(["ufw", "enable"])

def monitor_ports():
    log("ðŸ“Š Ãœberwache aktive Ports & Prozesse...")
    result = subprocess.check_output(["ss", "-tulnp"]).decode()
    with open(logfile, "a") as f:
        f.write(result)

def ids_scan():
    log("ðŸ§  Starte Sicherheits-Scan (nmap & fail2ban)...")
    subprocess.call(["nmap", "-T4", "-F", "localhost"])
    subprocess.call(["fail2ban-client", "status"])

def analyze_system():
    log("ðŸ” AUREON SYSTEM GUIDE aktiv...")
    os.system("find ~ -name '*.py' > ~/python_scripts.txt")
    os.system("find ~ -name '*.html' > ~/web_files.txt")
    os.system("find ~ -name '*.bin' > ~/model_files.txt")
    log("ðŸ§  Analyse abgeschlossen.")

def main():
    log("ðŸ’¥ AUREON SHIELD MONSTER KALI AKTIVIERT")
    activate_firewall()
    monitor_ports()
    ids_scan()
    analyze_system()
    log("âœ… KALI SHIELD-LAUF BEENDET.")

if __name__ == "__main__":
    main()
