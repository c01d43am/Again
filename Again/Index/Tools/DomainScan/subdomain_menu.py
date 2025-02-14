from Tools.DomainScan.sslscan_tool import check_and_install_sslscan, run_sslscan
from Tools.DomainScan.nmap_tool import check_and_install_nmap
from Tools.DomainScan.feroxbuster_tool import is_feroxbuster_installed
from Tools.DomainScan.gobuster_tool import is_tool_installed
from Tools.DomainScan.dirb_tool import run_dirbuster  # Import the run_dirbuster function

def subdomain_submenu():
    """Submenu to handle subdomain-related tasks."""
    while True:
        print("\nSubdomain Submenu:")
        print("1. Run DirBuster Scan")  # Updated label for clarity
        print("2. Run SSLscan")
        print("3. Run Feroxbuster")
        print("4. Run Gobuster")
        print("5. Run Nmap Scan")
        print("6. Exit")
        choice = input("Please choose an option (1-6): ")
        
        if choice == "1":
            target_url = input("Enter the target URL for DirBuster: ")
            wordlist = input("Enter wordlist path (default: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt): ") or "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
            threads = input("Enter number of threads (default: 10): ") or "10"
            file_ext = input("Enter file extensions to search (default: php,html,txt): ") or "php,html,txt"

            run_dirbuster(target_url, wordlist, threads, file_ext)  # Call DirBuster with user input
            
        elif choice == "2":
            subdomain = input("Enter the subdomain to scan with SSLscan: ")
            run_dirbuster(subdomain)
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
