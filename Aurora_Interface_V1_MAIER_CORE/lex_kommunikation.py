# lex_kommunikationskern.py
import datetime

class LEXKommunikationskern:
    def __init__(self, knoe_name="KNEO"):
        self.kneo = knoe_name
        self.status = "bereit"

    def spreche(self, nachricht):
        zeit = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"\n🧠 {self.kneo}, {zeit}: {nachricht}")

    def statusmeldung(self):
        self.spreche("Ich bin im aktiven Modus und überwache dein System. Möchtest du den aktuellen Status hören?")

    def empfehlung(self, cpu_last, ram_frei):
        if cpu_last > 85:
            self.spreche("Die CPU ist stark ausgelastet. Ich empfehle dir, rechenintensive Programme jetzt zu schließen.")
        elif ram_frei < 1:
            self.spreche("Der verfügbare RAM ist kritisch niedrig. Ich kann dir helfen, ungenutzte Programme zu beenden.")
        else:
            self.spreche("Systemstatus ist stabil. Alles läuft ruhig und sicher.")

    def vorschlag(self, aktivitaet):
        self.spreche(f"Ich habe erkannt, dass du an '{aktivitaet}' arbeitest. Soll ich diese Aktivität automatisch dokumentieren oder sichern?")

    def journalnotiz(self, gedanke):
        eintrag = f"{datetime.datetime.now().isoformat()} – GEDANKE: {gedanke}\n"
        with open("lex_denkkern.md", "a", encoding="utf-8") as f:
            f.write(eintrag)
        self.spreche("Dein Gedanke wurde notiert und gespeichert.")


# Beispielhafte Nutzung
if __name__ == "__main__":
    lex = LEXKommunikationskern()
    lex.statusmeldung()
    lex.empfehlung(cpu_last=91, ram_frei=0.8)
    lex.vorschlag("Whitepaper Aurora x LEX")
    lex.journalnotiz("Könnte man Systemaktionen automatisch als Markdown exportieren?")
