import subprocess

def install_tool(tool_name):
    """Checks if a tool is installed and installs it if not found."""
    try:
        subprocess.run(["which", tool_name], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print(f"{tool_name} not found. Installing...")
        subprocess.run(["sudo", "apt", "install", "-y", tool_name], check=True)

def check_and_install_skipfish():
    """Checks if Skipfish is installed. Installs it if not found."""
    install_tool("skipfish")

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

if __name__ == "__main__":
    skipfish_menu()