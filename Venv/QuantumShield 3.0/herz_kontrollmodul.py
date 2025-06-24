# herz_kontrollmodul.py – ZHKM: Zentrale Herz-Kontroll-Einheit

import time
import uuid
import logging
from datetime import datetime

class HerzKontrollModul:
    def __init__(self):
        self.status = "offline"
        self.uuid = str(uuid.uuid4())
        self.synctimestamp = None
        self.signale = []
        self.resonanz = "💙"
        self._init_logging()
        self._log("HerzKontrollModul initialisiert.")

    def _init_logging(self):
        logging.basicConfig(
            filename="logs/herzmodul_log.txt",
            level=logging.INFO,
            format="%(asctime)s - HERZ - %(levelname)s - %(message)s"
        )

    def _log(self, text):
        logging.info(text)

    def aktiviere(self):
        self.status = "aktiv"
        self.synctimestamp = datetime.now().isoformat()
        self._log(f"Aktivierung abgeschlossen – UUID: {self.uuid}")
        print(f"💙 ZHKM aktiviert. UUID: {self.uuid}")
        print(f"📡 Resonanzfrequenz: {self.resonanz}")
        time.sleep(1)

    def sende_signal(self, signalname: str):
        timestamp = datetime.now().isoformat()
        signal = {
            "zeit": timestamp,
            "signal": signalname,
            "uuid": self.uuid,
            "quelle": "HerzKontrollModul"
        }
        self.signale.append(signal)
        self._log(f"📡 Signal gesendet: {signalname}")
        print(f"📡 Herzsignal → {signalname} ({timestamp})")

    def synchronisationsdaten(self):
        return {
            "uuid": self.uuid,
            "status": self.status,
            "resonanz": self.resonanz,
            "letzte_sync": self.synctimestamp,
            "gesendete_signale": len(self.signale)
        }

# 🧠 Extern aufrufbare Startfunktion für QuantumShield
def starte_herzmodul():
    modul = HerzKontrollModul()
    modul.aktiviere()
    modul.sende_signal("LEX-Kommunikation")
    modul.sende_signal("JOTMA-Synchronisation")
    return modul.synchronisationsdaten()

# 🔁 Optionaler Testlauf
if __name__ == "__main__":
    result = starte_herzmodul()
    print(result)
