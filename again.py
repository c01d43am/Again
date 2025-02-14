import sys
import time
import subprocess

#-------------------------------------------------------------------------------------------------------------
# Function to display a loading animation
def loading_animation():
    animation = "|/-\\"
    for _ in range(3):  # You can adjust the range for a longer animation
        for char in animation:
            sys.stdout.write(f"\rLoading... {char} ")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\rLoading... done!       \n")
    sys.stdout.flush()

#-------------------------------------------------------------------------------------------------------------
# Function to display an "exploitation" animation
def exploitation_animation():
    exploit_text = [
        "Yummy...",
        "Exploiting...",
    ]
    for text in exploit_text:
        sys.stdout.write(f"\r{text}    ")
        sys.stdout.flush()
        time.sleep(0)
    
    print("\nExploit successful!")

#-------------------------------------------------------------------------------------------------------------
# Function to check for updates from the GitHub repository (Pull the latest changes)
def check_for_updates():
    print("\nChecking for updates from the GitHub repository...")
    try:
        result = subprocess.run(["git", "pull", "origin", "main"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print("GitHub repository is up-to-date.")
        else:
            print(f"Failed to update the repository: {result.stderr.strip()}")
    except Exception as e:
        print(f"Error checking for updates: {e}")

#-------------------------------------------------------------------------------------------------------------
# Function to execute index.py after completing actions
def run_index():
    print("\nExecuting Index...\n")
    try:
        subprocess.run(["python3", "Again/Index/index.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Execution failed: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

#-------------------------------------------------------------------------------------------------------------
# Start the tool by checking for updates, then running the necessary functions
def start_tool():
    print("\nStarting Tool...\n")
    check_for_updates()  # Check for the latest updates from GitHub
    loading_animation()  # Show the loading animation
    exploitation_animation()  # Add the exploitation animation
    run_index()  # Execute index.py

if __name__ == "__main__":
    start_tool()
