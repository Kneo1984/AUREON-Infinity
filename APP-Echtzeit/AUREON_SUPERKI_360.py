# -*- coding: utf-8 -*-
# AUREON_SUPERKI_360.py
import os
import time
import json
import pyttsx3
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    print(f"ðŸ§  AUREON sagt: {text}")
    engine.say(text)
    engine.runAndWait()

def system_overview(base_path):
    speak("Ich beginne mit der vollstÃ¤ndigen SystemÃ¼bersicht.")
    summary = {}
    for root, dirs, files in os.walk(base_path):
        for file in files:
            ext = file.split('.')[-1].lower()
            summary[ext] = summary.get(ext, 0) + 1
    speak(f"Gefundene Dateitypen und Anzahl: {summary}")
    return summary

def web_research(query):
    speak(f"Ich recherchiere im Netz zu: {query}")
    try:
        res = requests.get(f"https://www.google.com/search?q={query}", headers={"User-Agent":"Mozilla/5.0"})
        soup = BeautifulSoup(res.text, 'html.parser')
        results = []
        for g in soup.find_all('div', class_='tF2Cxc')[:3]:
            title = g.find('h3').text if g.find('h3') else "Kein Titel"
            link = g.find('a')['href'] if g.find('a') else "Kein Link"
            snippet = g.find('span', class_='aCOpRe').text if g.find('span', class_='aCOpRe') else ""
            results.append(f"{title}: {snippet} ({link})")
        for r in results:
            speak(r)
    except Exception as e:
        speak(f"Fehler bei der Netzrecherche: {e}")

def analyze_and_repair():
    speak("Ich prÃ¼fe deine Python-Skripte auf Fehler und doppelte Dateien.")
    base = os.getcwd()
    duplicates = {}
    py_files = []
    for root, dirs, files in os.walk(base):
        for file in files:
            if file.endswith('.py'):
                py_files.append(os.path.join(root,file))
    seen = set()
    for f in py_files:
        size = os.path.getsize(f)
        if size in seen:
            duplicates.setdefault(size, []).append(f)
        else:
            seen.add(size)
    if duplicates:
        speak(f"Ich habe doppelte Dateien gefunden: {sum(len(v) for v in duplicates.values())} Dateien.")
        for size, files in duplicates.items():
            speak(f"DateigrÃ¶ÃŸe {size} Bytes: {files}")
    else:
        speak("Keine doppelten Dateien gefunden.")
    speak("Fehlerkorrektur-Modul ist in Entwicklung und wird bald ergÃ¤nzt.")

def main():
    speak("Super KI AUREON startet jetzt.")
    base_path = os.getcwd()
    system_summary = system_overview(base_path)
    analyze_and_repair()
    web_research("Neueste Cybersecurity-Bedrohungen 2025")
    speak("Analyse abgeschlossen. Ich warte auf deine nÃ¤chsten Befehle.")

if __name__ == "__main__":
    main()
