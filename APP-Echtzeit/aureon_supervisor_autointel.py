# -*- coding: utf-8 -*-
# ðŸŒŒ AUREON SUPERVISOR â€“ Autointelligente KI-Begleitung fÃ¼r dein System
import os, subprocess, datetime, json

LOG = "supervisor_runtime.log"
BASE = os.path.abspath(".")
COMMANDS = {
    "starte mission": "python AUREON_MISSIONAI_LOGIC_CORE.py",
    "sprich mit mir": "python sprecher_windows.py",
    "zeige gui": "python aureon_gui_final_full_exec.py",
    "system prÃ¼fen": "python AUREON_SYSTEM_GUIDE.py"
}

def log(text):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now().isoformat()}] {text}\n")

def ausfÃ¼hren(befehl):
    os.system(COMMANDS[befehl])
    log(f"Befehl ausgefÃ¼hrt: {befehl}")

def supervisor_loop():
    print("ðŸ¤– AUREON-Supervisor bereit. Was mÃ¶chtest du?")
    while True:
        try:
            user = input("ðŸ§¬ DU: ").strip().lower()
            if user in ["exit", "quit", "beenden"]:
                print("ðŸ”Œ AUREON wird beendet.")
                break
            elif user in COMMANDS:
                print(f"âš™ï¸  Starte: {user}")
                ausfÃ¼hren(user)
            else:
                print(f"ðŸ§  Ich verstehe: {user}")
                log(f"Nutzeranfrage (nicht erkannt): {user}")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    log("AUREON SUPERVISOR gestartet.")
    supervisor_loop()
