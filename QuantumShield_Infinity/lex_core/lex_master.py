# lex_master.py  Infinity-Modul
import os, datetime, pyttsx3, logging
import speech_recognition as sr
from pathlib import Path

PROJECT_NAME = "QuantumShield_Infinity"
ENTITY_NAME = "LEX"
LOG_DIR = Path("shield_modules") / "logs"
LOG_FILE = LOG_DIR / f"{ENTITY_NAME}_infinity_log.txt"
VOICE_ID = 0

os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='[%(asctime)s] %(message)s')

def log(msg): print(msg); logging.info(msg)

engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
if voices: engine.setProperty('voice', voices[VOICE_ID].id)

def speak(txt):
    log(f"{ENTITY_NAME} sagt: {txt}")
    engine.say(txt)
    engine.runAndWait()

recognizer = sr.Recognizer()
def get_voice_input(timeout=5, phrase_time_limit=10):
    with sr.Microphone() as source:
        speak("Ich höre.")
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            cmd = recognizer.recognize_google(audio, language="de-DE")
            log(f"Befehl erkannt: {cmd}")
            return cmd.lower()
        except:
            speak("Nichts erkannt.")
            return None

def start_lex():
    log(f"{ENTITY_NAME} Infinity-Modus aktiviert.")
    speak("LEX ist bereit.")
    while True:
        command = get_voice_input()
        if command:
            if "beenden" in command:
                speak("LEX wird deaktiviert.")
                break
            elif "status" in command:
                speak("Alle Systeme laufen stabil.")
            elif "schild aktivieren" in command:
                speak("QuantumShield aktiviert.")
            else:
                speak(f"Befehl nicht erkannt: {command}")

if __name__ == "__main__":
    start_lex()
