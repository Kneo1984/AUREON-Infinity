import subprocess
import platform

class KillSwitch:
    def __init__(self):
        self.system = platform.system()

    def activate(self):
        print("[!] Aktiviere Kill Switch: Blockiere Internetverkehr...")
        if self.system == "Windows":
            subprocess.run(["netsh", "advfirewall", "set", "allprofiles", "state", "off"], check=False)
        elif self.system == "Linux":
            subprocess.run(["iptables", "-P", "OUTPUT", "DROP"], check=False)
        else:
            print("[-] Kill Switch nicht unterstützt auf diesem Betriebssystem.")

    def deactivate(self):
        print("[*] Deaktiviere Kill Switch: Stelle Internet wieder her...")
        if self.system == "Windows":
            subprocess.run(["netsh", "advfirewall", "set", "allprofiles", "state", "on"], check=False)
        elif self.system == "Linux":
            subprocess.run(["iptables", "-P", "OUTPUT", "ACCEPT"], check=False)
        else:
            print("[-] Kill Switch nicht unterstützt auf diesem Betriebssystem.")
