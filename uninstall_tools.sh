#!/bin/bash

# Define the list of tools to uninstall
TOOLS=(
    "nessus"
    "armitage"
    "akto"
    "dirb"
    "sslscan"
    "feroxbuster"
    "gobuster"
    "nmap"
    "nikto"
    "skipfish"
    "sqlmap"
)

echo "[+] Starting uninstallation of tools..."

for tool in "${TOOLS[@]}"; do
    if command -v "$tool" &>/dev/null; then
        echo "[+] Uninstalling $tool..."
        sudo apt remove --purge -y "$tool" || sudo pacman -Rns --noconfirm "$tool" || brew uninstall "$tool"
    else
        echo "[-] $tool is not installed."
    fi
done

echo "[+] Cleaning up..."
sudo apt autoremove -y && sudo apt clean

echo "[+] Uninstallation complete!"
