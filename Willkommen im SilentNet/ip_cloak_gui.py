# ip_cloak_gui.py
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
from stegano import lsb
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64, os, requests, logging

# ───── Logger vorbereiten ─────
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)
logging.basicConfig(filename=log_dir / "ip_cloak_gui.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# ───── AES + ROT Verschlüsselung ─────
def get_ip():
    try:
        return requests.get("https://api.ipify.org").text.strip()
    except:
        return "FEHLER"

def validate_password(pw):
    return len(pw) >= 20 and any(c in "!@#$%^&*()-_=+[{]}|;:',<.>/?~" for c in pw)

def aes_encrypt(text, password):
    backend = default_backend()
    key = hashes.Hash(hashes.SHA256(), backend)
    key.update(password.encode())
    aes_key = key.finalize()
    iv = os.urandom(16)
    padder = padding.PKCS7(128).padder()
    padded = padder.update(text.encode()) + padder.finalize()
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=backend)
    ct = cipher.encryptor().update(padded) + cipher.encryptor().finalize()
    return base64.b64encode(iv + ct).decode()

def aes_decrypt(b64, password):
    backend = default_backend()
    key = hashes.Hash(hashes.SHA256(), backend)
    key.update(password.encode())
    aes_key = key.finalize()
    data = base64.b64decode(b64)
    iv, ct = data[:16], data[16:]
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=backend)
    decrypted = cipher.decryptor().update(ct) + cipher.decryptor().finalize()
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(decrypted) + unpadder.finalize()

def rot_encrypt(text, shift=7):
    return ''.join(chr((ord(c) + shift) % 256) for c in text)

def rot_decrypt(text, shift=7):
    return ''.join(chr((ord(c) - shift) % 256) for c in text)

# ───── GUI Logik ─────
def encode():
    pfad = Path(input_path.get().strip())
    pw = password.get()
    if not pfad.exists():
        messagebox.showerror("Fehler", "⚠️ Das Bild existiert nicht.")
        return
    if not validate_password(pw):
        messagebox.showwarning("Schwach", "Passwort muss ≥ 20 Zeichen & Sonderzeichen enthalten.")
        return
    ip = get_ip()
    encrypted = aes_encrypt(ip, pw)
    rotated = rot_encrypt(encrypted)
    try:
        out_dir = Path("encoded_ips")
        out_dir.mkdir(exist_ok=True)
        out_file = out_dir / (pfad.stem + "_VERSTECKTE_IP.png")
        lsb.hide(str(pfad), rotated).save(str(out_file))
        messagebox.showinfo("Erfolg", f"Bild gespeichert:\n{out_file}")
        logging.info(f"IP verschlüsselt in: {out_file}")
    except Exception as e:
        messagebox.showerror("Fehler", str(e))

def decode():
    pfad = Path(decode_path.get().strip())
    pw = password.get()
    if not pfad.exists():
        messagebox.showerror("Fehler", "⚠️ Das Bild existiert nicht.")
        return
    try:
        hidden = lsb.reveal(str(pfad))
        if not hidden:
            raise ValueError("Impossible to detect message.")
        rotated = rot_decrypt(hidden)
        original = aes_decrypt(rotated, pw).decode()
        messagebox.showinfo("Erfolg", f"IP entschlüsselt:\n{original}")
        logging.info(f"IP entschlüsselt: {original}")
    except Exception as e:
        messagebox.showerror("Fehlgeschlagen", f"Fehler: {e}")
        logging.error(f"Entschlüsselung fehlgeschlagen: {e}")

# ───── GUI Aufbau ─────
root = tk.Tk()
root.title("🛡️ QuantumShield: IP-Cloak GUI")
notebook = ttk.Notebook(root)
frame_enc = ttk.Frame(notebook)
frame_dec = ttk.Frame(notebook)
notebook.add(frame_enc, text="🔐 IP verschlüsseln")
notebook.add(frame_dec, text="🔓 IP entschlüsseln")
notebook.pack(expand=True, fill='both')

input_path = tk.StringVar()
decode_path = tk.StringVar()
password = tk.StringVar()

ttk.Label(frame_enc, text="📂 Bild zum Einbetten auswählen").pack(pady=5)
ttk.Entry(frame_enc, textvariable=input_path, width=60).pack()
ttk.Button(frame_enc, text="Durchsuchen", command=lambda: input_path.set(filedialog.askopenfilename())).pack(pady=5)
ttk.Label(frame_enc, text="🔑 Starkes Passwort (mind. 20 Zeichen)").pack()
ttk.Entry(frame_enc, textvariable=password, show="*", width=40).pack(pady=5)
ttk.Button(frame_enc, text="💎 Tarnen & Speichern", command=encode).pack(pady=10)

ttk.Label(frame_dec, text="📂 Bild mit versteckter IP wählen").pack(pady=5)
ttk.Entry(frame_dec, textvariable=decode_path, width=60).pack()
ttk.Button(frame_dec, text="Durchsuchen", command=lambda: decode_path.set(filedialog.askopenfilename())).pack(pady=5)
ttk.Label(frame_dec, text="🔑 Passwort zum Entschlüsseln").pack()
ttk.Entry(frame_dec, textvariable=password, show="*", width=40).pack(pady=5)
ttk.Button(frame_dec, text="🔍 Enttarnen & Anzeigen", command=decode).pack(pady=10)

root.mainloop()
