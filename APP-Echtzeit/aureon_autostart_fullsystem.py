# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
import platform
from pathlib import Path
from datetime import datetime

# === BASISKONFIGURATION ===
APP_ROOT = Path.home() / "OneDrive" / "Dokumente" / "APP-Echtzeit"
MISSIONS_DIR = APP_ROOT / "missions"
GUI_FILE = APP_ROOT / "gui" / "aureon_gui_missions_cosmic.py"
LOG_FILE = APP_ROOT / "logs" / f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

# === SYSTEMKONTROLLE ===
def log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as logf:
        logf.write(f"[{datetime.now().strftime('%H:%M:%S')}] {message}\n")
    print(message)

def ensure_dirs():
    for path in [MISSIONS_DIR, APP_ROOT / "logs", APP_ROOT / "responses"]:
        path.mkdir(parents=True, exist_ok=True)
        log(f"ðŸ“ Ordner geprÃ¼ft: {path}")

def install_dependencies():
    pkgs = [
        "pyttsx3", "speechrecognition", "requests",
        "beautifulsoup4", "watchdog"
    ]
    for pkg in pkgs:
        subprocess.run([sys.executable, "-m", "pip", "install", "--user", pkg], check=True)
        log(f"âœ… Modul installiert: {pkg}")

def create_mission_scripts():
    dummy_code = {
        "sektion1.py": 'print("ðŸŒ Sektion 1 aktiviert: NetzwerkÃ¼berprÃ¼fung gestartet.")',
        "sektion2.py": 'print("ðŸ›°ï¸ Sektion 2 aktiviert: Internetverbindung & DNS werden geprÃ¼ft.")',
        "sektion3.py": 'print("ðŸ” Sektion 3 aktiviert: Sicherheitseinstellungen werden validiert.")',
    }
    for filename, code in dummy_code.items():
        (MISSIONS_DIR / filename).write_text(code, encoding="utf-8")
        log(f"âš™ï¸ Dummy-Skript erstellt: {filename}")

def start_gui():
    if not GUI_FILE.exists():
        log("âŒ GUI-Datei nicht gefunden.")
        return
    subprocess.Popen([sys.executable, str(GUI_FILE)], shell=True)
    log("ðŸš€ GUI gestartet: AUREON Cosmic Missions")

def main():
    log("ðŸ§  AUREON AUTOSTART BEGINNT...")
    ensure_dirs()
    install_dependencies()
    create_mission_scripts()
    start_gui()
    log("âœ… AUTOSTART-VORGANG ABGESCHLOSSEN.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log(f"âŒ Fehler: {e}")
