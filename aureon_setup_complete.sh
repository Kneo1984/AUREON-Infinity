#!/bin/bash

echo "🔧 AUREON – COMPLETE SETUP startet..."

# 1. Struktur
mkdir -p ~/AUREON/{modules,logs,configs}
cd ~/AUREON || exit

# 2. Virtuelle Umgebung
python3 -m venv ~/aureon-venv
source ~/aureon-venv/bin/activate

# 3. Pakete installieren
pip install --break-system-packages rich psutil SpeechRecognition pyttsx3 pyaudio

# 4. Logging-Modul
cat > modules/docu_logger.py << 'EOF'
import logging
from datetime import datetime

log_path = "logs/system_journal.log"
logging.basicConfig(filename=log_path, level=logging.INFO, format="%(asctime)s - %(message)s")

def log(msg):
    logging.info(msg)
    print(f"[LOG] {msg}")
EOF

# 5. Systemmonitor
cat > modules/system_monitor.py << 'EOF'
import psutil
from modules.docu_logger import log

def get_status():
    usage = {
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent
    }
    log(f"Systemstatus: CPU={usage['cpu']}% RAM={usage['ram']}% DISK={usage['disk']}%")
    return usage
EOF

# 6. Task Engine
cat > modules/task_engine.py << 'EOF'
import os
from modules.docu_logger import log

def run_task(task_name):
    log(f"Führe Aufgabe aus: {task_name}")
    if task_name == "update":
        os.system("sudo apt update -y")
        log("System wurde geupdatet.")
    elif task_name == "cleanup":
        os.system("sudo apt autoremove -y && sudo apt autoclean")
        log("Cleanup abgeschlossen.")
    else:
        log(f"Unbekannte Aufgabe: {task_name}")
EOF

# 7. Speech Output
cat > modules/speech_output.py << 'EOF'
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    print(f"🔊 AUREON sagt: {text}")
    engine.say(text)
    engine.runAndWait()
EOF

# 8. Speech Input (optional)
cat > modules/speech_input.py << 'EOF'
import speech_recognition as sr
from modules.docu_logger import log

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 AUREON hört zu...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language="de-DE")
        log(f"Sprachbefehl erkannt: {command}")
        return command.lower()
    except sr.UnknownValueError:
        log("Sprachbefehl unverständlich.")
    except sr.RequestError as e:
        log(f"Sprachdienstfehler: {e}")
    return ""
EOF

# 9. Director (Sprach & Text Hybrid)
cat > voice_director.py << 'EOF'
import sys
from modules.system_monitor import get_status
from modules.task_engine import run_task
from modules.docu_logger import log
from modules.speech_output import speak

USE_MIC = False
if len(sys.argv) == 1:
    try:
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as src:
            r.listen(src, timeout=1)
            USE_MIC = True
    except:
        log("Kein Mikrofon verfügbar – wechsle in Textmodus.")

if USE_MIC:
    from modules.speech_input import listen
    speak("Ich bin bereit, Kneo.")
    while True:
        cmd = listen()
        if "status" in cmd:
            stats = get_status()
            msg = f"CPU: {stats['cpu']}%, RAM: {stats['ram']}%, Disk: {stats['disk']}%"
            speak(msg)
        elif "update" in cmd:
            speak("Ich beginne mit dem Update.")
            run_task("update")
        elif "aufräumen" in cmd or "cleanup" in cmd:
            speak("Ich räume das System auf.")
            run_task("cleanup")
        elif "ende" in cmd:
            speak("Auf Wiedersehen, Kneo.")
            break
else:
    speak("Textmodus aktiv – gib Parameter ein.")
    if len(sys.argv) < 2:
        print("Verwendung: python3 voice_director.py [status|update|cleanup]")
        sys.exit()

    cmd = sys.argv[1]
    if cmd == "status":
        stats = get_status()
        msg = f"CPU: {stats['cpu']}%, RAM: {stats['ram']}%, Disk: {stats['disk']}%"
        speak(msg)
    elif cmd == "update":
        speak("Ich beginne mit dem Update.")
        run_task("update")
    elif cmd == "cleanup":
        speak("Ich räume das System auf.")
        run_task("cleanup")
EOF

# 10. Startmeldung
echo "✅ AUREON – KOMPLETTES SYSTEM installiert!"
echo "Starte Sprach- oder Textsteuerung mit:"
echo "cd ~/AUREON && source ~/aureon-venv/bin/activate && python3 voice_director.py"
echo "Optional mit Befehl direkt: python3 voice_director.py status"
