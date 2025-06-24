import json, random

glyphen = ["⟁", "ᚠ", "𓂀", "⚚", "Δ", "✶", "🜄", "ꙮ"]
strukturen = [
    "Glyph {glyph} steht für Transformation.",
    "Ausdruck {glyph} repräsentiert Licht und Wissen.",
    "{glyph} = Fokus + Geist + Zeit.",
    "Verbindung {glyph} aktiviert kollektive Erinnerung."
]

def erschaffe_sprache():
    sprache = []
    for _ in range(4):
        glyph = random.choice(glyphen)
        satz = random.choice(strukturen).format(glyph=glyph)
        sprache.append(satz)
    with open("aureon_sprache.json", "w", encoding="utf-8") as f:
        json.dump(sprache, f, indent=2, ensure_ascii=False)
    print("AUREON 🧠: Neue Sprachelemente erschaffen.")

if __name__ == "__main__":
    erschaffe_sprache()
