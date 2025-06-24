#!/bin/bash
echo "🧠 AUREON STATUS"
echo "CPU: $(top -bn1 | grep 'Cpu(s)' | awk '{print $2 + $4}')%"
echo "RAM: $(free -m | awk '/Mem:/ { printf("%.2f%%", $3/$2*100) }')"
echo "Disk: $(df -h / | awk 'NR==2 { print $5 }')"
