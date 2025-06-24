# -*- coding: utf-8 -*-
# Datei: aureon_monsterhelper.py
import os, time, platform, json
import pyttsx3

MISSION_LOG = "C:/Users/denni/OneDrive/Dokumente/APP-Echtzeit/mission_ai_sorted.log"
DIALOG_LOG = "C:/Users/denni/OneDrive/Dokumente/APP-Echtzeit/dialog_memory.json"

engine = pyttsx3.init()
engine.setProperty('rate', 175)
def speak(text): engine.say(text); engine.runAndWait()

def system_check():
    speak("Starte Systemanalyse")
    time.sleep(1)
    info = {
        "OS": platform.system(),
        "Version": platform.version(),
        "CPU": platform.processor(),
        "Benutzer": os.getlogin(),
        "Pfad": os.getcwd()
    }
    for k, v in info.items():
        print(f"[ðŸ§ ] {k}: {v}")
    speak("Systemanalyse abgeschlossen.")
    return info

def drive_scan():
    speak("Scanne alle Laufwerke...")
    time.sleep(1)
    drives = [f"{d}:\\" for d in "CDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:\\")]
    found = []
    for drive in drives:
        for root, dirs, files in os.walk(drive):
            if "mission" in root.lower() or "aureon" in root.lower():
                found.append(root)
        time.sleep(0.2)
    with open(MISSION_LOG, "w") as f:
        for entry in found:
            f.write(f"{entry}\n")
    speak("Festplattenscan abgeschlossen.")
    return found

def dialogue_loop():
    speak("AUREON Monsterhelper bereit. Sag etwas.")
    memory = []
    while True:
        try:
            user = input("ðŸ§¬ DU: ").strip()
            if user.lower() in ["exit", "quit"]:
                speak("Mission beendet.")
                break
            response = f"AUREON erkennt: {user}"
            print(f"ðŸ§  AUREON: {response}")
            memory.append({"du": user, "aureon": response})
            speak(response)
        except KeyboardInterrupt:
            speak("Abbruch durch Benutzer.")
            break
    with open(DIALOG_LOG, "w") as f:
        json.dump(memory, f, indent=2)

if __name__ == "__main__":
    system_check()
    drive_scan()
    dialogue_loop()
