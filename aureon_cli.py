#!/usr/bin/env python3
import os

def start(cmd):
    print(f"\nAUREON 🛡️: Starte → {cmd}")
    os.system(cmd)

def menu():
    while True:
        print("\n🌌 AUREON – Hauptsteuerung")
        print("1️⃣  Netzwerkscan starten")
        print("2️⃣  Sprachmodul aktivieren")
        print("3️⃣  Denkplan erzeugen")
        print("4️⃣  Community öffnen")
        print("5️⃣  Karte anzeigen")
        print("6️⃣  VS Code öffnen")
        print("7️⃣  Triggerüberwachung aktivieren")
        print("0️⃣  Beenden")

        choice = input("\n🎙️  Deine Wahl: ").strip()

        if choice == "1":
            start("python3 ~/AUREON/aureon_scanner_wsl.py && python3 ~/AUREON/aureon_autocore.py")
        elif choice == "2":
            start("python3 ~/AUREON/aureon_langgen.py")
        elif choice == "3":
            start("python3 ~/AUREON/aureon_dayplan.py")
        elif choice == "4":
            start("python3 ~/AUREON/aureon_community.py")
        elif choice == "5":
            start("firefox ~/AUREON/aureon_map.html")
        elif choice == "7":
            start("python3 ~/AUREON/aureon_watchdog_trigger.py")
        elif choice == "6":
            start("code ~/AUREON/AUREON.code-workspace")
        elif choice == "0":
            print("\nAUREON: Abschaltung eingeleitet. 💤")
            break
        else:
            print("⚠️  Ungültige Eingabe.")

if __name__ == "__main__":
    menu()
