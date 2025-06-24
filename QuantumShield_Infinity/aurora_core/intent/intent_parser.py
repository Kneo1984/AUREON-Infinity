# aurora_core/intent/intent_parser.py  FINAL
import re

def parse_intent(text):
    text = text.lower().strip()

    if re.search(r"\b(status|systemstatus)\b", text):
        return "SYSTEM_STATUS"
    elif re.search(r"\b(verbindung|connect)\b", text):
        return "CONNECT"
    elif re.search(r"\b(hörst du mich|kannst du mich hören|hören)\b", text):
        return "HEARING_CHECK"
    elif re.search(r"\b(beenden|exit|stopp)\b", text):
        return "TERMINATE"
    elif re.search(r"\b(start|beginn|aktivieren|quantumshield aktivieren)\b", text):
        return "ACTIVATE"
    elif re.search(r"\b(neustart|restart|reboot)\b", text):
        return "REBOOT"
    elif re.search(r"\b(schild|schutz|abschirmung)\b", text):
        return "SHIELD_ON"
    elif re.search(r"\b(jotma|jotma starten|jotma aktivieren)\b", text):
        return "JOTMA_START"
    elif re.search(r"\b(lex|sprich lex|aktivieren lex|lex starten)\b", text):
        return "LEX_START"
    elif re.search(r"\b(systemanalyse|scan|überprüfen)\b", text):
        return "SYS_ANALYSE"
    elif re.search(r"\b(dokumente|ordner|explorer)\b", text):
        return "OPEN_DOCS"
    else:
        return "UNKNOWN"
