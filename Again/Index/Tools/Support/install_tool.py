import subprocess
import shutil

def install_tool(tool_name, package_name=None, post_install_cmd=None):
    """Check if a tool is installed and install it if missing."""
    
    if package_name is None:
        package_name = tool_name

    # Check if the tool is already installed
    if shutil.which(tool_name):
        print(f"{tool_name} is already installed.")
        return True

    print(f"{tool_name} not found. Installing...")

    # Detect package manager
    if shutil.which("apt"):
        package_manager = "apt"
        update_cmd = ["sudo", "apt", "update"]
        install_cmd = ["sudo", "apt", "install", "-y", package_name]
    elif shutil.which("pacman"):
        package_manager = "pacman"
        update_cmd = ["sudo", "pacman", "-Sy"]
        install_cmd = ["sudo", "pacman", "-S", "--noconfirm", package_name]
    elif shutil.which("brew"):
        package_manager = "brew"
        update_cmd = None  # Brew doesn't require an update command
        install_cmd = ["brew", "install", package_name]
    else:
        print("No supported package manager found. Please install manually.")
        return False

    try:
        # Run update command first (only for apt and pacman)
        if update_cmd:
            subprocess.run(update_cmd, check=True)

        # Run installation command
        subprocess.run(install_cmd, check=True)
        print(f"{tool_name} installed successfully.")

        # Run post-installation command if specified
        if post_install_cmd:
            subprocess.run(post_install_cmd, shell=True, check=True)
        
        return True

    except subprocess.CalledProcessError as e:
        print(f"Error while installing {tool_name}: {e}")
        return False
