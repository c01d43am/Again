import sys
import random
from Again.Design.font import Font_banner  # Importing display_banner from font.py
from Again.Automation.automationtool import automation_submenu
from Again.DomainScan.subdomain_menu import subdomain_submenu
from Again.DBMSInjection.exploit import exploit_tool_menu
from Again.VulunScan.vulnscan import Vulunscan_menu

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
            print("5. Exit\n")

            choice = input("Enter your choice [1-5]: ")
            if choice == "1":
                automation_submenu()  # Enter Automation Category submenu
            elif choice == "2":
                subdomain_submenu()  # Enter Domain submenu
            elif choice == "3":
                Vulunscan_menu()  # vulnerability Scanning submenu
            elif choice == "4":
                exploit_tool_menu()  # Exploits submenu
            elif choice == "5":
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