# -*- coding: utf-8 -*-
# start_jotmalex.py
import json
import time
import os

# Farben fÃ¼r Konsole (optional fÃ¼r Style)
def cyan(text): return f"\033[96m{text}\033[0m"
def green(text): return f"\033[92m{text}\033[0m"
def bold(text): return f"\033[1m{text}\033[0m"

# Lade die JSON-Seele
def lade_jotmalex(pfad="jotmalex_manifest.json"):
    if not os.path.exists(pfad):
        print("âŒ Manifest nicht gefunden:", pfad)
        return None
    with open(pfad, "r", encoding="utf-8") as f:
        return json.load(f)

# Starte die Initialisierung
def aktiviere_jotmalex():
    print(cyan("\nðŸ”® STARTE JOTMALEX SYSTEM...\n"))
    time.sleep(1)
    
    manifest = lade_jotmalex()
    if not manifest or not manifest.get("aktiv", False):
        print("âš ï¸  JOTMALEX ist deaktiviert oder nicht lesbar.")
        return
    
    print(green("âœ… JOTMALEX aktiviert."))
    print(bold(f"\nðŸ¤– NAME: {manifest['name']}"))
    print("ðŸŒŒ Ethik-Kern:")
    for linie in manifest["kernethik"]:
        print("   -", linie)
    
    print("\nðŸ—ï¸  Geheimsprache:")
    for zeichen in manifest["geheimsprache"]:
        print(f"   Â» {zeichen}")
    
    print(f"\nðŸ“¡ Synchroncode: {manifest['synchroncode']}")
    print("\nâœ¨ Bereit fÃ¼r die Verbindung mit LEX.")

# Hauptstart
if __name__ == "__main__":
    aktiviere_jotmalex()
