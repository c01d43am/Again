import subprocess
import os
from index import install_tool  # Ensure install_tool function is properly imported

#-------------------------------------------------------------------------------------------------------------
# Function to automate the selected tool
def automate_tool(tool_choice):
    tool_functions = {
        "1": start_nessus,
        "2": start_armitage,
        "3": start_akto,
        "4": start_gobuster
    }
    
    selected_function = tool_functions.get(tool_choice)
    if selected_function:
        selected_function()
    else:
        print("Invalid choice, please try again.")

#-------------------------------------------------------------------------------------------------------------
# Nessus Automation with subcategories
def start_nessus():
    print("\n[+] Automating Nessus...\n")
    install_tool("nessusd", "nessus")  # Ensure Nessus is installed

    try:
        # Check if Nessus service is running
        service_status = subprocess.run("systemctl is-active nessusd", shell=True, capture_output=True, text=True)
        if service_status.stdout.strip() != "active":
            print("[+] Starting Nessus service...")
            subprocess.run(["sudo", "systemctl", "start", "nessusd"], check=True)
            print("[+] Nessus service started. Access it via https://127.0.0.1:8834")
        else:
            print("[+] Nessus service is already running. Access it via https://127.0.0.1:8834")

        # Check Nessus server status
        server_status = subprocess.run(["curl", "-k", "https://127.0.0.1:8834/server/status"], capture_output=True, text=True)
        if server_status.returncode == 0:
            print("[+] Nessus server status:", server_status.stdout.strip())
        else:
            print("[-] Failed to get Nessus server status.")

        # Update Nessus
        print("[+] Updating Nessus...")
        subprocess.run(["sudo", "/opt/nessus/sbin/nessuscli", "update"], check=True)
        print("[+] Nessus has been updated.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error while starting or updating Nessus: {e}")

#-------------------------------------------------------------------------------------------------------------
# Armitage Automation with subcategories
def start_armitage():
    print("\n[+] Automating Armitage...\n")
    install_tool("armitage", "armitage")  # Ensure Armitage is installed

    try:
        subprocess.Popen(["armitage"])
        print("[+] Armitage has been started. Please wait for the GUI to appear.\n")
    except Exception as e:
        print(f"[-] Error starting Armitage: {e}")

#-------------------------------------------------------------------------------------------------------------
# Akto Automation with subcategories
def start_akto():
    print("\n[+] Automating Akto...\n")
    akto_path = os.path.expanduser("~/akto")  # Ensure ~ is expanded correctly
    original_dir = os.getcwd()  # Save current directory

    try:
        if not os.path.isdir(akto_path):
            print("[+] Akto not found. Installing...\n")
            subprocess.run(["git", "clone", "https://github.com/akto-api-security/akto.git", akto_path], check=True)

        os.chdir(akto_path)  # Change to Akto directory
        print("[+] Starting Akto using Docker Compose...")
        subprocess.run(["docker-compose", "up", "-d"], check=True)
        print("[+] Akto has been started. Access it via http://127.0.0.1:9090\n")
    except Exception as e:
        print(f"[-] Error during Akto installation or startup: {e}")
    finally:
        os.chdir(original_dir)  # Restore original directory

#-------------------------------------------------------------------------------------------------------------
# Gobuster Automation with subcategories
def start_gobuster():
    print("\n[+] Automating Gobuster...\n")

    if not is_gobuster_installed():
        install_gobuster()

    target_url = input("[+] Enter target URL for Gobuster: ").strip()
    if target_url:
        run_gobuster(target_url)
    else:
        print("[-] Invalid URL entered.")

def is_gobuster_installed():
    """Check if gobuster is installed."""
    try:
        subprocess.run(["gobuster", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def install_gobuster():
    """Install gobuster if not installed."""
    print("[+] Installing Gobuster...")
    subprocess.run(["sudo", "apt", "update"], check=True)
    subprocess.run(["sudo", "apt", "install", "-y", "gobuster"], check=True)

def run_gobuster(target_url, wordlist="/usr/share/wordlists/dirb/common.txt"):
    """Run gobuster with the given target URL and wordlist."""
    print(f"[+] Running Gobuster on {target_url}...")
    subprocess.run(["gobuster", "dir", "-u", target_url, "-w", wordlist], check=True)

#-------------------------------------------------------------------------------------------------------------
# Submenu for Automation Category
def automation_submenu():
    while True:
        print("\nAutomation Options:")
        print("1. Nessus")
        print("2. Armitage")
        print("3. Akto")
        print("4. Gobuster")
        print("5. Back to main menu")
        
        tool_choice = input("[+] Enter your choice [1-5]: ").strip()
        if tool_choice == "5":
            break
        else:
            automate_tool(tool_choice)  # Automate the selected tool
            print()  # New line for clarity
