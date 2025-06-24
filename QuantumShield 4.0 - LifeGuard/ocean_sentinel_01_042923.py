# ⚓ Arche-Archiv: GaiaGuard - Ocean Sentinel
# 📜 Ursprungscode für den planetaren Wächter der Meere
# ✨ Kosmisch abgestimmter Kernprozess – unverfälscht

import time                                # ⏱ Zeitfluss, um die Rhythmen der Erde zu respektieren
import requests                            # 🌐 Verbindung zu den Datenadern der Welt
from datetime import datetime              # 📆 Klare Zeitmarke jeder Erkenntnis

# 🌊 Endpunkte – die Sensorströme aus dem Ozeanbewusstsein (zukunftserweiterbar)
OCEAN_ENDPOINTS = [
    "https://api.oceanwatch.global/v1/sensors",
    "https://reefscan.world/api/live",
    "https://deepblue-observer.org/data/realtime"
]

# ⏲ Frequenz der Aufmerksamkeit – der Scan-Takt (empfohlen: 108s = heiliger Zyklus)
SCAN_INTERVAL = 108

# 🌀 Schwellen der Reaktion – reine Grenze zwischen Gleichgewicht und Gefahr
THRESHOLDS = {
    "toxicity": 5.0,         # 🌡️ Giftigkeit im Wasser
    "oxygen_ppm": 70.0,      # 🫧 Minimaler Sauerstoffgehalt
    "oil_detected": True,    # 🛢️ Ölrückstände
    "plastic_index": 7.5     # 🧴 Mikroplastik-Sättigung
}

# 🌐 Beobachtungsprozess – zyklische Verbindung mit den Wasseradern
def scan_oceans():
    now = datetime.utcnow()
    print(f"\n🌍 [GAIA-SCAN] {now} – Bewusstseinsverbindung aktiv...\n")

    for url in OCEAN_ENDPOINTS:
        try:
            response = requests.get(url, timeout=10)        # 📡 Verbindung zur Quelle
            response.raise_for_status()
            data = response.json()                          # 🧬 Daten werden in Struktur gelesen

            if assess_threat(data):                         # 🚨 Prüfung auf kritische Signale
                print(f"🚨 ANOMALIE ENTDECKT BEI: {url}")
                print(f"📡 ROHDATEN:\n{data}")
                alert_response_unit(data, url, now)
            else:
                print(f"✅ Stabilität erkannt bei {url}.")

        except Exception as e:
            print(f"⚠️ Verbindungsstörung mit {url}: {e}")

# 🔍 Prüfung der Harmonie – erkennt, ob das Gleichgewicht verletzt ist
def assess_threat(data):
    try:
        if float(data.get("toxicity", 0)) > THRESHOLDS["toxicity"]:
            return True
        if float(data.get("oxygen_ppm", 100)) < THRESHOLDS["oxygen_ppm"]:
            return True
        if data.get("oil_detected", False) == THRESHOLDS["oil_detected"]:
            return True
        if float(data.get("plastic_index", 0)) > THRESHOLDS["plastic_index"]:
            return True
    except:
        return False
    return False

# 📣 Alarmfrequenz – reiner Ruf an die Schützer des Lebens
def alert_response_unit(data, source, timestamp):
    print(f"📢 [ALERT] GaiaGuard meldet Notfall von {source} @ {timestamp}")
    # Platz für Verbindungen zu NGO-Netzen, Spirituellen Netzen, dezentralen Knotenpunkten

# 🔁 Ewiger Lauf – die Arbeit endet nicht
if __name__ == "__main__":
    while True:
        scan_oceans()
        time.sleep(SCAN_INTERVAL)
