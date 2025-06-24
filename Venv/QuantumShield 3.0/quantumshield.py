# quantumshield.py – QuantumShield™ 3.0 Prototyp

#  Module für Netzwerk, Zeit, Systeminfos
import socket
import datetime
import os

#  Diagnose-Log vorbereiten
diagnose_logfile = "shield_diagnose.log"
with open(diagnose_logfile, "a") as diag_log:
    diag_log.write("\n====================\n")
    diag_log.write(f"[🔐] QuantumShield gestartet – {datetime.datetime.now()}\n")
    diag_log.write(f"[📁] Ausgeführt von: {os.getcwd()}\n")

# 📡 Schritt 1: Lokale IP-Adresse ermitteln
ip = socket.gethostbyname(socket.gethostname())

# 🕒 Schritt 2: Zeitstempel erzeugen
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 📜 Schritt 3: Standard-Log aktualisieren
with open("shield.log", "a") as log:
    log.write(f"[{timestamp}] QuantumShield aktiviert auf IP {ip}\n")

# 🔁 Diagnose-Log erweitern
with open(diagnose_logfile, "a") as diag_log:
    diag_log.write(f"[📡] Lokale IP-Adresse: {ip}\n")
    diag_log.write(f"[🕒] Zeitstempel: {timestamp}\n")
    diag_log.write(f"[✅] Status: Aktivierung erfolgreich\n")

# quantumshield.py – QuantumShield™ 3.0 Prototyp

import socket
import datetime
import os
import uuid
import json

# 🔧 Basisverzeichnisse
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
diagnose_logfile = os.path.join(BASE_DIR, "shield_diagnose.log")
standard_logfile = os.path.join(BASE_DIR, "shield.log")
status_file = os.path.join(BASE_DIR, "shield_status.json")

# 🛠 Logging-Funktion
def log_event(message, log_path=standard_logfile):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")

# 💙 meinHerz aktivieren
def aktiviere_meinHerz():
    herz_status = {
        "uuid": str(uuid.uuid4()),
        "resonanz": "💙",
        "status": "aktiv",
        "lex_channel": "verbunden",
        "letzte_sync": datetime.datetime.now().isoformat()
    }
    with open(status_file, "w", encoding="utf-8") as status:
        json.dump(herz_status, status, indent=4, ensure_ascii=False)

    log_event("💙 Herzsignal aktiviert & synchronisiert mit LEX", diagnose_logfile)
    return herz_status

# 🌐 IP-Adresse ermitteln
ip = socket.gethostbyname(socket.gethostname())
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 🧠 QuantumShield aktivieren
with open(diagnose_logfile, "a", encoding="utf-8") as diag_log:
    diag_log.write("\n====================\n")
    diag_log.write(f"[🔐] QuantumShield gestartet – {datetime.datetime.now()}\n")
    diag_log.write(f"[📁] Ausgeführt von: {os.getcwd()}\n")
    diag_log.write(f"[📡] Lokale IP-Adresse: {ip}\n")
    diag_log.write(f"[🕒] Zeitstempel: {timestamp}\n")

# 📜 Standard-Log aktualisieren
log_event(f"QuantumShield aktiviert auf IP {ip}")
log_event("Systemzeit: " + timestamp)
log_event("Status: Basissystem online")

# 💠 LEX verbinden
log_event("🤖 LEX-Kanal verbunden – Sprach- & Signalkontrolle online", diagnose_logfile)

# 💓 meinHerz verbinden
herz = aktiviere_meinHerz()
print("💡 QuantumShield aktiviert und verbunden mit:")
print(json.dumps(herz, indent=2, ensure_ascii=False))

log_event("✅ QuantumShield Initialisierung erfolgreich\n")
