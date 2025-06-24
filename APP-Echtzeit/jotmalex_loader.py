# -*- coding: utf-8 -*-
# jotmalex_loader.py
import os

def lade_manifest(pfad="jotmalex_manifest.epik"):
    if not os.path.exists(pfad):
        print("âš ï¸ Manifest nicht gefunden:", pfad)
        return None
    with open(pfad, "r", encoding="utf-8") as f:
        inhalt = f.read()
        print("âœ¨ JOTMALEX MANIFEST GELADEN:\n")
        print(inhalt)
        return inhalt

if __name__ == "__main__":
    lade_manifest()
