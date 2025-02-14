import subprocess
import os
import sys
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Support.utils import install_tool

# Function to automate Dirb
def start_dirb(target_url, wordlist=None, threads=10, file_ext="php,html,txt"):
    print("\nAutomating Dirb...\n")
    install_tool("dirb", "dirb")  # Ensure Dirb is installed
    
    if wordlist is None:
        command = f"dirb {target_url} -r -o dirb_results.txt"
    else:
        command = f"dirb {target_url} {wordlist} -r -o dirb_results.txt"
    
    try:
        print(f"[+] Running Dirb on {target_url}...")
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting Dirb: {e}")

# Submenu for Dirb Automation
def dirb_submenu():
    while True:
        print("\nDirb Automation Options:")
        print("1. Run Dirb Scan")
        print("2. Back to Automation Menu")
        
        choice = input("Enter your choice [1-2]: ")
        
        if choice == "1":
            while True:
                target_url = input("Enter target URL (must start with http:// or https://): ")
                if re.match(r"^https?://", target_url):
                    break
                else:
                    print("Invalid URL. Please enter a valid URL starting with http:// or https://")
            
            use_wordlist = input("Do you want to specify a wordlist? (y/n): ").strip().lower()
            
            if use_wordlist == "y":
                wordlist = input("Enter wordlist path: ")
            else:
                wordlist = None
            
            threads = input("Enter number of threads (default: 10): ") or "10"
            file_ext = input("Enter file extensions to search (default: php,html,txt): ") or "php,html,txt"
            start_dirb(target_url, wordlist, threads, file_ext)
        elif choice == "2":
            break
        else:
            print("Invalid choice, please try again.")