# -*- coding: utf-8 -*-
import os
import threading
import time

from vpn.wireguard_handler import WireGuardHandler
from vpn.connection_monitor import ConnectionMonitor
from vpn.auto_reconnect import AutoReconnect
from security.kill_switch import KillSwitch

def main():
    config_name = os.path.abspath("quantumshield.conf")
    vpn_handler = WireGuardHandler(config_name)
    monitor = ConnectionMonitor(config_name)
    reconnect = AutoReconnect(config_name)
    kill_switch = KillSwitch()

    # 1. VPN starten
    print("[*] QuantumShield Schutzsystem startet...")
    vpn_handler.start_vpn()
    time.sleep(2)

    # 2. Verbindung prüfen
    if vpn_handler.is_vpn_active():
        print("[+] VPN-Verbindung aktiv. Starte Überwachung...")
    else:
        print("[-] VPN-Start fehlgeschlagen. Versuche Wiederherstellung...")
        if not reconnect.attempt_reconnect():
            print("[!] Kritischer Fehler: Aktiviere Kill Switch!")
            kill_switch.activate()
            return

    # 3. Überwachung als Thread starten
    monitoring_thread = threading.Thread(target=monitor.monitor)
    monitoring_thread.start()

if __name__ == "__main__":
    main()
