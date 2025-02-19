import os
import subprocess
import random

def run_sqlmap_command(command):
    os.system(command)

def run_sqlmap(target_url):
    """Run sqlmap to check for SQL injection vulnerabilities on the target URL."""
    python_cmd = "python3" if subprocess.run("which python3", shell=True, capture_output=True).returncode == 0 else "python"
    print(f"\nRunning sqlmap on {target_url} ")
    try:
        command = f"sqlmap -u {target_url} --batch --risk=3 --level=5"
        subprocess.run(command, shell=True, check=True)
        print(f"sqlmap scan completed for {target_url}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run sqlmap on {target_url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while running sqlmap: {e}")

def sql_tool_menu():
    """Tool to check for SQL injection vulnerabilities using sqlmap."""
    funny_responses = [
        "Oops! That wasn't on the menu. Try again!",
        "Nice try, but that's not an option!",
        "Invalid choice. Are you testing my patience?",
        "Error 404: Your choice not found!",
        "You broke the menu... Just kidding, try again!"
    ]

    while True:
        print("\nMySQL Injection Tool:")
        print("1. Run sqlmap on a Target URL")
        print("2. Return to Main Menu\n")

        choice = input("Enter your choice [1-2]: ")
        if choice == "1":
            target_url = input("Enter the target URL (including http/https): ")
            if target_url:
                run_sqlmap(target_url)  # Run sqlmap for the given URL
            else:
                print("Invalid URL. Please try again.")
        elif choice == "2":
            print("Returning to Main Menu.")
            break
        else:
            print(random.choice(funny_responses))

