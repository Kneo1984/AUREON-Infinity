from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os, json, base64

# ───── Schlüsselpaar erzeugen ─────
def generate_keypair():
    priv = x25519.X25519PrivateKey.generate()
    pub = priv.public_key()
    return priv, pub

# ───── AES-Schlüssel aus Shared Key ableiten ─────
def derive_aes_key(shared_key: bytes) -> bytes:
    return HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"quantum-ipcloak",
    ).derive(shared_key)

# ───── Export/Import Funktionen ─────
def export_key(key, private=False):
    if private:
        raw = key.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw,
            encryption_algorithm=serialization.NoEncryption()
        )
    else:
        raw = key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
    return base64.b64encode(raw).decode()

def load_key(b64, private=False):
    raw = base64.b64decode(b64)
    if private:
        return x25519.X25519PrivateKey.from_private_bytes(raw)
    return x25519.X25519PublicKey.from_public_bytes(raw)

# ───── JSON speichern/laden ─────
def save_keys(filepath, privkey, pubkey):
    with open(filepath, "w") as f:
        json.dump({
            "private_key": export_key(privkey, True),
            "public_key": export_key(pubkey)
        }, f, indent=2)

def load_keys(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return load_key(data["private_key"], True), load_key(data["public_key"])

# ───── AES-Verschlüsselung ─────
def encrypt_aes(text, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    pad_len = 16 - len(text.encode()) % 16
    padded = text.encode() + bytes([pad_len] * pad_len)
    ct = encryptor.update(padded) + encryptor.finalize()
    return base64.b64encode(iv + ct).decode()

def decrypt_aes(b64, key):
    raw = base64.b64decode(b64)
    iv, ct = raw[:16], raw[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decrypted = cipher.decryptor().update(ct) + cipher.decryptor().finalize()
    pad_len = decrypted[-1]
    return decrypted[:-pad_len].decode()

# ───── Haupttest ─────
if __name__ == "__main__":
    print("🔐 Starte QuantumShield Core...")
    
    # Keypair erzeugen & speichern
    priv, pub = generate_keypair()
    save_keys("quantum_identity.json", priv, pub)

    # Keypair laden (simuliert Empfänger)
    receiver_pub = load_key(export_key(pub))
    shared = priv.exchange(receiver_pub)
    aes_key = derive_aes_key(shared)

    msg = "192.168.0.143"
    encrypted = encrypt_aes(msg, aes_key)
    decrypted = decrypt_aes(encrypted, aes_key)

    print("\n🔎 Ergebnis:")
    print(f"🧠 Original-IP:          {msg}")
    print(f"📦 Verschlüsselt (b64): {encrypted}")
    print(f"🧩 Entschlüsselt:        {decrypted}")
