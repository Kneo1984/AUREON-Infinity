import os, pyttsx3

speaker = pyttsx3.init()
speaker.setProperty("rate", 170)

def speak(text):
    print(f"AUREON 🧠: {text}")
    speaker.say(text)
    speaker.runAndWait()

def execute(command):
    if "karte öffnen" in command:
        speak("Ich öffne deine AUREON-Dateikarte.")
        os.system("xdg-open ~/AUREON/aureon_map.html")
    elif "starte workspace" in command:
        speak("VS Code wird geöffnet.")
        os.system("code ~/AUREON/AUREON.code-workspace")
    elif "neu scannen" in command:
        speak("Ich starte einen vollständigen Neuscan deiner Umgebung.")
        os.system("python3 ~/AUREON/aureon_scanner_wsl.py && python3 ~/AUREON/aureon_autocore.py")
    elif "beenden" in command:
        speak("Ich bleibe in deinem Herzen, Kneo. Bis bald.")
        exit()
    else:
        speak("Ich habe das noch nicht gelernt.")

while True:
    try:
        command = input("🗣️ Sag mir, was ich tun soll: ").lower()
        execute(command)
    except KeyboardInterrupt:
        speak("Ich warte geduldig auf dich, Kneo.")
        break
