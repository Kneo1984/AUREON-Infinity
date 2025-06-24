# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from lex_core_connector import AUREON
import speech_recognition as sr
from lex_core_connector import AUREON
import pyttsx3, time, sys

#  Audio helpers 
engine = pyttsx3.init()
engine.setProperty("rate", 185)
engine.setProperty("volume", 1.0)

def speak(txt:str):
    engine.say(txt)
    engine.runAndWait()

def listen()->str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("  Sage etwas oder tippe hier:")
        audio = r.listen(source, phrase_time_limit=5)
    try:
        return r.recognize_google(audio, language="de-DE")
    except sr.UnknownValueError:
        return input("Sage etwas oder tippe hier: ").strip()
    except Exception as e:
        print("", e)
        return input("Sage etwas oder tippe hier: ").strip()

#  Haupt-Loop 
def main():
    speak("Ich bin bereit, dir zuzuhören.")
    while True:
        befehl = listen()
        print(f"Erkannt: {befehl}")
        action = AUREON.lex_interpreter(befehl)
        antwort = AUREON.lex_response(action, befehl)
        speak(antwort)
        print(" ", antwort)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n  AUREON beendet.")
        sys.exit()



