import sys
import time
import subprocess

# Function to display a loading animation
def loading_animation():
    animation = "|/-\\"
    for _ in range(20):  # You can adjust the range for a longer animation
        for char in animation:
            sys.stdout.write(f"\rLoading {char}")
            sys.stdout.flush()
            time.sleep(0.1)

# Function to check for updates from the GitHub repository (Pull the latest changes)
def check_for_updates():
    try:
        print("\nChecking for updates in the GitHub repository...")
        # Pull the latest changes from the remote repository, suppressing output
        subprocess.run(["git", "pull", "origin", "main"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("GitHub repository is up-to-date.")
    except Exception as e:
        print(f"Error checking for updates: {e}")

# Function to execute index.py after completing actions
def run_index():
    print("\nExecuting index.py...\n")
    try:
        # Run index.py after the main actions are completed
        subprocess.run(["python3", "index.py"])
    except Exception as e:
        print(f"Error executing index.py: {e}")

# Start the tool by checking for updates, then running the necessary functions
def start_tool():
    print("\nStarting Tool...\n")
    check_for_updates()  # Check for the latest updates from GitHub
    loading_animation()  # Show the loading animation
    run_index()  # After completing all actions, execute index.py

if __name__ == "__main__":
    start_tool()
