#!/usr/bin/env python3
import os
import time
import pyttsx3
import threading

# 🎯 Trigger-Schlüsselwörter für Alarm
triggers = ["passwort", "key", "vpn", "shadow", "secret"]

# 🧱 Infinity-Whitelist – ignorierte Pfade mit Systemdateien
whitelist = [
    "BreadcrumbStore", "NetFramework", "Microsoft.Extensions", "Microsoft.Identity", "System.",
    "WindowsApps", "ProgramData\\Microsoft", "AppData", "Windows.old", "SoftwareDistribution",
    "Logs", "Windows Defender", "Assembly", "Prefetch", "Installer", "Temp", "Program Files",
    "Program Files (x86)", "Intel", "dotnet", "WinSxS", "ServiceProfiles", "WebCache", "Recovery",
    "Recycle.Bin", "DiagTrack", "D3DSCache", "NVIDIA", "Packages", "OneDriveTemp", "Fonts",
    "ShellExperienceHost", "DefaultAppPool", "MSBuild", "Tracing", "Perflogs", "example_folder"
]

# 🔍 Überwachte Pfade
watch_paths = ["/mnt/c/ProgramData", "/mnt/c/Users", "/mnt/c/temp"]

# Log-Verzeichnis sicherstellen
log_dir = "/root/AUREON/logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "trigger.log")

# Initialisiere pyttsx3 Engine EINMAL
engine = pyttsx3.init()
engine.setProperty("rate", 180)
engine.setProperty("volume", 1.0)

# Threadsafe Sprechen
engine_lock = threading.Lock()

def say(text):
    with engine_lock:
        engine.say(text)
        engine.runAndWait()

print("AUREON ∞ 🛡️ Triggerüberwachung aktiviert mit pyttsx3...")

try:
    while True:
        for path in watch_paths:
            for root, dirs, files in os.walk(path):
                for file in files:
                    full_path = os.path.join(root, file)
                    # Whitelist prüfen
                    if any(w in full_path for w in whitelist):
                        continue
                    lower_name = file.lower()
                    # Trigger prüfen
                    if any(trigger in lower_name for trigger in triggers):
                        print(f"\n⚠️  Alarm: Verdächtige Datei → {full_path}")
                        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                        with open(log_file, "a") as log:
                            log.write(f"{timestamp} - Trigger: {full_path}\n")
                        say("⚠️ Achtung – potenzieller Zugriff erkannt.")
        time.sleep(30)

except KeyboardInterrupt:
    print("\n🛑 Triggerüberwachung manuell beendet.")
    engine.stop()
