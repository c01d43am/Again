from Tools.DomainScan.sslscan_tool import run_sslscan
from Tools.DomainScan.nmap_tool import check_and_install_nmap, run_nmap_scan
from Tools.DomainScan.feroxbuster_tool import is_tool_installed as is_ferox_installed, feroxbuster_menu
from Tools.DomainScan.gobuster_tool import is_tool_installed as is_gobuster_installed, install_tool, gobuster_menu
from Tools.DomainScan.dirb_tool import is_tool_installed as is_dirb_installed, dirb_submenu

def subdomain_submenu():
    """Submenu to handle subdomain-related tasks."""
    while True:
        print("\nSubdomain Submenu:")
        print("1. Run Dirb Scan")
        print("2. Run SSLscan")
        print("3. Run Feroxbuster")
        print("4. Run Gobuster")
        print("5. Run Nmap Scan")
        print("6. Exit")
        
        choice = input("Please choose an option (1-6): ").strip()
        
        if choice == "1":
            if not is_dirb_installed():
                print("[!] Dirb is not installed. Installing now...")
                install_tool("dirb")
            dirb_submenu()
        
        elif choice == "2":
            subdomain = input("Enter the subdomain to scan with SSLscan: ").strip()
            run_sslscan(subdomain)
        
        elif choice == "3":
            if not is_ferox_installed():
                print("[!] Feroxbuster is not installed. Installing now...")
                install_tool("feroxbuster")
            feroxbuster_menu()
        
        elif choice == "4":
            if not is_gobuster_installed():
                print("[!] Gobuster is not installed. Installing now...")
                install_tool("gobuster")
            gobuster_menu()  # Open menu without asking for URL initially
        
        elif choice == "5":
            if not check_and_install_nmap():  # Ensures installation before scanning
                print("[!] Nmap installation failed.")
                continue
            subdomain = input("Enter the subdomain to scan with Nmap: ").strip()
            run_nmap_scan(subdomain)
        
        elif choice == "6":
            print("Exiting the subdomain submenu...")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    subdomain_submenu()
