import pyttsx3
tts = pyttsx3.init()
tts.setProperty("rate", 160)

def speak(text):
    print(f"[AURORA] {text}")
    tts.say(text)
    tts.runAndWait()
