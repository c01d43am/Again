import os
import subprocess

def is_dirbuster_installed():
    """Check if DirBuster is installed and if the JAR file exists."""
    return os.path.exists("/usr/share/dirbuster/dirbuster.jar")  # Corrected path

def install_dirbuster():
    """Install DirBuster if not installed."""
    print("[+] Installing DirBuster...")
    os.system("sudo apt update && sudo apt install -y dirbuster")
    
    # Verify installation after installing
    if not is_dirbuster_installed():
        print("[-] DirBuster installation failed. Please check your package manager.")
        return False
    
    return True

def run_dirbuster(target_url, wordlist="/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt", threads=10, file_ext="php,html,txt"):
    """Run DirBuster with specified parameters."""
    if not is_dirbuster_installed():
        if not install_dirbuster():
            print("[-] DirBuster installation failed. Cannot proceed.")
            return
    
    dirbuster_path = "/usr/share/dirbuster/dirbuster.jar"  # Corrected path
    command = (
        f"java -jar {dirbuster_path} -u {target_url} "
        f"-w {wordlist} -t {threads} -e {file_ext}"
    )
    
    print(f"[+] Running DirBuster on {target_url}...")
    os.system(command)

def menu():
    """Display menu options for running DirBuster."""
    while True:
        print("\nChoose an option:")
        print("1. Run DirBuster")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            target_url = input("Enter target URL: ")
            wordlist = input("Enter wordlist path (default: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt): ") or "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
            threads = input("Enter number of threads (default: 10): ") or "10"
            file_ext = input("Enter file extensions to search (default: php,html,txt): ") or "php,html,txt"
            run_dirbuster(target_url, wordlist, threads, file_ext)
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
