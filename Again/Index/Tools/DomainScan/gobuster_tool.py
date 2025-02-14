import os
import subprocess
import shutil
from Again.Index.Tools.Support.install_tool import install_tool

def run_gobuster(mode, target, wordlist, additional_args):
    """Run Gobuster with user-selected options."""
    if not shutil.which("gobuster"):
        install_tool("gobuster")  # Ensure Gobuster is installed
    
    command = ["gobuster", mode, "-w", wordlist]
    
    if mode in ["dir", "dns", "vhost"] and target:
        command.extend(["-u", target])
    
    if additional_args:
        command.extend(additional_args.split())
    
    print(f"[+] Running: {' '.join(command)}")
    subprocess.run(command)

def gobuster_menu():
    """Gobuster submenu for selecting scan mode."""
    while True:
        print("\nGobuster Menu:")
        print("1. Directory Scan (dir mode)")
        print("2. DNS Subdomain Scan (dns mode)")
        print("3. Virtual Host Scan (vhost mode)")
        print("4. S3 Bucket Scan (s3 mode)")
        print("5. Exit")
        
        choice = input("Enter your choice [1-5]: ")
        
        if choice in ["1", "2", "3", "4"]:
            target = "" if choice == "4" else input("Enter target (URL/domain): ").strip()
            wordlist = input("Enter wordlist path: ").strip()
            additional_args = input("Enter additional arguments (optional): ").strip()
            mode = {"1": "dir", "2": "dns", "3": "vhost", "4": "s3"}[choice]
            run_gobuster(mode, target, wordlist, additional_args)
        elif choice == "5":
            print("Exiting Gobuster menu...")
            break
        else:
            print("[!] Invalid choice. Try again.")

def main():
    """Check if Gobuster is installed, then open the menu."""
    if not shutil.which("gobuster"):
        install_tool("gobuster")
    print("[+] Gobuster is ready.")
    gobuster_menu()

if __name__ == "__main__":
    main()
