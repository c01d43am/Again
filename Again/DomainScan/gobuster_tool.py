import os
import subprocess

def is_tool_installed(tool):
    """Check if a tool is installed."""
    try:
        subprocess.run([tool, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def install_tool(tool):
    """Install a tool if not installed."""
    print(f"[+] Installing {tool}...")
    os.system(f"sudo apt update && sudo apt install -y {tool}")

def run_gobuster(mode, target, wordlist, additional_args=""):
    """Run Gobuster in different modes."""
    if not is_tool_installed("gobuster"):
        install_tool("gobuster")
    
    command = f"gobuster {mode} -u {target} -w {wordlist} {additional_args}"
    print(f"[+] Running Gobuster in {mode} mode on {target}...")
    os.system(command)

def menu():
    """Display menu options for running gobuster."""
    while True:
        print("\nChoose an option:")
        print("1. Run Gobuster - dir mode")
        print("2. Run Gobuster - dns mode")
        print("3. Run Gobuster - vhost mode")
        print("4. Run Gobuster - s3 mode")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            target = input("Enter target URL: ")
            wordlist = input("Enter wordlist path: ")
            additional_args = input("Enter additional arguments (optional): ")
            run_gobuster("dir", target, wordlist, additional_args)
        elif choice == "2":
            target = input("Enter domain: ")
            wordlist = input("Enter wordlist path: ")
            additional_args = input("Enter additional arguments (optional): ")
            run_gobuster("dns", target, wordlist, additional_args)
        elif choice == "3":
            target = input("Enter target URL: ")
            wordlist = input("Enter wordlist path: ")
            additional_args = input("Enter additional arguments (optional): ")
            run_gobuster("vhost", target, wordlist, additional_args)
        elif choice == "4":
            wordlist = input("Enter wordlist path: ")
            additional_args = input("Enter additional arguments (optional): ")
            run_gobuster("s3", "", wordlist, additional_args)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
