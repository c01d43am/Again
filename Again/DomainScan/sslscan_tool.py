import subprocess
from Again.Support.utils import install_tool

def check_and_install_sslscan():
    """Checks if sslscan is installed. Installs it if not found."""
    install_tool("sslscan")

def run_sslscan(subdomain):
    """Run sslscan to check for SSL/TLS vulnerabilities."""
    check_and_install_sslscan()
    print(f"\nRunning SSL/TLS scan for {subdomain}...")
    try:
        subprocess.run(f"sslscan {subdomain}", shell=True, check=True)
        print(f"SSL/TLS scan completed for {subdomain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run SSL/TLS scan for {subdomain}: {e}")

if __name__ == "__main__":
    subdomain = input("Enter the subdomain to scan with SSLscan: ")
    run_sslscan(subdomain)