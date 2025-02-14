import subprocess
import os
import sys
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Support.utils import install_tool

def is_feroxbuster_installed():
    """Check if Feroxbuster is installed."""
    try:
        subprocess.run(["feroxbuster", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def install_feroxbuster():
    """Install Feroxbuster if not installed."""
    print("[+] Installing Feroxbuster...")
    install_tool("feroxbuster", "feroxbuster")

def run_feroxbuster(target_url, wordlist="/usr/share/wordlists/dirb/common.txt", filters="", recursion=False, extensions="", proxy="", threads=50, delay=0, output=""):
    """Run Feroxbuster with customizable options."""
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
        print("9. Automated Scan")
        print("10. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "10":
            break
        
        while True:
            target_url = input("Enter target URL (must start with http:// or https://): ")
            if re.match(r"^https?://", target_url):
                break
            else:
                print("Invalid URL. Please enter a valid URL starting with http:// or https://")
        
        wordlist = "/usr/share/wordlists/dirb/common.txt"
        filters = ""
        recursion = False
        extensions = ""
        proxy = ""
        threads = 50
        delay = 0
        output = ""
        
        if choice == "2":
            wordlist = input("Enter wordlist path: ")
        elif choice == "3":
            filters = input("Enter status codes to filter (comma-separated): ")
        elif choice == "4":
            recursion = True
        elif choice == "5":
            extensions = input("Enter file extensions (comma-separated): ")
        elif choice == "6":
            proxy = input("Enter proxy (e.g., http://127.0.0.1:8080): ")
        elif choice == "7":
            threads = int(input("Enter number of threads: "))
            delay = int(input("Enter delay in seconds: "))
        elif choice == "8":
            output = input("Enter output file path: ")
        elif choice == "9":
            recursion = True
            filters = "403,404"
            extensions = "php,html,txt"
            threads = 100
            delay = 1
        
        run_feroxbuster(target_url, wordlist, filters, recursion, extensions, proxy, threads, delay, output)

if __name__ == "__main__":
    feroxbuster_menu()