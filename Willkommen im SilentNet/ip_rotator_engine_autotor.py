
import os
import threading
import time
import requests
import tkinter as tk
from tkinter import messagebox
import subprocess





TOR_PATH = r"C:\Users\denni\OneDrive\Tor\Tor\tor.exe"

def start_tor():
    try:
        if not os.path.exists(TOR_PATH):
            raise FileNotFoundError(f"tor.exe wurde nicht gefunden: {TOR_PATH}")

        subprocess.Popen([TOR_PATH], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(10)
    except Exception as e:
        print(f"Fehler: {e}")
        messagebox.showerror("Tor Fehler", f"Tor konnte nicht gestartet werden: {e}")



def get_ip():
    try:
        proxies = {
            'http': f'socks5h://localhost:{SOCKS_PORT}',
            'https': f'socks5h://localhost:{SOCKS_PORT}'
        }
        ip = requests.get('https://api.ipify.org', proxies=proxies, timeout=10).text
        return ip
    except:
        return "Keine Verbindung"

class RotatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("IP-Rotator: QuantumCloak")
        master.geometry("340x160")
        master.resizable(False, False)

        self.status = tk.StringVar(value="🌐 Aktuelle IP (Tor): 🔄 Wird ermittelt...")
        self.running = False

        self.status_label = tk.Label(master, textvariable=self.status, fg="blue")
        self.status_label.pack(pady=10)

        self.start_btn = tk.Button(master, text="▶ Start", command=self.start_rotation)
        self.start_btn.pack(pady=2)

        self.stop_btn = tk.Button(master, text="■ Stop", command=self.stop_rotation)
        self.stop_btn.pack(pady=2)

        self.update_thread = None

    def start_rotation(self):
        if not self.running:
            self.running = True
            threading.Thread(target=start_tor, daemon=True).start()
            self.update_thread = threading.Thread(target=self.update_ip, daemon=True)
            self.update_thread.start()

    def stop_rotation(self):
        self.running = False
        self.status.set("🌐 Aktuelle IP (Tor): ❌ Gestoppt")

    def update_ip(self):
        while self.running:
            ip = get_ip()
            self.status.set(f"🌐 Aktuelle IP (Tor): {ip}")
            time.sleep(30)

if __name__ == "__main__":
    root = tk.Tk()
    app = RotatorGUI(root)
    root.mainloop()
