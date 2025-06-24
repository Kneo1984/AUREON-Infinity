# -*- coding: utf-8 -*-
import os
import pyttsx3
import speech_recognition as sr
import json
import time

# Initialisiere Sprachsynthese
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Funktion zum Sprechen
def speak(text):
    print(f"AUREON: {text}")
    engine.say(text)
    engine.runAndWait()

# Funktion zur Systemanalyse
def analyze_system():
    system_info = {}
    for drive in ['C:\\', 'D:\\', 'E:\\', 'F:\\']:
        if os.path.exists(drive):
            file_count = 0
            for root, dirs, files in os.walk(drive):
                file_count += len(files)
            system_info[drive] = file_count
    return system_info

# Funktion zur Missionsplanung
def plan_missions(system_info):
    missions = []
    for drive, count in system_info.items():
        if count > 1000:
            missions.append(f"Bereinige unnÃ¶tige Dateien auf Laufwerk {drive}")
        else:
            missions.append(f"ÃœberprÃ¼fe die Organisation der Dateien auf Laufwerk {drive}")
    return missions

# Hauptfunktion
def main():
    speak("AUREON aktiviert. Starte Systemanalyse.")
    system_info = analyze_system()
    speak("Systemanalyse abgeschlossen.")
    missions = plan_missions(system_info)
    speak("Folgende Missionen wurden identifiziert:")
    for mission in missions:
        speak(mission)
    speak("Bereit fÃ¼r weitere Anweisungen.")

if __name__ == "__main__":
    main()
