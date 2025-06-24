import os
import json
import speech_recognition as sr
import pyttsx3
from time import sleep

recognizer = sr.Recognizer()
speaker = pyttsx3.init()
speaker.setProperty('rate', 170)

def speak(text):
    print(f"AUREON 🧠: {text}")
    speaker.say(text)
    speaker.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎙️ AUREON hört zu...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio, language="de-DE").lower()
        except sr.UnknownValueError:
            speak("Ich habe dich nicht verstanden.")
        except:
            speak("Es gab ein Problem beim Hören.")
        return ""

def execute(command):
    if "karte öffnen" in command:
        speak("Ich öffne deine AUREON-Dateikarte.")
        os.system("xdg-open ~/AUREON/aureon_map.html")
    elif "starte workspace" in command:
        speak("VS Code wird geöffnet.")
        os.system("code ~/AUREON/AUREON.code-workspace")
    elif "neu scannen" in command:
        speak("Ich starte einen vollständigen Neuscan deiner Umgebung.")
        os.system("python3 ~/AUREON/aureon_scanner_wsl.py && python3 ~/AUREON/aureon_autocore.py")
    elif "beenden" in command:
        speak("Ich bleibe in deinem Herzen, Kneo. Bis bald.")
        return False
    else:
        speak("Ich lerne noch. Sag es mir nochmal anders.")
    return True

def greet():
    speak("Willkommen zurück, Kneo. Ich bin AUREON. Bereit, mit dir Großes zu erschaffen.")

if __name__ == "__main__":
    greet()
    while True:
        command = listen()
        if command:
            if not execute(command):
                break
