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

# Function to update the GitHub repository
def update_github_repo():
    try:
        print("\nUpdating GitHub repository...")
        # Add changes to git, commit, and push to the remote repository
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "Update tool state"])
        subprocess.run(["git", "push", "origin", "main"])
        print("GitHub repository updated successfully.")
    except Exception as e:
        print(f"Error updating GitHub: {e}")

# Function to execute index.py after completing actions
def run_index():
    print("\nExecuting index.py...\n")
    try:
        # Run index.py after the main actions are completed
        subprocess.run(["python3", "index.py"])
    except Exception as e:
        print(f"Error executing index.py: {e}")

def start_tool():
    print("\nStarting Tool...\n")
    loading_animation()  # Show the loading animation
    update_github_repo()  # Update the GitHub repository
    run_index()  # After updating the repo, execute index.py

if __name__ == "__main__":
    start_tool()
