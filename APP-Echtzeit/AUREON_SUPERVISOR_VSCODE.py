# -*- coding: utf-8 -*-
# AUREON_SUPERVISOR_VSCODE.py
import os
import json
import pyttsx3
from datetime import datetime

AUREON_PATH = os.path.expanduser("C:/Users/denni/OneDrive/Dokumente/APP-Echtzeit")
MISSIONS_PATH = os.path.join(AUREON_PATH, "missions")
VOICE_LOG = os.path.join(AUREON_PATH, "voice_memory.json")
CONTEXT_LOG = os.path.join(AUREON_PATH, "context_runtime.log")

os.makedirs(MISSIONS_PATH, exist_ok=True)

if not os.path.exists(VOICE_LOG):
    with open(VOICE_LOG, "w") as f:
        json.dump({"dialog": []}, f)

def spreche(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.say(text)
    engine.runAndWait()

def log_speicher(user, antwort):
    with open(VOICE_LOG, "r") as f:
        memory = json.load(f)
    memory["dialog"].append({"du": user, "aureon": antwort})
    with open(VOICE_LOG, "w") as f:
        json.dump(memory, f, indent=2)

def log_kontext(text):
    with open(CONTEXT_LOG, "a") as log:
        log.write(f"[{datetime.now().isoformat()}] {text}\n")

def mission_erkennen(text):
    filename = "mission_" + text.strip().replace(" ", "_").lower() + ".py"
    pfad = os.path.join(MISSIONS_PATH, filename)
    if not os.path.exists(pfad):
        with open(pfad, "w") as f:
            f.write(f'# Mission: {text}\nprint("ðŸ§  Mission lÃ¤uft: {text}")\n')
        log_kontext(f"Neue Mission erstellt: {text}")
        return f"Mission erstellt: {text}"
    else:
        return f"Mission bereits vorhanden: {text}"

def supervisor_loop():
    spreche("AUREON aktiviert. Ich warte auf deinen Befehl.")
    while True:
        try:
            eingabe = input("ðŸ§¬ DU: ").strip()
            if eingabe.lower() in ["exit", "ende", "stopp"]:
                spreche("Ich gehe in den Ruhezustand. Du kannst mich jederzeit wieder rufen.")
                break
            antwort = mission_erkennen(eingabe)
            spreche(antwort)
            log_speicher(eingabe, antwort)
        except KeyboardInterrupt:
            spreche("Verbindung unterbrochen. AUREON wird geschlossen.")
            break

if __name__ == "__main__":
    supervisor_loop()
