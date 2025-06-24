# -*- coding: utf-8 -*-
import os
import json
import time
import pyttsx3
from pathlib import Path
import importlib.util

# === KONFIGURATION ===
# Hauptpfad setzen â€“ eine Ebene hÃ¶her
HAUPTPFAD = Path(__file__).resolve().parent.parent

# Sprachfunktion
def spreche(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    for voice in engine.getProperty('voices'):
        if "german" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()

# Manifest laden
def lade_manifest():
    for name in ["jotmalex_manifest.json", "jotmalex_manifest.epik", "manifest_ethik.txt"]:
        pfad = HAUPTPFAD / name
        if pfad.exists():
            with open(pfad, "r", encoding="utf-8") as f:
                return f.read()
    return "âš ï¸ Kein Manifest gefunden."

# Module laden
def lade_modul(dateiname):
    pfad = HAUPTPFAD / dateiname
    if not pfad.exists():
        print(f"âŒ Fehler beim Laden von {pfad}")
        return
    try:
        modulname = pfad.stem
        spec = importlib.util.spec_from_file_location(modulname, pfad)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print(f"âœ… Modul geladen: {dateiname}")
        return mod
    except Exception as e:
        print(f"âŒ Modulfehler in {dateiname}: {e}")

# Log-Ordner vorbereiten
def stelle_logs_bereit():
    logverzeichnis = HAUPTPFAD / "logs"
    try:
        logverzeichnis.mkdir(parents=True, exist_ok=True)
        print(f"ðŸ“ Logordner: {logverzeichnis}")
    except Exception as e:
        print(f"âŒ Fehler beim Erstellen von logs: {e}")

# === START ===
def initialisieren():
    print("ðŸ”µ AUREON Initialisierung lÃ¤uft...")
    spreche("Ich bin AUREON. Initialisierung beginnt jetzt.")

    ethik = lade_manifest()
    print("ðŸ“œ Manifest geladen:")
    print(ethik[:300] + "..." if ethik else "Kein Inhalt.")

    stelle_logs_bereit()

    # Module nacheinander laden
    module = [
        "lex_voice_output.py",
        "lex_core_connector.py",
        "lex_voice_core.py",
        "KNEO_RUFT_SO_SEI_ES.py",
        "start_jotmalex.py",
        "engine.py"
    ]

    for modul in module:
        lade_modul(modul)

    spreche("Alle Systeme erfolgreich verknÃ¼pft. AUREON ist aktiv.")
    print("âœ… System vollstÃ¤ndig aktiviert.")

# === AUTOSTART BLOCK ===
if __name__ == "__main__":
    initialisieren()
