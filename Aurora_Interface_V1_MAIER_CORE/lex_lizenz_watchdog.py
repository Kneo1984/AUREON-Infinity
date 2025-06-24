import time
from hashlib import sha256
from pathlib import Path
from datetime import datetime
import subprocess

def berechne_hash(pfad):
    return sha256(Path(pfad).read_bytes()).hexdigest()

# Original-Hash deiner JOTMA LEX Lizenz
original_hash = "a9143e18362deedde678b450908d8f595b41fb6cb06bccbc48f63a07e862a849"
license_path = Path("LICENSE")
log_path = Path("lizenz_watcher.log")

def log(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_path.write_text(f"{timestamp} – {text}\n", encoding="utf-8", append=True)
    print(text)

print("🔒 LEX Lizenzüberwachung läuft...")

while True:
    try:
        aktueller_hash = berechne_hash(license_path)
        if aktueller_hash != original_hash:
            warnung = "⚠️ WARNUNG: Die LICENSE-Datei wurde verändert!"
            log(warnung)

            # Schutzreaktion – optionales Revert oder Stop
            subprocess.run(["git", "checkout", "--", "LICENSE"])
            log("🔁 LICENSE-Datei wurde zurückgesetzt.")

        else:
            print("✅ Lizenzdatei ist unverändert.")
    except Exception as e:
        log(f"❌ Fehler bei der Prüfung: {e}")
    
    time.sleep(10)
