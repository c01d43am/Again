# Description: This file contains the functions to automate the selected tool.
# The automate_tool function takes the user's choice and calls the appropriate function to automate the selected tool.
# Each function ensures the tool is installed before running.

import subprocess
import os
import sys
import shutil

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ..Support.install_tool import install_tool

# Function to automate the selected tool
def automate_tool(tool_choice):
    if tool_choice == "1":
        start_nessus()
    elif tool_choice == "2":
        start_armitage()
    elif tool_choice == "3":
        start_akto()
    else:
        print("Invalid choice, please try again.")

# Nessus Automation
def start_nessus():
    print("\nAutomating Nessus...\n")
    
    if not shutil.which("nessusd"):
        print("Nessus not found. Installing...\n")
        install_tool("nessusd", "nessus")  # Ensure Nessus is installed
    
    try:
        # Start Nessus service
        subprocess.run(["sudo", "systemctl", "start", "nessusd"], check=True)
        print("Nessus service started. Access it via https://127.0.0.1:8834")

        # Check Nessus server status
        server_status = subprocess.run(["curl", "-k", "https://127.0.0.1:8834/server/status"], capture_output=True, text=True)
        if server_status.returncode == 0:
            print("Nessus server status:", server_status.stdout)
        else:
            print("Failed to get Nessus server status.")

        # Update Nessus
        print("Updating Nessus...")
        subprocess.run(["sudo", "/opt/nessus/sbin/nessuscli", "update"], check=True)
        print("Nessus has been updated.")
    
    except subprocess.CalledProcessError as e:
        print(f"Error while starting or updating Nessus: {e}")

# Armitage Automation
def start_armitage():
    print("\nAutomating Armitage...\n")
    
    if not shutil.which("armitage"):
        print("Armitage not found. Installing...\n")
        install_tool("armitage", "armitage")  # Ensure Armitage is installed

    try:
        subprocess.Popen(["armitage"])
        print("Armitage has been started. Please wait for the GUI to appear.\n")
    except Exception as e:
        print(f"Error starting Armitage: {e}")

# Akto Automation
def start_akto():
    print("\nAutomating Akto...\n")
    akto_path = os.path.expanduser("~/akto")  # Ensure ~ is expanded correctly
    
    if not os.path.isdir(akto_path):
        print("Akto not found. Installing...\n")
        try:
            # Clone Akto repository
            os.system(f"git clone https://github.com/akto-api-security/akto.git {akto_path}")
            
            # Change to the Akto directory and start Akto
            os.chdir(akto_path)
            os.system("docker-compose up -d")  # Install and start Akto via Docker Compose
            print("Akto has been installed and started.\n")
        except Exception as e:
            print(f"Error during Akto installation or startup: {e}")
    else:
        print("Akto is already installed.\n")
    print("Akto has been started. Please access it via http://127.0.0.1:9090\n")

# Submenu for Automation Category
def automation_submenu():
    while True:
        print("\nAutomation Options:")
        print("1. Nessus")
        print("2. Armitage")
        print("3. Akto")
        print("4. Back to main menu")
        
        tool_choice = input("Enter your choice [1-4]: ")
        if tool_choice == "4":
            break
        else:
            automate_tool(tool_choice)  # Automate the selected tool
            print()  # New line for clarity
