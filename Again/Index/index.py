import sys
import os
import subprocess
import random

# Add the parent directory of "index" (which is "Again") to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Tools')))

from Tools.Design.font import Font_banner  # Importing display_banner from font.py
from Tools.Automation.automationtool import automation_submenu
from Tools.DomainScan.subdomain_menu import subdomain_submenu
from Tools.DBMSInjection.exploit import exploit_tool_menu
from Tools.VulunScan.vulnscan import Vulunscan_menu

# Function to set execute permissions and run shell scripts
def run_script(script_name): # Pass the script name as an argument
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Checker', script_name)) # Get the script path
    
    if os.path.isfile(script_path):
        print(f"\n[+] Ensuring execute permissions for {script_name}...")
        subprocess.run(["chmod", "+x", script_path], check=True)  # Set execute permission
        
        print(f"\n[+] Running {script_name}...")
        try:
            subprocess.run(["bash", script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"[!] Error executing {script_name}: {e}")
    else:
        print(f"[!] Error: {script_name} not found!")

# Function for Updates & Check submenu
def updates_check_menu():
    while True:
        print("\n[ Updates & Check Menu ]")
        print("1. Install all tools")
        print("2. Uninstall all tools")
        print("3. Check installation status")
        print("4. Back to Main Menu")

        choice = input("Enter your choice [1-4]: ")
        if choice == "1":
            run_script("install.sh")
        elif choice == "2":
            run_script("uninstall_tools.sh")
        elif choice == "3":
            run_script("check_installation.sh")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Main script logic
def main():
    Font_banner()  # Call the function from font.py
    print("Starting menu...")

    try:
        while True:
            print("\nSelect a task to perform:")
            print("1. Automation Tool")
            print("2. Domain")
            print("3. Vulnerability Scanning")
            print("4. Exploits")
            print("5. Updates & Check")
            print("6. Exit\n")

            choice = input("Enter your choice [1-6]: ")
            if choice == "1":
                automation_submenu()  # Enter Automation Category submenu
            elif choice == "2":
                subdomain_submenu()  # Enter Domain submenu
            elif choice == "3":
                Vulunscan_menu()  # Vulnerability Scanning submenu
            elif choice == "4":
                exploit_tool_menu()  # Exploits submenu
            elif choice == "5":
                updates_check_menu()  # Runs Updates & Check submenu
            elif choice == "6":
                print("Exiting. Goodbye!")
                sys.exit(0)
            else:
                funny_responses = [
                    "Oops! That wasn't on the menu. Try again!",
                    "Nice try, but that's not an option!",
                    "Invalid choice. Are you testing my patience?",
                    "Error 404: Your choice not found!",
                    "You broke the menu... Just kidding, try again!"
                ]
                print(random.choice(funny_responses))
    except KeyboardInterrupt:
        print("\n[!] KeyboardInterrupt detected. Exiting gracefully...")
        sys.exit(0)

if __name__ == "__main__":
    main()
