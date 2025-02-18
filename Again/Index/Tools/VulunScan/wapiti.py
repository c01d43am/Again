import os

def run_wapiti_command(command):
    os.system(command)

def wapiti_menu():
    print("Welcome to the Wapiti Web Vulnerability Scanner")
    print("Choose an option:")
    print("1. Full Scan (All Modules)")
    print("2. Scan for SQL Injection")
    print("3. Scan for XSS (Cross-Site Scripting)")
    print("4. Scan for Command Injection")
    print("5. Scan for File Inclusion")
    print("6. Scan for Remote File Inclusion (RFI)")
    print("7. Scan for LDAP Injection")
    print("8. Scan for Security Misconfiguration")
    print("9. Authentication Options")
    print("10. Set Timeout for Requests")
    print("11. Set Retry Count for Failed Requests")
    print("12. Custom User-Agent Header")
    print("13. Send Custom HTTP Headers")
    print("14. Proxy Support")
    print("15. Scan with Custom Wordlist")
    print("16. Output Results in HTML Format")
    print("17. Output Results in XML Format")
    print("18. Output Results in JSON Format")
    print("19. Output Results in CSV Format")
    print("20. Track HTTP Headers During Scan")
    print("21. Limit the Number of URLs to Scan")
    print("22. Exclude Specific URLs from Scan")
    print("23. Scan Specific HTTP Methods (GET, POST)")
    print("24. Scan Specific URL or Folder")
    print("25. Scan with CSRF Token")
    print("26. Scan with Session Cookie")
    print("27. Exit")

    choice = input("Enter your choice (1-27): ")

    if choice == '1':
        subdomain = input("Enter the subdomain URL [https:// or https://]: ")
        command = f"wapiti -u {subdomain} -m all"
        run_wapiti_command(command)
    elif choice == '2':
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m sqli"
        run_wapiti_command(command)
    elif choice == '3':
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m xss"
        run_wapiti_command(command)
    elif choice == '4':
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m cmd"
        run_wapiti_command(command)
    elif choice == '5':
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m file"
        run_wapiti_command(command)
    elif choice == '6':
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m rfi"
        run_wapiti_command(command)
    elif choice == '7':
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m ldap"
        run_wapiti_command(command)
    elif choice == '8':
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m misconfig"
        run_wapiti_command(command)
    elif choice == '9':
        auth_type = input("Choose Authentication Type (1. Basic, 2. Session-based, 3. Form-based): ")
        subdomain = input("Enter the subdomain URL: ")
        if auth_type == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            command = f"wapiti -u {subdomain} -m all -a '{username}:{password}'"
        elif auth_type == '2':
            cookie = input("Enter session cookie: ")
            command = f"wapiti -u {subdomain} -m all --cookie '{cookie}'"
        elif auth_type == '3':
            form = input("Enter the login form URL: ")
            username_field = input("Enter the username field name: ")
            password_field = input("Enter the password field name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            command = f"wapiti -u {subdomain} -m all --form '{form}' --user '{username}' --password '{password}' --field-username '{username_field}' --field-password '{password_field}'"
        run_wapiti_command(command)
    elif choice == '10':
        timeout = input("Enter the timeout in seconds: ")
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m all --timeout {timeout}"
        run_wapiti_command(command)
    elif choice == '11':
        retries = input("Enter the number of retries: ")
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m all --retries {retries}"
        run_wapiti_command(command)
    elif choice == '12':
        user_agent = input("Enter the custom User-Agent: ")
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m all --user-agent '{user_agent}'"
        run_wapiti_command(command)
    elif choice == '13':
        header_name = input("Enter the header name: ")
        header_value = input("Enter the header value: ")
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m all --header '{header_name}: {header_value}'"
        run_wapiti_command(command)
    elif choice == '14':
        proxy = input("Enter the proxy URL (e.g., http://localhost:8080): ")
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m all -p {proxy}"
        run_wapiti_command(command)
    elif choice == '15':
        wordlist = input("Enter the path to the wordlist: ")
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m all --wordlist {wordlist}"
        run_wapiti_command(command)
    elif choice == '16':
        output_path = input("Enter the output HTML file path: ")
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m all -o html -p {output_path}"
        run_wapiti_command(command)
    elif choice == '17':
        output_path = input("Enter the output XML file path: ")
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m all -o xml -p {output_path}"
        run_wapiti_command(command)
    elif choice == '18':
        output_path = input("Enter the output JSON file path: ")
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m all -o json -p {output_path}"
        run_wapiti_command(command)
    elif choice == '19':
        output_path = input("Enter the output CSV file path: ")
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m all -o csv -p {output_path}"
        run_wapiti_command(command)
    elif choice == '20':
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m all --track-headers"
        run_wapiti_command(command)
    elif choice == '21':
        max_urls = input("Enter the maximum number of URLs to scan: ")
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m all --max-urls {max_urls}"
        run_wapiti_command(command)
    elif choice == '22':
        exclude_urls = input("Enter the URL pattern to exclude: ")
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m all --exclude '{exclude_urls}'"
        run_wapiti_command(command)
    elif choice == '23':
        methods = input("Enter the HTTP methods to use (GET, POST, etc.): ")
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m all --methods {methods}"
        run_wapiti_command(command)
    elif choice == '24':
        url = input("Enter the specific URL or folder to scan: ")
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {url} -m all"
        run_wapiti_command(command)
    elif choice == '25':
        csrf_token = input("Enter the CSRF token: ")
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m all --csrf-token {csrf_token}"
        run_wapiti_command(command)
    elif choice == '26':
        session_cookie = input("Enter the session cookie: ")
        subdomain = input("Enter the subdomain URL: ")
        command = f"wapiti -u {subdomain} -m all --cookie {session_cookie}"
        run_wapiti_command(command)
    elif choice == '27':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")
        wapiti_menu()

if __name__ == "__main__":
    wapiti_menu()
