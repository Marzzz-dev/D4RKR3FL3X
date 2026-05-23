#!/bin/bash
# =============================================
# DarkReflex Pro - Auto Installer
# =============================================

clear
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║   ██████╗  █████╗ ██████╗ ██╗  ██╗██████╗ ███████╗██╗         ║"
echo "║   ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔════╝██║         ║"
echo "║   ██║  ██║███████║██████╔╝█████╔╝ ██████╔╝█████╗  ██║         ║"
echo "║   ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██╗██╔══╝  ██║         ║"
echo "║   ██████╔╝██║  ██║██║  ██║██║  ██╗██████╔╝███████╗███████╗     ║"
echo "║   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝     ║"
echo "║                                                               ║"
echo "║              DARKREFLEX PRO - INSTALLER                       ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Cek Termux
if [ -d "/data/data/com.termux" ]; then
    echo "[✓] Termux detected"
    pkg update && pkg upgrade -y
    pkg install python -y
else
    echo "[!] Bukan Termux, install python biasa"
    if command -v apt &>/dev/null; then
        sudo apt update && sudo apt install python3 -y
    elif command -v pkg &>/dev/null; then
        pkg install python -y
    fi
fi

# Install dependencies
echo "[*] Installing Python dependencies..."
pip install requests

# Selesai
echo ""
echo "[✓] DarkReflex Pro installed successfully!"
echo "[*] Run: python darkreflex.py"
echo ""
