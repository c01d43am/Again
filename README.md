# Again Tool  

**Author:** [c01d43am](https://github.com/c01d43am)  

## Overview  

`Again` is a Python-based penetration testing tool designed for security professionals and ethical hackers. It provides a **modular, menu-driven interface** for automating security tasks such as **vulnerability scanning, reconnaissance, and exploit execution**. This tool simplifies workflows by integrating multiple security tools into a single framework.  

## Features  

✅ **Automation:** Automate security tasks like vulnerability scanning.  
✅ **Reconnaissance:** Perform domain enumeration and content discovery.  
✅ **Exploits:** Test for known vulnerabilities using automated tools.  
✅ **Extensibility:** Easily customizable to add new tools.  
✅ **Auto-Update:** Fetches the latest changes from the GitHub repository.  

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🤖 Automation Tools
- **Nessus** - Professional vulnerability scanner
- **Armitage** - GUI for Metasploit Framework
- **Akto** - Comprehensive API security testing

</td>
<td width="50%">

### 🔍 Reconnaissance & Scanning
- **Dirb** - Web content directory brute-forcing
- **SSLScan** - SSL/TLS protocol analyzer
- **Feroxbuster** - High-speed content discovery
- **Gobuster** - Directory/DNS/vhost enumeration
- **Nmap** - Network discovery and security auditing

</td>
</tr>
<tr>
<td width="50%">

### 🛡️ Vulnerability Assessment
- **Nikto** - Web server security scanner
- **Skipfish** - Active web application security testing
- **Wapiti** - Web application vulnerability scanner

</td>
<td width="50%">

### 💣 Exploitation Tools
- **SQLMap** - Automated SQL injection testing
- Custom exploit modules
- Integration-ready architecture

</td>
</tr>
</table>

---

## 📦 Installation

### Prerequisites

- **Python 3.8+** installed
- **Git** for cloning repository
- **pip** package manager
- Administrative privileges (for some tools)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/c01d43am/Again.git

# Navigate to directory
cd Again

# Install Python dependencies
pip install -r requirements.txt

# Run the tool
python again.py
```

### Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv .venv

# Activate (Linux/Mac)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the tool
python again.py
```

---

## 🚀 Usage

### Basic Usage

```bash
python again.py
```

The tool will:
1. ✅ Check for updates from GitHub
2. ⏳ Display loading animation
3. 🎨 Show the main menu interface

### Menu Navigation

```
╔═══════════════════════════════════════════╗
║         AGAIN - Main Menu                 ║
╠═══════════════════════════════════════════╣
║  1. 🤖 Automation Tools                   ║
║  2. 🔍 Domain Reconnaissance & Scanning   ║
║  3. 🛡️  Vulnerability Assessment          ║
║  4. 💣 Exploitation Tools                 ║
║  5. 🔧 Updates & System Check             ║
║  6. 🚪 Exit                               ║
╚═══════════════════════════════════════════╝
```

### Tool Management

The **Updates & Check** menu provides:
- ✅ Install all required security tools
- ❌ Uninstall tools
- 🔍 Check installation status
- ⚙️ System configuration verification

---

## 🛠️ Tools & Capabilities

### 1. 🤖 Automation Tools

| Tool | Purpose | Command |
|------|---------|---------|
| Nessus | Enterprise vulnerability scanner | Automated launch |
| Armitage | Metasploit GUI interface | Automated launch |
| Akto | API security testing platform | Automated launch |

### 2. 🔍 Domain Reconnaissance

| Tool | Purpose | Features |
|------|---------|----------|
| Dirb | Directory brute-forcing | Wordlist-based discovery |
| SSLScan | SSL/TLS analysis | Certificate & cipher testing |
| Feroxbuster | Fast content discovery | Multi-threaded scanning |
| Gobuster | DNS/subdomain enumeration | High-performance scanning |
| Nmap | Network mapping | Port scanning, OS detection |

### 3. 🛡️ Vulnerability Assessment

| Tool | Purpose | Coverage |
|------|---------|----------|
| Nikto | Web server scanning | 6700+ vulnerabilities |
| Skipfish | Web app security | Automated crawling & testing |
| Wapiti | Web vulnerability detection | XSS, SQL injection, etc. |

### 4. 💣 Exploitation

| Tool | Purpose | Capability |
|------|---------|------------|
| SQLMap | SQL injection testing | Database takeover automation |

---

## 📋 Requirements

### Python Dependencies

```
requests>=2.31.0       # HTTP library
beautifulsoup4>=4.12.0 # HTML parsing
lxml>=4.9.0            # XML/HTML processing
gitpython>=3.1.0       # Git integration
pyyaml>=6.0            # YAML parsing
colorama>=0.4.6        # Terminal colors
tabulate>=0.9.0        # Table formatting
rich>=13.0.0           # Enhanced terminal output
```

### External Tools (Optional)

Most security tools are installed automatically through the tool's management menu. Manual installation may be required for:
- Nessus (commercial license)
- Metasploit Framework
- Additional specialized tools

---

## 🔧 Configuration

### config.yaml

The configuration file supports CI/CD integration and automated testing:

```yaml
name: CI Pipeline
on: 
  push:
    branches:
      - main
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
      - name: Setup Python
      - name: Install Dependencies
      - name: Run Tests
```

---

## 🌐 Platform Compatibility

| Platform | Status | Notes |
|----------|--------|-------|
| 🐧 Linux | ✅ Fully Supported | Recommended environment |
| 🪟 Windows | ✅ Supported | PowerShell/CMD compatible |
| 🍎 macOS | ⚠️ Partial | Most features work |

---

## 📖 Documentation

### Project Structure

```
Again/
├── again.py              # Main entry point
├── requirements.txt      # Python dependencies
├── config.yaml          # CI/CD configuration
├── default.sh           # Global installation script
├── Again/
│   ├── Index/
│   │   ├── index.py     # Main menu controller
│   │   └── Tools/       # Tool modules
│   │       ├── Automation/
│   │       ├── DBMSInjection/
│   │       ├── Design/
│   │       ├── DomainScan/
│   │       ├── Support/
│   │       └── VulunScan/
│   └── Checker/         # Installation scripts
└── docs/                # Additional documentation
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

1. 🐛 **Report Bugs** - Submit detailed issue reports
2. 💡 **Suggest Features** - Share your ideas
3. 🔧 **Submit PRs** - Contribute code improvements
4. 📖 **Improve Docs** - Enhance documentation
5. ⭐ **Star the Repo** - Show your support

### Contribution Process

```bash
# Fork the repository
git clone https://github.com/YourUsername/Again.git

# Create a feature branch
git checkout -b feature/amazing-feature

# Commit your changes
git commit -m "Add amazing feature"

# Push to your fork
git push origin feature/amazing-feature

# Open a Pull Request
```

### Code Standards

- Follow PEP 8 style guidelines
- Add docstrings to functions
- Include comments for complex logic
- Test thoroughly before submitting

---

## 📜 License

This project is licensed under the **GNU General Public License v2.0**.

```
Copyright (C) 2025 c01d43am

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
```

See [LICENSE](LICENSE) file for full details.

---

## ⚠️ Disclaimer  

This tool is intended **for educational and ethical hacking purposes only**. The author is **not responsible** for any misuse or illegal activities conducted using this tool.  

**Security:** See updated SECURITY.md and requirements.txt for latest mitigations.

