import os, json, base64, requests
from tkinter import Tk, filedialog, messagebox, ttk
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from stegano import lsb
from start_tor import start_tor

# ========= Hilfsfunktionen =========
def get_public_ip():
    try:
        proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        return requests.get("https://api.ipify.org", proxies=proxies, timeout=10).text.strip()
    except Exception as e:
        print(f"❌ Fehler beim IP-Check über Tor: {e}")
        return "0.0.0.0"

def derive_key(shared_key):
    return HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"Quantum-IP-Cloak",
    ).derive(shared_key)

def encrypt_message(key, plaintext):
    backend = default_backend()
    iv = os.urandom(16)
    pad_len = 16 - (len(plaintext) % 16)
    padded = plaintext + chr(pad_len) * pad_len
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded.encode()) + encryptor.finalize()
    return base64.b64encode(iv + ct).decode()

# ========= IP im Bild verstecken =========
def cloak_ip():
    try:
        with open(keyfile_var.get(), "r") as f:
            keys = json.load(f)

        priv = x25519.X25519PrivateKey.from_private_bytes(bytes.fromhex(keys["private"]))
        pub = x25519.X25519PublicKey.from_public_bytes(bytes.fromhex(keys["public"]))

        shared = priv.exchange(pub)
        aes_key = derive_key(shared)

        ip = ip_var.get().strip()
        encrypted = encrypt_message(aes_key, ip)

        img_path = image_var.get().strip()
        output = os.path.splitext(img_path)[0] + "_VERSTECKT.png"
        lsb.hide(img_path, encrypted).save(output)

        messagebox.showinfo("✅ Erfolg", f"IP versteckt in:\n{output}")
    except Exception as e:
        messagebox.showerror("❌ Fehler", str(e))

# ========= IP aus Bild extrahieren =========
def reveal_ip():
    try:
        img_path = filedialog.askopenfilename(title="Bild mit eingebetteter IP auswählen")
        if not img_path:
            return

        hidden = lsb.reveal(img_path)

        if hidden:
            messagebox.showinfo("🎯 Gefundene IP", f"Versteckte IP: {hidden}")
        else:
            messagebox.showwarning("⚠️ Hinweis", "Keine versteckte IP gefunden.")
    except Exception as e:
        messagebox.showerror("❌ Fehler", str(e))

# ========= GUI =========
root = Tk()
root.title("🌐 Quantum IP-Cloak GUI (X25519 + AES-256)")

frame = ttk.Frame(root, padding=20)
frame.pack()

keyfile_var = ttk.Entry(frame, width=70)
keyfile_var.pack()
ttk.Button(frame, text="📂 Schlüsseldatei (JSON)", command=lambda: keyfile_var.insert(0, filedialog.askopenfilename())).pack(pady=2)

image_var = ttk.Entry(frame, width=70)
image_var.pack()
ttk.Button(frame, text="🖼 Bild zum Einbetten", command=lambda: image_var.insert(0, filedialog.askopenfilename())).pack(pady=2)

ip_var = ttk.Entry(frame, width=40)
ip_var.insert(0, get_public_ip())
ip_var.pack(pady=10)

ttk.Button(frame, text="🧬 Verstecken & Speichern", command=cloak_ip).pack(pady=10)
ttk.Button(frame, text="🔍 IP aus Bild extrahieren", command=reveal_ip).pack(pady=5)

root.mainloop()
