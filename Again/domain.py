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

def check_and_install_nikto():
    """Checks if Nikto is installed. Installs it if not found."""
    try:
        result = subprocess.run("which nikto", shell=True, capture_output=True)
        if result.returncode == 0:
            print("Nikto is already installed.")
            return True
        else:
            print("Nikto is not installed. Installing now...")
            os.system("sudo apt update && sudo apt install -y nikto")
            print("Nikto has been installed successfully.")
            return True
    except Exception as e:
        print(f"Failed to install Nikto: {e}")
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

def run_nikto_scan(subdomain):
    """Run Nikto scan for vulnerabilities."""
    print(f"\nRunning Nikto scan for {subdomain}...")
    try:
        subprocess.run(f"nikto -h {subdomain}", shell=True, check=True)
        print(f"Nikto scan completed for {subdomain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run Nikto scan for {subdomain}: {e}")

def run_sslscan(subdomain):
    """Run sslscan to check for SSL/TLS vulnerabilities."""
    print(f"\nRunning SSL/TLS scan for {subdomain}...")
    try:
        subprocess.run(f"sslscan {subdomain}", shell=True, check=True)
        print(f"SSL/TLS scan completed for {subdomain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run SSL/TLS scan for {subdomain}: {e}")

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
            subdomain_vuln_scan_submenu()
        elif choice == "3":
            print("Exiting the submenu...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def subdomain_vuln_scan_submenu():
    """Submenu for running vulnerability scans on subdomains."""
    while True:
        print("\nVulnerability Scan Submenu:")
        print("1. Run Nmap Scan")
        print("2. Run Nikto Scan")
        print("3. Run SSLscan")
        print("4. Exit")

        choice = input("Please choose an option (1-4): ")

        if choice == "1":
            subdomain = input("Enter the subdomain to scan with Nmap: ")
            scan_type = input("Enter scan type (fast/full): ")
            run_nmap_scan(subdomain, scan_type)
        elif choice == "2":
            subdomain = input("Enter the subdomain to scan with Nikto: ")
            run_nikto_scan(subdomain)
        elif choice == "3":
            subdomain = input("Enter the subdomain to scan with SSLscan: ")
            run_sslscan(subdomain)
        elif choice == "4":
            print("Exiting the vulnerability scan submenu...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def main_menu():
    """Main menu for the tool that checks and installs required tools."""
    print("Welcome to the Recon Tool!")
    check_and_install_sublister()
    check_and_install_nmap()
    check_and_install_sslscan()
    check_and_install_dirb()
    check_and_install_nikto()

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
