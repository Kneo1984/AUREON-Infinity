import requests
import base64
import os
import sys
import logging
from pathlib import Path
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.backends import default_backend
from stegano import lsb
from getpass import getpass

# ───── Logging vorbereiten ─────
LOG_PATH = Path("logs/ip_cloak_trinity_log.txt")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# ───── IP-Adresse abrufen ─────
def get_public_ip():
    try:
        ip = requests.get("https://api.ipify.org").text.strip()
        logging.info(f"IP erkannt: {ip}")
        return ip
    except Exception as e:
        logging.error(f"IP konnte nicht abgerufen werden: {e}")
        return None

# ───── AES-256 Verschlüsselung ─────
def encrypt_aes256(plaintext, password):
    backend = default_backend()
    key = hashes.Hash(hashes.SHA256(), backend)
    key.update(password.encode())
    aes_key = key.finalize()

    iv = os.urandom(16)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_data) + encryptor.finalize()

    result = base64.b64encode(iv + ct).decode()
    logging.info("AES-256 Verschlüsselung abgeschlossen.")
    return result

# ───── Rotationsverschlüsselung (ROT+7) ─────
def rotation_encrypt(text, offset=7):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rotated = chr((ord(char) - base + offset) % 26 + base)
            result.append(rotated)
        else:
            result.append(char)
    return ''.join(result)

# ───── Nachricht in Bild verstecken ─────
def embed_in_image(image_path, secret_data, output_suffix="_VERSTECKTE_IP.png"):
    output_path = Path(image_path).with_name(Path(image_path).stem + output_suffix)
    try:
        lsb.hide(str(image_path), secret_data).save(str(output_path))
        logging.info(f"Nachricht erfolgreich eingebettet: {output_path}")
        print(f"✅ Erfolgreich gespeichert als: {output_path}")
    except Exception as e:
        logging.error(f"Fehler beim Einbetten: {e}")
        print("❌ Fehler beim Einbetten der Daten ins Bild.")

# ───── Passwortprüfung ─────
def validate_password(password):
    if len(password) < 20 or not any(c in "!@#$%^&*()-_=+[{]}|;:',<.>/?~" for c in password):
        print("❗ Passwort nicht stark genug! Abbruch.")
        sys.exit(1)

# ───── Hauptfunktion ─────
def main():
    print("🌐 IP-Cloak Trinity Initialisierung ...")
    image_path = input("📂 Pfad zu einem Bild (.png/.jpg): ").strip().strip('"').strip("'")
    if not Path(image_path).exists():
        print("❌ Bildpfad ungültig.")
        return

    ip = get_public_ip()
    if not ip:
        print("❌ Keine IP erkannt.")
        return

    password = getpass("🔑 Starkes Passwort eingeben (min. 20 Zeichen, Sonderzeichen empfohlen): ")
    validate_password(password)

    print("🔒 Starte Verschlüsselungsschritte ...")
    encrypted = encrypt_aes256(ip, password)
    rotated = rotation_encrypt(encrypted)
    embed_in_image(image_path, rotated)

if __name__ == "__main__":
    main()
