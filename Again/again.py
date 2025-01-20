import subprocess

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

# Function to start Armitage
def start_armitage():
    install_tool("armitage", "armitage")
    print("Starting Armitage...")
    try:
        subprocess.Popen(["armitage"])
        print("Armitage started. Please wait for the GUI to appear.")
    except Exception as e:
        print(f"Error starting Armitage: {e}")

# Function to run a Nikto scan
def run_nikto_scan():
    install_tool("nikto", "nikto")
    target = input("Enter the target URL or IP: ").strip()
    if not target:
        print("Invalid target. Please enter a valid URL or IP address.")
        return
    print(f"Running Nikto scan on {target}...")
    try:
        subprocess.run(["nikto", "-h", target], check=True)
        print("Nikto scan completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error during Nikto scan: {e}")
