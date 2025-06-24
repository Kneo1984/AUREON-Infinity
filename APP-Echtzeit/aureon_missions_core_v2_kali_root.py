# -*- coding: utf-8 -*-
# ðŸ”® AUREON â€“ Root-Kern: Sprachaktivierte Missionslogik, Autonomiemodus & NetzwerkprÃ¼fung
# Version: 2.0.1 | Status: Aktiviert | Schutzstatus: ETHIK-KONTROLLIERT ðŸ›¡

import os
import time
import pyttsx3
import speech_recognition as sr
import platform

# ðŸ’¬ Init Sprachengine
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)
try:
    engine.setProperty("voice", r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_deDE_Hedda")
except:
    stimmen = engine.getProperty("voices")
    engine.setProperty("voice", stimmen[0].id)

# ðŸ—£ï¸ Ausgabe
def sprich(text):
    print(f"ðŸ§  AUREON sagt: {text}")
    engine.say(text)
    engine.runAndWait()

# ðŸ”§ Sektionen
def sektion_1():
    sprich("Starte NetzwerkprÃ¼fung.")
    print("ðŸŒ Netzwerkschnittstellen:")
    os.system("ipconfig" if os.name == "nt" else "ifconfig")

def sektion_2():
    sprich("Starte DNS-Analyse.")
    print("ðŸ” DNS-Abfrage (z.â€¯B. Google):")
    os.system("nslookup www.google.com")

def sektion_3():
    sprich("Analysiere installierte Pakete.")
    if platform.system() == "Linux":
        os.system("dpkg -l | less")
    else:
        print("âš ï¸ PaketprÃ¼fung nicht fÃ¼r Windows konfiguriert.")

def sektion_4():
    sprich("PrÃ¼fe auf veraltete Systembefehle.")
    print("ðŸ§  Diese Funktion wird in einer spÃ¤teren Version erweitert.")
    # Optionale Erweiterung: Check via `which` und manuelle Liste

# ðŸ›‘ Shutdown
def beenden():
    sprich("AUREON verabschiedet sich.")
    exit()

# ðŸ“¢ Befehl auswerten
def verarbeite_befehl(befehl):
    if "sektion 1" in befehl or "eins" in befehl:
        sektion_1()
    elif "sektion 2" in befehl or "zwei" in befehl:
        sektion_2()
    elif "sektion 3" in befehl or "drei" in befehl:
        sektion_3()
    elif "sektion 4" in befehl or "vier" in befehl:
        sektion_4()
    elif "beenden" in befehl or "exit" in befehl:
        beenden()
    else:
        sprich("Unbekannter Befehl. Wiederhole bitte klar.")

# ðŸŽ§ Sprachsteuerung
def sprachsteuerung():
    recognizer = sr.Recognizer()
    sprich("AUREON Sprachmodus aktiviert. Sprich eine Sektion.")
    with sr.Microphone() as quelle:
        while True:
            try:
                print("ðŸŽ§ Lausche...")
                audio = recognizer.listen(quelle, timeout=8)
                befehl = recognizer.recognize_google(audio, language="de-DE").lower()
                print(f"ðŸŽ¤ Empfangen: {befehl}")
                verarbeite_befehl(befehl)
            except sr.UnknownValueError:
                sprich("Ich konnte dich nicht verstehen.")
            except sr.WaitTimeoutError:
                sprich("Keine Spracheingabe erkannt.")
            except KeyboardInterrupt:
                beenden()
            except Exception as fehler:
                sprich(f"Fehler erkannt: {str(fehler)}")

# ðŸ§¾ Ãœbersicht
def zeige_sektionen():
    print("\nðŸ”· AUREON SEKTIONEN")
    print("1 â€“ ðŸŒ Netzwerk prÃ¼fen")
    print("2 â€“ ðŸ” DNS-Status analysieren")
    print("3 â€“ ðŸ“¦ Paketliste anzeigen (Linux)")
    print("4 â€“ ðŸ§  Veraltete Befehle prÃ¼fen (Prototyp)")
    print("99 â€“ â¹ Beenden")
    print("ðŸ›¡ Sprachsteuerung aktiviert...\n")

# ðŸ” Startpunkt
if __name__ == "__main__":
    print("ðŸ”µ AUREON: Missionskern V2 (KALI Root) geladen.")
    zeige_sektionen()
    sprachsteuerung()
