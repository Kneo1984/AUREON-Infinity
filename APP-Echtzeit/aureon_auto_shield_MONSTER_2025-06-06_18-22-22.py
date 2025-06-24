# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import platform
from datetime import datetime
from pathlib import Path

# === SYSTEMBASIS ===
now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_file = Path.home() / f"aureon_shield_log_{now}.log"

def log(msg):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")
    print(msg)

# === FIREWALL AKTIVIERUNG ===
def activate_firewall():
    if platform.system() == "Windows":
        subprocess.run(["powershell", "-Command", "Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True"])
    elif platform.system() == "Linux":
        subprocess.run(["sudo", "ufw", "enable"])
    log("ðŸ” Firewall aktiviert.")

# === PORT- UND PROZESSÃœBERWACHUNG ===
def monitor_ports():
    if platform.system() == "Windows":
        cmd = "netstat -aon"
    else:
        cmd = "ss -tuln"
    result = subprocess.getoutput(cmd)
    log("ðŸ“Š Aktive Verbindungen und Ports:")
    log(result)

# === IDS-CHECKS ===
def run_ids():
    if platform.system() == "Linux":
        log("ðŸ›¡ï¸ IDS gestartet: nmap, auditd, fail2ban")
        subprocess.run(["sudo", "nmap", "-sS", "127.0.0.1"])
        subprocess.run(["sudo", "auditctl", "-s"])
        subprocess.run(["sudo", "fail2ban-client", "status"])
    else:
        log("âš ï¸ IDS auf Windows nicht direkt unterstÃ¼tzt.")

# === SYSTEM GUIDE ===
def system_guide():
    base = Path.home()
    py_files = list(base.rglob("*.py"))
    web_files = list(base.rglob("*.html")) + list(base.rglob("*.js")) + list(base.rglob("*.css"))
    model_files = list(base.rglob("*.bin")) + list(base.rglob("*.pt")) + list(base.rglob("*.onnx"))

    log("ðŸ§  Analyse abgeschlossen â€“ priorisierte Hinweise folgen.")
    log(f"â–¶ï¸ Du hast {len(py_files)} Python-Skripte â€“ prÃ¼fe auf alte, doppelte oder unvollstÃ¤ndige.")
    log(f"ðŸŒ Web-Dateien erkannt: {len(web_files)}")
    log(f"ðŸ§¬ Modell-Dateien gefunden: {len(model_files)}")
    log("ðŸ“Œ Vorschlag: Starte âž¤ AUREON_MISSIONAI_LOGIC_CORE.py oder sprecher_windows.py")

# === AUSFÃœHRUNG ===
def main():
    log("ðŸ’¥ AUREON SHIELD MONSTER AKTIVIERT")
    activate_firewall()
    monitor_ports()
    run_ids()
    system_guide()
    log("âœ… SHIELD-DURCHLAUF BEENDET.")

if __name__ == "__main__":
    main()
