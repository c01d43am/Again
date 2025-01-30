from Again.scan import start_openvas, start_nessus, start_armitage, install_tool

# Function to automate the selected tool
def automate_tool(tool_choice):
    if tool_choice == "1":
        start_openvas()
    elif tool_choice == "2":
        start_nessus()
    elif tool_choice == "3":
        start_armitage()
    elif tool_choice == "4":
        start_akto()
    else:
        print("Invalid choice, please try again.")

# OpenVAS Automation with subcategories
def start_openvas():
    print("\nAutomating OpenVAS...\n")
    install_tool("gvm-start", "gvm")  # Ensure OpenVAS is installed
    start_openvas()  # Start OpenVAS
    print("OpenVAS has been started and is accessible via https://127.0.0.1:9392\n")

# Nessus Automation with subcategories
def start_nessus():
    print("\nAutomating Nessus...\n")
    install_tool("nessusd", "nessus")  # Ensure Nessus is installed
    start_nessus()  # Start Nessus
    print("Nessus has been started and is accessible via https://127.0.0.1:8834\n")

# Armitage Automation with subcategories
def start_armitage():
    print("\nAutomating Armitage...\n")
    install_tool("armitage", "armitage")  # Ensure Armitage is installed
    start_armitage()  # Start Armitage
    print("Armitage has been started. Please wait for the GUI to appear.\n")

# Akto Automation with subcategories
def start_akto():
    print("\nAutomating Akto...\n")
    install_tool("akto", "akto")  # Ensure Akto is installed
    # Start Akto or its associated services (e.g., Puppeteer, Dashboard)
    start_akto()  # Implement the start_akto function to start Akto (you may need to define it)
    print("Akto has been started. Please access it via http://127.0.0.1:9090\n")


