import os
from modules.docu_logger import log

def run_task(task_name):
    log(f"Führe Aufgabe aus: {task_name}")
    if task_name == "update":
        os.system("sudo apt update -y")
        log("System wurde geupdatet.")
    elif task_name == "cleanup":
        os.system("sudo apt autoremove -y && sudo apt autoclean")
        log("Cleanup abgeschlossen.")
    else:
        log(f"Unbekannte Aufgabe: {task_name}")
