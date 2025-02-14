from Tools.DomainScan.sslscan_tool import check_and_install_sslscan
from Tools.DomainScan.nmap_tool import check_and_install_nmap
from Tools.DomainScan.feroxbuster_tool import is_feroxbuster_installed
from Tools.DomainScan.gobuster_tool import is_tool_installed
from Tools.DomainScan.dirb_tool import dirb_submenu  # Import the run_dirb function

def subdomain_submenu():
    """Submenu to handle subdomain-related tasks."""
    while True:
        print("\nSubdomain Submenu:")
        print("1. Run dirb Scan")  # Updated label for clarity
        print("2. Run SSLscan")
        print("3. Run Feroxbuster")
        print("4. Run Gobuster")
        print("5. Run Nmap Scan")
        print("6. Exit")
        choice = input("Please choose an option (1-6): ")
        
        if choice == "1":
            dirb_submenu()  # Call dirb with user input
        elif choice == "2":
            subdomain = input("Enter the subdomain to scan with SSLscan: ")
            check_and_install_sslscan()
        elif choice == "3":
            subdomain = input("Enter the subdomain to scan with Feroxbuster: ")
            is_feroxbuster_installed()
        elif choice == "4":
            subdomain = input("Enter the subdomain to scan with Gobuster: ")
            is_tool_installed()
        elif choice == "5":
            check_and_install_nmap()
        elif choice == "6":
            print("Exiting the subdomain submenu...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    subdomain_submenu()
