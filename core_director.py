import time
from modules.ai_planner import decide
from modules.docu_logger import log

log("🔵 AUREON CORE DIRECTOR aktiviert.")

while True:
    try:
        decide()
        time.sleep(600)  # 10 Minuten
    except KeyboardInterrupt:
        log("🟥 Manueller Abbruch durch Benutzer.")
        break
