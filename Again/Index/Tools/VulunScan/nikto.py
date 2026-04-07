import subprocess

from ..Support.install_tool import install_tool

def check_and_install_nikto():
    """Checks if Nikto is installed. Installs it if not found."""
    install_tool("nikto")

def run_nikto_scan(subdomain):
    """Run Nikto scan for vulnerabilities."""
    check_and_install_nikto()
    print(f"\nRunning Nikto scan for {subdomain}...")
    try:
        subprocess.run(f"nikto -h {subdomain}", shell=True, check=True)
        print(f"Nikto scan completed for {subdomain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run Nikto scan for {subdomain}: {e}")

def nikto_menu():
    """Menu for Nikto scanning options."""
    while True:
        print("\nNikto Automation Menu:")
        print("1. Nikto Scan")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            subdomain = input("Enter the subdomain to scan with Nikto: ")
            run_nikto_scan(subdomain)
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    nikto_menu()