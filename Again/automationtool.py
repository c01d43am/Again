# Description: A tool to perform reconnaissance on a domain or subdomain. 
# The tool checks and installs required tools like Nmap, sslscan, dirb, Nikto, and feroxbuster. 
# It then provides a menu to run scans on subdomains using these tools. 
# The user can choose to run Dirb, Nmap, Nikto, SSLscan, or Feroxbuster scans on a subdomain.
import os
import subprocess
from utils import install_tool

#-------------------------------------------------------------------------------------------------------------
def check_and_install_nmap():
    """Checks if Nmap is installed. Installs it if not found."""
    install_tool("nmap")

#-------------------------------------------------------------------------------------------------------------
def check_and_install_sslscan():
    """Checks if sslscan is installed. Installs it if not found."""
    install_tool("sslscan")

#-------------------------------------------------------------------------------------------------------------
def check_and_install_dirb():
    """Checks if dirb is installed. Installs it if not found."""
    install_tool("dirb")

#-------------------------------------------------------------------------------------------------------------
def check_and_install_nikto():
    """Checks if Nikto is installed. Installs it if not found."""
    install_tool("nikto")

#-------------------------------------------------------------------------------------------------------------
def is_feroxbuster_installed():
    """Check if feroxbuster is installed."""
    try:
        subprocess.run(["feroxbuster", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except FileNotFoundError:
        return False

def install_feroxbuster():
    """Install feroxbuster if not installed."""
    print("[+] Installing feroxbuster...")
    os.system("sudo apt update && sudo apt install -y feroxbuster")

def run_feroxbuster(target_url, wordlist="/usr/share/wordlists/dirb/common.txt"):
    """Run feroxbuster with the given target URL and wordlist."""
    if not is_feroxbuster_installed():
        install_feroxbuster()
    print(f"[+] Running feroxbuster on {target_url}...")
    os.system(f"feroxbuster -u {target_url} -w {wordlist}")

#-------------------------------------------------------------------------------------------------------------
def is_gobuster_installed():
    """Check if gobuster is installed."""
    try:
        subprocess.run(["gobuster", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except FileNotFoundError:
        return False

def install_gobuster():
    """Install gobuster if not installed."""
    print("[+] Installing gobuster...")
    os.system("sudo apt update && sudo apt install -y gobuster")

def run_gobuster(target_url, wordlist="/usr/share/wordlists/dirb/common.txt"):
    """Run gobuster with the given target URL and wordlist."""
    if not is_gobuster_installed():
        install_gobuster()
    if is_gobuster_installed():
        print(f"[+] Running gobuster on {target_url}...")
        os.system(f"gobuster dir -u {target_url} -w {wordlist}")
    else:
        print("Failed to install gobuster. Please check your repository settings and try again.")

#-------------------------------------------------------------------------------------------------------------
def run_nmap_scan(subdomain, scan_type="full"):
    """Run an Nmap scan on the subdomain to check for open ports."""
    check_and_install_nmap()
    print(f"\nRunning Nmap scan on {subdomain} (Scan Type: {scan_type})...")
    try:
        if scan_type == "fast":
            subprocess.run(f"nmap -Pn -T4 -F {subdomain}", shell=True, check=True)  # Fast scan
        else:
            subprocess.run(f"nmap -Pn {subdomain}", shell=True, check=True)  # Full scan
        print(f"Nmap scan completed for {subdomain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run Nmap scan for {subdomain}: {e}")

#-------------------------------------------------------------------------------------------------------------
def run_nikto_scan(subdomain):
    """Run Nikto scan for vulnerabilities."""
    check_and_install_nikto()
    print(f"\nRunning Nikto scan for {subdomain}...")
    try:
        subprocess.run(f"nikto -h {subdomain}", shell=True, check=True)
        print(f"Nikto scan completed for {subdomain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run Nikto scan for {subdomain}: {e}")

#-------------------------------------------------------------------------------------------------------------
def run_sslscan(subdomain):
    """Run sslscan to check for SSL/TLS vulnerabilities."""
    check_and_install_sslscan()
    print(f"\nRunning SSL/TLS scan for {subdomain}...")
    try:
        subprocess.run(f"sslscan {subdomain}", shell=True, check=True)
        print(f"SSL/TLS scan completed for {subdomain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run SSL/TLS scan for {subdomain}: {e}")

#-------------------------------------------------------------------------------------------------------------
def run_dirb_scan(subdomain):
    """Run Dirb scan to check for directories and files."""
    check_and_install_dirb()
    print(f"[+] Running Dirb scan on {subdomain}...")
    try:
        subprocess.run(f"dirb http://{subdomain}", shell=True, check=True)
        print(f"Dirb scan completed for {subdomain}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run Dirb scan for {subdomain}: {e}")

#------------------------------------------------------------------------------------------------------------