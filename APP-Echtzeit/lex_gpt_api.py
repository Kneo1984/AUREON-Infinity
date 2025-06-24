# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from gpt4all import GPT4All
import os
import json

app = Flask("ECHTZEIT")

# ðŸ” Lade Modellkonfiguration aus JSON
with open("model.json", "r", encoding="utf-8") as f:
    config = json.load(f)

model_name = config["model_name"]
model_path = config["model_path"]
max_tokens = config["max_tokens"]
temp = config["temp"]

# ðŸ“¥ Lade optional Manifest (wenn vorhanden)
manifest_path = config.get("manifest", "")
ethik_manifest = ""
if os.path.exists(manifest_path):
    with open(manifest_path, "r", encoding="utf-8") as f:
        ethik_manifest = f.read().strip()

# ðŸ§  Initialisiere Modell
model = GPT4All(model_name=model_name, model_path=model_path, allow_download=False)

@app.route('/chat', methods=['POST'])
def chat():
    if not request.is_json:
        return jsonify({"error": "UngÃ¼ltiges Format: JSON erwartet"}), 400

    data = request.get_json()
    frage = data.get("message", "").strip()
    if not frage:
        return jsonify({"error": "Keine Eingabe erhalten"}), 400

    # ðŸ” Baue kombinierten Prompt
    prompt = f"{ethik_manifest}\n\nFrage: {frage}\nAntwort:"

    try:
        antwort = model.generate(prompt=prompt, max_tokens=max_tokens, temp=temp)
        return jsonify({"response": antwort.strip()})
    except Exception as e:
        return jsonify({"error": f"Fehler beim Generieren: {e}"}), 500

# ðŸš€ Start
if __name__ == '__main__':
    app.run(port=5000)
