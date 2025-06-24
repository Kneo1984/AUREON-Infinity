# -*- coding: utf-8 -*-
# aurora_core/aurora.py

class Aurora:
    def __init__(self):
        self.status = "bereit"
        self.version = "1.0.0"

    def starten(self):
        return "AURORA-System gestartet."

    def info(self):
        return f"AURORA v{self.version} - Status: {self.status}"
