import os
from rich.progress import track

ROOTS = [
    "/mnt/c/Users/Dennis/Documents",
    "/mnt/c/Users/Dennis/Desktop",
    "/mnt/c/Program Files",
    "/mnt/c/Program Files (x86)",
    "/mnt/c/Windows/System32",
    "/mnt/c/Windows/LiveKernelReports"
]

OUTPUT_FILE = "aureon_wsl_scan.txt"
KEYWORDS = [
    "flask", "quantum", "sqlite", "model", "aureon", "maya", "core",
    "tokenizer", "speech", "api", "embedding", "server", "langchain", "llm"
]

def is_interesting(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read().lower()
            return any(k in content for k in KEYWORDS)
    except:
        return False

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    for root in ROOTS:
        for dirpath, _, files in track(os.walk(root), description=f"[cyan]Scanne {root}"):
            for file in files:
                full_path = os.path.join(dirpath, file)
                if file.endswith((".py", ".json", ".txt", ".md", ".cfg")):
                    if is_interesting(full_path):
                        out.write(full_path + "\n")
