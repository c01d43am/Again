import subprocess
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Support.utils import install_tool

# Function to automate DirBuster
def start_dirbuster(target_url, wordlist="/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt", threads=10, file_ext="php,html,txt"):
    print("\nAutomating DirBuster...\n")
    install_tool("dirbuster", "dirbuster")  # Ensure DirBuster is installed
    
    command = f"dirbuster -u {target_url} -w {wordlist} -t {threads} -e {file_ext}"
    
    try:
        print(f"[+] Running DirBuster on {target_url}...")
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting DirBuster: {e}")

# Submenu for DirBuster Automation
def dirbuster_submenu():
    while True:
        print("\nDirBuster Automation Options:")
        print("1. Run DirBuster Scan")
        print("2. Back to Automation Menu")
        
        choice = input("Enter your choice [1-2]: ")
        
        if choice == "1":
            target_url = input("Enter target URL: ")
            wordlist = input("Enter wordlist path (default: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt): ") or "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
            threads = input("Enter number of threads (default: 10): ") or "10"
            file_ext = input("Enter file extensions to search (default: php,html,txt): ") or "php,html,txt"
            start_dirbuster(target_url, wordlist, threads, file_ext)
        elif choice == "2":
            break
        else:
            print("Invalid choice, please try again.")
