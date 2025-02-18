from ..VulunScan.nikto import nikto_menu
from ..VulunScan.skipfish import skipfish_menu
from ..VulunScan.wapiti import wapiti_menu

def Vulunscan_menu():
    """Menu for the user to choose the tool."""
    while True:
        print("\nVulnerability Scan Menu:")
        print("1. Nikto Scan")
        print("2. Skipfish Scan")
        print("3. Wapiti Scan")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            nikto_menu()
        elif choice == "2":
            skipfish_menu()
        elif choice == "3":
            wapiti_menu()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Vulunscan_menu()