# Again Tool

**Author:** [c01d43am](https://github.com/c01d43am)  

## Overview

`Again` is a Python-based penetration testing tool designed for security professionals and ethical hackers. It provides a modular menu-driven interface for automating tasks such as vulnerability scanning, reconnaissance, and exploit execution. This tool simplifies the workflow by integrating multiple security tools into a single framework.

## Features

- **Automation:** Automate security tasks such as vulnerability scanning.
- **Reconnaissance:** Perform domain enumeration and content discovery.
- **Exploits:** Test for known vulnerabilities using automated tools.
- **Extensibility:** Easily customizable to include new modules and tools.
- **Auto-Update:** Fetches the latest changes from the repository automatically.

## Modules

### 1. Automation Tool  
Automates security scanning with the following tools:
- **Nessus** (Vulnerability Scanning)
- **Armitage** (Metasploit GUI)
- **Akto** (API Security Testing)

### 2. Domain (Recon & Scanning)  
Performs reconnaissance and scanning using:
- **Dirb** (Directory Brute Force)
- **SSLScan** (SSL/TLS Security Check)
- **Feroxbuster** (Content Discovery)
- **Gobuster** (Subdomain & Directory Enumeration)
- **Nmap** (Network Scanning)

### 3. Vulnerability Scanning  
Detects vulnerabilities using:
- **Nikto** (Web Server Security Scan)
- **Skipfish** (Automated Web Vulnerability Scan)

### 4. Exploits  
Tests for known exploits using:
- **SQLMap** (SQL Injection Testing)

## Prerequisites

Ensure the following dependencies are installed before running `Again`:

- **Python 3.8+**
- `git` (for fetching updates)
- Third-party security tools (e.g., Nessus, Nikto, Armitage, etc.)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/c01d43am/Again.git
   cd Again
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tool:
   ```bash
   python again.py
   ```

## Usage

1. Execute the script:
   ```bash
   python again.py
   ```

2. Choose an option from the interactive menu:
   - **1**: Automation Tool
   - **2**: Domain Recon & Scanning
   - **3**: Vulnerability Scanning
   - **4**: Exploits
   - **5**: Exit

## Example Output

```plaintext
░█████╗░░██████╗░░█████╗░██╗███╗░░██╗░█████╗░
██╔══██╗██╔════╝░██╔══██╗██║████╗░██║██╔══██╗
███████║██║░░██╗░███████║██║██╔██╗██║╚═╝███╔╝
██╔══██║██║░░╚██╗██╔══██║██║██║╚████║░░░╚══╝░
██║░░██║╚██████╔╝██║░░██║██║██║░╚███║░░░██╗░░
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░╚═╝░░

https://github.com/c01d43am

v1.0.0 by c01d43am
```

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with your changes.

## License

This project is licensed under the **GNU General Public License v2.0**. See the `LICENSE` file for details.

## Disclaimer

This tool is intended for educational and ethical hacking purposes only. The author is not responsible for any misuse or illegal activities conducted using this tool.

