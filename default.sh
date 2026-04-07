#!/bin/bash
set -e

# Define paths
TOOL_NAME="Again"
INSTALL_DIR="/opt/$TOOL_NAME"
EXECUTABLE="/usr/local/bin/again"
SCRIPT_NAME="again.py"

# Detect where this installer is being run from
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$SCRIPT_DIR"

# If installer is inside repository root where Again/ exists, prefer repository root
if [ -d "$SCRIPT_DIR/$TOOL_NAME" ]; then
    SOURCE_DIR="$SCRIPT_DIR/$TOOL_NAME"
elif [ "$(basename "$SCRIPT_DIR")" = "$TOOL_NAME" ]; then
    SOURCE_DIR="$SCRIPT_DIR"
fi

echo "[*] Installer location: $SCRIPT_DIR"
echo "[*] Resolved source: $SOURCE_DIR"

# Install/copy files to /opt/Again
if [ ! -d "$INSTALL_DIR" ]; then
    echo "[*] Creating $INSTALL_DIR..."
    sudo mkdir -p "$INSTALL_DIR"
fi

echo "[*] Syncing files to $INSTALL_DIR..."
if command -v rsync >/dev/null 2>&1; then
    sudo rsync -a --delete "$SOURCE_DIR"/ "$INSTALL_DIR"/
else
    # Fallback if rsync is unavailable
    sudo rm -rf "$INSTALL_DIR"/*
    sudo cp -a "$SOURCE_DIR"/. "$INSTALL_DIR"/
fi

# Validate target script exists
if [ ! -f "$INSTALL_DIR/$SCRIPT_NAME" ]; then
    echo "[-] ERROR: $SCRIPT_NAME not found in $INSTALL_DIR"
    echo "[-] Ensure the Again project root (containing $SCRIPT_NAME) is being installed."
    exit 1
fi

# Create a global wrapper script
echo "[*] Creating global command..."
sudo tee "$EXECUTABLE" > /dev/null <<EOF
#!/bin/bash
cd "$INSTALL_DIR" || exit 1
python3 "$SCRIPT_NAME" "\$@"
EOF

# Make the wrapper script executable
echo "[*] Setting permissions..."
sudo chmod +x "$EXECUTABLE"

# Done!
echo "[+] Installation complete! You can now run 'again' from anywhere."
