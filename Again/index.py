# Version: 0.0.7
# Description: This script is a simple menu-driven tool that allows users to select different categories of tools to automate tasks.
# The script provides three main categories: Automation Tool, Domain, and Exploits.
# The user can select a category and then choose a specific tool or task to perform within that category.
# The script includes submenus for each category to provide more options and functionalities.
import sys
from automationtool import automation_submenu
from domain import subdomain_submenu
from exploit import exploit_tool_menu
import random
# Function to display the banner with color
def display_banner():
    # ANSI escape codes for colors
    colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
    reset = "\033[0m"  # Reset color
    green = "\033[32m"  # Green color
    color = random.choice(colors)  # Pick a random color

    print(f"{color}")
    print("""
░█████╗░░██████╗░░█████╗░██╗███╗░░██╗░█████╗░
██╔══██╗██╔════╝░██╔══██╗██║████╗░██║██╔══██╗
███████║██║░░██╗░███████║██║██╔██╗██║╚═╝███╔╝
██╔══██║██║░░╚██╗██╔══██║██║██║╚████║░░░╚══╝░
██║░░██║╚██████╔╝██║░░██║██║██║░╚███║░░░██╗░░
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░╚═╝░░
                   """)
    # Display version at the bottom left corner
    version = f"{green}\t\t\tv0.0.7 by c01d43am{reset}"
    print("\t\thttps://github.com/c01d43am")
    print(f"\n{version}\n")  # Version at the bottom left corner

import subprocess

# General function to check and install a tool
def install_tool(tool_name, package_name=None, post_install_cmd=None):
    if package_name is None:
        package_name = tool_name

    try:
        # Check if the tool is installed
        result = subprocess.run(f"which {tool_name}", shell=True, capture_output=True)
        if result.returncode != 0:
            print(f"{tool_name} not found. Installing...")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", package_name], check=True)
            print(f"{tool_name} installed successfully.")
            if post_install_cmd:
                subprocess.run(post_install_cmd, shell=True, check=True)
        else:
            print(f"{tool_name} is already installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error while installing {tool_name}: {e}")
#-------------------------------------------------------------------------------------------------------------
# Main script logics
def main():
    display_banner()  # Display the banner
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
                exploit_tool_menu()  # Enter Domain submenu
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
