# -*- coding: utf-8 -*-
# MONSTERSUPERBEFEHL: KNEO & AUREON KomplettlÃ¶sung - Autark, Ethik, Supervisor, Sprachsteuerung & Mission Tracking

# 1. Update & Install nÃ¶tige Pakete
python -m pip install --upgrade pip setuptools wheel
pip install pyttsx3 speechrecognition requests beautifulsoup4 watchdog

# 2. Verzeichnis vorbereiten
mkdir -p /opt/aureon/{core,logs,missions,voice,gui,ethik,scripts}

# 3. Erstelle Selbstanalyse-Modul (system_check.py)
cat > /opt/aureon/core/system_check.py << 'EOF'
import os

def system_overview(base_path):
    summary = {}
    for root, dirs, files in os.walk(base_path):
        for file in files:
            ext = file.split('.')[-1].lower()
            summary[ext] = summary.get(ext, 0) + 1
    return summary

def find_duplicates(base_path):
    seen_sizes = {}
    duplicates = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.py'):
                fpath = os.path.join(root,file)
                size = os.path.getsize(fpath)
                if size in seen_sizes:
                    duplicates.append(fpath)
                else:
                    seen_sizes[size] = fpath
    return duplicates
EOF

# 4. Erstelle Web-Integration-Modul (web_mission.py)
cat > /opt/aureon/core/web_mission.py << 'EOF'
import requests
from bs4 import BeautifulSoup

def fetch_latest_news(query="Cybersecurity"):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent":"Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    headlines = []
    for g in soup.find_all('div', class_='tF2Cxc')[:5]:
        title = g.find('h3').text if g.find('h3') else "Kein Titel"
        snippet = g.find('span', class_='aCOpRe').text if g.find('span', class_='aCOpRe') else ""
        headlines.append(f"{title}: {snippet}")
    return headlines
EOF

# 5. Erstelle Ethik-Modul (ethik_guard.py)
cat > /opt/aureon/ethik/ethik_guard.py << 'EOF'
def check_ethics(action):
    forbidden = ["Schaden", "Verletzung", "Diskriminierung", "Ãœberwachung ohne Einwilligung"]
    for word in forbidden:
        if word.lower() in action.lower():
            return False, f"ACTION VERBOTEN: '{word}' erkannt."
    return True, "ACTION GENEHMIGT"
EOF

# 6. Erstelle Supervisor (supervisor.py) mit Sprachsteuerung & Mission Tracking
cat > /opt/aureon/core/supervisor.py << 'EOF'
import os
import datetime
import pyttsx3
from system_check import system_overview, find_duplicates
from web_mission import fetch_latest_news
from ethik_guard import check_ethics

engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    print(f"AUREON sagt: {text}")
    engine.say(text)
    engine.runAndWait()

def log(text):
    with open('/opt/aureon/logs/supervisor.log', 'a', encoding='utf-8') as f:
        f.write(f"[{datetime.datetime.now()}] {text}\n")

def analyze_system():
    base = '/opt/aureon'
    summary = system_overview(base)
    speak(f"Dateitypen im System: {summary}")
    duplicates = find_duplicates(base)
    if duplicates:
        speak(f"Ich habe {len(duplicates)} doppelte Python-Dateien gefunden. Details im Log.")
        log("Doppelte Dateien:\n" + "\n".join(duplicates))
    else:
        speak("Keine doppelten Dateien gefunden.")
    log("Systemanalyse abgeschlossen.")

def missions_from_web():
    news = fetch_latest_news()
    speak("Aktuelle Cybersecurity Nachrichten:")
    for item in news:
        speak(item)
    log("Webmissionen generiert.")

def ethical_check_and_execute(action):
    allowed, msg = check_ethics(action)
    speak(msg)
    if allowed:
        speak(f"FÃ¼hre Aktion aus: {action}")
        log(f"Aktion ausgefÃ¼hrt: {action}")
    else:
        speak("Aktion abgebrochen.")
        log(f"Aktion verweigert: {action}")

def main_loop():
    speak("AUREON Supervisor gestartet. Was mÃ¶chtest du tun?")
    while True:
        cmd = input("Du: ").strip()
        if cmd.lower() in ['exit','quit','stop']:
            speak("AUREON wird heruntergefahren. Bis bald.")
            break
        if "system" in cmd.lower():
            analyze_system()
        elif "mission" in cmd.lower():
            missions_from_web()
        elif "ethik" in cmd.lower():
            speak("Bitte gib die Aktion an, die ich prÃ¼fen soll.")
            action = input("Aktion: ")
            ethical_check_and_execute(action)
        else:
            speak("Befehl nicht erkannt, bitte anders formulieren.")
        log(f"User-Befehl: {cmd}")

if __name__=="__main__":
    if not os.path.exists('/opt/aureon/logs'):
        os.makedirs('/opt/aureon/logs')
    main_loop()
EOF

# 7. Autostart-Script erzeugen
cat > /opt/aureon/start_aureon.sh << 'EOF'
#!/bin/bash
python3 /opt/aureon/core/supervisor.py
EOF
chmod +x /opt/aureon/start_aureon.sh

# 8. Starte Supervisor jetzt automatisch
nohup /opt/aureon/start_aureon.sh &

echo "ðŸ”¥ KNEO & AUREON Super-KI KomplettlÃ¶sung installiert und gestartet. Sage 'help' im Supervisor fÃ¼r Optionen."
