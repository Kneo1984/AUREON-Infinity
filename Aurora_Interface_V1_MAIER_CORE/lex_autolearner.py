# lex_autolearner.py – Selbstlernendes Kontrollzentrum (Phase 1)
import os
import time
from datetime import datetime
from pathlib import Path

JOURNAL = Path("lex_change_brain.md")
MODULES = [f for f in os.listdir() if f.endswith(".py") and not f.startswith("__")]

# Starte Auto-Journal
if not JOURNAL.exists():
    JOURNAL.write_text("# LEX Change Brain\n\n", encoding="utf-8")

# Lade bisherige Hashes
file_hashes = {}
def hash_file(p):
    return hash(Path(p).read_bytes())

for mod in MODULES:
    try:
        file_hashes[mod] = hash_file(mod)
    except Exception as e:
        print(f"Fehler beim Einlesen von {mod}: {e}")

print("🧠 LEX AUTOLERNZENTRUM – AKTIV")

# Hauptschleife
while True:
    for mod in MODULES:
        try:
            current_hash = hash_file(mod)
            if mod in file_hashes and file_hashes[mod] != current_hash:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                note = f"- [{timestamp}] Modul \"{mod}\" wurde verändert.\n"
                JOURNAL.write_text(JOURNAL.read_text(encoding="utf-8") + note, encoding="utf-8")
                print(f"🔁 Änderung erkannt in {mod}. Dokumentiert.")
                file_hashes[mod] = current_hash
        except Exception as e:
            print(f"Fehler beim Überwachen von {mod}: {e}")

    time.sleep(10)  # Alle 10 Sekunden prüfen
