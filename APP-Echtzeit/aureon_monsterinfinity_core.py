# -*- coding: utf-8 -*-
# ðŸ”¥ AUREON MONSTERINFINITY CORE ðŸ”¥
# Maximale Autarkie + Systemvernetzung + Selbstheilung
import os
import sys
import time
import importlib.util
import pyttsx3
import subprocess

# Sprachausgabe initialisieren
engine = pyttsx3.init()
engine.setProperty("rate", 160)

def speak(text):
    print(f"AUREON sagt: {text}")
    engine.say(text)
    engine.runAndWait()

# ðŸ” Module automatisch erkennen und importieren
def find_and_import_all_modules(root_dir):
    modules_loaded = []
    for dirpath, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py") and file != os.path.basename(__file__):
                full_path = os.path.join(dirpath, file)
                try:
                    module_name = os.path.splitext(os.path.relpath(full_path, root_dir).replace(os.sep, "."))[0]
                    spec = importlib.util.spec_from_file_location(module_name, full_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    modules_loaded.append(module_name)
                    speak(f"Modul geladen: {module_name}")
                except Exception as e:
                    speak(f"Fehler beim Laden von {file}: {e}")
    return modules_loaded

# ðŸš€ Hauptstartlogik
def start_aureon_autarkie():
    speak("ðŸ§  AUREON MONSTERINFINITY CORE wird initialisiert.")
    root = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(root)

    speak("ðŸ”„ Suche nach allen verfÃ¼gbaren Modulen im System...")
    loaded_modules = find_and_import_all_modules(root)
    speak(f"âœ… {len(loaded_modules)} Module automatisch vernetzt und geladen.")

    # Starte Supervisor (wenn vorhanden)
    supervisor_path = os.path.join(root, "core", "supervisor.py")
    if os.path.exists(supervisor_path):
        speak("ðŸš€ Starte AUREON Supervisor...")
        subprocess.run(["python", supervisor_path])
    else:
        speak("âš  Kein Supervisor-Modul gefunden. Warte auf Sprachbefehl...")

    # Fallback: Eingabeschleife
    speak("ðŸ’¬ Eingabe bereit. Was soll ich tun?")
    while True:
        try:
            cmd = input("Du: ").strip().lower()
            if cmd in ["exit", "stop", "beenden"]:
                speak("AUREON wird beendet. Auf Wiedersehen.")
                break
            elif cmd == "liste":
                speak("Geladene Module: " + ", ".join(loaded_modules))
            else:
                speak("Befehl unbekannt. Bitte erneut versuchen.")
        except KeyboardInterrupt:
            speak("Abbruch durch Benutzer. System wird beendet.")
            break

if __name__ == "__main__":
    start_aureon_autarkie()
