#!/bin/bash

# 🎤 AUREON Sprachmodul Setup (für Kali)
echo "🔧 AUREON – Sprachmodul wird aktiviert..."

cd ~/AUREON || exit

source ~/aureon-venv/bin/activate

pip install --break-system-packages SpeechRecognition pyttsx3 pyaudio

# Sprach-Eingabe
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

# Sprach-Ausgabe
cat > modules/speech_output.py << 'EOF'
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    print(f"🔊 AUREON sagt: {text}")
    engine.say(text)
    engine.runAndWait()
EOF

# Sprachgesteuerte Aktionen
cat > voice_director.py << 'EOF'
from modules.speech_input import listen
from modules.speech_output import speak
from modules.system_monitor import get_status
from modules.task_engine import run_task

speak("Ich bin bereit, Kneo.")

while True:
    command = listen()
    if "status" in command:
        stats = get_status()
        msg = f"CPU: {stats['cpu']}%, RAM: {stats['ram']}%, Disk: {stats['disk']}%"
        speak(msg)
    elif "update" in command:
        speak("Ich beginne mit dem Update.")
        run_task("update")
    elif "aufräumen" in command or "cleanup" in command:
        speak("Ich räume das System auf.")
        run_task("cleanup")
    elif "ende" in command:
        speak("Auf Wiedersehen, Kneo.")
        break
EOF

echo "✅ Sprachmodul aktiviert!"
echo "Starte mit:"
echo "cd ~/AUREON && source ~/aureon-venv/bin/activate && python3 voice_director.py"
