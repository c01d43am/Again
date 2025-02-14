#!/bin/bash

# List of tools to check
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

# GitHub-based tools (Require directory check)
declare -A GIT_TOOLS
GIT_TOOLS["akto"]="$HOME/akto"
GIT_TOOLS["armitage"]="$HOME/armitage"

echo "[+] Checking installation status of tools..."

# Track missing tools
MISSING_TOOLS=()
FAILED_GIT_TOOLS=()

# Check each tool
for tool in "${TOOLS[@]}"; do
    if command -v "$tool" &>/dev/null; then
        echo "[✔] $tool is installed."
    else
        echo "[✘] $tool is NOT installed!"
        MISSING_TOOLS+=("$tool")
    fi
done

# Check GitHub-based tools
for tool in "${!GIT_TOOLS[@]}"; do
    if [[ -d "${GIT_TOOLS[$tool]}" ]]; then
        echo "[✔] $tool directory exists."
    else
        echo "[✘] $tool directory is missing!"
        FAILED_GIT_TOOLS+=("$tool")
    fi
done

# Print Summary
if [[ ${#MISSING_TOOLS[@]} -gt 0 ]] || [[ ${#FAILED_GIT_TOOLS[@]} -gt 0 ]]; then
    echo -e "\n[!] Installation Issues Found!"
    
    if [[ ${#MISSING_TOOLS[@]} -gt 0 ]]; then
        echo "Missing package-based tools:"
        for tool in "${MISSING_TOOLS[@]}"; do
            echo "  - $tool"
        done
    fi

    if [[ ${#FAILED_GIT_TOOLS[@]} -gt 0 ]]; then
        echo "Missing GitHub-based tools:"
        for tool in "${FAILED_GIT_TOOLS[@]}"; do
            echo "  - $tool"
        done
    fi
    exit 1
else
    echo -e "\n[✔] All tools are correctly installed!"
    exit 0
fi
