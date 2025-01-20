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


def run_nmap_scan():
    """Runs Nmap port scan on the subdomains discovered by Sublist3r."""
    if not os.path.exists("subdomains.txt"):
        print("No subdomains file found. Please run Sublist3r first.")
        return

    # Run Nmap on each subdomain found
    with open("subdomains.txt", "r") as file:
        subdomains = file.readlines()

    print("\nRunning Nmap scans on discovered subdomains...")
    for subdomain in subdomains:
        subdomain = subdomain.strip()
        print(f"Scanning {subdomain}...")
        try:
            subprocess.run(f"nmap {subdomain}", shell=True, check=True)
            print(f"Nmap scan completed for {subdomain}.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to run Nmap scan for {subdomain}: {e}")


def subdomain_submenu():
    """Submenu to handle subdomain-related tasks."""
    while True:
        print("\nSubdomain Submenu:")
        print("1. Enumerate Subdomains with Sublist3r")
        print("2. Run Nmap scan on discovered subdomains")
        print("3. Return to Domain Menu\n")

        choice = input("Enter your choice [1-3]: ")
        if choice == "1":
            print("Enumerate Subdomains with Sublist3r selected.")
            domain = input("Enter the domain to enumerate subdomains for: ")
            if domain:
                if check_and_install_sublister():  # Check and install Sublist3r if not installed
                    run_sublister(domain)  # Run Sublist3r for the given domain
            else:
                print("No domain entered. Please try again.")
        elif choice == "2":
            if check_and_install_nmap():  # Check and install Nmap if not installed
                run_nmap_scan()  # Run Nmap scan on the discovered subdomains
        elif choice == "3":
            print("Returning to Domain Menu.")
            break
        else:
            print("Invalid choice, please try again.")
        print()


if __name__ == "__main__":
    subdomain_submenu()
