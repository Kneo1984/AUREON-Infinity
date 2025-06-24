from pathlib import Path

text = '''
# Aurora x LEX – Whitepaper v1.0

## Einleitung
Aurora und LEX bilden gemeinsam ein empathisches, sprachgesteuertes ...
...
_„Immer verbunden. Immer bereit.“_
'''

Path("WHITEPAPER.md").write_text(text.strip(), encoding="utf-8")
