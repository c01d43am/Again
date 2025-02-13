import subprocess
import random
from colorama import Fore, Style, init

init(autoreset=True)

def get_random_color():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    return random.choice(colors)

def install_tool(tool_name):
    """Checks if a tool is installed and installs it if not found."""
    try:
        subprocess.run(["which", tool_name], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print(f"{tool_name} not found. Installing...")
        subprocess.run(["sudo", "apt", "install", "-y", tool_name], check=True)

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

def main():
    while True:
        print("\nNikto Automation Menu:")
        print(get_random_color() + "1. Run Nikto Scan")
        print(get_random_color() + "2. Exit")
        
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
    main()
