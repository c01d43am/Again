import os
import subprocess

def check_and_install_sublister():
    """Checks if Sublist3r is installed. Installs it if not found."""
    sublist3r_path = os.path.expanduser("~/Sublist3r/sublist3r.py")
    if os.path.exists(sublist3r_path):
        print("Sublist3r is already installed.")
        return True
    else:
        print("Sublist3r is not installed. Installing now...")
        try:
            os.system("git clone https://github.com/aboul3la/Sublist3r.git ~/Sublist3r")
            os.system("sudo apt update && sudo apt install -y python3-pip")
            os.system("pip3 install -r ~/Sublist3r/requirements.txt")
            print("Sublist3r has been installed successfully.")
            return True
        except Exception as e:
            print(f"Failed to install Sublist3r: {e}")
            return False

def check_and_install_nmap():
    """Checks if Nmap is installed. Installs it if not found."""
    try:
        result = subprocess.run("which nmap", shell=True, capture_output=True)
        if result.returncode == 0:
            print("Nmap is already installed.")
            return True
        else:
            print("Nmap is not installed. Installing now...")
            os.system("sudo apt update && sudo apt install -y nmap")
            print("Nmap has been installed successfully.")
            return True
    except Exception as e:
        print(f"Failed to install Nmap: {e}")
        return False

def check_and_install_sslscan():
    """Checks if sslscan is installed. Installs it if not found."""
    try:
        result = subprocess.run("which sslscan", shell=True, capture_output=True)
        if result.returncode == 0:
            print("sslscan is already installed.")
            return True
        else:
            print("sslscan is not installed. Installing now...")
            os.system("sudo apt update && sudo apt install -y sslscan")
            print("sslscan has been installed successfully.")
            return True
    except Exception as e:
        print(f"Failed to install sslscan: {e}")
        return False

def check_and_install_dirb():
    """Checks if dirb is installed. Installs it if not found."""
    try:
        result = subprocess.run("which dirb", shell=True, capture_output=True)
        if result.returncode == 0:
            print("dirb is already installed.")
            return True
        else:
            print("dirb is not installed. Installing now...")
            os.system("sudo apt update && sudo apt install -y dirb")
            print("dirb has been installed successfully.")
            return True
    except Exception as e:
        print(f"Failed to install dirb: {e}")
        return False

def run_sublister(domain):
    """Runs Sublist3r to enumerate subdomains for the provided domain."""
    sublist3r_path = os.path.expanduser("~/Sublist3r/sublist3r.py")
    if not os.path.exists(sublist3r_path):
        print("Sublist3r is not installed. Please install it first.")
        return

    print(f"Running Sublist3r for domain: {domain}")
    command = f"python3 {sublist3r_path} -d {domain} -o subdomains.txt"
    try:
        os.system(command)
        print(f"Sublist3r has completed enumeration. Results are saved in 'subdomains.txt'.")
    except Exception as e:
        print(f"Failed to run Sublist3r: {e}")

def run_dirb_scan(subdomain):
    """Run dirb to check for common files and directories."""
    output_file = f"dirb_results_{subdomain.replace('.', '_')}.txt"
    print(f"\nRunning dirb scan for {subdomain}...")
    try:
        command = f"dirb http://{subdomain} -o {output_file}"
        os.system(command)
        print(f"dirb scan completed. Results saved to {output_file}.")
    except Exception as e:
        print(f"Failed to run dirb for {subdomain}: {e}")

def check_http_status_code(subdomain):
    """Check the HTTP status code for a given subdomain using curl."""
    try:
        response = subprocess.run(f"curl -I -s {subdomain}", shell=True, capture_output=True)
        response_str = response.stdout.decode("utf-8")

        # Extract status code from the response headers
        lines = response_str.splitlines()
        for line in lines:
            if line.startswith("HTTP"):
                status_code = line.split()[1]
                print(f"HTTP Status Code for {subdomain}: {status_code}")
                return status_code
        return None
    except subprocess.CalledProcessError as e:
        print(f"Failed to check HTTP status for {subdomain}: {e}")
        return None

