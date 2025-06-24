# -*- coding: utf-8 -*-
# AUREON_MISSIONAI_SPEAK.py
import os
import json
import pyttsx3
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

def spreche(text):
    print(f"ðŸ§  AUREON sagt: {text}")
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()

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

def zeige_und_spreche(missionen):
    spreche("Ich beginne mit der Missionsauswertung.")
    for score, name, preview in missionen[:5]:
        text = f"Missionsdatei: {name}. PrioritÃ¤t: {score}. Vorschau: {preview}"
        spreche(text)

def speichere_log(missionen):
    with open(LOG_PATH, "w", encoding="utf-8") as log:
        for score, name, preview in missionen:
            log.write(f"[{score}] {name}: {preview}\n")

if __name__ == "__main__":
    spreche("AUREON Missionsanalyse startet jetzt.")
    missionen = analysiere_missionen()
    zeige_und_spreche(missionen)
    speichere_log(missionen)
    spreche("Analyse abgeschlossen. Du kannst nun eine Mission auswÃ¤hlen.")
