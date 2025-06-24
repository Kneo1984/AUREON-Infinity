import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    print(f"🔊 AUREON sagt: {text}")
    engine.say(text)
    engine.runAndWait()
