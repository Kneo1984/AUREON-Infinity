# aurora_core/aurora_dashboard.py
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from datetime import datetime

class AuroraDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AURORA Dashboard")
        self.geometry("900x600")
        self.configure(bg="#f0f4fb")

        self.init_ui()

    def init_ui(self):
        self.nav_frame = tk.Frame(self, bg="#dfe9f5", width=180)
        self.nav_frame.pack(side="left", fill="y")

        self.main_frame = tk.Frame(self, bg="#ffffff")
        self.main_frame.pack(side="right", expand=True, fill="both")

        self.sections = {
            "Systemstatus": self.render_status,
            "Gesprächslog": self.render_log,
            "Feedback": self.render_feedback,
            "Speicher": self.render_memory,
            "Intents": self.render_intents,
        }

        for section in self.sections:
            btn = tk.Button(self.nav_frame, text=section, command=lambda s=section: self.switch_section(s),
                            bg="#e7effb", fg="#333", relief="flat", pady=10)
            btn.pack(fill="x", padx=10, pady=5)

        self.switch_section("Systemstatus")

    def switch_section(self, name):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.sections[name]()

    def render_status(self):
        tk.Label(self.main_frame, text="Systemstatus", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        status_items = [
            ("Controller", "Aktiv"),
            ("TTS-Modul", "Bereit"),
            ("Intent-Erkennung", "Aktiv"),
            ("Feedback-Loop", "Online"),
            ("Speicher", "Schreibbereit")
        ]
        for name, val in status_items:
            ttk.Label(self.main_frame, text=f"{name}: {val}", font=("Arial", 12), background="white").pack(anchor="w", padx=20, pady=5)

    def render_log(self):
        tk.Label(self.main_frame, text="Gesprächslog", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        log = tk.Text(self.main_frame, wrap="word", bg="#f8faff", fg="#333")
        log.pack(expand=True, fill="both", padx=20, pady=10)
        log.insert("end", f"[{datetime.now().strftime('%H:%M:%S')}] AURORA gestartet\n")
        log.insert("end", f"[{datetime.now().strftime('%H:%M:%S')}] Interaktion mit KNEO erkannt\n")
        log.config(state="disabled")

    def render_feedback(self):
        tk.Label(self.main_frame, text="Feedbackauswertung", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        ttk.Label(self.main_frame, text="Positive Reaktionen: 87%", background="white").pack(anchor="w", padx=20, pady=5)
        ttk.Label(self.main_frame, text="Lernzyklen initiiert: 12", background="white").pack(anchor="w", padx=20, pady=5)

    def render_memory(self):
        tk.Label(self.main_frame, text="Speicherstatus", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        ttk.Label(self.main_frame, text="Aktuelle Memory-Keys: 5", background="white").pack(anchor="w", padx=20, pady=5)
        ttk.Label(self.main_frame, text="Letzter Eintrag: 'Intent: Hilfe'", background="white").pack(anchor="w", padx=20, pady=5)

    def render_intents(self):
        tk.Label(self.main_frame, text="Intent-Verlauf", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        intents = ["Frage: 'Wie geht es dir?' -> Intent: Smalltalk",
                   "Frage: 'Kannst du mir helfen?' -> Intent: Hilfe",
                   "Frage: 'Was kannst du tun?' -> Intent: Fähigkeiten"]
        for i in intents:
            ttk.Label(self.main_frame, text=i, background="white").pack(anchor="w", padx=20, pady=3)

if __name__ == "__main__":
    app = AuroraDashboard()
    app.mainloop()
