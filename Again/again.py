import subprocess

# Function to check and install required tools
def install_tool(tool_name, package_name=None, post_install_cmd=None):
    if package_name is None:
        package_name = tool_name

    if subprocess.call(f"which {tool_name}", shell=True) != 0:
        print(f"{tool_name} not found. Installing...")
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "-y", package_name])
        print(f"{tool_name} installed successfully.")

        if post_install_cmd:
            subprocess.run(post_install_cmd, shell=True)
    else:
        print(f"{tool_name} is already installed.")

# Function to start OpenVAS
def start_openvas():
    # Check if OpenVAS is installed, if not install it
    if subprocess.call("which gvm-start", shell=True) != 0:
        print("OpenVAS not installed. Installing...")
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "-y", "gvm"])
        print("OpenVAS installed successfully.")

    # Start OpenVAS service
    print("Starting OpenVAS...")
    subprocess.run(["sudo", "gvm-start"])
    print("OpenVAS started. Access it via https://127.0.0.1:9392")

# Function to start Nessus
def start_nessus():
    if subprocess.call("systemctl list-units --type=service | grep -q nessusd", shell=True) != 0:
        print("Nessus not installed. Installing...")
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "-y", "nessus"])
        subprocess.run(["sudo", "/opt/nessus/sbin/nessuscli", "fetch", "--register"])
        subprocess.run(["sudo", "systemctl", "enable", "nessusd"])
        print("Nessus installed and configured.")
    print("Starting Nessus...")
    subprocess.run(["sudo", "systemctl", "start", "nessusd"])
    print("Nessus service started. Access it via https://127.0.0.1:8834")

# Function to start Armitage
def start_armitage():
    install_tool("armitage", "armitage")
    print("Starting Armitage...")
    subprocess.Popen(["armitage"])
    print("Armitage started. Please wait for the GUI to appear.")

# Function to run a Nikto scan
def run_nikto_scan():
    install_tool("nikto", "nikto")
    target = input("Enter the target URL or IP: ")
    print(f"Running Nikto scan on {target}...")
    subprocess.run(["nikto", "-h", target])
    print("Nikto scan completed.")
