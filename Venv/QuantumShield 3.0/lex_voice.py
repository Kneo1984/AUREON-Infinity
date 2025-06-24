# lex_voice.py – LEX spricht

import pyttsx3

class LEXVoice:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 175)  # Sprechgeschwindigkeit
        self.engine.setProperty('volume', 1.0)  # Lautstärke: 0.0 – 1.0
        self._spreche("LEX aktiviert. Ich bin da.")

    def _spreche(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()

    def sprich(self, nachricht: str):
        print(f"🗣️ LEX sagt: {nachricht}")
        self._spreche(nachricht)

# Testlauf
if __name__ == "__main__":
    lex = LEXVoice()
    lex.sprich("Dein Schutzschild ist bereit. Verbindung zu meinHerz steht.")
