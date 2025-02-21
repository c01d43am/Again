from Tools.DomainScan.sslscan_tool import run_sslscan
from Tools.DomainScan.nmap_tool import nmap_host_discovery
from Tools.DomainScan.feroxbuster_tool import feroxbuster_menu  # Updated to call the menu function
from Tools.DomainScan.gobuster_tool import gobuster_menu
from Tools.DomainScan.dirb_tool import dirb_submenu  # Import the dirb submenu
from Tools.DomainScan.Normal import get_local_ip

def subdomain_submenu():
    """Submenu to handle subdomain-related tasks."""
    while True:
        print("\nSubdomain Submenu:")
        print("1. Run Dirb Scan")
        print("2. Run SSLscan")
        print("3. Run Feroxbuster")
        print("4. Run Gobuster")
        print("5. Run Nmap Scan")
        print("6. Get Local IP Address")
        print("7. Return to Main Menu\n")
        choice = input("Please choose an option (1-6): ")
        
        if choice == "1":
            dirb_submenu()  # Call dirb submenu
        elif choice == "2":
            subdomain = input("Enter the subdomain to scan: ")
            run_sslscan(subdomain)   # Call the SSLscan function
        elif choice == "3":
            feroxbuster_menu()  # Call the Feroxbuster menu
        elif choice == "4":
            gobuster_menu()     # Call the Gobuster menu
        elif choice == "5":
            nmap_host_discovery()    # Call the Nmap function
        elif choice == "6":
            get_local_ip()      # Call the get_local_ip function
        elif choice == "7":
            print("Exiting the subdomain submenu...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    subdomain_submenu()
