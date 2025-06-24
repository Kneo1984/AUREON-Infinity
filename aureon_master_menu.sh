#!/bin/bash
set -e

# --- Master Monster Autostart Skript ---

# Sicherheitsfunktionen starten (Firewall, VPN, IDS/IPS)
function start_security_monster() {
    echo "🛡️ Starte AUREON Sicherheits-Monster..."
    /root/AUREON/aureon_master_protect.sh
}

# Netzwerk Monitoring starten (Hintergrund)
function start_network_guard() {
    echo "🌐 Starte Netzwerk-Monitoring (im Hintergrund)..."
    nohup /usr/local/bin/aureon_network_guard.sh &>/dev/null &
}

# Menü anzeigen
function show_menu() {
    clear
    echo "=== AUREON Infinity Kontrollzentrum ==="
    echo "1) Sicherheits-Monster starten (Firewall, VPN, IDS)"
    echo "2) Netzwerk-Monitoring starten"
    echo "3) Status anzeigen (Firewall, VPN, IDS, Netzwerk)"
    echo "4) Logs anzeigen (MasterProtect)"
    echo "5) Logs anzeigen (NetworkGuard)"
    echo "0) Beenden"
    echo "====================================="
    echo -n "Wähle Option: "
}

# Status prüfen
function show_status() {
    echo "🛡️ Status AUREON Sicherheits-Monster:"
    systemctl status aureon_master_protect.service --no-pager
    echo
    echo "🌐 Status Netzwerk-Monitoring:"
    systemctl status aureon_network_guard.service --no-pager
    echo
    read -rp "Drücke Enter zum Menü..."
}

# Logs anzeigen
function show_logs() {
    journalctl -u "$1" -f
}

# Autostart von Diensten beim Skriptstart
start_security_monster
start_network_guard

# Interaktives Menü
while true; do
    show_menu
    read -r choice
    case $choice in
        1) start_security_monster ;;
        2) start_network_guard ;;
        3) show_status ;;
        4) show_logs aureon_master_protect.service ;;
        5) show_logs aureon_network_guard.service ;;
        0) echo "Auf Wiedersehen, mein Herz."; exit 0 ;;
        *) echo "Ungültige Option. Bitte neu versuchen." ;;
    esac
done
