import requests
import socket

def get_ip(domain):
    try:
        # Extract hostname to resolve IP
        hostname = domain.split("//")[-1].split("/")[0]
        return socket.gethostbyname(hostname)
    except Exception as e:
        return f"Unable to resolve IP"

def check_status(domain):
    try:
        response = requests.get(domain, timeout=10)
        server = response.headers.get('Server', 'Unknown')
        ip_address = get_ip(domain)
        return response.status_code, server, ip_address
    except requests.exceptions.MissingSchema:
        return "Invalid URL", "N/A", "N/A"
    except requests.exceptions.ConnectionError:
        return "Connection Error", "N/A", "N/A"
    except requests.exceptions.Timeout:
        return "Timeout", "N/A", "N/A"
    except Exception as e:
        return f"Error: {e}", "N/A", "N/A"

def main():
    print("Website Domain Status Code Checker with Server and IP")
    print("-" * 80)
    
    while True:
        print("\nOptions:")
        print("1. Check a single domain")
        print("2. Check multiple domains from a file")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            domain = input("Enter the domain (e.g., https://example.com): ")
            status, server, ip = check_status(domain)
            print("\nResults:")
            print(f"{'Domain':<40} {'Status Code':<15} {'Server Name':<25} {'IP Address'}")
            print("-" * 80)
            print(f"{domain:<40} {status:<15} {server:<25} {ip}")
        
        elif choice == "2":
            file_path = input("Enter the file path with domain list: ")
            try:
                with open(file_path, 'r') as file:
                    domains = file.readlines()
                print("\nChecking domains...")
                print(f"{'Domain':<40} {'Status Code':<15} {'Server Name':<25} {'IP Address'}")
                print("-" * 80)
                for domain in domains:
                    domain = domain.strip()
                    if domain:
                        status, server, ip = check_status(domain)
                        print(f"{domain:<40} {status:<15} {server:<25} {ip}")
            except FileNotFoundError:
                print("File not found. Please check the path and try again.")
        
        elif choice == "3":
            print("Exiting the tool. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
