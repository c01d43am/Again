# Description: This file contains the functions to automate the selected tool.
# The automate_tool function takes the user's choice and calls the appropriate function to automate the selected tool.
# The start_nessus function automates Nessus by checking the service status, starting the service if not running, updating Nessus, and displaying the server status.
# The start_armitage function automates Armitage by starting the Armitage GUI.
import subprocess
import os
from Again.scan import install_tool
#-------------------------------------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------------------------------------
# Nessus Automation with subcategories
import subprocess
def start_nessus():
    print("Checking for Nessus installation...")
    check_install = subprocess.run("which nessusd", shell=True, capture_output=True, text=True)
    
    if check_install.returncode != 0:
        print("Nessus is not installed. Installing now...")
        subprocess.run("wget https://www.tenable.com/downloads/api/v2/pages/nessus/files/Nessus-10.7.2-debian10_amd64.deb", shell=True, check=True)
        subprocess.run("sudo dpkg -i Nessus-10.7.2-debian10_amd64.deb", shell=True, check=True)
        print("Nessus installed. You may need to start the service manually.")
    else:
        print("Nessus is already installed.")

start_nessus()

#-------------------------------------------------------------------------------------------------------------
# Armitage Automation with subcategories
def start_armitage():
    print("\nAutomating Armitage...\n")
    install_tool("armitage", "armitage")  # Ensure Armitage is installed
    try:
        subprocess.Popen(["armitage"])
        print("Armitage has been started. Please wait for the GUI to appear.\n")
    except Exception as e:
        print(f"Error starting Armitage: {e}")
#-------------------------------------------------------------------------------------------------------------
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