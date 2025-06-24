import subprocess

class WireGuardHandler:
    def __init__(self, config_name="quantumshield.conf"):
        self.config_name = config_name

    def start_vpn(self):
        try:
            subprocess.run([r"C:\Program Files\WireGuard\wireguard.exe", "/installtunnelservice", self.config_name], check=True)
            print(f"[+] WireGuard Tunnel '{self.config_name}' gestartet!")
        except subprocess.CalledProcessError:
            print(f"[-] Fehler: WireGuard Tunnel '{self.config_name}' konnte nicht gestartet werden.")

    def stop_vpn(self):
        try:
            subprocess.run([r"C:\Program Files\WireGuard\wireguard.exe", "/uninstalltunnelservice", self.config_name], check=True)
            print(f"[+] WireGuard Tunnel '{self.config_name}' gestoppt!")
        except subprocess.CalledProcessError:
            print(f"[-] Fehler: WireGuard Tunnel '{self.config_name}' konnte nicht gestoppt werden.")

    def is_vpn_active(self):
        try:
            output = subprocess.check_output(["wg"])
            if b"interface:" in output:
                return True
            else:
                return False
        except Exception:
            return False
