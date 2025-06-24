import platform
import shutil
import os
import psutil
from datetime import datetime
import pyttsx3
import time
from hashlib import sha256
from pathlib import Path
import subprocess
import threading
import matplotlib.pyplot as plt

# === KONSTANTEN ===
LICENSE_PATH = Path("LICENSE")
# SHA-256 Hash der Original-Lizenzdatei (anpassen, falls sich deine Lizenzdatei ändert)
ORIGINAL_HASH = "a9143e18362deedde678b450908d8f595b41fb6cb06bccbc48f63a07e862a849"

# === FUNKTION: Sprachfeedback ===
def aurora_spricht(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)       # Sprechgeschwindigkeit
    engine.setProperty('volume', 1.0)     # Lautstärke (0.0 bis 1.0)
    engine.say(text)
    engine.runAndWait()

# === FUNKTION: Lizenzüberwachung ===
def lizenz_watchdog():
    while True:
        try:
            aktueller_hash = sha256(LICENSE_PATH.read_bytes()).hexdigest()
            if aktueller_hash != ORIGINAL_HASH:
                print("⚠️ WARNUNG: Die LICENSE-Datei wurde verändert!")
                aurora_spricht("Achtung. Die Lizenzdatei wurde verändert.")
            else:
                print("✅ Lizenzdatei ist unverändert.")
        except Exception as e:
            print(f"Fehler bei der Lizenzprüfung: {e}")
        time.sleep(30)  # Alle 30 Sekunden prüfen

# === FUNKTION: Automatisches GitHub Pushen ===
def auto_git_push(commit_message="Automatische Systemaktualisierung"):
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Änderungen wurden automatisch gepusht.")
    except subprocess.CalledProcessError:
        print("⚠️ Keine neuen Änderungen zum Pushen oder Fehler beim Push.")

# === FUNKTION: Visuelles Dashboard ===
def system_dashboard(cpu_last, ram_used, ram_avail, ram_total):
    fig, axs = plt.subplots(1, 2, figsize=(10, 4))
    axs[0].bar(["CPU"], [cpu_last], color='orange')
    axs[0].set_ylim(0, 100)
    axs[0].set_title("CPU-Auslastung")
    axs[1].bar(["RAM benutzt", "RAM frei"], [ram_used, ram_avail], color=['red', 'green'])
    axs[1].set_ylim(0, ram_total)
    axs[1].set_title("RAM-Nutzung")
    plt.tight_layout()
    plt.show()

# === FUNKTION: LEX Statusprüfung ===
def check_system_status():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n📊 LEX SYSTEMSTATUSPRÜFUNG – {now}")
    aurora_spricht("Systemprüfung gestartet")

    os_info = f"{platform.system()} {platform.release()}"
    print(f"🖥️ Betriebssystem: {os_info}")

    cpu_kerne = psutil.cpu_count(logical=True)
    cpu_last = psutil.cpu_percent(interval=1)
    print(f"💾 CPU-Kerne: {cpu_kerne}")
    print(f"🔄 CPU-Auslastung: {cpu_last}%")

    ram = psutil.virtual_memory()
    ram_gesamt = round(ram.total / (1024**3), 2)
    ram_frei = round(ram.available / (1024**3), 2)
    ram_used = ram_gesamt - ram_frei
    print(f"🧠 RAM: {ram_gesamt} GB total – {ram_frei} GB verfügbar")

    total, used, free = shutil.disk_usage(".")
    total_gb = round(total / (1024**3), 2)
    free_gb = round(free / (1024**3), 2)
    print(f"💽 Festplatte: {total_gb} GB gesamt – {free_gb} GB frei")

    aurora_spricht(f"CPU Last bei {cpu_last} Prozent. RAM verfügbar: {ram_frei} von {ram_gesamt} Gigabyte.")
    if cpu_last > 85 or ram_frei < 1:
        aurora_spricht("Achtung Dennis. Die Systemlast ist hoch oder der Speicher knapp.")

    print("⚙️ Wichtigste aktive Prozesse:")
    for proc in psutil.process_iter(['pid', 'name']):
        name = proc.info['name']
        if name and name.lower() in ['python.exe', 'uvicorn.exe', 'chrome.exe']:
            print(f"  - {proc.info['pid']}: {name}")

    system_dashboard(cpu_last, ram_used, ram_frei, ram_gesamt)
    auto_git_push("Automatischer Systemstatus Push")

# === AUSFÜHRUNG ===
if __name__ == "__main__":
    threading.Thread(target=lizenz_watchdog, daemon=True).start()
    check_system_status()
