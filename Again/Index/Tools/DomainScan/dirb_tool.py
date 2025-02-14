import subprocess
import os
import sys
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Add parent directory to path so we can import utils

from Again.Index.Tools.Support.install_tool import install_tool # Import the install_tool function from the utils module

# Function to automate Dirb
def start_dirb(target_url, wordlist=None, threads=10, file_ext="php,html,txt", ignore_403=False, save_output=False, proxy=None, user_agent=None, cookies=None, auth=None):
    print("\nAutomating Dirb...\n")
    install_tool("dirb", "dirb")  # Ensure Dirb is installed
    
    command = f"dirb {target_url}"
    
    if wordlist:
        command += f" {wordlist}"
    
    command += " -r"
    
    if ignore_403:
        command += " -N 403"
    
    if save_output:
        command += " -o dirb_results.txt"
    
    if file_ext:
        command += f" -X {file_ext}"
    
    if proxy:
        command += f" -p {proxy}"
    
    if user_agent:
        command += f" -A \"{user_agent}\""
    
    if cookies:
        command += f" -c \"{cookies}\""
    
    if auth:
        command += f" -u {auth}"
    
    try:
        print(f"[+] Running Dirb on {target_url}...")
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting Dirb: {e}")

# Submenu for Dirb Automation
def dirb_submenu():
    while True:
        print("\nDirb Automation Options:")
        print("1. Recursive Scan")
        print("2. Custom Wordlist Scan")
        print("3. Ignore 403 Forbidden Responses")
        print("4. Use a Proxy")
        print("5. Specify User-Agent")
        print("6. Use Cookies for Authentication")
        print("7. Use Basic Authentication")
        print("8. Exit")
        
        choice = input("Enter your choice [1-8]: ")
        
        if choice == "8":
            break
        
        while True:
            target_url = input("Enter target URL (must start with http:// or https://): ")
            if re.match(r"^https?://", target_url):
                break
            else:
                print("Invalid URL. Please enter a valid URL starting with http:// or https://")
        
        wordlist = None
        ignore_403 = False
        save_output = input("Save output to a file? (y/n): ").strip().lower() == "y"
        file_ext = input("Enter file extensions to search (default: php,html,txt): ") or "php,html,txt"
        proxy = None
        user_agent = None
        cookies = None
        auth = None
        
        if choice == "2":
            wordlist = input("Enter wordlist path: ")
        elif choice == "3":
            ignore_403 = True
        elif choice == "4":
            proxy = input("Enter proxy (e.g., 127.0.0.1:8080): ")
        elif choice == "5":
            user_agent = input("Enter User-Agent string: ")
        elif choice == "6":
            cookies = input("Enter cookies (e.g., PHPSESSID=1234567890): ")
        elif choice == "7":
            auth = input("Enter credentials (username:password): ")
        
        start_dirb(target_url, wordlist, file_ext=file_ext, ignore_403=ignore_403, save_output=save_output, proxy=proxy, user_agent=user_agent, cookies=cookies, auth=auth)

if __name__ == "__main__":
    dirb_submenu()
