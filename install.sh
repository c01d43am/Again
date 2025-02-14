#!/bin/bash

# List of tools to install/update
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

# GitHub-based tools (Require git pull)
declare -A GIT_TOOLS
GIT_TOOLS["akto"]="https://github.com/akto-api-security/akto.git"
GIT_TOOLS["armitage"]="https://github.com/rsmudge/armitage.git"

# Detect package manager
detect_package_manager() {
    if command -v apt &>/dev/null; then
        echo "apt"
    elif command -v pacman &>/dev/null; then
        echo "pacman"
    elif command -v brew &>/dev/null; then
        echo "brew"
    else
        echo "none"
    fi
}

# Install or update a tool
install_or_update_tool() {
    local tool=$1
    local package_manager=$(detect_package_manager)

    if [[ -n "${GIT_TOOLS[$tool]}" ]]; then
        install_or_update_git_tool "$tool"
        return
    fi

    if command -v "$tool" &>/dev/null; then
        echo "[+] $tool is already installed. Updating..."
        case $package_manager in
            apt) sudo apt upgrade -y "$tool" ;;
            pacman) sudo pacman -Syu --noconfirm "$tool" ;;
            brew) brew upgrade "$tool" ;;
            *) echo "[-] No package manager found for $tool." ;;
        esac
    else
        echo "[-] $tool not found. Installing..."
        install_tool "$tool"
    fi
}

# Install a tool using the package manager
install_tool() {
    local tool=$1
    local package_manager=$(detect_package_manager)

    case $package_manager in
        apt)
            sudo apt update && sudo apt install -y "$tool"
            ;;
        pacman)
            sudo pacman -Sy --noconfirm "$tool"
            ;;
        brew)
            brew install "$tool"
            ;;
        *)
            echo "[-] No supported package manager found for $tool."
            ;;
    esac
}

# Install or update GitHub-based tools
install_or_update_git_tool() {
    local tool=$1
    local repo="${GIT_TOOLS[$tool]}"
    local tool_dir="$HOME/$tool"

    if [[ -d "$tool_dir" ]]; then
        echo "[+] Updating $tool via git pull..."
        (cd "$tool_dir" && git pull)
    else
        echo "[-] $tool not found. Cloning from GitHub..."
        git clone "$repo" "$tool_dir"
    fi
}

# Install and update all tools
install_and_update_all_tools() {
    echo "[+] Starting installation & update process..."
    for tool in "${TOOLS[@]}"; do
        install_or_update_tool "$tool"
    done
    echo "[+] All tools installed and updated successfully!"
}

# Run the script
install_and_update_all_tools
