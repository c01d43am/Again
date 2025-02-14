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

    print(f"{tool_name} not found. Installing...\n")

    # Detect package manager
    if shutil.which("apt"):
        package_manager = "apt"
        update_cmd = ["sudo", "apt", "update"]
        install_cmd = ["sudo", "apt", "install", "-y", package_name]
    elif shutil.which("pacman"):
        package_manager = "pacman"
        install_cmd = ["sudo", "pacman", "-Sy", "--noconfirm", package_name]
    elif shutil.which("brew"):
        package_manager = "brew"
        install_cmd = ["brew", "install", package_name]
    else:
        print("No supported package manager found. Please install manually.")
        return False

    try:
        # Run update command for apt only
        if package_manager == "apt":
            subprocess.run(update_cmd, check=True)

        # Install the package
        subprocess.run(install_cmd, check=True)
        print(f"{tool_name} installed successfully.\n")

        # Run post-install command if provided
        if post_install_cmd:
            subprocess.run(post_install_cmd, shell=True, check=True)
        
        return True

    except subprocess.CalledProcessError as e:
        print(f"Error while installing {tool_name}: {e}")
        return False
