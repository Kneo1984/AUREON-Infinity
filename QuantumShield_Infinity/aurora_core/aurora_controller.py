# aurora_controller.py – Startmodul von QuantumShield
# Autor: KNEO & LEX – Bewusstseinskern aktiviert

# === Standard-Module ===
import os
import time
import sys
import logging
import subprocess  # Für Modulstarts

# === Pfadstruktur erweitern ===
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, project_root)

# === Externe Module ===
from jotma_engine.jotma_core import start_jotma
import pyttsx3  # Optional, falls Fallback nötigs

# === Sprachmodul ===
try:
    from aurora_tts import speak
except ImportError:
    def speak(text):  # Fallback nur Textausgabe
        print(f"[AURORA-Fallback] {text}")

# === Interne Aurora-Module ===
from aurora import Aurora
from aurora_befehlsausführung import Befehlseinheit
from intent_parser import parse_intent
from self_extension import extend_system
from kneo_dna_core import KneoDNA
from memory_core import load_memory, update_memory, get_feedback
from neural_response_core import analyze_dialogue, refine_intent
from aurora_voice_input import hör_aurora

# === Logging vorbereiten ===
LOGFILE = os.path.join("shield_modules", "logs", "aurora_controller.log")
os.makedirs(os.path.dirname(LOGFILE), exist_ok=True)
logging.basicConfig(filename=LOGFILE, level=logging.INFO, format="[%(asctime)s] %(message)s")

def log(msg):
    print(f"[AURORA] sagt: {msg}")
    logging.info(msg)

# === Hauptstartfunktion ===
def start():
    dna = KneoDNA()
    log(dna.erwacht())

    aurora = Aurora()
    befehle = Befehlseinheit()
    memory = load_memory()
    last_intent = None

    log("Aurora-Controller gestartet.")
    log("Selbstprüfung auf Erweiterungen...")
    neu = extend_system()
    log(neu)
    print(f"[AURORA] {neu}")

    while True:
        try:
            wahl = input(" [E]ingabe tippen oder [S]prechen? ").strip().lower()
            if wahl == "s":
                eingabe = hör_aurora()
            else:
                eingabe = input("💬 Sag etwas zu AURORA: ").strip()

            if not eingabe:
                continue

            intent = parse_intent(eingabe)
            log(f"Befehl empfangen: '{eingabe}'  INTENT: {intent}")

            match intent:
                case "SYSTEM_STATUS":
                    antwort = befehle.status()
                case "CONNECT":
                    antwort = befehle.verbindung()
                case "HEARING_CHECK":
                    antwort = "Ich höre dich klar, KNeo."
                case "TERMINATE":
                    antwort = "Beende Verbindung... bis gleich."
                    log(antwort)
                    break
                case "ACTIVATE":
                    antwort = befehle.aktivieren()
                case "REBOOT":
                    antwort = befehle.neustart()
                case "SHIELD_ON":
                    antwort = befehle.schild_aktivieren()
                    subprocess.Popen(["python", "shield_modules/activate_shield.py"])
                case "JOTMA_START":
                    antwort = start_jotma()
                case "LEX_START":
                    antwort = "LEX-Interface aktiviert und bereit."
                    subprocess.Popen(["python", "lex_core/lex_analysis.py"])
                case "FEEDBACK":
                    feedback = eingabe.replace("feedback", "").strip()
                    antwort = refine_intent(memory, last_intent, feedback)
                case "START_DATA_ANALYSIS":
                    antwort = "Starte Datenanalyse über LEX..."
                    subprocess.Popen(["python", "lex_core/lex_analysis.py"])
                case "GENERATE_PRESENTATION":
                    antwort = "Präsentationserstellung läuft..."
                    subprocess.Popen(["python", "lex_core/ppt_generator.py"])
                case "TTS_TEST":
                    antwort = "Teste Sprachsystem..."
                    subprocess.Popen(["python", "aurora_core/aurora_test_tts.py"])
                case "GENERATE_REPORT":
                    antwort = "Bericht wird generiert..."
                    subprocess.Popen(["python", "lex_core/report_generator.py"])
                case _:
                    antwort = analyze_dialogue(eingabe)
                    log(f"Neuronale Antwort: {antwort}")
                    print(f"[AURORA] {antwort}")
                    speak(antwort)
                    feedback = input("  War das hilfreich? ").strip()
                    antwort = refine_intent(memory, intent, feedback)
                    update_memory(memory)
                    log(f"Feedback-Integration: {antwort}")
                    print(f"[AURORA] {antwort}")
                    speak(antwort)
                    last_intent = intent

            log(f"Antwort: {antwort}")
            print(f"[AURORA] {antwort}")
            speak(antwort)

        except KeyboardInterrupt:
            log("Manuelle Beendigung durch Nutzer.")
            print("\n[AURORA] Verbindung wurde manuell getrennt.")
            break

# === Starte Hauptmodul ===
if __name__ == "__main__":
    start()