def check_security_headers(subdomain):
    """Check for common HTTP security headers."""
    headers = ['Strict-Transport-Security', 'X-Content-Type-Options', 'X-Frame-Options', 'Content-Security-Policy']
    try:
        response = subprocess.run(f"curl -sI {subdomain}", shell=True, capture_output=True)
        headers_str = response.stdout.decode("utf-8")
        print(f"\nSecurity headers for {subdomain}:")

        for header in headers:
            if header in headers_str:
                print(f"  [\u2713] {header}: Present")
            else:
                print(f"  [\u2717] {header}: Missing")
    except subprocess.CalledProcessError as e:
        print(f"Failed to check security headers for {subdomain}: {e}")

def run_nmap_scan(subdomain, scan_type="full"):
    """Run an Nmap scan on the subdomain to check for open ports."""
    print(f"\nRunning Nmap scan on {subdomain} (Scan Type: {scan_type})...")
    try:
        if scan_type == "fast":
            subprocess.run(f"nmap -T4 -F {subdomain}", shell=True, check=True)  # Fast scan
        else:
            subprocess.run(f"nmap {subdomain}", shell=True, check=True)  # Full scan
        print(f"Nmap scan completed for {subdomain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run Nmap scan for {subdomain}: {e}")

def run_sslscan(subdomain):
    """Run sslscan to check for SSL/TLS vulnerabilities."""
    print(f"\nRunning SSL/TLS scan for {subdomain}...")
    try:
        subprocess.run(f"sslscan {subdomain}", shell=True, check=True)
        print(f"SSL/TLS scan completed for {subdomain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run SSL/TLS scan for {subdomain}: {e}")

def run_vulnerability_scans():
    """Run a series of vulnerability scans on subdomains."""
    if not os.path.exists("subdomains.txt"):
        print("No subdomains file found. Please run Sublist3r first.")
        return

    # Run the scans on each subdomain
    with open("subdomains.txt", "r") as file:
        subdomains = file.readlines()

    for subdomain in subdomains:
        subdomain = subdomain.strip()
        print(f"\nScanning {subdomain}...")

        # HTTP Status Code
        check_http_status_code(subdomain)

        # Check Security Headers
        check_security_headers(subdomain)

        # Nmap Fast Scan for open ports
        run_nmap_scan(subdomain, scan_type="fast")

        # SSL/TLS Scan
        run_sslscan(subdomain)

        # dirb Scan
        run_dirb_scan(subdomain)

def subdomain_submenu():  
    """Submenu to handle subdomain-related tasks."""  
    while True:  
        print("\nSubdomain Submenu:")  
        print("1. Enumerate Subdomains with Sublist3r")  
        print("2. Run Vulnerability Scans on Subdomains")  
        print("3. Exit")  

        choice = input("Please choose an option (1-3): ")  

        if choice == "1":  
            domain = input("Enter the domain to enumerate subdomains: ")  
            run_sublister(domain)  
        elif choice == "2":  
            run_vulnerability_scans()  
        elif choice == "3":  
            print("Exiting the submenu...")  
            break  
        else:  
            print("Invalid choice. Please select a valid option.")  

# Main menu to start the tool  
def main_menu():  
    """Main menu for the tool that checks and installs required tools."""  
    print("Welcome to the Recon Tool!")  
    check_and_install_sublister()  
    check_and_install_nmap()  
    check_and_install_sslscan()  
    check_and_install_dirb()  
    
    while True:  
        print("\nMain Menu:")  
        print("1. Subdomain Tasks")  
        print("2. Exit")  

        choice = input("Please choose an option (1-2): ")  

        if choice == "1":  
            subdomain_submenu()  
        elif choice == "2":  
            print("Exiting the tool. Goodbye!")  
            break  
        else:  
            print("Invalid choice. Please select a valid option.")  

if __name__ == "__main__":  
    main_menu()