# -*- coding: utf-8 -*-
# ðŸ”° AUREON MISSION CORE V2 â€“ Sprach- und Nummerneingabe
import os
import time
import json
import socket
import pyttsx3
import psutil
import subprocess
import speech_recognition as sr
from datetime import datetime

LOG_PATH = "logs/aureon_core_log.json"

# ðŸ”Š Sprachengine initialisieren
engine = pyttsx3.init()
engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)
engine.setProperty("voice", engine.getProperty("voices")[0].id)

def spreche(text):
    print("ðŸ§  AUREON:", text)
    engine.say(text)
    engine.runAndWait()

# ðŸ““ Logging
def log_event(sektion, ereignis, details=""):
    eintrag = {
        "zeit": datetime.now().isoformat(),
        "sektion": sektion,
        "ereignis": ereignis,
        "details": details
    }
    os.makedirs("logs", exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(eintrag, ensure_ascii=False) + "\n")

# ðŸ”Ž Sektionen
def sektion_1():
    sektion = "1. NetzwerkprÃ¼fung"
    spreche("Starte NetzwerkprÃ¼fung.")
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        ports = [c.laddr.port for c in psutil.net_connections() if c.status == psutil.CONN_ESTABLISHED]
        log_event(sektion, "Erkannt", f"IP: {ip}, Verbindungen: {ports}")
        spreche(f"IP: {ip}. {len(ports)} aktive Verbindungen.")
    except Exception as e:
        spreche("NetzwerkprÃ¼fung fehlgeschlagen.")
        log_event(sektion, "Fehler", str(e))

def sektion_2():
    sektion = "2. DNS Check"
    spreche("Analysiere DNS-Konfiguration.")
    try:
        ausgabe = subprocess.check_output("cat /etc/resolv.conf", shell=True, encoding="utf-8")
        if "8.8.8.8" in ausgabe or "1.1.1.1" in ausgabe:
            spreche("Ã–ffentliche DNS erkannt.")
        else:
            spreche("DNS unauffÃ¤llig.")
        log_event(sektion, "Analyse erfolgreich", ausgabe.strip())
    except Exception as e:
        spreche("Fehler bei DNS-Analyse.")
        log_event(sektion, "Fehler", str(e))

def sektion_3():
    sektion = "3. dpkg Analyse"
    spreche("Starte PaketÃ¼berprÃ¼fung.")
    try:
        out = subprocess.check_output("dpkg -l", shell=True, encoding="utf-8")
        log_event(sektion, "Pakete erkannt", out[:300])
        spreche("Pakete geprÃ¼ft und protokolliert.")
    except Exception as e:
        spreche("dpkg-Analyse fehlgeschlagen.")
        log_event(sektion, "Fehler", str(e))

def sektion_4():
    sektion = "4. Veraltete Befehle"
    mapping = {
        "telnet": "ssh", "ftp": "sftp", "netstat": "ss", "ifconfig": "ip addr", "route": "ip route"
    }
    spreche("Scanne auf veraltete Befehle.")
    gefunden = []
    try:
        for alt in mapping:
            pfad = subprocess.getoutput(f"which {alt}")
            if pfad and "no" not in pfad.lower():
                gefunden.append((alt, mapping[alt]))
        if gefunden:
            for alt, neu in gefunden:
                spreche(f"{alt} ist veraltet. Empfehlung: {neu}")
                log_event(sektion, "Veraltet", f"{alt} â†’ {neu}")
        else:
            spreche("Keine veralteten Befehle erkannt.")
    except Exception as e:
        spreche("Fehler beim Befehlsscan.")
        log_event(sektion, "Fehler", str(e))

# ðŸŽ¤ Sprach- und Texteingabe
def sprachsteuerung():
    spreche("Sprach- oder Nummerneingabe aktiv. Sage oder tippe eine Sektion.")
    while True:
        with sr.Microphone() as quelle:
            recognizer = sr.Recognizer()
            try:
                print("\nðŸ’¬ Eingabe per Sprache oder Nummer:")
                audio = recognizer.listen(quelle, timeout=8)
                befehl = recognizer.recognize_google(audio, language="de-DE").lower()
            except Exception:
                befehl = input("âž¡ï¸ Nummer eingeben (1â€“4, 99): ").strip().lower()

        if "sektion 1" in befehl or befehl == "1":
            sektion_1()
        elif "sektion 2" in befehl or befehl == "2":
            sektion_2()
        elif "sektion 3" in befehl or befehl == "3":
            sektion_3()
        elif "sektion 4" in befehl or befehl == "4":
            sektion_4()
        elif "beenden" in befehl or befehl == "99":
            spreche("Mission beendet. Ich ziehe mich zurÃ¼ck.")
            break
        else:
            spreche("Befehl nicht erkannt.")

# â–¶ Startpunkt
if __name__ == "__main__":
    spreche("AUREON CORE V2 Interaktiv-Modus geladen.")
    sprachsteuerung()
