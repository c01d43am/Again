import sys
from tools import automation_submenu

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
    print(f"{green}0.0.1{reset}\n")  # Display version in green

# Main script logic
def main():
    display_banner()  # Display the banner
    print("Starting menu...")

    while True:
        print("\nSelect a task to perform:")
        print("1. Automation Tool ")
        print("2. ")
        print("3. ")
        print("4. ")
        print("5. Exit\n")

        choice = input("Enter your choice [1-5]: ")
        if choice == "1":
            automation_submenu()  # Enter Automation Category submenu
        elif choice == "5":
            print("Exiting. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice, please try again.")
        print()

if __name__ == "__main__":
    main()
