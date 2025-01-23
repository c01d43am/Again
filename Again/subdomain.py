import os
import sys
import requests
import subprocess
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def check_and_install(module_name):
    try:
        __import__(module_name)
    except ImportError:
        print(f"[INFO] Installing {module_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])

def install_pip():
    try:
        import pip
    except ImportError:
        print("[INFO] Installing pip...")
        subprocess.check_call(["sudo", "apt-get", "install", "-y", "python3-pip"])
        
        # Ensure pip is updated after installation
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

# Ensure pip is installed
install_pip()

# Ensure required libraries are installed
for module in ["requests", "bs4"]:
    check_and_install(module)

def bing_search(domain):
    print("[INFO] Searching Bing for subdomains...")
    subdomains = set()
    base_url = "https://www.bing.com/search?q=site:%s"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(base_url % domain, headers=headers, timeout=10)
        print(f"[INFO] Bing search status code: {response.status_code}")  # Log status code
        print(f"[INFO] Bing search page size: {len(response.content)} bytes")  # Log page size
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.find_all("a")
            for link in links:
                href = link.get("href")
                if href:
                    parsed_url = urlparse(href)
                    if parsed_url.hostname and domain in parsed_url.hostname:
                        subdomains.add(parsed_url.hostname)
    except Exception as e:
        print(f"[ERROR] Bing search failed: {e}")
    return subdomains

def crt_sh_search(domain):
    print("[INFO] Searching crt.sh for subdomains...")
    subdomains = set()
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=10)
        print(f"[INFO] crt.sh search status code: {response.status_code}")  # Log status code
        print(f"[INFO] crt.sh search page size: {len(response.content)} bytes")  # Log page size
        if response.status_code == 200:
            json_data = response.json()
            for entry in json_data:
                subdomain = entry["name_value"]
                subdomains.update(subdomain.split("\n"))
    except Exception as e:
        print(f"[ERROR] crt.sh search failed: {e}")
    return subdomains

def enumerate_subdomains(domain):
    print(f"[INFO] Starting subdomain enumeration for: {domain}")
    all_subdomains = set()

    # Bing search
    bing_subdomains = bing_search(domain)
    all_subdomains.update(bing_subdomains)

    # crt.sh search
    crt_sh_subdomains = crt_sh_search(domain)
    all_subdomains.update(crt_sh_subdomains)

    # Print results
    print("\n[RESULTS] Subdomains found:")
    for subdomain in sorted(all_subdomains):
        print(subdomain)

    # Save to file
    with open(f"{domain}_subdomains.txt", "w") as file:
        for subdomain in sorted(all_subdomains):
            file.write(subdomain + "\n")
    print(f"\n[INFO] Results saved to {domain}_subdomains.txt")

if __name__ == "__main__":
    target_domain = input("Enter the target domain: ").strip()
    if target_domain:
        enumerate_subdomains(target_domain)
    else:
        print("[ERROR] Please provide a valid domain.")