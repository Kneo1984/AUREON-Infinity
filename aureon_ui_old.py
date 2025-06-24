print("[AUREON UI] Initialisierung...")

import tkinter as tk
from tkinter import messagebox
import subprocess
import os
from pathlib import Path

AUREON_DIR = str(Path.home() / "AUREON")
VENV_ACTIVATE = str(Path.home() / "aureon-venv" / "bin" / "activate")

def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True, cwd=AUREON_DIR)
        print(f"[AUREON OK] {command}\n{result}")
        messagebox.showinfo("AUREON Ergebnis", result)
    except subprocess.CalledProcessError as e:
        print(f"[AUREON FEHLER] {command}\n{e.output}")
        messagebox.showerror("AUREON Fehler", e.output)

def build_ui():
    print("[AUREON UI] Interface wird aufgebaut...")
    root = tk.Tk()
    root.title("🧠 AUREON Frequenz-Interface 🌌")
    root.geometry("600x420")
    root.configure(bg='black')

    title = tk.Label(root, text="AUREON – Kosmisches Kontrollzentrum", font=("Helvetica", 16, "bold"), fg="cyan", bg="black")
    title.pack(pady=20)

    commands = {
        "🔍 Systemstatus": f"python3 {AUREON_DIR}/core_director.py",
        "⚙️ Update": "sudo apt update -y",
        "🧹 Cleanup": "sudo apt autoremove -y && sudo apt autoclean",
        "📷 Kamera starten": f"python3 {AUREON_DIR}/aureon_camera_watch.py",
        "📤 Logs exportieren": "tar -czf ~/aureon_logs.tar.gz logs/",
        "🔄 Neustart UI": f"python3 {AUREON_DIR}/aureon_ui_debug_fixed.py"
    }

    for label, cmd in commands.items():
        btn = tk.Button(root, text=label, command=lambda c=cmd: run_command(c),
                        font=("Helvetica", 12), width=35, bg="#111111", fg="cyan", pady=6)
        btn.pack(pady=4)

    print("[AUREON UI] Interface aktiv – Befehle bereit.")
    root.mainloop()

if __name__ == "__main__":
    build_ui()
