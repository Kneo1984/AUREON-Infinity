import time
from vpn.wireguard_handler import WireGuardHandler

class AutoReconnect:
    def __init__(self, config_name="quantumshield", max_attempts=3, delay_between_attempts=5):
        self.handler = WireGuardHandler(config_name)
        self.max_attempts = max_attempts
        self.delay = delay_between_attempts

    def attempt_reconnect(self):
        print("[*] VPN-Verbindung verloren. Versuche Wiederherstellung...")
        attempts = 0
        while attempts < self.max_attempts:
            if self.handler.is_vpn_active():
                print("[+] VPN ist wieder aktiv.")
                return True
            else:
                print(f"[*] Neuer Verbindungsversuch ({attempts+1}/{self.max_attempts})...")
                self.handler.start_vpn()
                time.sleep(self.delay)
                attempts += 1

        print("[-] Konnte VPN nicht wiederherstellen nach mehreren Versuchen.")
        return False
