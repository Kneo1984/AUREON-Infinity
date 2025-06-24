# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox, ttk
import pyttsx3
import subprocess
import threading

# Sprachengine initialisieren
engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.setProperty("volume", 1.0)

def spreche(text):
    print("ðŸ§  AUREON:", text)
    engine.say(text)
    engine.runAndWait()

# Sektionen
sektionen = {
    "Sektion 1": "ðŸŒ NetzwerkprÃ¼fung",
    "Sektion 2": "ðŸ” DNS-Konfiguration prÃ¼fen",
    "Sektion 3": "ðŸ“¦ dpkg-Paketanalyse",
    "Sektion 4": "ðŸ§  Veraltete Befehle erkennen",
    "Sektion 5": "ðŸ›¡ï¸ Supervisor-Modus aktivieren",
    "Sektion 6": "ðŸ“Š Ressourcen Ã¼berwachen",
    "Sektion 7": "ðŸ“ˆ Verbindung & Portanalyse",
    "Sektion 8": "ðŸ§© IntegritÃ¤tsprÃ¼fung & Rootkits",
    "Sektion 9": "ðŸ“œ Logging & Dialogfortsetzung",
    "Beenden": "â¹ AUREON zieht sich zurÃ¼ck"
}

def ausfÃ¼hren(sektion):
    spreche(f"Starte {sektion}")
    ausgabe = f"AUREON fÃ¼hrt jetzt aus: {sektion}\n"
    if sektion == "Beenden":
        spreche("Mission beendet. AUREON zieht sich zurÃ¼ck.")
        root.destroy()
    else:
        textfeld.insert(tk.END, ausgabe)

def auswahl_aus_dropdown():
    sektion = dropdown.get()
    if sektion:
        ausfÃ¼hren(sektion)
    else:
        messagebox.showinfo("Hinweis", "Bitte zuerst eine Sektion auswÃ¤hlen.")

def spracheingabe_simuliert():
    antwort = eingabefeld.get().strip().lower()
    if "1" in antwort or "sektion 1" in antwort:
        ausfÃ¼hren("Sektion 1")
    elif "2" in antwort:
        ausfÃ¼hren("Sektion 2")
    elif "3" in antwort:
        ausfÃ¼hren("Sektion 3")
    elif "4" in antwort:
        ausfÃ¼hren("Sektion 4")
    elif "5" in antwort:
        ausfÃ¼hren("Sektion 5")
    elif "6" in antwort:
        ausfÃ¼hren("Sektion 6")
    elif "7" in antwort:
        ausfÃ¼hren("Sektion 7")
    elif "8" in antwort:
        ausfÃ¼hren("Sektion 8")
    elif "9" in antwort:
        ausfÃ¼hren("Sektion 9")
    elif "99" in antwort or "beenden" in antwort:
        ausfÃ¼hren("Beenden")
    else:
        spreche("Ich konnte den Befehl nicht zuordnen.")

# GUI
root = tk.Tk()
root.title("ðŸ§  AUREON Kontrollzentrum")
root.geometry("700x450")

title = tk.Label(root, text="ðŸ§  WÃ¤hle deine Mission:", font=("Segoe UI", 14, "bold"))
title.pack(pady=10)

dropdown = ttk.Combobox(root, values=list(sektionen.keys()), font=("Segoe UI", 12))
dropdown.pack(pady=5)

button_start = tk.Button(root, text="ðŸš€ Starte Mission", font=("Segoe UI", 12), command=auswahl_aus_dropdown)
button_start.pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_eingabe = tk.Label(frame_input, text="Oder sprich/schreibe (z.â€¯B. 'Sektion 1' oder '99'):", font=("Segoe UI", 10))
label_eingabe.pack(side=tk.LEFT, padx=5)

eingabefeld = tk.Entry(frame_input, font=("Segoe UI", 12), width=25)
eingabefeld.pack(side=tk.LEFT, padx=5)

button_eingabe = tk.Button(frame_input, text="ðŸŽ¤ AusfÃ¼hren", font=("Segoe UI", 10), command=spracheingabe_simuliert)
button_eingabe.pack(side=tk.LEFT)

textfeld = tk.Text(root, height=10, font=("Consolas", 10))
textfeld.pack(pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
