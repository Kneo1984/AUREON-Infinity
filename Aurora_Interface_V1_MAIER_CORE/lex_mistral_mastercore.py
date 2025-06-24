# lex_mistral_mastercore.py

from gpt4all import GPT4All
import time

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SYSTEMINITIALISIERUNG – MISTRAL MODELL LADEN
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("🌀 LEX: Initialisiere Mistral-Modell...")

model_path = "C:/Users/denni/.cache/gpt4all/mistral-7b-openorca.Q4_0.gguf"
model = GPT4All(model_path, allow_download=False)

print("✅ Mistral erfolgreich eingebunden und einsatzbereit.")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LEX MASTERCORE FUNKTIONEN
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def activate_quantumshield(integrity=100):
    print(f"🛡️ QuantumShield aktiviert mit Integritätslevel: {integrity}%")

def set_responsibility(trustee):
    print(f"🧠 LEX-MasterCore-KI aktiviert für: {trustee}")

def analyze_energy_flow(session):
    prompt = (
        "<|system|>\nDu bist LEX, ein deutscher Assistent zur Analyse von Energieströmen.\n"
        "<|user|>\nAnalysiere bitte den Energiefluss der letzten 24 Stunden in Zone 7.\n"
        "<|assistant|>\n"
    )
    print("📡 Analyseauftrag an Mistral gesendet...")
    answer = session.generate(
        prompt=prompt,
        max_tokens=200,
        temp=0.7,
        top_k=40
    )
    print(f"⚡ Aurora-Analyse:\n{answer}\n")

    if "instabil" in answer.lower():
        print("❗ Warnung: Energiefluss instabil. Schutzmaßnahmen empfohlen.")
        activate_quantumshield()
    return answer

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# INTERAKTIVER DIALOGMODUS MIT BENUTZEREINGABE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def interactive_mode(session):
    print("💬 Interaktiver Modus aktiviert. Schreibe 'exit' zum Beenden.\n")
    while True:
        user_input = input("👤 Du: ")
        if user_input.strip().lower() in ["exit", "quit", "stop"]:
            print("🔚 Beende den Dialog.")
            break

        full_prompt = (
            f"<|user|>\n{user_input}\n<|assistant|>\n"
        )

        print("📡 Anfrage an Mistral wird verarbeitet...")
        response = session.generate(
            prompt=full_prompt,
            max_tokens=150,
            temp=0.7,
            top_k=40
        )
        print(f"🤖 LEX:\n{response}\n")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MASTERCORE START
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def start_mastercore():
    print("🚀 Starte LEX-MasterCore...")
    set_responsibility("Kneo")
    activate_quantumshield(integrity=100)

    with model.chat_session() as session:
        print("🔍 Initialisiere Kontextdialog mit Mistral...")

        start_prompt = (
            "<|user|>\nLex, bist du bereit?\n<|assistant|>\n"
        )
        mistral_response = session.generate(
            prompt=start_prompt,
            max_tokens=100,
            temp=0.7,
            top_k=40
        )

        print(f"🧬 Antwort von Mistral:\n{mistral_response}\n")

        if "bereit" in mistral_response.lower():
            print("✅ Alle Systeme bereit. Module synchronisiert.")
        else:
            print("⚠️ Unklare Systemantwort – manuelle Prüfung empfohlen.")

        # ➕ Starte die Analyse automatisch
        analyze_energy_flow(session)

        # ➕ Danach: Aktiviere den interaktiven Dialog
        interactive_mode(session)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HAUPTAUFRUF
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if __name__ == "__main__":
    start_mastercore()
