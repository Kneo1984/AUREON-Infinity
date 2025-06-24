# ip_rotator_engine.py
import subprocess, time, threading, os, requests
import tkinter as tk
from tkinter import ttk, messagebox

TOR_PATH = r"C:\Users\denni\OneDrive\Tor\tor.exe"


CHECK_IP_URL = "https://api.ipify.org"

class IP_Rotator:
    def __init__(self):
        self.tor_process = None
        self.running = False

    def start_tor(self):
        if not os.path.exists(TOR_PATH):
            messagebox.showerror("Fehler", "Tor nicht gefunden.")
            return
        self.tor_process = subprocess.Popen([TOR_PATH], stdout=subprocess.DEVNULL)
        time.sleep(10)  # ⏳ Warten auf Bootstrapping
        self.running = True

    def stop_tor(self):
        if self.tor_process:
            self.tor_process.terminate()
            self.tor_process.wait()
            self.tor_process = None
            self.running = False

    def get_new_ip(self):
        try:
            return requests.get(CHECK_IP_URL, proxies={"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}, timeout=5).text
        except:
            return "⛔ Keine Verbindung"

rotator = IP_Rotator()

def start_rotation():
    threading.Thread(target=rotation_cycle).start()

def rotation_cycle():
    rotator.start_tor()
    while rotator.running:
        ip = rotator.get_new_ip()
        status.set(f"Aktuelle IP (Tor): {ip}")
        time.sleep(60 * 3)  # ⏱ alle 3 Minuten
        subprocess.run(["tor.exe", "-controlport", "9051", "signal", "newnym"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def stop_rotation():
    rotator.stop_tor()
    status.set("❌ Rotation gestoppt")

# ───── GUI ─────
root = tk.Tk()
root.title("🕵️ IP-Rotator: QuantumCloak")
root.geometry("400x200")

status = tk.StringVar()
status.set("🕸️ Bereit")

ttk.Label(root, text="IP-Rotator für Unsichtbarkeit", font=("Segoe UI", 12)).pack(pady=10)
ttk.Label(root, textvariable=status, foreground="blue").pack(pady=10)

btn_frame = ttk.Frame(root)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="🚀 Start", command=start_rotation).grid(row=0, column=0, padx=10)
ttk.Button(btn_frame, text="🛑 Stop", command=stop_rotation).grid(row=0, column=1, padx=10)

root.mainloop()
