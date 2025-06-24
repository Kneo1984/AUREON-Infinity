#!/usr/bin/env python3
import json
import os

# Pfad zur JSON-Datenbank vom Scan
json_path = "/root/AUREON/aureon_db.json"
# Ausgabe-Datei mit Analyse-Ergebnissen
report_path = "/root/AUREON/scan_summary.txt"

# Trigger-Wörter für verdächtige Dateien
triggers = ["passwort", "key", "vpn", "shadow", "secret"]

def load_scan_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def filter_suspicious_files(data, triggers):
    suspicious = []
    for entry in data:
        filepath = entry.get("path", "").lower()
        if any(trigger in filepath for trigger in triggers):
            suspicious.append(filepath)
    return suspicious

def create_report(suspicious_files):
    count = len(suspicious_files)
    lines = [f"Scan-Auswertung - Verdächtige Dateien: {count}\n"]
    lines += suspicious_files if count > 0 else ["Keine verdächtigen Dateien gefunden."]
    return "\n".join(lines)

def save_report(report, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(report)

def main():
    if not os.path.exists(json_path):
        print(f"Fehler: Scan-Datei {json_path} nicht gefunden.")
        return
    data = load_scan_data(json_path)
    suspicious_files = filter_suspicious_files(data, triggers)
    report = create_report(suspicious_files)
    save_report(report, report_path)
    print(report)

if __name__ == "__main__":
    main()
