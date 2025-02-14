import os
import subprocess

def check_and_install_nmap():
    """Checks if Nmap is installed. Installs it if not found."""
    try:
        result = subprocess.run(["nmap", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        if result.returncode != 0:
            raise FileNotFoundError
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("[+] Installing nmap...")
        os.system("sudo apt update && sudo apt install -y nmap")

def nmap_host_discovery():
    """Nmap host discovery with various scan options."""
    check_and_install_nmap()
    
    print("Select an Nmap scan option:")
    print("1. Basic Ping Scan (-sn)")
    print("2. Ping Scan with Direct IP Packet (-sn --send-ip)")
    print("3. Ping Scan on Specific IPs (-sn {ip} {ip})")
    print("4. TCP SYN Ping Scan (-sn -PS{port})")
    print("5. Ping Acknowledgment Scan (-sn -PA)")
    print("6. ICMP Echo Request Scan (-sn -PE --send-ip)")
    print("7. Host Discovery with Version Detection (-sn -V -T4)")
    print("8. Host Discovery with TCP SYN & UDP (-sn -PS{port} -PU{port} -T4)")
    print("9. Fast Port Scan (-Pn -F)")
    print("10. Specific Port Scan (-Pn -p{port})")
    print("11. Aggressive Full Port Scan (-T4 -Pn -p-)")
    print("12. Stealth SYN Scan (-Pn -sS -F)")
    print("13. TCP Connect Scan (-Pn -sT)")
    print("14. UDP Scan (-sU -p{port})")
    
    choice = input("Enter your choice (1-14): ")
    ip = input("Enter target IP or IP range: ")
    
    if choice == "1":
        command = f"nmap -sn {ip}"
    elif choice == "2":
        command = f"nmap -sn {ip} --send-ip"
    elif choice == "3":
        ips = input("Enter additional IPs separated by space: ")
        command = f"nmap -sn {ip} {ips}"
    elif choice == "4":
        port = input("Enter port number: ")
        command = f"nmap -sn -PS{port} {ip}"
    elif choice == "5":
        command = f"nmap -sn -PA {ip}"
    elif choice == "6":
        command = f"nmap -sn -PE {ip} --send-ip"
    elif choice == "7":
        command = f"nmap -sn -V -T4 {ip}"
    elif choice == "8":
        tcp_port = input("Enter TCP port: ")
        udp_port = input("Enter UDP port: ")
        command = f"nmap -sn -PS{tcp_port} -PU{udp_port} -T4 {ip}"
    elif choice == "9":
        command = f"nmap -Pn -F {ip}"
    elif choice == "10":
        port = input("Enter port number: ")
        command = f"nmap -Pn -p{port} {ip}"
    elif choice == "11":
        command = f"nmap -T4 -Pn -p- {ip}"
    elif choice == "12":
        command = f"nmap -Pn -sS -F {ip}"
    elif choice == "13":
        command = f"nmap -Pn -sT {ip}"
    elif choice == "14":
        port = input("Enter port number: ")
        command = f"nmap -sU -p{port} {ip}"
    else:
        print("Invalid choice. Exiting...")
        return
    
    print(f"Running command: {command}")
    os.system(command)

if __name__ == "__main__":
    nmap_host_discovery()