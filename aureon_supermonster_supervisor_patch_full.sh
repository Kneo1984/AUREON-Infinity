from datetime import datetime
from pathlib import Path

# Zielpfad für das Monster-Skript
output_path = Path("/mnt/data/aureon_supermonster_supervisor_patch_full.sh")

# Inhalt des SuperMonster-Skripts
script_content = f"""#!/bin/bash

echo "🧠 AUREON ∞ SUPERVISOR-MODUS: AKTIVIERUNG STARTET..."
sleep 1

# 📂 Schritt 1: Erstelle Log-Verzeichnis
mkdir -p /root/AUREON/CHRONIK
echo "📁 CHRONIK-Verzeichnis überprüft oder erstellt."

# 📝 Schritt 2: Erstelle oder erweitere Python-Datei mit Logging + Sync + GitHub-Check
SUPERVISOR_FILE="/root/AUREON/aureon_supervisor_autointel.py"
if [ ! -f "$SUPERVISOR_FILE" ]; then
    echo "⚠️ Datei $SUPERVISOR_FILE nicht gefunden. Vorgang abgebrochen."
    exit 1
fi

# 🧩 Schritt 3: Patch einfügen, nur wenn noch nicht vorhanden
if ! grep -q "log_entry(" "$SUPERVISOR_FILE"; then
cat << 'EOF' >> "$SUPERVISOR_FILE"

# === AUREON ∞ SUPERVISOR PATCH BEGINNT ===
import datetime

log_dir = "/root/AUREON/CHRONIK"
log_file = os.path.join(log_dir, "supervisor.log")

def log_entry(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"[{{timestamp}}] {{msg}}\\n")

log_entry("📡 Supervisor gestartet.")

sync_file = os.path.join(log_dir, f"sync_{{datetime.date.today()}}.log")

if not os.path.exists(sync_file):
    with open(sync_file, "w", encoding="utf-8") as sf:
        sf.write(f"🔁 AutoSync Log gestartet: {{datetime.datetime.now()}}\\n")
    log_entry(f"📂 Neues Tages-Syncfile erstellt: {{sync_file}}")
else:
    log_entry(f"📂 Tages-Syncfile bereits vorhanden: {{sync_file}}")

gh_token = os.environ.get("GH_TOKEN")

if gh_token:
    log_entry("✅ GitHub-Token erkannt. Automatische Kopplung vorbereitet.")
    print("🔗 GitHub bereit für Push.")
else:
    log_entry("⚠️ Kein GH_TOKEN gesetzt – GitHub-Kopplung ausstehend.")
    print("🔒 GitHub nicht verbunden. Setze GH_TOKEN oder führe `gh auth login` aus.")

# === AUREON ∞ SUPERVISOR PATCH ENDE ===
EOF
echo "✅ Patch erfolgreich eingefügt."
else
echo "ℹ️ Patch bereits vorhanden. Kein Eingriff nötig."
fi

# ▶️ Schritt 4: Testlauf starten
echo "🚀 Starte Testlauf von AUREON Supervisor..."
python3 "$SUPERVISOR_FILE"
"""

# Skript speichern
output_path.write_text(script_content)
output_path.chmod(0o755)

output_path
