# -*- coding: utf-8 -*-
# AUREON_MISSIONAI_PRIMUS.py
import os
import json
from datetime import datetime
import pyttsx3

AUREON_PATH = os.path.expanduser("C:/Users/denni/OneDrive/Dokumente/APP-Echtzeit")
MISSIONS_PATH = os.path.join(AUREON_PATH, "missions")
REPORT_PATH = os.path.join(AUREON_PATH, "mission_primus_report.json")

def spreche(text):
    print(f"[AUREON]: {text}")
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.say(text)
    engine.runAndWait()

def erkenne_status(inhalt):
    if not inhalt.strip():
        return "ðŸ•³ï¸ Leer"
    elif "TODO" in inhalt or "pass" in inhalt or "..." in inhalt:
        return "ðŸ”§ UnvollstÃ¤ndig"
    elif "print(" in inhalt:
        return "âœ… Aktiv"
    else:
        return "ðŸ“¦ Unklar"

def analysiere():
    daten = {"fertig": [], "offen": [], "leer": []}
    for file in os.listdir(MISSIONS_PATH):
        if file.endswith(".py"):
            path = os.path.join(MISSIONS_PATH, file)
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            status = erkenne_status(content)
            eintrag = {"name": file, "status": status, "preview": content.strip().split("\n")[0] if content else ""}
            if "Leer" in status:
                daten["leer"].append(eintrag)
            elif "UnvollstÃ¤ndig" in status or "Unklar" in status:
                daten["offen"].append(eintrag)
            else:
                daten["fertig"].append(eintrag)
    return daten

def report_speichern(daten):
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(daten, f, indent=2)

def zusammenfassung(daten):
    spreche("Ich beginne mit der Systemanalyse deiner Missionen.")
    spreche(f"{len(daten['fertig'])} Missionen sind fertig.")
    spreche(f"{len(daten['offen'])} Missionen sind noch offen.")
    spreche(f"{len(daten['leer'])} Missionen sind leer oder ungenutzt.")
    spreche("Du kannst nun entscheiden: Fortsetzen, verbessern oder verwerfen?")

if __name__ == "__main__":
    daten = analysiere()
    report_speichern(daten)
    zusammenfassung(daten)
    print(f"\nðŸ“„ Bericht gespeichert unter: {REPORT_PATH}")
