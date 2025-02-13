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
def run_nikto_scan(subdomain):#subdomain is the target
    """Run Nikto scan for vulnerabilities."""
    check_and_install_nikto()
    print(f"\nRunning Nikto scan for {subdomain}...")
    try:
        subprocess.run(f"nikto -h {subdomain}", shell=True, check=True)
        print(f"Nikto scan completed for {subdomain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run Nikto scan for {subdomain}: {e}")
#-----------------------------------------------------------------------------------------------
def run_skipfish_scan(subdomain):#subdomain is the target
    """Run Skipfish scan for vulnerabilities."""
    check_and_install_skipfish()
    print(f"\nRunning Skipfish scan for {subdomain}...")
    try:
        subprocess.run(f"skipfish -o scan_results {subdomain}", shell=True, check=True)
        print(f"Skipfish scan completed for {subdomain}.Results saved in scan_results folder.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run Skipfish scan for {subdomain}: {e}")
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
            subdomain = input("Enter the subdomain to scan with Skipfish: ")
            run_skipfish_scan(subdomain)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Vulunscan_menu()
#-----------------------------------------------------------------------------------------------