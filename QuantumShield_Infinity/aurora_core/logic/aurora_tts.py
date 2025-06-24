# aurora_tts.py
import pyttsx3

class AuroraVoice:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 160)

    def speak(self, text):
        print(f"[AURORA] {text}")
        self.engine.say(text)
        self.engine.runAndWait()

# Globale Instanz
tts = AuroraVoice()

def speak(text):
    tts.speak(text)
