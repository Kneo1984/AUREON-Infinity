# lex_core/lex_to_jotma_bridge.py  Stimme zu Analyse (LEX ⇌ JOTMA)

from threading import Lock, Thread
import speech_recognition as sr
import pyttsx3
import time
import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from jotma_engine import jotma_core

ENTITY = "LEX"
LOG_PATH = "shield_modules/logs/LEX_JOTMA_bridge.txt"
logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format="[%(asctime)s] %(message)s")

engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine_lock = Lock()  # Sichert Zugriff auf runAndWait()

def speak(msg):
    def run():
        with engine_lock:
            engine.say(msg)
            engine.runAndWait()
    Thread(target=run).start()

def log(msg):
    print(f"[{ENTITY}] sagt:", msg)
    logging.info(msg)

def get_voice_command(timeout=5):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Ich höre.")
        try:
            audio = r.listen(source, timeout=timeout)
            return r.recognize_google(audio, language="de-DE")
        except sr.WaitTimeoutError:
            speak("Nichts erkannt.")
            return ""
        except sr.UnknownValueError:
            speak("Unverständlich.")
            return ""
        except sr.RequestError as e:
            speak("Netzwerkfehler.")
            log(f"SR ERROR: {e}")
            return ""

def start_bridge():
    log("Infinity-Bridge wird gestartet...")
    speak("LEX aktiviert Brücke zu JOTMA.")
    time.sleep(1)
    while True:
        try:
            command = get_voice_command()
            if command:
                log(f"Eingehend: {command}")
                response = jotma_core.analyze_and_connect(command)
                speak(response)
                log(f"Antwort: {response}")
        except KeyboardInterrupt:
            speak("LEX beendet Brücke.")
            log("Beendet durch Benutzer.")
            break

if __name__ == "__main__":
    start_bridge()
