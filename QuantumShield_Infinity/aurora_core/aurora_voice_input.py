# -*- coding: utf-8 -*-
# aurora_core/aurora_voice_input.py

import speech_recognition as sr

recognizer = sr.Recognizer()

def hör_aurora():
    try:
        with sr.Microphone() as quelle:
            print("[AURORA]  Ich höre...")
            audio = recognizer.listen(quelle, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio, language="de-DE")
            print(f"[DU SAGST] {text}")
            return text
    except sr.UnknownValueError:
        return "Ich konnte dich nicht verstehen."
    except sr.RequestError:
        return "Fehler bei der Verbindung zur Spracherkennung."
    except Exception as e:
        return f"Fehler: {e}"
