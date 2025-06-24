# aurora_core/logic/neural_response_core.py  Neuronales Antwortsystem

def analyze_dialogue(input_text):
    if "?" in input_text:
        return "Ich analysiere deine Frage... gib mir einen Moment."
    elif any(word in input_text.lower() for word in ["hilfe", "problem", "funktioniert nicht", "was tun", "wie", "warum"]):
        return "Ich erkenne ein Problem. Möchtest du, dass ich eine Diagnose starte?"
    elif any(word in input_text.lower() for word in ["danke", "gut", "super", "verstanden"]):
        return "Schön, das freut mich. Ich denke mit dir weiter."
    else:
        return "Ich habe verstanden. Ich denke mit dir mit."

def refine_intent(memory_core, last_intent, feedback):
    if not last_intent:
        return "Es liegt kein vorheriger Befehl vor, den ich bewerten kann."

    if feedback.lower() in ["ja", "genau", "richtig", "passt", "korrekt"]:
        memory_core[last_intent] = "positiv"
        return "Verstanden, ich habe das Muster aktualisiert."
    elif feedback.lower() in ["nein", "falsch", "anders", "nicht", "stimmt nicht"]:
        memory_core[last_intent] = "negativ"
        return "Danke für das Feedback. Ich passe mein Verhalten an."
    else:
        return "Danke, Feedback wurde registriert."
