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

def run_gobuster(mode, target="", wordlist="", additional_args=""):
    """Run Gobuster in different modes."""
    command = f"gobuster {mode} -w {wordlist}"
    
    if mode in ["dir", "dns", "vhost"] and target:
        command += f" -u {target}"
    
    if additional_args:
        command += f" {additional_args}"

    print(f"[+] Running: {command}")
    os.system(command)

def gobuster_menu():
    """Gobuster submenu for selecting scan modes."""
    while True:
        print("\nGobuster Menu:")
        print("1. Directory Scan (dir mode)")
        print("2. DNS Subdomain Scan (dns mode)")
        print("3. Virtual Host Scan (vhost mode)")
        print("4. S3 Bucket Scan (s3 mode)")
        print("5. Exit")

        choice = input("Enter your choice [1-5]: ")

        if choice == "1":
            target = input("Enter target URL (e.g., https://example.com): ").strip()
            wordlist = input("Enter wordlist path: ").strip()
            additional_args = input("Enter additional arguments (optional): ").strip()
            run_gobuster("dir", target, wordlist, additional_args)
        elif choice == "2":
            target = input("Enter domain (e.g., example.com): ").strip()
            wordlist = input("Enter wordlist path: ").strip()
            additional_args = input("Enter additional arguments (optional): ").strip()
            run_gobuster("dns", target, wordlist, additional_args)
        elif choice == "3":
            target = input("Enter target URL (e.g., https://example.com): ").strip()
            wordlist = input("Enter wordlist path: ").strip()
            additional_args = input("Enter additional arguments (optional): ").strip()
            run_gobuster("vhost", target, wordlist, additional_args)
        elif choice == "4":
            wordlist = input("Enter wordlist path: ").strip()
            additional_args = input("Enter additional arguments (optional): ").strip()
            run_gobuster("s3", "", wordlist, additional_args)
        elif choice == "5":
            print("Exiting Gobuster menu...")
            break
        else:
            print("[!] Invalid choice. Try again.")

def main():
    """Check if Gobuster is installed, then open the submenu."""
    if not is_tool_installed("gobuster"):
        print("[!] Gobuster is not installed. Installing now...")
        install_tool("gobuster")
    
    print("[+] Gobuster is ready.")
    gobuster_menu()

if __name__ == "__main__":
    main()
