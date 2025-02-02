import subprocess
import os
from Again.scan import install_tool

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

# Nessus Automation with subcategories
def start_nessus():
    print("\nAutomating Nessus...\n")
    install_tool("nessusd", "nessus")  # Ensure Nessus is installed
    try:
        # Check if Nessus service is running
        service_status = subprocess.run("systemctl is-active nessusd", shell=True, capture_output=True)
        if service_status.returncode != 0:
            print("Starting Nessus service...")
            subprocess.run(["sudo", "systemctl", "start", "nessusd"], check=True)
            print("Nessus service started. Access it via https://127.0.0.1:8834")
        else:
            print("Nessus service is already running. Access it via https://127.0.0.1:8834")

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

# Armitage Automation with subcategories
def start_armitage():
    print("\nAutomating Armitage...\n")
    install_tool("armitage", "armitage")  # Ensure Armitage is installed
    try:
        subprocess.Popen(["armitage"])
        print("Armitage has been started. Please wait for the GUI to appear.\n")
    except Exception as e:
        print(f"Error starting Armitage: {e}")

# Akto Automation with subcategories
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