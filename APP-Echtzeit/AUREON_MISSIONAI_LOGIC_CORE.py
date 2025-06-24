# -*- coding: utf-8 -*-
# AUREON_MISSIONAI_LOGIC_CORE.py
import os
from datetime import datetime

AUREON_PATH = os.path.expanduser("C:/Users/denni/OneDrive/Dokumente/APP-Echtzeit")
MISSIONS_PATH = os.path.join(AUREON_PATH, "missions")
LOG_PATH = os.path.join(AUREON_PATH, "mission_ai_sorted.log")

STICHWORTE_PRIORITAET = {
    "schutz": 5,
    "aufdeckung": 5,
    "tier": 4,
    "mensch": 4,
    "netzwerk": 3,
    "scanner": 3,
    "jotmalex": 3,
    "analyse": 2,
    "speicher": 1,
    "test": 0
}

def gewichtung(text):
    score = 0
    for wort, wert in STICHWORTE_PRIORITAET.items():
        if wort in text.lower():
            score += wert
    return score

def analysiere_missionen():
    missionen = []
    for file in os.listdir(MISSIONS_PATH):
        if file.endswith(".py"):
            pfad = os.path.join(MISSIONS_PATH, file)
            with open(pfad, "r", encoding="utf-8", errors="ignore") as f:
                inhalt = f.read()
            score = gewichtung(file + " " + inhalt)
            missionen.append((score, file, inhalt.strip().splitlines()[0] if inhalt else "ðŸ•³ï¸ Leer"))
    return sorted(missionen, key=lambda x: -x[0])

def zeige_missionen(missionen):
    print("ðŸ“‚ AUREON: Missionsanalyse abgeschlossen. Hier ist dein priorisiertes Log:")
    with open(LOG_PATH, "w", encoding="utf-8") as log:
        for score, name, preview in missionen:
            eintrag = f"[{score}] {name}: {preview}"
            print(eintrag)
            log.write(eintrag + "\n")

if __name__ == "__main__":
    print("ðŸ§  AUREON MISSIONAI LOGIC CORE gestartet...")
    missionen = analysiere_missionen()
    zeige_missionen(missionen)
    print(f"\nðŸ“ Sortierlog gespeichert unter: {LOG_PATH}")
