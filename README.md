# Again Tool

**Version:** v0.0.7  
**Author:** [c01d43am](https://github.com/c01d43am)  

## Overview

`Again` is a Python-based tool designed for penetration testers and security enthusiasts. It provides a modular menu-driven interface to automate tasks such as vulnerability scanning, subdomain enumeration, and exploit execution. This tool simplifies the workflow for ethical hacking and automates common security operations.

## Features

- **Automation**: Perform vulnerability scans and other security tasks efficiently.
- **Domain Enumeration**: Identify subdomains for target websites.
- **Exploit Tools**: Test for known exploits and vulnerabilities.
- **Extensibility**: Easily customizable and extendable to include new modules and tools.

## Modules

1. **Automation Tool**  
   Automates vulnerability scanning with tools like OpenVAS, Nessus, Armitage, and Nikto.

2. **Domain**  
   Performs subdomain enumeration and related tasks.

3. **Exploits**  
   Leverages tools for exploiting known vulnerabilities.

## Prerequisites

Before running this tool, ensure the following are installed:

- **Python 3.8+**
- `git` for fetching updates.
- Supported third-party tools (e.g., OpenVAS, Nessus, Nikto).

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

1. Run the script:
   ```bash
   python again.py
   ```

2. Select an option from the menu:
   - **1**: Automation Tool
   - **2**: Domain
   - **3**: Exploits
   - **4**: Exit

## How It Works

`Again` provides a modular structure:
- The **Automation** module installs and starts tools like Nessus, OpenVAS, etc.
- The **Domain** module focuses on subdomain enumeration.
- The **Exploits** module integrates various exploit scripts.

The script also includes an **auto-update feature**, pulling the latest changes from the repository automatically on execution.

## Example

```plaintext
░█████╗░░██████╗░░█████╗░██╗███╗░░██╗░█████╗░
██╔══██╗██╔════╝░██╔══██╗██║████╗░██║██╔══██╗
███████║██║░░██╗░███████║██║██╔██╗██║╚═╝███╔╝
██╔══██║██║░░╚██╗██╔══██║██║██║╚████║░░░╚══╝░
██║░░██║╚██████╔╝██║░░██║██║██║░╚███║░░░██╗░░
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░╚═╝░░

https://github.com/c01d43am

v0.0.8 by c01d43am
```

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with your changes.

## License

This project is licensed under the **GNU General Public License v2.0**. See the `LICENSE` file for details.

## Disclaimer

This tool is intended for educational purposes and ethical hacking only. The author is not responsible for any misuse.

---

Feel free to modify the content to align with the specific purpose of your tool. Let me know if you need any additional sections! 🚀
