# Port Scanner

This is a simple Python script that scans a target IP address or hostname for the most commonly used TCP ports. It attempts to connect to each port and reports which ones are open.

## How It Works
- The script uses Python’s built-in `socket` module
- It scans a predefined list of common ports (e.g., 22 for SSH, 80 for HTTP, 443 for HTTPS)
- If a connection to a port succeeds, it’s marked as open

## Usage
1. Make sure you have Python 3 installed
2. Run the script:
   ```bash
    port-scanner.py
