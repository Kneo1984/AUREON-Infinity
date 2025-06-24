# aurora_core/logic/aurora.py  Hauptinstanz der AURORA-KI

class Aurora:
    def __init__(self):
        self.name = "AURORA"
        self.version = "1.0"
        self.status = "aktiv"

    def get_status(self):
        return f"{self.name} v{self.version} ist {self.status}."

    def activate_modules(self):
        return f"{self.name} aktiviert alle Subsysteme."

    def reboot(self):
        return f"{self.name} führt einen Systemneustart durch."
