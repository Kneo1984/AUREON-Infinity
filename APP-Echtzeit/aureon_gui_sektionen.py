# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

data = [
    (1, "â€žSektion 1â€œ", "ðŸŒ NetzwerkprÃ¼fung (IP, aktive Verbindungen)"),
    (2, "â€žSektion 2â€œ", "ðŸ” DNS-Konfiguration prÃ¼fen (Leak, Google DNS etc.)"),
    (3, "â€žSektion 3â€œ", "ðŸ“¦ dpkg-Paketanalyse (installierte Pakete, Sicherheitsstatus)"),
    (4, "â€žSektion 4â€œ", "ðŸ§  Veraltete Befehle erkennen & Alternativen anzeigen"),
    (5, "â€žSektion 5â€œ", "ðŸ›¡ï¸ Supervisor-Modus aktivieren und SystemÃ¼berwachung starten"),
    (6, "â€žSektion 6â€œ", "ðŸ“Š Ressourcen- und Prozessanalyse mit psutil"),
    (7, "â€žSektion 7â€œ", "ðŸ“ˆ Analyse verdÃ¤chtiger Verbindungen & Ports"),
    (8, "â€žSektion 8â€œ", "ðŸ§© IntegritÃ¤tsprÃ¼fung und Rootkit-Scanner"),
    (9, "â€žSektion 9â€œ", "ðŸ“œ JSON-Logging & Sprachdialog fortsetzen"),
    (99, "â€žBeendenâ€œ", "â¹ AUREON zieht sich zurÃ¼ck")
]

root = tk.Tk()
root.title("AUREON â€“ Interaktive Sektionen")

tree = ttk.Treeview(root, columns=("Nummer", "Sprachbefehl", "Funktion"), show="headings")
tree.heading("Nummer", text="Nummer")
tree.heading("Sprachbefehl", text="Sprachbefehl")
tree.heading("Funktion", text="Funktion")

for eintrag in data:
    tree.insert("", tk.END, values=eintrag)

tree.pack(expand=True, fill=tk.BOTH)
root.mainloop()
