import os
import subprocess
from datetime import datetime
from hashlib import sha256
from pathlib import Path

def aurora_spricht(text):
    print(f"AURORA 🔊: {text}")

def berechne_hash(pfad):
    try:
        return sha256(Path(pfad).read_bytes()).hexdigest()
    except Exception as e:
        aurora_spricht(f"Fehler beim Hashen: {e}")
        return None

def commit_und_push(commit_message="Automatischer Commit"):
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"{commit_message} – {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"], check=True)
        subprocess.run(["git", "push"], check=True)
        aurora_spricht("Änderungen erfolgreich gepusht.")
    except subprocess.CalledProcessError as e:
        aurora_spricht(f"Fehler beim Commit oder Push: {e}")

def check_lizenz_integritaet():
    license_path = Path("LICENSE")
    expected_hash = "a9143e18362deedde678b450908d8f595b41fb6cb06bccbc48f63a07e862a849"  # Optional anpassen
    aktueller_hash = berechne_hash(license_path)
    if aktueller_hash != expected_hash:
        aurora_spricht("⚠️ Lizenzdatei wurde verändert oder stimmt nicht mehr überein!")
    else:
        aurora_spricht("✅ Lizenzschutz bestätigt.")

if __name__ == "__main__":
    aurora_spricht("Starte automatischen GitHub Push mit Lizenzüberprüfung...")
    check_lizenz_integritaet()
    commit_und_push("Systemupdate durch LEX")