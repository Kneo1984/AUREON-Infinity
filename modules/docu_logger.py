import logging
from datetime import datetime

log_path = "logs/system_journal.log"
logging.basicConfig(filename=log_path, level=logging.INFO, format="%(asctime)s - %(message)s")

def log(msg):
    logging.info(msg)
    print(f"[LOG] {msg}")
