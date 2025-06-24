# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUREON â€ VollstÃ¤ndiger Autostartâ€‘Launcher (MONSTER Edition)
Dateiname : aureon_autostart_fullsystem_MONSTER_2025-06-06_17-19-08.py
Pfad      : C:/Users/denni/OneDrive/Dokumente/APP-Echtzeit/
Version   : 2025â€‘06â€‘22 (Rootâ€‘optimiert)

Beschreibung
============
â€¢ PrÃ¼ft/legt Missionsâ€‘, Logâ€‘ und Responseâ€‘Ordner an
â€¢ Installiert fehlende Pythonâ€‘AbhÃ¤ngigkeiten (falls nÃ¶tig)
â€¢ Erstellt Dummyâ€‘Missionsskripte, wenn keine vorhanden
â€¢ Startet erkannte Missionsskripte im Hintergrund
â€¢ LÃ¤dt die Cosmicâ€‘GUI

Hinweis
=======
Die automatische Installation verwendet **kein** `--user`, sodass der Code
innerhalb von Virtualâ€‘Environments ebenso funktioniert wie systemweit.
"""

import importlib
import os
import platform
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# === BASISKONFIGURATION ======================================================
HOME = Path.home()
APP_ROOT      = HOME / "OneDrive" / "Dokumente" / "APP-Echtzeit"
MISSIONS_DIR  = APP_ROOT / "missions"
LOG_DIR       = APP_ROOT / "logs"
RESP_DIR      = APP_ROOT / "responses"
GUI_FILE      = APP_ROOT / "gui" / "aureon_gui_missions_cosmic.py"
LOG_FILE      = LOG_DIR / f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

# === HILFSFUNKTIONEN =========================================================

def log(message: str) -> None:
    """Schreibt eine Zeitmarke in die Logdatei und gibt sie auf stdout aus."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("[%H:%M:%S]")
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"{timestamp} {message}\n")
    print(message)


def ensure_dirs() -> None:
    """Erzeugt benÃ¶tigte Verzeichnisse, falls sie fehlen."""
    for path in (MISSIONS_DIR, LOG_DIR, RESP_DIR):
        path.mkdir(parents=True, exist_ok=True)
        log(f"ðŸ“ Ordner geprÃ¼ft: {path}")


def install_dependencies() -> None:
    """Installiert fehlende AbhÃ¤ngigkeiten ohne --userâ€‘Flag."""
    pkgs = [
        "pyttsx3",
        "SpeechRecognition",
        "requests",
        "beautifulsoup4",
        "watchdog",
    ]
    for pkg in pkgs:
        try:
            importlib.import_module(pkg.split("==")[0].lower())
            log(f"âœ… Modul bereits vorhanden: {pkg}")
        except ImportError:
            log(f"â¬‡ï¸  Installiere fehlendes Modul: {pkg}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
            log(f"âœ… Modul installiert: {pkg}")


def create_dummy_missions() -> None:
    """Erstellt Beispielâ€‘Missionsskripte, falls Missionsordner leer ist."""
    dummy_code = {
        "sektion1.py": 'print("ðŸŒ SektionÂ 1 aktiviert: NetzwerkÃ¼berprÃ¼fung â€¦")',
        "sektion2.py": 'print("ðŸ›°ï¸  SektionÂ 2 aktiviert: Internetverbindung â€¦")',
        "sektion3.py": 'print("ðŸ” SektionÂ 3 aktiviert: Sicherheitseinstellungen â€¦")',
    }
    if any(MISSIONS_DIR.iterdir()):
        log("ðŸ“„ Missionsskripte bereits vorhanden â€“ Dummyâ€‘Erstellung Ã¼bersprungen.")
        return
    for filename, code in dummy_code.items():
        filepath = MISSIONS_DIR / filename
        filepath.write_text(code, encoding="utf-8")
        log(f"âš™ï¸  Dummyâ€‘Skript erstellt: {filename}")


def run_missions() -> None:
    """Startet jedes Missionsskript als separaten Prozess."""
    missions = sorted(MISSIONS_DIR.glob("*.py"))
    log("ðŸ” Spiegelmodus aktiviert â€“ erkannte Missionen: " + ", ".join(m.name for m in missions))
    for mission in missions:
        log(f"âœ¨ Starte Mission: {mission.name}")
        subprocess.Popen([sys.executable, str(mission)], shell=False)


def start_gui() -> None:
    """Startet die Cosmicâ€‘GUI, falls vorhanden."""
    if not GUI_FILE.exists():
        log("âŒ GUIâ€‘Datei nicht gefunden: " + str(GUI_FILE))
        return
    subprocess.Popen([sys.executable, str(GUI_FILE)], shell=False)
    log("ðŸš€ GUI gestartet: AUREON Cosmic Missions")


# === HAUPTPLAN ==============================================================

def main() -> None:
    log("ðŸ§  AUREON AUTOSTART BEGINNTâ€¦")
    ensure_dirs()
    install_dependencies()
    create_dummy_missions()
    run_missions()
    start_gui()
    log("âœ… AUTOSTARTâ€‘VORGANG ABGESCHLOSSEN.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        log(f"âŒ Fehler: {exc}")
