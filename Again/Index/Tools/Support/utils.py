import subprocess

# General function to check and install a tool
def install_tool(tool_name, package_name=None, post_install_cmd=None):
    if package_name is None:
        package_name = tool_name

    try:
        # Check if the tool is installed
        result = subprocess.run(f"which {tool_name}", shell=True, capture_output=True)
        if result.returncode != 0:
            print(f"{tool_name} not found. Installing...")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", package_name], check=True)
            print(f"{tool_name} installed successfully.")
            if post_install_cmd:
                subprocess.run(post_install_cmd, shell=True, check=True)
        else:
            print(f"{tool_name} is already installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error while installing {tool_name}: {e}")