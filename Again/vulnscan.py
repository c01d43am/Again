import subprocess
#-----------------------------------------------------------------------------------------------
def install_tool(tool_name):#tool_name is the name of the tool to be installed
    """Checks if a tool is installed and installs it if not found."""
    try:
        subprocess.run(["which", tool_name], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print(f"{tool_name} not found. Installing...")
        subprocess.run(["sudo", "apt", "install", "-y", tool_name], check=True)
#-----------------------------------------------------------------------------------------------
def check_and_install_nikto():#nikto is a tool for web server scanning
    """Checks if Nikto is installed. Installs it if not found."""
    install_tool("nikto")
    
def check_and_install_skipfish():#skipfish is a tool for web application security scanning
    """Checks if Skipfish is installed. Installs it if not found."""
    install_tool("skipfish")
#-----------------------------------------------------------------------------------------------
def run_nikto_scan(subdomain):#subdomain is the target nikto is scanning
    """Run Nikto scan for vulnerabilities."""
    check_and_install_nikto()
    print(f"\nRunning Nikto scan for {subdomain}...")
    try:
        subprocess.run(f"nikto -h {subdomain}", shell=True, check=True)
        print(f"Nikto scan completed for {subdomain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run Nikto scan for {subdomain}: {e}")
#-----------------------------------------------------------------------------------------------
def run_skipfish_scan(subdomain, options):
    """Run Skipfish scan for vulnerabilities."""
    check_and_install_skipfish()
    print(f"\nRunning Skipfish scan for {subdomain} with options: {options}...")
    try:
        subprocess.run(f"skipfish {options} -o output {subdomain}", shell=True, check=True)
        print(f"Skipfish scan completed for {subdomain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run Skipfish scan for {subdomain}: {e}")

def skipfish_menu():
    """Menu to select Skipfish scanning options."""
    print("\nSelect Skipfish scan mode:")
    print("1. Basic Scan")
    print("2. Authenticated Scan (Basic Auth)")
    print("3. Scan with Proxy")
    print("4. Rate-Limited Scan")
    print("5. Custom Wordlist Scan")
    print("6. Ignore URLs with Specific Keywords")
    print("7. Back to Main Menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        options = ""
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        options = f"-A {username}:{password}"
    elif choice == "3":
        proxy = input("Enter proxy (e.g., http://127.0.0.1:8080): ")
        options = f"-J {proxy}"
    elif choice == "4":
        rate = input("Enter requests per second (e.g., 2): ")
        options = f"-r {rate}"
    elif choice == "5":
        wordlist = input("Enter path to custom wordlist: ")
        options = f"-W {wordlist}"
    elif choice == "6":
        keyword = input("Enter keyword to ignore (e.g., logout): ")
        options = f"-X {keyword}"
    elif choice == "7":
        return
    else:
        print("Invalid choice. Returning to menu.")
        return

    subdomain = input("Enter the subdomain to scan with Skipfish: ")
    run_skipfish_scan(subdomain, options)
#-----------------------------------------------------------------------------------------------
def Vulunscan_menu():#menu for the user to choose the tool
    while True:
        print("\nNikto Automation Menu:")
        print( "1. Nikto Scan")
        print( "2. Skipfish Scan")
        print( "3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            subdomain = input("Enter the subdomain to scan with Nikto: ")
            run_nikto_scan(subdomain)
        elif choice == "2":
            skipfish_menu()(subdomain)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Vulunscan_menu()
#-----------------------------------------------------------------------------------------------