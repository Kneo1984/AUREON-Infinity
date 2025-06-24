# -*- coding: utf-8 -*-
import pyttsx3
import subprocess
import time

# Sprachmodul initialisieren
engine = pyttsx3.init()
engine.setProperty("rate", 185)   # Sprechgeschwindigkeit
engine.setProperty("volume", 1.0)

# Stimme wählen (männlich/weiblich – nimm ggf. voices[1] für weiblich)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# Begrüßung
engine.say("Willkommen zurück, Commander. AUREON wird aktiviert.")
engine.runAndWait()

# Kurze Pause, dann Voice-Core starten
time.sleep(1)
subprocess.Popen([r".\\lex_env_311\\Scripts\\python.exe", "lex_voice_core.py"])
