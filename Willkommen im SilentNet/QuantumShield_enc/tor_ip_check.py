import requests

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

try:
    response = requests.get("https://api.ipify.org", proxies=proxies, timeout=10)
    print("🟢 Deine aktuelle (versteckte) IP über Tor ist:", response.text)
except Exception as e:
    print("🔴 Fehler beim Abrufen der IP über Tor:", e)
