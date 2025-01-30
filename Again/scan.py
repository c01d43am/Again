import subprocess
import os

# General function to check and install a tool
def install_tool(tool_name, package_name=None, post_install_cmd=None):
    if package_name is None:
        package_name = tool_name

    try:
        # Check if the tool is installed
        result = subprocess.run(f"which {tool_name}", shell=True, capture_output=True)
        if result.returncode != 0:
            print(f"{tool_name} not found. Installing...")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", package_name], check=True)
            print(f"{tool_name} installed successfully.")
            if post_install_cmd:
                subprocess.run(post_install_cmd, shell=True, check=True)
        else:
            print(f"{tool_name} is already installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error while installing {tool_name}: {e}")

# Function to start OpenVAS
def start_openvas():
    install_tool("gvm-start", "gvm")
    print("Starting OpenVAS...")
    try:
        subprocess.run(["sudo", "gvm-start"], check=True)
        print("OpenVAS started. Access it via https://127.0.0.1:9392")
    except subprocess.CalledProcessError as e:
        print(f"Error starting OpenVAS: {e}")

# Function to start Nessus
def start_nessus():
    try:
        # Check if Nessus is installed
        result = subprocess.run("which nessusd", shell=True, capture_output=True)
        if result.returncode != 0:
            print("Nessus not installed. Installing...")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", "nessus"], check=True)
            subprocess.run(["sudo", "/opt/nessus/sbin/nessuscli", "fetch", "--register"], check=True)
            subprocess.run(["sudo", "systemctl", "enable", "nessusd"], check=True)
            print("Nessus installed and configured.")
        else:
            print("Nessus is already installed.")

        # Check if Nessus service is running
        service_status = subprocess.run("systemctl is-active nessusd", shell=True, capture_output=True)
        if service_status.returncode != 0:
            print("Starting Nessus service...")
            subprocess.run(["sudo", "systemctl", "start", "nessusd"], check=True)
            print("Nessus service started. Access it via https://127.0.0.1:8834")
        else:
            print("Nessus service is already running. Access it via https://127.0.0.1:8834")
    except subprocess.CalledProcessError as e:
        print(f"Error while installing or starting Nessus: {e}")
# Akto Automation with subcategories
def start_akto():
    print(f"Checking if {start_akto} is installed...\n")
    
    if start_akto == "akto":
        # Check for Akto installation and install it if not present
        akto_path = os.path.expanduser("~/akto")  # Ensure ~ is expanded correctly
        
        if not os.path.isdir(akto_path):
            print(f"Akto not found. Installing...\n")
            try:
                # Clone Akto repository
                os.system(f"git clone https://github.com/akto-api-security/akto.git {akto_path}")
                
                # Change to the Akto directory and start Akto
                os.chdir(akto_path)
                os.system("docker-compose up -d")  # Install and start Akto via Docker Compose
                print(f"Akto has been installed and started.\n")
            except Exception as e:
                print(f"Error during Akto installation or startup: {e}")
        else:
            print(f"Akto is already installed.\n")
        
    else:
        print(f"Installation check for {start_akto}...\n")
        

# Function to start Armitage
def start_armitage():
    install_tool("armitage", "armitage")
    print("Starting Armitage...")
    try:
        subprocess.Popen(["armitage"])
        print("Armitage started. Please wait for the GUI to appear.")
    except Exception as e:
        print(f"Error starting Armitage: {e}")
# Function to automate the selected tool
def automate_tool(tool_choice):
    if tool_choice == "1":
        start_openvas()
    elif tool_choice == "2":
        start_nessus()
    elif tool_choice == "3":
        start_armitage()
    else:
        print("Invalid choice, please try again.")

# OpenVAS Automation with subcategories
def start_openvas():
    print("\nAutomating OpenVAS...\n")
    install_tool("gvm-start", "gvm")  # Ensure OpenVAS is installed
    start_openvas()  # Start OpenVAS
    print("OpenVAS has been started and is accessible via https://127.0.0.1:9392\n")

# Nessus Automation with subcategories
def start_nessus():
    print("\nAutomating Nessus...\n")
    install_tool("nessusd", "nessus")  # Ensure Nessus is installed
    start_nessus()  # Start Nessus
    print("Nessus has been started and is accessible via https://127.0.0.1:8834\n")

# Armitage Automation with subcategories
def start_armitage():
    print("\nAutomating Armitage...\n")
    install_tool("armitage", "armitage")  # Ensure Armitage is installed
    start_armitage()  # Start Armitage
    print("Armitage has been started. Please wait for the GUI to appear.\n")


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
