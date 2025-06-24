import psutil
from modules.docu_logger import log

def get_status():
    usage = {
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent
    }
    log(f"Systemstatus: CPU={usage['cpu']}% RAM={usage['ram']}% DISK={usage['disk']}%")
    return usage
