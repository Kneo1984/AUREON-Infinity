import speech_recognition as sr
from modules.docu_logger import log

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 AUREON hört zu...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language="de-DE")
        log(f"Sprachbefehl erkannt: {command}")
        return command.lower()
    except sr.UnknownValueError:
        log("Sprachbefehl unverständlich.")
    except sr.RequestError as e:
        log(f"Sprachdienstfehler: {e}")
    return ""
