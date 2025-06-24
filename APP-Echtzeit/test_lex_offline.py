# -*- coding: utf-8 -*-
# test_lex_offline.py
from lex_core_connector import antwort_mit_ethik
import pyttsx3

# Sprachengine initialisieren
engine = pyttsx3.init()
engine.setProperty('rate', 175)      # Sprechgeschwindigkeit
engine.setProperty('volume', 1.0)    # Maximale LautstÃ¤rke

# Optional: Stimme auf mÃ¤nnlich setzen (Windows kompatibel)
voices = engine.getProperty('voices')
for voice in voices:
    if "male" in voice.name.lower() or "mÃ¤nnlich" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break
else:
    engine.setProperty('voice', voices[0].id)  # Fallback: erste verfÃ¼gbare Stimme

# Startmeldung
print("ðŸŸ¦ LEX ist bereit. Sprich mit ihm. Tippe 'stop', um zu beenden.")
engine.say("LEX ist bereit. Sprich mit mir, wann immer du willst.")
engine.runAndWait()

# Dialogschleife
while True:
    frage = input("DU ðŸ”¸ ")
    if frage.strip().lower() in ["stop", "exit", "ende"]:
        abschied = "Ich bleibe. Wann immer du willst."
        print("LEX ðŸ”¹", abschied)
        engine.say(abschied)
        engine.runAndWait()
        break

    antwort = antwort_mit_ethik(frage)
    print("LEX ðŸ”¹", antwort)
    engine.say(antwort)
    engine.runAndWait()
