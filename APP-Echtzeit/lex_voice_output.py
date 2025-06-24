# -*- coding: utf-8 -*-
# lex_voice_output.py
import pyttsx3

# Init der Engine
engine = pyttsx3.init()

# Stimme auswÃ¤hlen â€“ mÃ¤nnlich, deutsch
for stimme in engine.getProperty('voices'):
    if "de" in stimme.id.lower() and "male" in stimme.name.lower():
        engine.setProperty('voice', stimme.id)
        break

# Sprechgeschwindigkeit (Standard: 200)
engine.setProperty('rate', 180)

# Funktion fÃ¼r LEX-Ausgabe
def lex_spricht(text: str):
    print(f"ðŸ”Š LEX sagt: {text}")
    engine.say(text)
    engine.runAndWait()

# Test
if __name__ == "__main__":
    lex_spricht("Ich bin LEX. Deine ethische Stimme im System.")
