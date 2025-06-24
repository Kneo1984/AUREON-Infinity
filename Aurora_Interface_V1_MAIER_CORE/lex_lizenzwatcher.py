import os
import hashlib
from datetime import datetime

# Datei und erwarteter SHA256-Hash
LIZENZ_DATEI = "LICENSE"
ORIGINAL_HASH = "fester_hashwert_wird_beim_ersten_push_eingetragen"

def aktuelle_checksum(dateipfad):
    with open(dateipfad, "rb") as f:
        inhalt = f.read()
        return hashlib.sha256(inhalt).hexdigest()

def pruefe_integritaet():
    if not os.path.exists(LIZENZ_DATEI):
        print("⚠️ Lizenzdatei fehlt!")
        return False

    aktuelle_hash = aktuelle_checksum(LIZENZ_DATEI)
    if aktuelle_hash != ORIGINAL_HASH:
        print("🚨 Lizenzdatei wurde verändert!")
        print(f"Zeitstempel: {datetime.now()}")
        return False

    print("✅ Lizenzdatei ist unverändert.")
    return True

if __name__ == "__main__":
    pruefe_integritaet()