import base64
import logging
from pathlib import Path
from getpass import getpass
from stegano import lsb
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.backends import default_backend

# ───── Logging vorbereiten ─────
LOG_PATH = Path("logs/ip_cloak_trinity_log.txt")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# ───── ROT-7 Rückentschlüsselung ─────
def rotation_decrypt(text, offset=7):
    return ''.join(chr((ord(c) - offset) % 256) for c in text)

# ───── AES-256 Entschlüsselung ─────
def decrypt_aes256(encrypted_base64, password):
    try:
        backend = default_backend()
        key_hash = hashes.Hash(hashes.SHA256(), backend)
        key_hash.update(password.encode())
        aes_key = key_hash.finalize()

        encrypted_data = base64.b64decode(encrypted_base64)
        iv = encrypted_data[:16]
        ct = encrypted_data[16:]

        cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=backend)
        decryptor = cipher.decryptor()
        padded = decryptor.update(ct) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        plaintext = unpadder.update(padded) + unpadder.finalize()

        return plaintext.decode()
    except Exception as e:
        logging.error(f"❌ AES-Entschlüsselung fehlgeschlagen: {e}")
        print("❌ Entschlüsselung fehlgeschlagen. Passwort korrekt?")
        return None

# ───── Hauptlogik ─────
def main():
    print("🖼️ IP-Extraktion aus Bild starten...")
    image_path = input("📂 Pfad zum Bild mit versteckter IP: ").strip('"').strip("'")

    if not Path(image_path).exists():
        print("❌ Bildpfad nicht gefunden.")
        logging.warning(f"Pfad nicht gefunden: {image_path}")
        return

    try:
        hidden_data = lsb.reveal(image_path)
    except Exception as e:
        print(f"❌ Fehler beim LSB-Zugriff: {e}")
        logging.error(f"Fehler beim Zugriff auf Bildinhalt: {e}")
        return

    if not hidden_data:
        print("⚠️ Keine eingebettete IP erkannt – ist dies das richtige Bild?")
        logging.warning("Leerer LSB-Datenblock erkannt.")
        return

    print("🔁 ROT-7-Entschlüsselung...")
    rot_decoded = rotation_decrypt(hidden_data)

    password = getpass("🔑 Passwort zur Entschlüsselung: ")

    print("🔓 Starte AES-256 Entschlüsselung...")
    ip = decrypt_aes256(rot_decoded, password)

    if ip:
        print(f"\n✅ Ursprüngliche IP erfolgreich wiederhergestellt:\n📡 {ip}")
        logging.info(f"IP entschlüsselt: {ip}")
    else:
        logging.error("IP konnte nicht entschlüsselt werden.")

if __name__ == "__main__":
    main()




