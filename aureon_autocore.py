import os
import json
from collections import defaultdict

SCAN_FILE = "aureon_wsl_scan.txt"
DB_FILE = "aureon_db.json"
HTML_FILE = "aureon_map.html"
WORKSPACE_FILE = "AUREON.code-workspace"

def read_scan_file():
    if not os.path.exists(SCAN_FILE):
        print(f"[ERROR] Scan file {SCAN_FILE} nicht gefunden.")
        return []

    with open(SCAN_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines

def append_missing_paths():
    new_targets = [
        "/mnt/c/Users/denni/Aureon"
    ]

    keywords = [
        "flask", "quantum", "sqlite", "model", "aureon", "maya", "core",
        "tokenizer", "speech", "api", "embedding", "server", "langchain", "llm"
    ]

    existing = set()
    if os.path.exists(SCAN_FILE):
        with open(SCAN_FILE, "r", encoding="utf-8") as f:
            existing = set(line.strip() for line in f.readlines())

    with open(SCAN_FILE, "a", encoding="utf-8") as out:
        for root in new_targets:
            for dirpath, _, files in os.walk(root):
                for file in files:
                    if file.endswith((".py", ".json", ".txt", ".md", ".cfg")):
                        full_path = os.path.join(dirpath, file)
                        if full_path in existing:
                            continue
                        try:
                            with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                                content = f.read().lower()
                                if any(k in content for k in keywords):
                                    out.write(full_path + "\n")
                        except:
                            continue

def categorize(path):
    mapping = {
        "voice": ["speech", "stt", "recognition"],
        "api": ["flask", "request", "route", "fastapi"],
        "llm": ["tokenizer", "embedding", "langchain", "model", "transformer"],
        "system": ["quantum", "maya", "core", "aureon"],
        "data": ["sqlite", "csv", "json", "pandas"]
    }
    categories = []
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read().lower()
            for cat, keywords in mapping.items():
                if any(kw in content for kw in keywords):
                    categories.append(cat)
    except:
        categories.append("unreadable")
    return list(set(categories)) or ["uncategorized"]

def build_database(paths):
    db = []
    for path in paths:
        try:
            cats = categorize(path)
            db.append({"path": path, "categories": cats})
        except:
            pass
    return db

def write_json(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[✓] JSON-Datenbank gespeichert unter {DB_FILE}")

def generate_workspace(data):
    folders = [{"path": os.path.dirname(entry["path"])} for entry in data]
    unique_folders = []
    seen = set()
    for folder in folders:
        if folder["path"] not in seen:
            seen.add(folder["path"])
            unique_folders.append(folder)

    workspace = {
        "folders": unique_folders,
        "settings": {}
    }

    with open(WORKSPACE_FILE, "w", encoding="utf-8") as f:
        json.dump(workspace, f, indent=2)
    print(f"[✓] VS Code Workspace gespeichert als {WORKSPACE_FILE}")

def generate_html(data):
    html = """<html><head><title>AUREON Map</title></head><body>
    <h1>AUREON Dateikarte</h1><ul>"""
    for entry in data:
        html += f"<li><b>{', '.join(entry['categories'])}</b>: {entry['path']}</li>"
    html += "</ul></body></html>"

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[✓] HTML Map erstellt als {HTML_FILE}")

def main():
    print("[⧉] Lese Scan-Daten...")
    paths = read_scan_file()
    print(f"[✓] {len(paths)} Pfade geladen.")

    print("[+] Ergänze zusätzliche Verzeichnisse (nicht überschreiben)...")
    append_missing_paths()

    print("[✓] Lade aktualisierte Liste...")
    paths = read_scan_file()

    print("[⧉] Kategorisiere Dateien...")
    db = build_database(paths)

    write_json(db)
    generate_html(db)
    generate_workspace(db)

    print("\n🧠 AUREON AutoCore abgeschlossen.")

if __name__ == "__main__":
    main()
