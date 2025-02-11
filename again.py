# Description: This script is used to check for updates from the GitHub repository, display a loading animation, and execute index.py after completing all actions.
# The script checks for updates from the GitHub repository by pulling the latest changes from the remote repository.
import sys
import time
import subprocess
#-------------------------------------------------------------------------------------------------------------
# Function to display a loading animation
def loading_animation():
    animation = "|/-!@#$%^&*()_+\\"
    for _ in range(1):  # You can adjust the range for a longer animation
        for char in animation:
            sys.stdout.write(f"\rLoading..........{char}")
            sys.stdout.flush()
            time.sleep(0.2)
#-------------------------------------------------------------------------------------------------------------
# Function to display an "exploitation" animation
def exploitation_animation():
    exploit_text = [
        "yummy...",
        "tasty...",
        "i want more...",
        "am full...",
        "All systems compromised!"
    ]
    for text in exploit_text:
        sys.stdout.write(f"\r{text}")
        sys.stdout.flush()
        time.sleep(1)
    
    print("\nExploit successful!")
#-------------------------------------------------------------------------------------------------------------
# Function to check for updates from the GitHub repository (Pull the latest changes)
def check_for_updates():
    try:
        print("\nChecking for updates in the GitHub repository...")
        # Pull the latest changes from the remote repository, suppressing output
        subprocess.run(["git", "pull", "origin", "main"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("GitHub repository is up-to-date.")
    except Exception as e:
        print(f"Error checking for updates: {e}")
#-------------------------------------------------------------------------------------------------------------
# Function to execute index.py after completing actions
def run_index():
    print("\nExecuting ....\n")
    try:
        # Specify the path to index.py inside the again folder
        subprocess.run(["python3", "Again/index.py"])
    except Exception as e:
        print(f"Error !!!!!????: {e}")
#-------------------------------------------------------------------------------------------------------------
# Start the tool by checking for updates, then running the necessary functions
def start_tool():
    print("\nStarting Tool...\n")
    check_for_updates()  # Check for the latest updates from GitHub
    loading_animation()  # Show the loading animation
    exploitation_animation()  # Add the exploitation animation
    run_index()  # After completing all actions, execute index.py

if __name__ == "__main__":
    start_tool()
