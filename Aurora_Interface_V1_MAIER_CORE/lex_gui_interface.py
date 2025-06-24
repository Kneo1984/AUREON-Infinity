import tkinter as tk
from tkinter import scrolledtext
from gpt4all import GPT4All

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SYSTEMINITIALISIERUNG
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("🌀 LEX-GUI: Initialisiere Mistral-Modell...")

model_path = "C:/Users/denni/.cache/gpt4all/mistral-7b-openorca.Q4_0.gguf"
model = GPT4All(model_path, allow_download=False)

print("✅ Mistral-Modell bereit für GUI-Kommunikation.")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# GUI-FUNKTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def sende_anfrage():
    user_input = eingabe_feld.get()
    if not user_input.strip():
        return

    gui_log.insert(tk.END, f"👤 Du: {user_input}\n")
    gui_log.see(tk.END)

    with model.chat_session() as session:
        system_prompt = (
            "<|system|>\nDu bist LEX, ein deutschsprachiger Schutzsystem-Operator.\n"
            f"<|user|>\n{user_input}\n<|assistant|>\n"
        )

        gui_log.insert(tk.END, "📡 Anfrage wird verarbeitet...\n")
        gui_log.see(tk.END)

        antwort = session.generate(
            prompt=system_prompt,
            max_tokens=200,
            temp=0.7,
            top_k=40
        )

        gui_log.insert(tk.END, f"🤖 LEX: {antwort}\n\n")
        gui_log.see(tk.END)
        eingabe_feld.delete(0, tk.END)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# GUI-AUFBAU
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
fenster = tk.Tk()
fenster.title("LEX – Aurora Operator v1")
fenster.geometry("700x500")
fenster.configure(bg="#101820")

# Eingabe
eingabe_feld = tk.Entry(fenster, width=80, font=("Arial", 12))
eingabe_feld.pack(pady=10)
eingabe_feld.focus()

# Senden-Button
senden_button = tk.Button(fenster, text="➤ Senden an Mistral", command=sende_anfrage, bg="#0f62fe", fg="white", font=("Arial", 12, "bold"))
senden_button.pack(pady=5)

# Protokollfenster
gui_log = scrolledtext.ScrolledText(fenster, wrap=tk.WORD, width=85, height=20, font=("Consolas", 11), bg="#1e1e1e", fg="#39ff14")
gui_log.pack(pady=10)
gui_log.insert(tk.END, "💬 LEX Operator-Interface gestartet. Gib deine Befehle ein.\n\n")

# GUI starten
fenster.mainloop()
