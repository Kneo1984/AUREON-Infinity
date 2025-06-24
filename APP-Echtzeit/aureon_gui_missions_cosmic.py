# -*- coding: utf-8 -*-

import os
import tkinter as tk
from tkinter import messagebox
import subprocess
import datetime

class AUREONGUI:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("ðŸ§¿ AUREON Kontrollzentrum")
        self.app.geometry("780x550")
        self.app.configure(bg="#101010")

        self.mission_var = tk.StringVar()
        self.mission_var.set("Sektion 1")

        self.cmd = tk.StringVar()

        tk.Label(self.app, text="WÃ¤hle deine Mission:", fg="white", bg="#101010", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Entry(self.app, textvariable=self.mission_var, width=40).pack()
        tk.Button(self.app, text="ðŸš€ Starte Mission", command=self.start_mission, bg="#303030", fg="white").pack(pady=10)

        tk.Label(self.app, text="Oder sprich/schreibe (z.â€¯B. 'Sektion 1' oder 'alles'):", fg="gray", bg="#101010").pack()
        tk.Entry(self.app, textvariable=self.cmd, width=50).pack(pady=5)
        tk.Button(self.app, text="ðŸ§  AusfÃ¼hren", command=self.run_input).pack()

        self.output = tk.Text(self.app, height=20, bg="black", fg="lime", font=("Courier", 10))
        self.output.pack(fill="both", expand=True)

        self.log("ðŸ” AUREON Spiegelmodus aktiv.")
        self.scan_environment()

    def log(self, text):
        timestamp = datetime.datetime.now().strftime("[%H:%M:%S]")
        self.output.insert(tk.END, f"{timestamp} {text}
")
        self.output.see(tk.END)

    def start_mission(self):
        sektion = self.mission_var.get().lower().replace(" ", "").replace("sektion", "")
        base = os.path.join(os.path.dirname(__file__), "..", "_missions")

        if sektion == "alles":
            missions = sorted([f for f in os.listdir(base) if f.endswith(".py")])
            for mission in missions:
                pfad = os.path.join(base, mission)
                self.log(f"âœ¨ Starte {mission} ...")
                subprocess.Popen(["python", pfad], shell=True)
            return

        pfad = os.path.join(base, f"sektion{sektion}.py")
        if os.path.exists(pfad):
            self.log(f"ðŸ› ï¸ AUREON fÃ¼hrt jetzt aus: Sektion {sektion}")
            subprocess.Popen(["python", pfad], shell=True)
        else:
            self.log("âš ï¸ Sektion nicht gefunden.")
            messagebox.showwarning("Hinweis", "Bitte gÃ¼ltige Mission eingeben (z.B. Sektion 1)")

    def run_input(self):
        eingabe = self.cmd.get().lower().strip()
        self.log(f"Eingabe: {eingabe}")
        self.mission_var.set(eingabe)
        self.start_mission()

    def scan_environment(self):
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        module_count = sum(len(files) for _, _, files in os.walk(root_dir))
        mission_dir = os.path.join(root_dir, "_missions")
        if not os.path.exists(mission_dir):
            os.makedirs(mission_dir)
            self.log("ðŸ“‚ _missions-Verzeichnis erstellt.")
        sektionen = [f for f in os.listdir(mission_dir) if f.endswith(".py")]
        self.log(f"ðŸ§  {len(sektionen)} Sektionen erkannt: {', '.join(sektionen)}")
        self.log(f"ðŸ“Š Systemweite Module erkannt: {module_count}")

    def mainloop(self):
        self.app.mainloop()

if __name__ == "__main__":
    app = AUREONGUI()
    app.mainloop()
