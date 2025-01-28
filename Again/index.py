import sys
from scan import automation_submenu
from domain import subdomain_submenu
from exploit import exploit_tool_menu
# Function to display the banner with color
def display_banner():
    # ANSI escape codes for colors
    red = "\033[31m"  # Red color
    green = "\033[32m"  # Green color
    reset = "\033[0m"  # Reset color

    # Banner with version in green
    print(f"{red}")
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


# Main script logics
def main():
    display_banner()  # Display the banner
    print("Starting menu...")

    while True:
        print("\nSelect a task to perform:")
        print("1. Automation Tool")
        print("2. Domain")
        print("3. Exploits")
        print("4. Exit\n")

        choice = input("Enter your choice [1-5]: ")
        if choice == "1":
            automation_submenu()  # Enter Automation Category submenu
        elif choice == "2":
            subdomain_submenu()  # Enter Domain submenu
        elif choice == "3":
            exploit_tool_menu()  # Enter Domain submenu
        elif choice == "4":
            print("Ex2iting. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice, please try again.")
        print()


if __name__ == "__main__":
    main()
