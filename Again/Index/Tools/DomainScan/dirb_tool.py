import os

def is_dirbuster_installed():
    """Check if DirBuster is installed using the `which` command."""
    return os.system("which dirbuster > /dev/null 2>&1") == 0

def install_dirbuster():
    """Install DirBuster only if it's not installed."""
    if is_dirbuster_installed():
        print("[+] DirBuster is already installed.")
        return True  # Prevents reinstallation

    print("[+] Installing DirBuster...")
    os.system("sudo apt update && sudo apt install -y dirbuster")

    if is_dirbuster_installed():
        print("[+] DirBuster installation successful.")
        return True
    else:
        print("[-] DirBuster installation failed. Please check your package manager.")
        return False

def run_dirbuster(target_url, wordlist="/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt", threads=10, file_ext="php,html,txt"):
    """Run DirBuster with specified parameters."""
    if not is_dirbuster_installed():
        if not install_dirbuster():
            print("[-] DirBuster installation failed. Cannot proceed.")
            return

    command = f"dirbuster -u {target_url} -w {wordlist} -t {threads} -e {file_ext}"

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
