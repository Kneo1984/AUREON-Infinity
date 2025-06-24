# 📌 QuantumShield 3.0 – Hauptmodul
# Entwickelt für den kontrollierten Start, Logging und Statusüberwachung des Herz-Kontrollmoduls

import datetime
import os
import uuid
import json
import socket

# 📁 Basisverzeichnisse definieren
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_STANDARD = os.path.join(BASE_DIR, "shield.log")
LOG_DIAGNOSE = os.path.join(BASE_DIR, "shield_diagnose.log")
STATUS_FILE = os.path.join(BASE_DIR, "shield_status.json")

# 🛠️ Zentrale Logging-Funktion (UTF-8 sicher)
def log_event(message, log_path=LOG_STANDARD):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")

# 💓 Aktivierung von „meinHerz“ – emotionale Schutzschicht
def aktiviere_meinHerz():
    herz_status = {
        "uuid": str(uuid.uuid4()),
        "resonanz": "💙",
        "status": "aktiv",
        "lex_channel": "verbunden",
        "letzte_sync": datetime.datetime.now().isoformat()
    }
    with open(STATUS_FILE, "w", encoding="utf-8") as status:
        json.dump(herz_status, status, indent=4, ensure_ascii=False)

    log_event("💙 Herzsignal aktiviert & synchronisiert mit LEX", LOG_DIAGNOSE)
    return herz_status

# 📡 IP-Adresse ermitteln
def ermittle_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception:
        return "unbekannt"

# 🧬 QuantumShield-Session starten
def quantumshield_start():
    session_id = str(uuid.uuid4())
    ip = ermittle_ip()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Diagnose-Log (detailliert)
    with open(LOG_DIAGNOSE, "a", encoding="utf-8") as diag_log:
        diag_log.write("\n====================\n")
        diag_log.write(f"[🔐] QuantumShield gestartet – {datetime.datetime.now()}\n")
        diag_log.write(f"[📁] Ausgeführt von: {os.getcwd()}\n")
        diag_log.write(f"[📡] Lokale IP-Adresse: {ip}\n")
        diag_log.write(f"[🕒] Zeitstempel: {timestamp}\n")

    # Standard-Log
    log_event(f"QuantumShield aktiviert auf IP {ip}")
    log_event("Systemzeit: " + timestamp)
    log_event("Status: Basissystem online")
    log_event("🤖 LEX-Kanal verbunden – Sprach- & Signalkontrolle online", LOG_DIAGNOSE)

    # Herzsignal aktivieren
    herz = aktiviere_meinHerz()
    print("💡 QuantumShield aktiviert und verbunden mit:")
    print(json.dumps(herz, indent=2, ensure_ascii=False))

    log_event(f"✅ QuantumShield Initialisierung erfolgreich – UUID: {session_id}\n")
    return session_id

# 🧠 Herzmodul separat starten (optional)
def start_herzmodul():
    try:
        import herz_kontrollmodul as hkm
        result = hkm.starte_herzmodul()
        log_event("💙 Herzmodul erfolgreich gestartet")
        print("💙 Herzmodul Antwort:", result)
    except ImportError:
        log_event("⚠️ Modul 'herz_kontrollmodul.py' nicht gefunden")
        print("⚠️ Hinweis: 'herz_kontrollmodul.py' nicht vorhanden oder fehlerhaft.")
    except Exception as e:
        log_event(f"❌ Fehler beim Start des Herzmoduls: {e}")
        print("❌ Fehler im Herzmodul:", e)

# 🔁 Hauptablauf
def main():
    session_id = quantumshield_start()
    start_herzmodul()

# 🚀 Programmstart
if __name__ == "__main__":
    main()
