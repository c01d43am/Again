#!/bin/bash

# Define paths
TOOL_NAME="Again"
INSTALL_DIR="/opt/$TOOL_NAME"
EXECUTABLE="/usr/local/bin/again"
SCRIPT_NAME="again.py"

# Move the tool to /opt/ if it's not already there
if [ ! -d "$INSTALL_DIR" ]; then
    echo "[*] Moving $TOOL_NAME to $INSTALL_DIR..."
    sudo mv ~/"$TOOL_NAME" "$INSTALL_DIR"
else
    echo "[*] $TOOL_NAME already exists in $INSTALL_DIR, skipping move."
fi

# Create a global wrapper script
echo "[*] Creating global command..."
echo '#!/bin/bash' | sudo tee "$EXECUTABLE" > /dev/null
echo "cd $INSTALL_DIR && python3 $SCRIPT_NAME \"\$@\"" | sudo tee -a "$EXECUTABLE" > /dev/null

# Make the wrapper script executable
echo "[*] Setting permissions..."
sudo chmod +x "$EXECUTABLE"

# Done!
echo "[+] Installation complete! You can now run 'again' from anywhere."
