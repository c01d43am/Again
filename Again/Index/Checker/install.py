import subprocess
import shutil
import os

# List of tools to install/update
TOOLS = [
    "nessus",
    "armitage",
    "akto",
    "dirb",
    "sslscan",
    "feroxbuster",
    "gobuster",
    "nmap",
    "nikto",
    "skipfish",
    "sqlmap"
]

# Tools installed via GitHub (Require 'git pull' for updates)
GIT_TOOLS = {
    "akto": "~/akto",
    "armitage": "/usr/share/armitage"
}

def run_command(command):
    """Run a shell command and return success status."""
    try:
        subprocess.run(command, check=True, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

def detect_package_manager():
    """Detect available package manager."""
    if shutil.which("apt"):
        return "apt"
    elif shutil.which("pacman"):
        return "pacman"
    elif shutil.which("brew"):
        return "brew"
    return None

def install_or_update_tool(tool):
    """Install or update a tool."""
    package_manager = detect_package_manager()

    if not package_manager:
        print(f"[-] No supported package manager found for {tool}. Install manually.")
        return False

    # If the tool is in GIT_TOOLS, perform git pull
    if tool in GIT_TOOLS:
        tool_path = os.path.expanduser(GIT_TOOLS[tool])
        if os.path.exists(tool_path):
            print(f"[+] Updating {tool} via Git pull...")
            if run_command(f"cd {tool_path} && git pull"):
                print(f"[+] {tool} updated successfully!\n")
                return True
            else:
                print(f"[-] Failed to update {tool}. Check manually.\n")
                return False
        else:
            print(f"[-] {tool} not found. Installing from GitHub...\n")
            return install_git_tool(tool, tool_path)

    print(f"[+] Checking {tool} installation status...")
    if shutil.which(tool):
        print(f"[+] {tool} is already installed. Updating...\n")
        update_cmd = ""
        if package_manager == "apt":
            update_cmd = f"sudo apt upgrade -y {tool}"
        elif package_manager == "pacman":
            update_cmd = f"sudo pacman -Syu --noconfirm {tool}"
        elif package_manager == "brew":
            update_cmd = f"brew upgrade {tool}"

        if run_command(update_cmd):
            print(f"[+] {tool} updated successfully!\n")
            return True
        else:
            print(f"[-] Failed to update {tool}. Try manually.\n")
            return False
    else:
        print(f"[-] {tool} not installed. Installing...\n")
        return install_tool(tool)

def install_tool(tool):
    """Install a tool using the appropriate package manager."""
    package_manager = detect_package_manager()
    
    if package_manager == "apt":
        run_command("sudo apt update")
        install_cmd = f"sudo apt install -y {tool}"
    elif package_manager == "pacman":
        install_cmd = f"sudo pacman -Sy --noconfirm {tool}"
    elif package_manager == "brew":
        install_cmd = f"brew install {tool}"
    else:
        print(f"[-] No package manager found. Cannot install {tool}.")
        return False

    if run_command(install_cmd):
        print(f"[+] {tool} installed successfully!\n")
        return True
    else:
        print(f"[-] Failed to install {tool}. Try manually.\n")
        return False

def install_git_tool(tool, tool_path):
    """Install a Git-based tool."""
    git_repos = {
        "akto": "https://github.com/akto-api-security/akto.git",
        "armitage": "https://github.com/rsmudge/armitage.git"
    }

    if tool in git_repos:
        print(f"[+] Cloning {tool} from {git_repos[tool]}...\n")
        if run_command(f"git clone {git_repos[tool]} {tool_path}"):
            print(f"[+] {tool} installed successfully.\n")
            return True
        else:
            print(f"[-] Failed to clone {tool}. Try manually.\n")
            return False
    else:
        print(f"[-] No Git repository found for {tool}.")
        return False

def install_and_update_all_tools():
    """Install and update all required tools."""
    print("[+] Starting installation & update process...\n")
    for tool in TOOLS:
        install_or_update_tool(tool)
    print("[+] All tools installed and updated successfully.")

if __name__ == "__main__":
    install_and_update_all_tools()
