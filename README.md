# IP Scanner

A simple Python IP scanner tool for Windows that can ping individual IP addresses or a range of IP addresses. Scan results are saved to `captured_ip.txt` so you can review them later.

## Features

- Scan one or more IP addresses at once
- Scan an IP range within the same subnet
- Save scan history to `captured_ip.txt`
- View previous scan results from the saved file

## Requirements

- Python 3.x
- Windows (uses the Windows `ping -n` command)

## Usage

1. Open a terminal in the project folder.
2. Run the script:

   ```bash
   python ipscanner.py
   ```

3. Choose an option from the menu:
   - `1` to scan one or more specific IP addresses
   - `2` to scan an IP range
   - `3` to view previous scan results
   - `4` to exit

4. When scanning specific IPs, enter addresses separated by spaces, for example:

   ```text
   192.168.1.1 192.168.1.10
   ```

5. When scanning a range, enter the start IP and the end IP within the same subnet, for example:

   ```text
   IP Range From: 192.168.1.1
   To: 192.168.1.10
   ```

## Output

- Scan activity prints whether each host is alive or down.
- Scan history is appended to `captured_ip.txt` with a timestamp.

## Notes

- This script is designed for Windows because it uses `ping -n 1`.
- The range scan assumes the first three octets are the same for both start and end IPs.

## Optional improvements

- Add IP validation before scanning
- Support Linux/macOS by switching `ping` flags
- Add a command-line interface with `argparse`
- Improve range scanning for different subnets

## License

This project is provided as-is for learning and personal use.
