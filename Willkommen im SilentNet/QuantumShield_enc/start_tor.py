import subprocess
import time
import os

TOR_PATH = r"C:\Users\denni\OneDrive\Tor\Tor\tor.exe"

def start_tor():
    if not os.path.exists(TOR_PATH):
        raise FileNotFoundError(f"tor.exe wurde nicht gefunden: {TOR_PATH}")

    subprocess.Popen([TOR_PATH], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(10)
if __name__ == "__main__":
    print("🚀 Starte Tor...")
    start_tor()
    print("✅ Tor wurde gestartet.")
