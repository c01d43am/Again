# Description: A tool to perform reconnaissance on a domain or subdomain. 
# The tool checks and installs required tools like Nmap, sslscan, dirb, Nikto, and feroxbuster. 
# It then provides a menu to run scans on subdomains using these tools. 
# The user can choose to run Dirb, Nmap, Nikto, SSLscan, or Feroxbuster scans on a subdomain.
import os
import subprocess
#-------------------------------------------------------------------------------------------------------------
def check_and_install_nmap():#nmap is a network scanning tool
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
#-------------------------------------------------------------------------------------------------------------
def check_and_install_sslscan():#sslscan is a tool to check SSL/TLS vulnerabilities
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
#-------------------------------------------------------------------------------------------------------------
def check_and_install_dirb():#dirb is a tool to check directories and files
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
#-------------------------------------------------------------------------------------------------------------
def check_and_install_nikto():#nikto is a web server scanner
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
#-------------------------------------------------------------------------------------------------------------
def is_feroxbuster_installed():#feroxbuster is a directory and file brute-forcing tool
    """Check if feroxbuster is installed."""
    try:
        subprocess.run(["feroxbuster", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except FileNotFoundError:
        return False

def install_feroxbuster():
    """Install feroxbuster if not installed."""
    print("[+] Installing feroxbuster...")
    os.system("sudo apt update && sudo apt install -y feroxbuster")

def run_feroxbuster(target_url, wordlist="/usr/share/wordlists/dirb/common.txt"):
    """Run feroxbuster with the given target URL and wordlist."""
    print(f"[+] Running feroxbuster on {target_url}...")
    os.system(f"feroxbuster -u {target_url} -w {wordlist}")

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
#-------------------------------------------------------------------------------------------------------------
def run_nikto_scan(subdomain):#nikto is a web server scanner
    """Run Nikto scan for vulnerabilities."""
    print(f"\nRunning Nikto scan for {subdomain}...")
    try:
        subprocess.run(f"nikto -h {subdomain}", shell=True, check=True)
        print(f"Nikto scan completed for {subdomain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run Nikto scan for {subdomain}: {e}")
#-------------------------------------------------------------------------------------------------------------
def is_gobuster_installed(): #gobuster is a directory and file brute-forcing tool
    """Check if gobuster is installed."""
    try:
        subprocess.run(["gobuster", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except FileNotFoundError:
        return False

def install_gobuster():
    """Install gobuster if not installed."""
    print("[+] Installing gobuster...")
    os.system("sudo apt update && sudo apt install -y gobuster")

def run_gobuster(target_url, wordlist="/usr/share/wordlists/dirb/common.txt"):
    """Run gobuster with the given target URL and wordlist."""
    print(f"[+] Running gobuster on {target_url}...")
    os.system(f"gobuster dir -u {target_url} -w {wordlist}")

#-------------------------------------------------------------------------------------------------------------
def run_sslscan(subdomain):#sslscan is a tool to check SSL/TLS vulnerabilities
    """Run sslscan to check for SSL/TLS vulnerabilities."""
    print(f"\nRunning SSL/TLS scan for {subdomain}...")
    try:
        subprocess.run(f"sslscan {subdomain}", shell=True, check=True)
        print(f"SSL/TLS scan completed for {subdomain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run SSL/TLS scan for {subdomain}: {e}")
#-------------------------------------------------------------------------------------------------------------
def run_dirb_scan(subdomain):#dirb is a tool to check directories and files
    """Run Dirb scan to check for directories and files."""
    try:
        subprocess.run(f"dirb http://{subdomain}", shell=True, check=True)
        print(f"Dirb scan completed for {subdomain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run Dirb scan for {subdomain}: {e}")
#-------------------------------------------------------------------------------------------------------------
def subdomain_submenu():#subdomain-related tasks
    """Submenu to handle subdomain-related tasks."""
    while True:
        print("\nSubdomain Submenu:")
        print("1. Run Dirb Scan")
        print("2. Run Nmap Scan")
        print("3. Run Nikto Scan")
        print("4. Run SSLscan")
        print("5. Run Feroxbuster")
        print("6. Run Gobuster")
        print("7. Exit")
        choice = input("Please choose an option (1-7): ")
        
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
            subdomain = input("Enter the subdomain to scan with Feroxbuster:{ex: https://google.com/} ")
            run_feroxbuster(subdomain)
        elif choice == "6":
            subdomain = input("Enter the subdomain to scan with Gobuster {ex: google.com}: ")
            run_gobuster(subdomain)
        elif choice == "7":
            print("Exiting the vulnerability scan submenu...")
            break
        else:
            print("Exiting the tool. Goodbye!")
            break
        else:
            funny_responses = [
                "Oops! That wasn't on the menu. Try again!",
                "Nice try, but that's not an option!",
                "Invalid choice. Are you testing my patience?",
                "Error 404: Your choice not found!",
                "You broke the menu... Just kidding, try again!"
            ]
            import random
            print(random.choice(funny_responses))

            print("Invalid choice. Please select a valid option.")
#-------------------------------------------------------------------------------------------------------------
def main_menu():
    """Main menu for the tool that checks and installs required tools."""
    print("Welcome to the Recon Tool!")
    check_and_install_nmap()
    check_and_install_sslscan()
    check_and_install_dirb()
    check_and_install_nikto()
    if not is_feroxbuster_installed():
        install_feroxbuster()
    if not is_gobuster_installed():
        install_gobuster()
#-------------------------------------------------------------------------------------------------------------
    while True:#main menu
        print("\nMain Menu:")
        print("1. Subdomain Tasks")
        print("2. Exit")

        choice = input("Please choose an option (1-2): ")

        if choice == "1":#subdomain-related tasks
            target_url = input("Enter target URL: ")
            if not is_installed():
                install_gobuster()
            run_gobuster(target_url)
        elif choice == "2":
            print("Exiting the tool. Goodbye!")
            break
        else:
            funny_responses = [
                "Oops! That wasn't on the menu. Try again!",
                "Nice try, but that's not an option!",
                "Invalid choice. Are you testing my patience?",
                "Error 404: Your choice not found!",
                "You broke the menu... Just kidding, try again!"
            ]
            import random
            print(random.choice(funny_responses))

if __name__ == "__main__":
    main_menu()