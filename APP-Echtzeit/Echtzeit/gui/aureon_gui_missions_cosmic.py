# -*- coding: utf-8 -*-
import os
import tkinter as tk
from tkinter import messagebox
import subprocess

class AUREONGUI:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("ðŸ§¿ AUREON Kontrollzentrum")
        self.app.geometry("720x500")
        self.app.configure(bg="#101010")

        self.mission_var = tk.StringVar()
        self.mission_var.set("Sektion 1")

        self.cmd = tk.StringVar()

        # Auswahlbereich
        tk.Label(self.app, text="WÃ¤hle deine Mission:", fg="white", bg="#101010", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Entry(self.app, textvariable=self.mission_var, width=40).pack()
        tk.Button(self.app, text="ðŸ” Starte Mission", command=self.start_mission, bg="#303030", fg="white").pack(pady=10)

        # Textfeld fÃ¼r Sprach- oder Texteingabe
        tk.Label(self.app, text="Oder sprich/schreibe (z.â€¯B. 'Sektion 1' oder 'alles'):", fg="gray", bg="#101010").pack()
        tk.Entry(self.app, textvariable=self.cmd, width=50).pack(pady=5)
        tk.Button(self.app, text="ðŸª„ AusfÃ¼hren", command=self.run_input).pack()

        # Ausgabetext
        self.output = tk.Text(self.app, height=20, bg="black", fg="lime", font=("Courier", 10))
        self.output.pack(fill="both", expand=True)

    def log(self, text):
        self.output.insert(tk.END, f"{text}\n")
        self.output.see(tk.END)

    def start_mission(self):
        sektion = self.mission_var.get().lower().replace(" ", "").replace("sektion", "")
        if sektion == "alles":
            base = os.path.join(os.path.dirname(__file__), "..", "_missions")
            missions = sorted([
                f for f in os.listdir(base) if f.endswith(".py")
            ])
            for mission in missions:
                pfad = os.path.join(base, mission)
                self.log(f"âœ¨ Starte {mission} ...")
                subprocess.Popen(["python", pfad], shell=True)
            return

        pfad = os.path.join(os.path.dirname(__file__), "..", "_missions", f"sektion{sektion}.py")
        self.log(f"AUREON fÃ¼hrt jetzt aus: sektion{sektion}")
        try:
            subprocess.Popen(["python", pfad], shell=True)
        except Exception as e:
            self.log(f"Fehler: {str(e)}")
            messagebox.showwarning("Hinweis", "Sektion nicht gefunden.")

    def run_input(self):
        eingabe = self.cmd.get().lower().strip()
        self.log(f"Eingabe: {eingabe}")
        self.mission_var.set(eingabe)
        self.start_mission()

    def mainloop(self):
        self.app.mainloop()

if __name__ == "__main__":
    app = AUREONGUI()
    app.mainloop()
