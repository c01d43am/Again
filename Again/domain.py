import os
import subprocess


def check_and_install_sublister():
    """Checks if Sublist3r is installed. Installs it if not found."""
    sublist3r_path = os.path.expanduser("~/Sublist3r/sublist3r.py")
    if os.path.exists(sublist3r_path):
        print("Sublist3r is already installed.")
    else:
        print("Sublist3r is not installed. Installing now...")
        try:
            os.system("git clone https://github.com/aboul3la/Sublist3r.git ~/Sublist3r")
            os.system("sudo apt update && sudo apt install -y python3-pip")
            os.system("pip3 install -r ~/Sublist3r/requirements.txt")
            print("Sublist3r has been installed successfully.")
        except Exception as e:
            print(f"Failed to install Sublist3r: {e}")


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


def domain_submenu():
    while True:
        print("\nDomain Submenu:")
        print("1. Add Domain")
        print("2. List Domains")
        print("3. Manage Subdomains")
        print("4. Return to Main Menu\n")

        choice = input("Enter your choice [1-4]: ")
        if choice == "1":
            print("Add Domain selected.")
            # Logic for adding a domain
        elif choice == "2":
            print("List Domains selected.")
            # Logic for listing domains
        elif choice == "3":
            subdomain_submenu()  # Call the Subdomain submenu
        elif choice == "4":
            print("Returning to Main Menu.")
            break
        else:
            print("Invalid choice, please try again.")
        print()


def subdomain_submenu():
    while True:
        print("\nSubdomain Submenu:")
        print("1. Enumerate Subdomains with Sublist3r")
        print("2. Empty Tool (Reserved)")
        print("3. Return to Domain Menu\n")

        choice = input("Enter your choice [1-3]: ")
        if choice == "1":
            print("Enumerate Subdomains with Sublist3r selected.")
            domain = input("Enter the domain to enumerate subdomains for: ")
            if domain:
                check_and_install_sublister()  # Check and install Sublist3r if not installed
                run_sublister(domain)  # Run Sublist3r for the given domain
            else:
                print("No domain entered. Please try again.")
        elif choice == "2":
            print("This tool is reserved for future use.")
        elif choice == "3":
            print("Returning to Domain Menu.")
            break
        else:
            print("Invalid choice, please try again.")
        print()
