# -*- coding: utf-8 -*-
# ðŸ”° AUREON MISSION CORE â€“ Sprachgesteuerte Schutz- & Analyseinstanz
import os
import time
import json
import socket
import pyttsx3
import psutil
import subprocess
import speech_recognition as sr
from datetime import datetime

LOG_PATH = "logs/mission_log.json"

# ðŸ”Š Sprachausgabe
engine = pyttsx3.init()
engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)
engine.setProperty("voice", engine.getProperty('voices')[0].id)

def spreche(text):
    print("ðŸ§  AUREON:", text)
    engine.say(text)
    engine.runAndWait()

# ðŸ§  Logging
def log_event(event, details=""):
    eintrag = {
        "zeit": datetime.now().isoformat(),
        "ereignis": event,
        "details": details
    }
    os.makedirs("logs", exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(eintrag, ensure_ascii=False) + "\n")

# ðŸŒ NetzwerkprÃ¼fung
def netzwerk_scan():
    spreche("Starte NetzwerkprÃ¼fung...")
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        verbindungen = psutil.net_connections()
        ports = [v.laddr.port for v in verbindungen if v.status == "ESTABLISHED"]
        log_event("Netzwerk-Scan", f"IP: {ip}, Ports: {ports}")
        spreche(f"Deine IP ist {ip}. {len(ports)} offene Verbindungen erkannt.")
    except Exception as e:
        spreche("Fehler beim Netzwerk-Scan.")
        log_event("Netzwerk-Fehler", str(e))

# ðŸ§ª DNS-HÃ¤rtungstest
def dns_schutz_check():
    spreche("ÃœberprÃ¼fe DNS-Konfiguration...")
    try:
        ausgabe = subprocess.check_output("ipconfig /all", shell=True, encoding="utf-8")
        if "8.8.8.8" in ausgabe or "1.1.1.1" in ausgabe:
            spreche("Ã–ffentliche DNS erkannt. Empfehlung: DNS absichern.")
        else:
            spreche("DNS-Konfiguration unauffÃ¤llig.")
        log_event("DNS-Scan", "DurchgefÃ¼hrt")
    except Exception as e:
        spreche("DNS-Check fehlgeschlagen.")
        log_event("DNS-Fehler", str(e))

# ðŸ“¡ TOR-Status
def tor_status():
    try:
        output = subprocess.check_output("tasklist", shell=True, encoding="utf-8")
        if "tor.exe" in output.lower():
            spreche("Tor ist aktiv. IP-Tarnung wahrscheinlich.")
            log_event("TOR-Status", "Tor lÃ¤uft")
        else:
            spreche("Tor scheint inaktiv.")
            log_event("TOR-Status", "Tor nicht erkannt")
    except Exception as e:
        spreche("Tor-Status konnte nicht ermittelt werden.")
        log_event("TOR-Fehler", str(e))

# ðŸ§  Sprachsteuerung
def befehl_ausfÃ¼hren(befehl):
    befehl = befehl.lower()
    if "netzwerk" in befehl:
        netzwerk_scan()
    elif "dns" in befehl:
        dns_schutz_check()
    elif "tor" in befehl:
        tor_status()
    elif "zeit" in befehl:
        jetzt = datetime.now().strftime("%H:%M:%S")
        spreche(f"Es ist {jetzt}.")
        log_event("Zeitabfrage")
    elif "beenden" in befehl:
        spreche("Ich ziehe mich zurÃ¼ck. Ruf mich, wenn du mich brauchst.")
        log_event("Session-Ende")
        exit(0)
    else:
        spreche("Befehl nicht erkannt. Bitte prÃ¤zisieren.")
        log_event("Unbekannter Befehl", befehl)

# ðŸŽ¤ Sprachinteraktion starten
def mission_starten():
    spreche("Mission gestartet. Ich bin wachsam.")
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as quelle:
            print("ðŸŽ§ AUREON lauscht...")
            try:
                audio = recognizer.listen(quelle, timeout=8)
                befehl = recognizer.recognize_google(audio, language="de-DE")
                print("ðŸ—£ï¸ Befehl empfangen:", befehl)
                befehl_ausfÃ¼hren(befehl)
            except sr.UnknownValueError:
                spreche("Akustisch unverstÃ¤ndlich.")
            except sr.WaitTimeoutError:
                spreche("Kein Sprachsignal erkannt.")
            except Exception as e:
                spreche("Fehler bei der Spracherkennung.")
                log_event("Spracherkennung-Fehler", str(e))

# ðŸ” Direkter Start
if __name__ == "__main__":
    mission_starten()
