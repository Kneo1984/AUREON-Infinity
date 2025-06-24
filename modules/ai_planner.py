from modules.system_monitor import get_status
from modules.task_engine import run_task
from modules.docu_logger import log

def decide():
    stats = get_status()
    if stats["ram"] > 80:
        log("RAM über 80% – Cleanup empfohlen.")
        run_task("cleanup")
    elif stats["cpu"] > 85:
        log("CPU über 85% – Update kann helfen.")
        run_task("update")
    else:
        log("System im stabilen Zustand. Kein Eingriff nötig.")
