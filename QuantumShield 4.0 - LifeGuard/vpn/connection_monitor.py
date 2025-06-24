import time
from vpn.wireguard_handler import WireGuardHandler

class ConnectionMonitor:
    def __init__(self, config_name="quantumshield", check_interval=5):
        self.handler = WireGuardHandler(config_name)
        self.check_interval = check_interval  # alle X Sekunden prüfen

    def monitor(self):
        print("[*] Starte VPN-Überwachung...")
        while True:
            if not self.handler.is_vpn_active():
                print("[-] VPN Verbindung verloren! Starte Notfallprotokoll...")
                self.handler.start_vpn()
            else:
                print("[+] VPN Verbindung stabil.")
            time.sleep(self.check_interval)
