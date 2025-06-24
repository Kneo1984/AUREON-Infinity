# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from gpt4all import GPT4All
import os

app = Flask(__name__)

model_path = os.path.dirname(os.path.abspath(__file__))
model_file = 'ggml-gpt4all-j-v1.2-jazzy.bin'  # âŒ veraltet â€“ GGML, nicht GGUF
model_full = os.path.join(model_path, model_file)

if not os.path.isfile(model_full):
    raise FileNotFoundError(f"Modell nicht gefunden: {model_full}")

model = GPT4All(model_name=model_file, model_path=model_path, allow_download=False)

@app.route('/lex', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({'error': 'Kein Prompt erhalten'}), 400

    response = model.generate(data['prompt'])
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=False)
