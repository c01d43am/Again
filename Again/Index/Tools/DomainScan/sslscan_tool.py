import subprocess
import shutil

try:
    from Tools.Support.utils import install_tool
except ImportError:
    def install_tool(tool_name):
        """Fallback function to install tools if utils module is not available."""
        print(f"Attempting to install {tool_name}...")
        if shutil.which("apt"):
            subprocess.run(["sudo", "apt", "install", "-y", tool_name], check=True)
        elif shutil.which("brew"):
            subprocess.run(["brew", "install", tool_name], check=True)
        else:
            print(f"Package manager not found. Install {tool_name} manually.")

def ssl_is_tool_installed(tool_name):
    """Check if a tool is installed."""
    return shutil.which(tool_name) is not None

def check_and_install_sslscan():
    """Checks if sslscan is installed. Installs it if not found."""
    if ssl_is_tool_installed("sslscan"):
        print("sslscan is already installed.")
    else:
        print("sslscan not found. Installing...")
        install_tool("sslscan")
        if ssl_is_tool_installed("sslscan"):
            print("sslscan installed successfully.")
        else:
            print("Failed to install sslscan. Please install it manually.")
            return False
    return True

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