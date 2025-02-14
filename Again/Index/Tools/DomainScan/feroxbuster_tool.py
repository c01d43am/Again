import os
import subprocess

def is_feroxbuster_installed():
    """Check if feroxbuster is installed."""
    try:
        subprocess.run(["feroxbuster", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def install_feroxbuster():
    """Install feroxbuster if not installed."""
    print("[+] Installing feroxbuster...")
    os.system("sudo apt update && sudo apt install -y feroxbuster")

def run_feroxbuster(target_url, wordlist="/usr/share/wordlists/dirb/common.txt", filters="", recursion=False, extensions="", proxy="", threads=50, delay=0, output=""):
    """Run feroxbuster with various options."""
    
    # Check if feroxbuster is installed, if not, install it
    if not is_feroxbuster_installed():
        print("[!] Feroxbuster is not installed. Installing now...")
        install_feroxbuster()
    else:
        print("[+] Feroxbuster is already installed. Running scan...")

    command = f"feroxbuster -u {target_url} -w {wordlist}"
    
    if filters:
        command += f" -C {filters}"
    if recursion:
        command += " -r"
    if extensions:
        command += f" -x {extensions}"
    if proxy:
        command += f" --proxy {proxy}"
    if threads:
        command += f" -t {threads}"
    if delay:
        command += f" -s {delay}"
    if output:
        command += f" -o {output}"
    
    print(f"[+] Running: {command}")
    os.system(command)

def feroxbuster_menu():
    while True:
        print("\n[Feroxbuster Menu]")
        print("1. Run Basic Scan")
        print("2. Set Custom Wordlist")
        print("3. Filter by Status Codes")
        print("4. Enable Recursion")
        print("5. Set File Extensions")
        print("6. Use Proxy")
        print("7. Set Threads and Delay")
        print("8. Save Output")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            target_url = input("Enter target URL: ")
            run_feroxbuster(target_url)
        elif choice == "2":
            target_url = input("Enter target URL: ")
            wordlist = input("Enter wordlist path: ")
            run_feroxbuster(target_url, wordlist=wordlist)
        elif choice == "3":
            target_url = input("Enter target URL: ")
            filters = input("Enter status codes (comma-separated): ")
            run_feroxbuster(target_url, filters=filters)
        elif choice == "4":
            target_url = input("Enter target URL: ")
            run_feroxbuster(target_url, recursion=True)
        elif choice == "5":
            target_url = input("Enter target URL: ")
            extensions = input("Enter file extensions (comma-separated): ")
            run_feroxbuster(target_url, extensions=extensions)
        elif choice == "6":
            target_url = input("Enter target URL: ")
            proxy = input("Enter proxy (e.g., http://127.0.0.1:8080): ")
            run_feroxbuster(target_url, proxy=proxy)
        elif choice == "7":
            target_url = input("Enter target URL: ")
            threads = input("Enter number of threads: ")
            delay = input("Enter delay in seconds: ")
            run_feroxbuster(target_url, threads=int(threads), delay=int(delay))
        elif choice == "8":
            target_url = input("Enter target URL: ")
            output = input("Enter output file path: ")
            run_feroxbuster(target_url, output=output)
        elif choice == "9":
            break
        else:
            print("Invalid choice, please try again.")
