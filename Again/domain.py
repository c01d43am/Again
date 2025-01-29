import os
import subprocess
def check_and_install_nmap():
    """Checks if Nmap is installed. Installs it if not found."""
    try:
        result = subprocess.run("where nmap", shell=True, capture_output=True)
        if result.returncode == 0:
            print("Nmap is already installed.")
            return True
        else:
            print("Nmap is not installed. Installing now...")
            os.system("choco install nmap -y")
            print("Nmap has been installed successfully.")
            return True
    except Exception as e:
        print(f"Failed to install Nmap: {e}")
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
def run_nmap_scan(subdomain, scan_type="full"):
    """Run an Nmap scan on the subdomain to check for open ports."""
    print(f"\nRunning Nmap scan on {subdomain} (Scan Type: {scan_type})...")
    try:
        if scan_type == "fast":
            subprocess.run(f"nmap -Pn -T4 -F {subdomain}", shell=True, check=True)  # Fast scan
        else:
            subprocess.run(f"nmap -Pn {subdomain}", shell=True, check=True)  # Full scan
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

def run_dirb_scan(subdomain):
    """Run Dirb scan to check for directories and files."""
    print(f"\nRunning Dirb scan for {subdomain}...")
    try:
        subprocess.run(f"dirb http://{subdomain}", shell=True, check=True)
        print(f"Dirb scan completed for {subdomain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run Dirb scan for {subdomain}: {e}")

def subdomain_submenu():
    """Submenu to handle subdomain-related tasks."""
    while True:
        print("\nSubdomain Submenu:")
        print("1. Run Dirb Scan")
        print("2. Run Nmap Scan")
        print("3. Run Nikto Scan")
        print("4. Run SSLscan")
        print("5. Exit")
        choice = input("Please choose an option (1-5): ")
        
        if choice == "1":
            subdomain = input("Enter the subdomain to scan with Dirb: ")
            run_dirb_scan(subdomain)
        elif choice == "2":
            subdomain = input("Enter the subdomain to scan with Nmap: ")
            scan_type = input("Enter scan type (fast/full): ")
            run_nmap_scan(subdomain, scan_type)
        elif choice == "3":
            subdomain = input("Enter the subdomain to scan with Nikto: ")
            run_nikto_scan(subdomain)
        elif choice == "4":
            subdomain = input("Enter the subdomain to scan with SSLscan: ")
            run_sslscan(subdomain)
        elif choice == "5":
            print("Exiting the vulnerability scan submenu...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def main_menu():
    """Main menu for the tool that checks and installs required tools."""
    print("Welcome to the Recon Tool!")
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
