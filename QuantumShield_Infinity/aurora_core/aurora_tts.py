import pyttsx3

engine = None

def speak(text):
    global engine
    if engine is None:
        try:
            engine = pyttsx3.init()
            engine.setProperty("rate", 160)
        except Exception as e:
            print(f"[AURORA] ❌ Fehler beim Initialisieren von pyttsx3: {e}")
            return
    print(f"[AURORA] {text}")
    engine.say(text)
    engine.runAndWait()
