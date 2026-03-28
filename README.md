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
✅ **Security Hardened:** Dependencies pinned to mitigate known CVEs (see SECURITY.md).

---

## 📌 Main Menu  

```
1. Automation Tool
   ├── Nessus (Vulnerability Scanner)
   ├── Armitage (Metasploit GUI)
   ├── Akto (API Security Testing)
   └── Back to Main Menu

2. Domain (Recon & Scanning)
   ├── Dirb (Directory Brute Force)
   ├── SSLScan (SSL/TLS Security Check)
   ├── Feroxbuster (Content Discovery)
   ├── Gobuster (Subdomain/Directory Enumeration)
   ├── Nmap (Network Scanning)
   └── Exit

3. Vulnerability Scanning
   ├── Nikto (Web Server Security Scan)
   ├── Skipfish (Automated Web Vulnerability Scan)
   └── Exit

4. Exploits
   ├── SQLMap (SQL Injection Testing)
   └── Return to Main Menu

5. Exit
```

---

## 📌 Installation  

### **1️⃣ Clone the Repository**  

```bash
git clone https://github.com/c01d43am/Again.git
cd Again
```

### **2️⃣ Install Dependencies**  

```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Tool**  

```bash
python again.py
```

---

## 📌 Usage  

### **Run the Tool:**
```bash
python again.py
```

### **Select an Option from the Menu:**
- **1**: Automation Tool  
- **2**: Domain Recon & Scanning  
- **3**: Vulnerability Scanning  
- **4**: Exploits  
- **5**: Exit  

---

## 📌 Running the Tool Globally  

To make `Again` available globally:  

```bash
sudo cd Again
sudo chmod +x default.sh
```

Now, you can run the tool from anywhere using:  

```bash
again
```

---

## 📌 Example Output  

```
░█████╗░░██████╗░░█████╗░██╗███╗░░██╗░█████╗░
██╔══██╗██╔════╝░██╔══██╗██║████╗░██║██╔══██╗
███████║██║░░██╗░███████║██║██╔██╗██║╚═╝███╔╝
██╔══██║██║░░╚██╗██╔══██║██║██║╚████║░░░╚══╝░
██║░░██║╚██████╔╝██║░░██║██║██║░╚███║░░░██╗░░
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░╚═╝░░

https://github.com/c01d43am

v1.0.0 by c01d43am
```

---

## 📌 Contributing  

Contributions are welcome! To contribute:  
1. **Fork the repository.**  
2. **Create a feature branch.**  
3. **Submit a pull request with your changes.**  

---

## 📌 License  

This project is licensed under the **GNU General Public License v2.0**. See the `LICENSE` file for details.  

---

## ⚠️ Disclaimer  

This tool is intended **for educational and ethical hacking purposes only**. The author is **not responsible** for any misuse or illegal activities conducted using this tool. 

**Security:** See updated SECURITY.md and requirements.txt for latest mitigations.

