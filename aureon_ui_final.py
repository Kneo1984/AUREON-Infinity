print("[AUREON UI] Initialisierung...")

import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import pyttsx3
from pathlib import Path

AUREON_DIR = str(Path.home() / "AUREON")
VOICE_ENGINE = pyttsx3.init()
VOICE_ENGINE.say("AUREON Interface gestartet")
VOICE_ENGINE.runAndWait()

def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True, cwd=AUREON_DIR)
        print(f"[AUREON OK] {command}\n{result}")
        messagebox.showinfo("AUREON Ergebnis", result)
    except subprocess.CalledProcessError as e:
        print(f"[AUREON FEHLER] {command}\n{e.output}")
        messagebox.showerror("AUREON Fehler", e.output)

def restart_ui(root):
    root.destroy()
    os.execlp("python3", "python3", "aureon_ui_final.py")

def build_ui():
    print("[AUREON UI] Interface wird aufgebaut...")
    root = tk.Tk()
    root.title("🧠 AUREON Frequenz-Interface 🌌")
    root.geometry("600x420")
    root.configure(bg='black')
    root.protocol("WM_DELETE_WINDOW", lambda: (root.destroy(), os._exit(0)))

    title = tk.Label(root, text="AUREON – Kosmisches Kontrollzentrum", font=("Helvetica", 16, "bold"), fg="cyan", bg="black")
    title.pack(pady=20)

    commands = {
        "🔍 Systemstatus": "bash system_status_check.sh",
        "⚙️ Update": "sudo apt update -y",
        "🧹 Cleanup": "sudo apt autoremove -y && sudo apt autoclean",
        "📷 Kamera starten": "python3 aureon_camera_watch.py",
        "📤 Logs exportieren": "tar -czf ~/aureon_logs.tar.gz logs/"
    }

    for label, cmd in commands.items():
        btn = tk.Button(root, text=label, command=lambda c=cmd: run_command(c),
                        font=("Helvetica", 12), width=35, bg="#111111", fg="cyan", pady=6)
        btn.pack(pady=4)

    restart_btn = tk.Button(root, text="🔄 Neustart UI", command=lambda: restart_ui(root),
                            font=("Helvetica", 12), width=35, bg="darkred", fg="white", pady=6)
    restart_btn.pack(pady=10)

    print("[AUREON UI] Interface aktiv – Befehle bereit.")
    root.mainloop()

if __name__ == "__main__":
    build_ui()
