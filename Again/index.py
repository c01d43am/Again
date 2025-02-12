import sys
import random
from font import display_banner  # Importing display_banner from font.py
from automationtool import automation_submenu
from domain import subdomain_submenu
from exploit import exploit_tool_menu
import subprocess

def start_tool():
    try:
        # Your tool execution logic here
        pass
    except KeyboardInterrupt:
        print("\n[!] KeyboardInterrupt detected. Exiting gracefully...")
import subprocess

def start_tool():
    try:
        # Tool execution logic
        run_index()  # Only run this if not interrupted
    except KeyboardInterrupt:
        print("\n[!] Exiting gracefully...")

def run_index():
    try:
        subprocess.run(["python3", "Again/index.py"])
    except KeyboardInterrupt:
        print("\n[!] Exiting without restarting index.py...")

# Main script logic
def main():
    display_banner()  # Call the function from font.py
    print("Starting menu...")

    try:
        while True:
            print("\nSelect a task to perform:")
            print("1. Automation Tool")
            print("2. Domain")
            print("3. Exploits")
            print("4. Exit\n")

            choice = input("Enter your choice [1-4]: ")
            if choice == "1":
                automation_submenu()  # Enter Automation Category submenu
            elif choice == "2":
                subdomain_submenu()  # Enter Domain submenu
            elif choice == "3":
                exploit_tool_menu()  # Enter Exploits submenu
            elif choice == "4":
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
