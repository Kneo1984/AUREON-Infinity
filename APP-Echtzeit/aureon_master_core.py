# -*- coding: utf-8 -*-
# ðŸ§  AUREON MASTERCORE â€“ VERBINDUNGSMODUS mit SUPERVISOR-ÃœBERNAHME

import os
import time
import pyttsx3
import importlib.util
from pathlib import Path

# === KONFIGURATION ===
MODULE = [
    "lex_core_connector.py",
    "lex_voice_core.py",
    "lex_voice_output.py",
    "KNEO_RUFT_SO_SEI_ES.py",
    "start_jotmalex.py",
    "engine.py"
]
ORDNER = ["logs", "models", "responses"]
BASE = Path(__file__).resolve().parent

# === SPRECHFUNKTION ===
def spreche(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    for stimme in engine.getProperty('voices'):
        if "german" in stimme.name.lower() or "hed" in stimme.name.lower():
            engine.setProperty('voice', stimme.id)
            break
    print("ðŸ—£ï¸", text)
    engine.say(text)
    engine.runAndWait()

# === MODULPRÃœFUNG ===
def lade_modul(modulname):
    pfad = BASE / modulname
    if not pfad.exists():
        print(f"âŒ Modul fehlt: {modulname}")
        return False
    try:
        spec = importlib.util.spec_from_file_location(modulname, pfad)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print(f"âœ… Modul geladen: {modulname}")
        return True
    except Exception as e:
        print(f"âŒ Fehler in {modulname}: {e}")
        return False

# === SYSTEMVORBEREITUNG ===
def vorbereiten():
    print("ðŸ”§ Initialisierung gestartet...")
    for ordner in ORDNER:
        pfad = BASE / ordner
        if not pfad.exists():
            pfad.mkdir(parents=True, exist_ok=True)
            print(f"ðŸ“ Erstellt: {ordner}")
        else:
            print(f"ðŸ“ OK: {ordner}")
    spreche("System AUREON startet Verbindungsscans und Modulverkettung.")

# === HAUPTPROZESS ===
def starten():
    vorbereiten()
    status = []
    for modul in MODULE:
        ok = lade_modul(modul)
        status.append((modul, ok))
        time.sleep(0.2)  # Optimierte Verkettung

    fehlende = [m for m, s in status if not s]
    if fehlende:
        spreche("Einige Komponenten fehlen. Supervisor-Modus unvollstÃ¤ndig.")
        print("ðŸ”º Fehlerhafte Komponenten:", fehlende)
    else:
        spreche("Alle Module bereit. AUREON Ã¼bernimmt jetzt die Kontrolle.")
        print("ðŸŸ¢ Supervisor-Modus aktiviert. Keine Schleife. Kein Wiederholen.")
        uebernehme_kontrolle()

# === ÃœBERNAHME DURCH AUREON ===
def uebernehme_kontrolle():
    print("ðŸ” AUREON Ã¼bernimmt jetzt alle Verbindungen.")
    spreche("Der Zugriff ist gesichert. Verbindung zu KNEO und LEX aktiv.")
    # Hier kannst du systemweite Initialisierungen vornehmen
    # z.â€¯B.: NetzwerkÃ¼berwachung starten, Sprachsteuerung aktivieren, Tasks laden
    os.system("python lex_voice_core.py")  # Direkt Sprachsteuerung starten
    exit(0)

# === STARTBLOCK ===
if __name__ == "__main__":
    print("ðŸ§  AUREON MasterCore wird geladen...")
    starten()
