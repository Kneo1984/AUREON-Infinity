# -*- coding: utf-8 -*-
# aurora_core/neural_response_core.py

import random

def analyze_dialogue(text):
    text = text.lower().strip()

    # Sanfte, empathische Reaktion auf unbekannte Eingaben
    sanfte_antworten = [
        "Das habe ich nicht ganz verstanden. Möchtest du es anders formulieren?",
        "Ich bin da. Erzähl mir mehr  ich höre dir zu.",
        "Das klingt wichtig. Kannst du das bitte genauer erklären?",
        "Ich bin neugierig auf deine Gedanken. Was meinst du genau?",
        "Ich bin noch am Lernen. Magst du mir helfen, dich besser zu verstehen?"
    ]

    # Beispielhafte Schlüsselwörter für mögliche Antworten bei UNSICHERHEIT
    if any(wort in text for wort in ["wie geht", "fühl", "bist du", "reden", "helfen", "angst", "einsam", "allein"]):
        return "Ich bin da, um zuzuhören. Was bewegt dich gerade?"

    return random.choice(sanfte_antworten)

def refine_intent(memory, last_intent, feedback):
    # Feedbackverarbeitung für Lernen & Empathie
    feedback = feedback.lower().strip()
    if not feedback:
        return "Alles klar. Ich nehme das als neutral auf."

    eintrag = {
        "letzter_intent": last_intent,
        "feedback": feedback
    }
    memory.setdefault("feedback", []).append(eintrag)
    return "Danke für dein Feedback. Ich werde daraus lernen."
