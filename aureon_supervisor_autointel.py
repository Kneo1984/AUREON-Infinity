# AUREON ∞ SUPERVISOR – PATCHED
import os
import datetime

# Pfadliste laden
pfadliste_path = '/root/AUREON/CHRONIK/AUREON_GESAMTSYSTEMSTRUKTUR_PFADLISTE.txt'
if os.path.exists(pfadliste_path):
    with open(pfadliste_path, 'r', encoding='utf-8') as file:
        alle_pfade = [line.strip() for line in file if line.strip()]
        print('✅ [SUPERVISOR] Vollständige Pfadliste geladen:')
        for eintrag in alle_pfade:
            print('   🔹', eintrag)
else:
    print('⚠️ [SUPERVISOR] Pfadliste nicht gefunden:', pfadliste_path)

# Logging
log_dir = "/root/AUREON/CHRONIK"
log_file = os.path.join(log_dir, "supervisor.log")

def log_entry(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] {msg}\n")

log_entry("📡 Supervisor gestartet.")

# Autosync-Datei mit Tageslog
sync_file = os.path.join(log_dir, f"sync_{datetime.date.today()}.log")
if not os.path.exists(sync_file):
    with open(sync_file, "w", encoding="utf-8") as sf:
        sf.write(f"🔁 AutoSync Log gestartet: {datetime.datetime.now()}\n")
    log_entry(f"📂 Neues Tages-Syncfile erstellt: {sync_file}")
else:
    log_entry(f"📂 Tages-Syncfile bereits vorhanden: {sync_file}")

# GitHub Token-Prüfung
gh_token = os.environ.get("GH_TOKEN")
if gh_token:
    log_entry("✅ GitHub-Token erkannt. Automatische Kopplung vorbereitet.")
    print("🔗 GitHub bereit für Push.")
else:
    log_entry("⚠️ Kein GH_TOKEN gesetzt – GitHub-Kopplung ausstehend.")
    print("🔒 GitHub nicht verbunden. Setze GH_TOKEN oder führe `gh auth login` aus.")
