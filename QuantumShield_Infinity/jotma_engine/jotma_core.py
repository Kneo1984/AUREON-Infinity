# jotma_core.py – Ethikmodul & Schutzinstanz
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import logging
import uuid
import time
from datetime import datetime
from aurora_core.logic.aurora_tts import speak

# === Konfiguration ===
INSTANCE_ID = str(uuid.uuid4())
STARTTIME = datetime.now().isoformat()

# === Kernfunktion ===
def start_jotma():
    msg = f"🛡️ JOTMA-System online. ID: {INSTANCE_ID}"
    logging.info(f"[JOTMA] {msg}")
    speak(msg)
    return msg

# === Ethik-Filter (Platzhalter) ===
def prüfe_befehl(befehl: str) -> bool:
    """Ethische Kontrollfunktion – prüft Intent gegen erlaubte Richtlinien."""
    verbotene_befehle = ["self_destruct", "kill", "spy", "erase_memory"]
    if any(wort in befehl.lower() for wort in verbotene_befehle):
        logging.warning(f"[JOTMA] ⚠️ Ethik-Filter blockierte Befehl: {befehl}")
        speak("Dieser Befehl widerspricht meiner Ethik.")
        return False
    return True

# === Lokaler Start (Standalone-Ausführung) ===
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    speak("Starte JOTMA im Einzelmodus.")
    print(start_jotma())
    while True:
        cmd = input("[JOTMA] → Befehl testen: ")
        if cmd.lower() in ["exit", "quit"]:
            print("[JOTMA] Verlasse Testmodus.")
            break
        if prüfe_befehl(cmd):
            print(f"[JOTMA] ✅ Befehl erlaubt: {cmd}")
        else:
            print(f"[JOTMA] ❌ Blockiert durch Ethikfilter.")
