# -*- coding: utf-8 -*-
# aurora_core/memory_core.py

import json
import os

MEMORY_FILE = os.path.join("shield_modules", "memory", "aurora_memory.json")

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {"feedback": []}
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def update_memory(memory):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)

def get_feedback():
    memory = load_memory()
    return memory.get("feedback", [])
