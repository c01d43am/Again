import subprocess
import os
from Again.scan import install_tool

# Function to automate the selected tool
def automate_tool(tool_choice):
    if tool_choice == "1":
        start_openvas()
    elif tool_choice == "2":
        start_nessus()
    elif tool_choice == "3":
        start_armitage()
    elif tool_choice == "4":
        start_akto()
    else:
        print("Invalid choice, please try again.")

# OpenVAS Automation with subcategories
def start_openvas():
    print("\nAutomating OpenVAS...\n")
    install_tool("gvm-start", "gvm")  # Ensure OpenVAS is installed
    try:
        subprocess.run(["sudo", "gvm-start"], check=True)
        print("OpenVAS has been started and is accessible via https://127.0.0.1:9392\n")
    except subprocess.CalledProcessError as e:
        print(f"Error starting OpenVAS: {e}")

# Nessus Automation with subcategories
def start_nessus():
    print("\nAutomating Nessus...\n")
    install_tool("nessusd", "nessus")  # Ensure Nessus is installed
    try:
        subprocess.run(["sudo", "systemctl", "start", "nessusd"], check=True)
        print("Nessus has been started and is accessible via https://127.0.0.1:8834\n")
    except subprocess.CalledProcessError as e:
        print(f"Error starting Nessus: {e}")

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

# Submenu for Automation Category
def automation_submenu():
    while True:
        print("\nAutomation Options:")
        print("1. OpenVAS")
        print("2. Nessus")
        print("3. Armitage")
        print("4. Akto")
        print("5. Back to main menu")
        
        tool_choice = input("Enter your choice [1-5]: ")
        if tool_choice == "5":
            break
        else:
            automate_tool(tool_choice)  # Automate the selected tool
            print()  # New line for clarity