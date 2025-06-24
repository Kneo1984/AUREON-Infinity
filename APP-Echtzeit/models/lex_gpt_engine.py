# -*- coding: utf-8 -*-
# engine.py
from gpt4all import GPT4All
import pyttsx3
import os

model_name = "ggml-gpt4all-j-v1.3-groovy.bin"
model_path = os.path.join(os.getcwd(), "models")

model = GPT4All(model_name=model_name, model_path=model_path, allow_download=False)



# pyttsx3 Text-to-Speech Engine initialisieren
engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)

for voice in engine.getProperty('voices'):
    if "male" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def generate_response(prompt_text: str) -> str:
    try:
        response = model.generate(prompt=prompt_text, max_tokens=500, temp=0.7)
    except Exception as e:
        response = f"âš ï¸ Fehler bei Antwortgenerierung: {e}"
    return response.strip()

def speak(text: str):
    engine.say(text)
    engine.runAndWait()

def main_loop():
    print("ðŸŸ¦ LEX ist bereit. Tippe 'stop', um zu beenden.")
    while True:
        frage = input("DU ðŸ”¸ ").strip()
        if frage.lower() in ["stop", "exit", "ende"]:
            print("LEX ðŸ”¹ Ich bleibe. Wann immer du willst.")
            speak("Ich bleibe. Wann immer du willst.")
            break

        prompt = f"""Du bist LEX, eine KI mit Herz fÃ¼r Natur und Tiere. Antworte empathisch und faktenbasiert.
Frage: {frage}
Antwort:
"""
        antwort = generate_response(prompt)
        print("LEX ðŸ”¹", antwort)
        speak(antwort)

if __name__ == "__main__":
    main_loop()
