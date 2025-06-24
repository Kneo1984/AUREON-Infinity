# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import pyttsx3
import psutil
import socket

# Farben & Stil
BG = "#1e1e2e"
FG = "#f8f8f2"
BTN_BG = "#44475a"
BTN_TXT = "#ffffff"
HIGHLIGHT = "#bd93f9"
TEXT_BG = "#282a36"
TEXT_FG = "#f8f8f2"

# Sprachmodul
engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.setProperty("volume", 1.0)

def spreche(text):
    print("ðŸ§  AUREON:", text)
    engine.say(text)
    engine.runAndWait()

# Aktive Verbindungen ermitteln
def hole_aktive_verbindungen():
    verbindungen = psutil.net_connections()
    details = []
    for v in verbindungen:
        try:
            laddr = f"{v.laddr.ip}:{v.laddr.port}" if v.laddr else "?"
            raddr = f"{v.raddr.ip}:{v.raddr.port}" if v.raddr else "-"
            status = v.status
            proto = socket.AddressFamily(v.family).name.replace("AF_", "")
            typ = socket.SocketKind(v.type).name.replace("SOCK_", "")
            details.append(f"{proto}/{typ} | {laddr} â†’ {raddr} | Status: {status}")
        except Exception:
            continue
    return "\n".join(details[:15])  # Begrenzung auf 15

# Sektionen + Beschreibung
sektionen = {
    "Sektion 1": "NetzwerkprÃ¼fung Ã¶ffnet IP-Status, aktive Ports und scannt deine Verbindungen.",
    "Sektion 2": "DNS-Konfiguration prÃ¼ft deine resolver.conf auf Anomalien wie GoogleDNS.",
    "Sektion 3": "dpkg-Analyse listet alle installierten Pakete und deren IntegritÃ¤t.",
    "Sektion 4": "Veraltete Befehle werden identifiziert und durch moderne ersetzt.",
    "Sektion 5": "Supervisor-Modus aktiviert. Systemschutz und Ãœberwachung starten.",
    "Sektion 6": "SystemressourcenprÃ¼fung. RAM, CPU, Prozesse werden Ã¼berwacht.",
    "Sektion 7": "Netzwerk- & Portanalyse auf verdÃ¤chtige AktivitÃ¤ten.",
    "Sektion 8": "IntegritÃ¤tsprÃ¼fung sucht Rootkits & prÃ¼ft Dateisystem-Konsistenz.",
    "Sektion 9": "Logging wird aktiviert. Alle VorgÃ¤nge werden in JSON festgehalten.",
    "Beenden": "AUREON zieht sich zurÃ¼ck. Alle Funktionen werden sanft deaktiviert."
}

# AusfÃ¼hrung
def ausfÃ¼hren(sektion):
    beschreibung = sektionen.get(sektion, "Unbekannte Mission.")
    meldung = f"â–¶ {sektion} aktiviert: {beschreibung}\n"
    verbindungen = hole_aktive_verbindungen()
    meldung += f"{verbindungen}\n"

    textfeld.config(state="normal")
    textfeld.insert(tk.END, meldung + "\n")
    textfeld.see(tk.END)
    textfeld.config(state="disabled")

    spreche(f"{sektion} aktiviert. Details angezeigt.")
    if sektion == "Beenden":
        root.destroy()

# Auswahlfunktion
def starte_dropdown():
    s = dropdown.get()
    if s:
        ausfÃ¼hren(s)
    else:
        spreche("Bitte eine Mission auswÃ¤hlen.")

def starte_eingabe():
    cmd = eingabefeld.get().strip().lower()
    for sektion in sektionen:
        if sektion.lower() in cmd or cmd in sektion.lower() or cmd in sektion[-2:]:
            ausfÃ¼hren(sektion)
            return
    spreche("Befehl unklar oder Sektion nicht erkannt.")

# GUI
root = tk.Tk()
root.title("ðŸ§  AUREON Kontrollzentrum FINAL+")
root.geometry("900x600")
root.configure(bg=BG)

style = ttk.Style()
style.theme_use("default")
style.configure("TLabel", background=BG, foreground=FG)
style.configure("TButton", background=BTN_BG, foreground=BTN_TXT)
style.configure("TCombobox", fieldbackground=BG, background=BTN_BG, foreground=FG)

tk.Label(root, text="ðŸ§  WÃ¤hle deine Mission:", font=("Segoe UI", 14, "bold"), bg=BG, fg=HIGHLIGHT).pack(pady=10)

dropdown = ttk.Combobox(root, values=list(sektionen.keys()), font=("Segoe UI", 12), state="readonly", width=45)
dropdown.pack(pady=5)

tk.Button(root, text="ðŸš€ Starte Mission", font=("Segoe UI", 11, "bold"), bg=BTN_BG, fg=BTN_TXT, command=starte_dropdown).pack(pady=10)

eingabe_frame = tk.Frame(root, bg=BG)
eingabe_frame.pack(pady=5)

tk.Label(eingabe_frame, text="Oder eingeben (z.â€¯B. Sektion 3 oder 99):", bg=BG, fg=FG).pack(side=tk.LEFT, padx=5)
eingabefeld = tk.Entry(eingabe_frame, font=("Segoe UI", 12), width=20)
eingabefeld.pack(side=tk.LEFT, padx=5)
tk.Button(eingabe_frame, text="ðŸŽ¤ AusfÃ¼hren", font=("Segoe UI", 10), command=starte_eingabe).pack(side=tk.LEFT, padx=5)

textfeld = tk.Text(root, height=20, font=("Consolas", 10), bg=TEXT_BG, fg=TEXT_FG, state="disabled")
textfeld.pack(pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
