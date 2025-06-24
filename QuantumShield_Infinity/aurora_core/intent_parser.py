# -*- coding: utf-8 -*-
# aurora_core/intent_parser.py

def parse_intent(text):
    text = text.lower().strip()

    if "status" in text:
        return "SYSTEM_STATUS"
    elif "verbindung" in text:
        return "CONNECT"
    elif "hörst du" in text or "hörst mich" in text:
        return "HEARING_CHECK"
    elif "beenden" in text or "tschüss" in text:
        return "TERMINATE"
    elif "aktivieren" in text or "systeme aktivieren" in text:
        return "ACTIVATE"
    elif "neustart" in text:
        return "REBOOT"
    elif "schild" in text or "sicherheitssystem" in text or "schutz" in text:
        return "SHIELD_ON"
    elif "jotma" in text:
        return "JOTMA_START"
    elif "lex" in text:
        return "LEX_START"
    elif "feedback" in text:
        return "FEEDBACK"
    
    # Neue Intents
    elif "datenanalyse" in text or "analyse starten" in text or "daten auswerten" in text:
        return "START_DATA_ANALYSIS"
    elif "präsentation" in text or "ppt" in text or "erstelle präsentation" in text:
        return "GENERATE_PRESENTATION"
    elif "berichte" in text or "report" in text:
        return "GENERATE_REPORT"
    elif "tts test" in text or "sprachtest" in text:
        return "TTS_TEST"
    
    else:
        return "UNKNOWN"