def main_menu():
    print("Welcome to SQLMap - Automated SQL Injection Tool")
    print("Choose an option:")
    print("1. Full Scan")
    print("2. Scan for SQL Injection on URL")
    print("3. Scan with Custom Risk Level")
    print("4. Scan with Custom Timeout")
    print("5. Scan with Proxy")
    print("6. Scan with Custom User-Agent")
    print("7. Scan with Authentication")
    print("8. Scan with Custom Cookie")
    print("9. Scan Specific Parameter")
    print("10. Scan for Union-Based SQL Injection")
    print("11. Scan for Time-Based SQL Injection")
    print("12. Scan for Blind SQL Injection")
    print("13. Output Results in CSV Format")
    print("14. Output Results in XML Format")
    print("15. Output Results in JSON Format")
    print("16. Scan with Random Agent")
    print("17. Enumerate Databases")
    print("18. Dump All Data from Database")
    print("19. Perform OS Commanding (OS Shell)")
    print("20. Scan with Specific Authentication")
    print("21. Crawl Target Website")
    print("22. Tamper with Requests (Bypass Filters)")
    print("23. Exit")

    choice = input("Enter your choice (1-23): ")

    if choice == '1':
        target = input("Enter the target URL: ")
        command = f"sqlmap -u {target} --batch"
        run_sqlmap_command(command)
    elif choice == '2':
        target = input("Enter the target URL: ")
        command = f"sqlmap -u {target} --batch --crawl 1"
        run_sqlmap_command(command)
    elif choice == '3':
        target = input("Enter the target URL: ")
        risk_level = input("Enter the risk level (1, 2, 3): ")
        command = f"sqlmap -u {target} --risk={risk_level} --batch"
        run_sqlmap_command(command)
    elif choice == '4':
        target = input("Enter the target URL: ")
        timeout = input("Enter the timeout in seconds: ")
        command = f"sqlmap -u {target} --timeout={timeout} --batch"
        run_sqlmap_command(command)
    elif choice == '5':
        target = input("Enter the target URL: ")
        proxy = input("Enter the proxy URL (e.g., http://localhost:8080): ")
        command = f"sqlmap -u {target} --proxy={proxy} --batch"
        run_sqlmap_command(command)
    elif choice == '6':
        target = input("Enter the target URL: ")
        user_agent = input("Enter the custom User-Agent: ")
        command = f"sqlmap -u {target} --user-agent '{user_agent}' --batch"
        run_sqlmap_command(command)
    elif choice == '7':
        target = input("Enter the target URL: ")
        auth_type = input("Choose Authentication Type (1. Basic, 2. Cookie-based): ")
        if auth_type == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            command = f"sqlmap -u {target} --auth-type=basic --auth-cred='{username}:{password}' --batch"
        elif auth_type == '2':
            cookie = input("Enter the session cookie: ")
            command = f"sqlmap -u {target} --cookie='{cookie}' --batch"
        run_sqlmap_command(command)
    elif choice == '8':
        target = input("Enter the target URL: ")
        cookie = input("Enter the session cookie: ")
        command = f"sqlmap -u {target} --cookie='{cookie}' --batch"
        run_sqlmap_command(command)
    elif choice == '9':
        target = input("Enter the target URL: ")
        parameter = input("Enter the parameter to scan (e.g., id, page): ")
        command = f"sqlmap -u {target} --data='{parameter}=test' --batch"
        run_sqlmap_command(command)
    elif choice == '10':
        target = input("Enter the target URL: ")
        command = f"sqlmap -u {target} --technique=U --batch"
        run_sqlmap_command(command)
    elif choice == '11':
        target = input("Enter the target URL: ")
        command = f"sqlmap -u {target} --technique=T --batch"
        run_sqlmap_command(command)
    elif choice == '12':
        target = input("Enter the target URL: ")
        command = f"sqlmap -u {target} --technique=B --batch"
        run_sqlmap_command(command)
    elif choice == '13':
        target = input("Enter the target URL: ")
        output_path = input("Enter the output CSV file path: ")
        command = f"sqlmap -u {target} --batch --output-dir={output_path} --csv"
        run_sqlmap_command(command)
    elif choice == '14':
        target = input("Enter the target URL: ")
        output_path = input("Enter the output XML file path: ")
        command = f"sqlmap -u {target} --batch --output-dir={output_path} --xml"
        run_sqlmap_command(command)
    elif choice == '15':
        target = input("Enter the target URL: ")
        output_path = input("Enter the output JSON file path: ")
        command = f"sqlmap -u {target} --batch --output-dir={output_path} --json"
        run_sqlmap_command(command)
    elif choice == '16':
        target = input("Enter the target URL: ")
        command = f"sqlmap -u {target} --random-agent --batch"
        run_sqlmap_command(command)
    elif choice == '17':
        target = input("Enter the target URL: ")
        command = f"sqlmap -u {target} --dbs --batch"
        run_sqlmap_command(command)
    elif choice == '18':
        target = input("Enter the target URL: ")
        command = f"sqlmap -u {target} --dbs --dump --batch"
        run_sqlmap_command(command)
    elif choice == '19':
        target = input("Enter the target URL: ")
        command = f"sqlmap -u {target} --os-shell --batch"
        run_sqlmap_command(command)
    elif choice == '20':
        target = input("Enter the target URL: ")
        auth_type = input("Choose Authentication Type (1. Basic, 2. Cookie-based): ")
        if auth_type == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            command = f"sqlmap -u {target} --auth-type=basic --auth-cred='{username}:{password}' --batch"
        elif auth_type == '2':
            cookie = input("Enter the session cookie: ")
            command = f"sqlmap -u {target} --cookie='{cookie}' --batch"
        run_sqlmap_command(command)
    elif choice == '21':
        target = input("Enter the target URL: ")
        command = f"sqlmap -u {target} --crawl=2 --batch"
        run_sqlmap_command(command)
    elif choice == '22':
        target = input("Enter the target URL: ")
        tamper_script = input("Enter the tamper script to use (e.g., between, randomcase): ")
        command = f"sqlmap -u {target} --tamper={tamper_script} --batch"
        run_sqlmap_command(command)
    elif choice == '23':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

if __name__ == "__main__":
    main_menu()