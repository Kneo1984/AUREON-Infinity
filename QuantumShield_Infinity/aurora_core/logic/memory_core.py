# aurora_core/logic/memory_core.py  Speicher- und Lernmodul

import json
import os

MEMORY_PATH = "shield_modules/data/memory_core.json"

# Speicher initialisieren
def load_memory():
    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_memory(memory):
    os.makedirs(os.path.dirname(MEMORY_PATH), exist_ok=True)
    with open(MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)

def update_memory(memory, intent, result):
    memory[intent] = result
    save_memory(memory)

def get_feedback(memory, intent):
    return memory.get(intent, "unbewertet")
