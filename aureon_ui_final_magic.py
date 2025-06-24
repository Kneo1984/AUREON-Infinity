print("[AUREON UI] Initialisierung...")

import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import threading
from pathlib import Path
import sys

AUREON_DIR = str(Path.home() / "AUREON")
PID_FILE = "/tmp/aureon_ui.lock"

def ensure_single_instance():
    if os.path.exists(PID_FILE):
        print("[AUREON BLOCK] Instanz läuft bereits.")
        sys.exit(0)
    with open(PID_FILE, "w") as f:
        f.write(str(os.getpid()))

def cleanup_pid():
    if os.path.exists(PID_FILE):
        os.remove(PID_FILE)

def run_command_async(command):
    def task():
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True, cwd=AUREON_DIR)
            print(f"[AUREON OK] {command}\n{result}")
            messagebox.showinfo("AUREON Ergebnis", result)
        except subprocess.CalledProcessError as e:
            print(f"[AUREON FEHLER] {command}\n{e.output}")
            messagebox.showerror("AUREON Fehler", e.output)
    threading.Thread(target=task).start()

def restart_ui(root):
    cleanup_pid()
    root.destroy()
    subprocess.Popen(["python3", os.path.join(AUREON_DIR, "aureon_ui_final_magic.py")])

def build_ui():
    print("[AUREON UI] Interface wird aufgebaut...")
    ensure_single_instance()

    root = tk.Tk()
    root.title("🧠 AUREON Frequenz-Interface 🌌")
    root.geometry("600x420+500+200")
    root.configure(bg='black')

    def on_closing():
        cleanup_pid()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    title = tk.Label(root, text="AUREON – Kosmisches Kontrollzentrum", font=("Helvetica", 16, "bold"), fg="cyan", bg="black")
    title.pack(pady=20)

    commands = {
        "🔍 Systemstatus": "python3 core_director.py",
        "⚙️ Update": "sudo apt update -y",
        "🧹 Cleanup": "sudo apt autoremove -y && sudo apt autoclean",
        "📷 Kamera starten": "python3 aureon_camera_watch.py",
        "📤 Logs exportieren": "tar -czf ~/aureon_logs.tar.gz logs/"
    }

    for label, cmd in commands.items():
        btn = tk.Button(root, text=label, command=lambda c=cmd: run_command_async(c),
                        font=("Helvetica", 12), width=35, bg="#111111", fg="cyan", pady=6)
        btn.pack(pady=4)

    restart_btn = tk.Button(root, text="🔄 Neustart UI", command=lambda: restart_ui(root),
                            font=("Helvetica", 12), width=35, bg="darkred", fg="white", pady=6)
    restart_btn.pack(pady=10)

    print("[AUREON UI] Interface aktiv – Befehle bereit.")
    root.mainloop()
    cleanup_pid()

if __name__ == "__main__":
    build_ui()
