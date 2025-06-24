# -*- coding: utf-8 -*-
# AUTOHEILUNG: Unicode & Logging vollstÃ¤ndig robust
import os, json

BASE = r"C:\Users\denni\OneDrive\Dokumente\APP-Echtzeit"
MISSION_LOG = os.path.join(BASE, "mission_ai_sorted.log")
GUIDANCE_LOG = os.path.join(BASE, "aureon_guidance.log")

def list_files():
    structure = {}
    for root, dirs, files in os.walk(BASE):
        if '__pycache__' in root:
            continue
        for file in files:
            full = os.path.join(root, file)
            ext = os.path.splitext(file)[-1].lower()
            structure.setdefault(ext, []).append(full)
    return structure

def generate_guidance(file_map):
    lines = ["ðŸ”§ AUREON SYSTEM GUIDE:"]
    lines.append("ðŸ§  Analyse abgeschlossen â€“ priorisierte Hinweise folgen.")
    
    if ".py" in file_map:
        lines.append(f"â–¶ï¸ Du hast {len(file_map['.py'])} Python-Skripte â€“ prÃ¼fe auf alte, doppelte oder unvollstÃ¤ndige.")
    if ".html" in file_map:
        lines.append("ðŸŒ Web-Dateien erkannt â€“ mÃ¶chtest du daraus ein Interface generieren?")
    if "model.json" in str(file_map):
        lines.append("ðŸ§¬ Modell-Dateien gefunden â€“ KI-Kern vorhanden.")
    if "log" in file_map:
        lines.append("ðŸ“œ Logs vorhanden â€“ Analysiere letzte Systemmeldungen.")
    
    lines.append("ðŸ“Œ Vorschlag: Starte als NÃ¤chstes âž¤ AUREON_MISSIONAI_LOGIC_CORE.py")
    lines.append("ðŸ“Œ Optional: Nutze sprecher_windows.py fÃ¼r Sprache oder GUI-Dateien fÃ¼r Steuerung.")

    return "\n".join(lines)

def save_guidance(text):
    try:
        with open(GUIDANCE_LOG, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"[âœ…] AUREON Guide gespeichert unter:\n{GUIDANCE_LOG}")
    except Exception as e:
        print(f"[âŒ] Fehler beim Speichern des Guides: {e}")

if __name__ == "__main__":
    files = list_files()
    guide = generate_guidance(files)
    print(guide)
    save_guidance(guide)
