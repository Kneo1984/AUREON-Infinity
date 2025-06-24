# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
import subprocess
import os

class AUREONGUI:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title(" AUREON Kontrollzentrum")
        self.app.geometry("720x480")

        tk.Label(self.app, text=" Wähle deine Mission:", font=("Arial", 12, "bold")).pack(pady=10)

        self.mission_var = tk.StringVar()
        self.mission_menu = tk.OptionMenu(self.app, self.mission_var, "Sektion 1", "Sektion 2", "Sektion 3")
        self.mission_menu.pack()

        tk.Button(self.app, text=" Starte Mission", command=self.start_mission).pack(pady=10)

        self.entry = tk.Entry(self.app, width=40)
        self.entry.pack()
        tk.Button(self.app, text=" Ausführen", command=self.run_input).pack()

        self.output = tk.Text(self.app, height=15, bg="black", fg="lime", font=("Courier", 10))
        self.output.pack(fill="both", expand=True)

    def start_mission(self):
        sektion = self.mission_var.get().lower().replace(" ", "")
        pfad = os.path.join("..", "missions", f"{sektion}.py")
        self.log(f"AUREON führt jetzt aus: {sektion}")
        try:
            subprocess.Popen(["python", pfad])
        except Exception as e:
            self.log(f"Fehler: {str(e)}")

    def run_input(self):
        cmd = self.entry.get().lower().strip()
        self.log(f" Eingabe: {cmd}")
        if cmd.startswith("sektion"):
            self.mission_var.set(cmd.title())
            self.start_mission()
        else:
            messagebox.showwarning(" Hinweis", "Bitte gültige Mission eingeben (z.B. Sektion 1)")

    def log(self, text):
        self.output.insert("end", text + "\n")
        self.output.see("end")

    def mainloop(self):
        self.app.mainloop()

if __name__ == "__main__":
    gui = AUREONGUI()
    gui.mainloop()
