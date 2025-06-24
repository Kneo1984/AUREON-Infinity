# -*- coding: utf-8 -*-
import os, time, subprocess, datetime
from pathlib import Path

def log(msg):
    with open("aureon_autolog.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] {msg}\n")

def check_and_compile(path):
    if not path.exists(): return False
    try:
        subprocess.run([".\lex_env_311\Scripts\python.exe", "-m", "py_compile", str(path)],
                       capture_output=True, check=True)
        log(f" Kompiliert: {path.name}")
        return True
    except Exception as e:
        log(f" Fehler: {path.name}  {e}")
        return False

def run_voice_core():
    subprocess.Popen([".\lex_env_311\Scripts\python.exe", "lex_voice_core.py"], cwd="C:\Users\denni\OneDrive\Dokumente\APP-Echtzeit",
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    os.chdir(r"C:\Users\denni\OneDrive\Dokumente\APP-Echtzeit")
    core = Path("lex_core_connector.py")
    voice = Path("lex_voice_core.py")
    if check_and_compile(core) and check_and_compile(voice):
        run_voice_core()
    else:
        log(" Start abgebrochen  Fehlerhafte Module erkannt.")

if __name__ == "__main__":
    main()
