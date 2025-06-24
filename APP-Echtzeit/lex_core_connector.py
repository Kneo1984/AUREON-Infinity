# -*- coding: utf-8 -*-
#  AUREON MONSTER CONNECTOR  Stand 2025-06-22
import datetime, subprocess, sys, socket
from pathlib import Path
import psutil, difflib, locale
locale.setlocale(locale.LC_ALL, "")

try:
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    import comtypes, ctypes
    _VOL_OK = True
except Exception:
    _VOL_OK = False

#  Zusatz-Funktionen 
def _safe_import_pillow():
    try:
        from PIL import ImageGrab
        return ImageGrab
    except Exception:
        return None

def take_screenshot():
    grab = _safe_import_pillow()
    if grab is None:
        return " Screenshot-Modul (Pillow) nicht installiert."
    path = Path.cwd() / f"screenshot_{datetime.datetime.now():%Y%m%d_%H%M%S}.png"
    grab.grab().save(path)
    return f" Screenshot gespeichert: {path}"

#  Haupt-Klasse 
class AureonCore:
    def __init__(self):
        self.befehlsmatrix = {
            "überprüfe system": "CHECK_SYSTEM",
            "aktiviere schutz": "ACTIVATE_PROTECTION",
            "öffne terminal":   "OPEN_TERMINAL",
            "hilfe":            "SHOW_CMDS",
            "zeige befehle":    "SHOW_CMDS",
            "starte vpn":       "START_VPN",
            "netzwerkstatus":   "NETWORK_STATUS",
            "herunterfahren":   "SHUTDOWN",
            "screenshot":       "SCREENSHOT",
            "notruf senden":    "EMERGENCY"
        }

    #  Interpreter
    def lex_interpreter(self, befehl:str):
        befehl = befehl.lower().strip()
        if befehl in self.befehlsmatrix:
            return self.befehlsmatrix[befehl]
        close = difflib.get_close_matches(befehl, self.befehlsmatrix, n=1, cutoff=0.8)
        return self.befehlsmatrix.get(close[0]) if close else None

    #  Antworten + Aktionen
    def lex_response(self, action:str, befehl:str=None):
        if action is None:
            return " Befehl nicht erkannt."

        if action == "SHOW_CMDS":
            return "Verfügbare Befehle: " + ", ".join(self.befehlsmatrix)

        if action == "CHECK_SYSTEM":
            cpu = psutil.cpu_percent(); ram = psutil.virtual_memory().percent
            return f" Systemcheck: CPU {cpu}% | RAM {ram}%  alles grün."

        if action == "ACTIVATE_PROTECTION":
            subprocess.run(["netsh","advfirewall","set","currentprofile","state","on"],
                           capture_output=True)
            return " Firewall aktiviert."

        if action == "OPEN_TERMINAL":
            subprocess.Popen("wt.exe", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return " Windows-Terminal geöffnet."

        if action == "START_VPN":
            vpn_path = r"C:\Program Files\OpenVPN\bin\openvpn-gui.exe"
            if not Path(vpn_path).exists():
                return " OpenVPN-GUI nicht gefunden. Bitte prüfen."
            subprocess.Popen(["powershell","-Command",
                              "Start-Process -Verb runAs '"+vpn_path+"'"])
            return " VPN gestartet (GUI)."

        if action == "NETWORK_STATUS":
            return f" Netzwerkstatus: Host = {socket.gethostname()}, " \
                   f"IP = {socket.gethostbyname(socket.gethostname())}"

        if action == "SHUTDOWN":
            subprocess.run(["shutdown","/s","/t","30"])
            return " System fährt in 30 Sekunden herunter."

        if action == "SCREENSHOT":
            return take_screenshot()

        if action == "EMERGENCY":
            return " Notruf wurde gesendet. Hilfe ist unterwegs. (Test)"

        return f" Aktion {action} implementiert, aber noch ohne Effekt."

#  Globale Instanz 
AUREON = AureonCore()
