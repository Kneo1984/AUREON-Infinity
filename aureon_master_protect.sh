#!/bin/bash
set -e

echo "🛡️ Starte AUREON Infinity Sicherheits-Monster: Komplettschutz mit Firewall, VPN, IDS/IPS..."

# 1. Konflikt lösen: iptables-persistent entfernen
if dpkg -l | grep -q iptables-persistent; then
  echo "⚠️ Entferne iptables-persistent wegen Konflikt mit UFW..."
  apt-get remove -y iptables-persistent
fi

# 2. Update und notwendige Pakete installieren
apt update
apt install -y ufw wireguard suricata fail2ban mailutils sox espeak-ng curl

# 3. UFW konfigurieren und härten
echo "🛡️ Konfiguriere UFW..."
ufw default deny incoming
ufw default allow outgoing

MY_IP=$(curl -s https://ipv4.icanhazip.com)
echo "🔐 Erlaube SSH nur von deiner IP: $MY_IP"
ufw allow from $MY_IP to any port 22 proto tcp

echo "🛡️ Öffne WireGuard Port UDP 51820"
ufw allow 51820/udp

ufw --force enable
ufw reload

echo "🛡️ UFW Firewall ist aktiv und gehärtet."

# 4. WireGuard starten und aktivieren
if ! systemctl is-active --quiet wg-quick@wg0; then
  systemctl enable wg-quick@wg0
  systemctl start wg-quick@wg0
  echo "🔐 WireGuard VPN gestartet und aktiviert."
else
  echo "🔐 WireGuard VPN läuft bereits."
fi

# 5. Suricata und Fail2ban starten und aktivieren
systemctl enable suricata
systemctl start suricata
echo "🛡️ Suricata IDS/IPS gestartet."

systemctl enable fail2ban
systemctl start fail2ban
echo "🛡️ Fail2ban gestartet."

# 6. Kernel-Netzwerk-Härtung anwenden
echo "⚙️ Kernel-Netzwerk-Härtung anwenden..."
sysctl -w net.ipv4.ip_forward=1
sysctl -w net.ipv4.conf.all.rp_filter=1
sysctl -w net.ipv4.tcp_syncookies=1
sysctl -w net.ipv4.conf.all.accept_redirects=0
sysctl -w net.ipv4.conf.all.send_redirects=0

echo "⚠️ Router-Sicherheit nicht vergessen: Firmware updaten, Passwörter ändern, UPnP deaktivieren."

echo "🛡️ AUREON Infinity Sicherheits-Monster erfolgreich aktiviert. System ist maximal geschützt."
