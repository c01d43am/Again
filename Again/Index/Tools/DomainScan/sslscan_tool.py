import subprocess
import shutil

def is_tool_installed(tool_name):
    """Check if a tool is installed."""
    return shutil.which(tool_name) is not None

def install_tool(tool_name):
    """Install the given tool using the available package manager."""
    print(f"Attempting to install {tool_name}...")
    if shutil.which("apt"):
        subprocess.run(["sudo", "apt", "install", "-y", tool_name], check=True)
    elif shutil.which("brew"):
        subprocess.run(["brew", "install", tool_name], check=True)
    else:
        print(f"Package manager not found. Install {tool_name} manually.")
        return False
    return is_tool_installed(tool_name)

def check_and_install_sslscan():
    """Checks if sslscan is installed. Installs it if not found."""
    if is_tool_installed("sslscan"):
        print("sslscan is already installed.")
        return True
    
    print("sslscan not found. Installing...")
    if install_tool("sslscan"):
        print("sslscan installed successfully.")
        return True
    else:
        print("Failed to install sslscan. Please install it manually.")
        return False

def run_sslscan(subdomain):
    """Run sslscan to check for SSL/TLS vulnerabilities."""
    if check_and_install_sslscan():
        print(f"\nRunning SSL/TLS scan for {subdomain}...")
        try:
            subprocess.run(["sslscan", subdomain], check=True)
            print(f"SSL/TLS scan completed for {subdomain}.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to run SSL/TLS scan for {subdomain}: {e}")

if __name__ == "__main__":
    subdomain = input("Enter the subdomain to scan with SSLscan: ").strip()
    if subdomain:
        run_sslscan(subdomain)
    else:
        print("Invalid input. Please enter a valid subdomain.")
