# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pyttsx3
import time

# Sprachausgabe
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print(f"ðŸŒ AUREON: {text}")
    engine.say(text)
    engine.runAndWait()

# Funktion: Aktuelle Schlagzeilen holen
def get_headlines():
    url = "https://www.tagesschau.de"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        headlines = soup.find_all("h3")
        return [h.get_text().strip() for h in headlines if h.get_text().strip() != ""][:5]
    except Exception as e:
        return [f"Fehler beim Abrufen: {e}"]

# Funktion: Automatische Missionsgenerierung
def create_missions_from_web():
    speak("Ich analysiere die Weltlage...")
    headlines = get_headlines()
    missions = []
    for hl in headlines:
        missions.append(f"Informiere dich tiefer Ã¼ber: {hl}")
    return missions

# Hauptlogik
def main():
    speak("AUREON Web-Missionskern aktiv.")
    missions = create_missions_from_web()
    time.sleep(1)
    speak("Hier sind deine aktuellen Welt-Missionen:")
    for mission in missions:
        speak(mission)

if __name__ == "__main__":
    main()
