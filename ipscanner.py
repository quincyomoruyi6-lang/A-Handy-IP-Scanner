import time
import subprocess
import platform  # New module to detect OS

# 1. Handle cross-platform ping commands


def ping_host(ip):
    # If OS is Windows, flag is '-n'. If Linux/Mac, flag is '-c'
    flag = "-n" if platform.system().lower() == "windows" else "-c"

    # Run the system command safely without opening a vulnerable shell
    answer = subprocess.run(["ping", flag, "1", ip],
                            capture_output=True, text=True)
    return answer.returncode


def scan_specific_ip():
    address = input("\nInput IP addresses to scan (separated by spaces): ")
    results = address.split()

    # Using 'with' is perfect. Let's log neatly
    with open("captured_ip.txt", "a") as save:
        save.write(f"Scanned sequence {results} at {time.ctime()} \n")

    for result in results:
        if ping_host(result) == 0:
            print(f"\033[92m[+] Host {result} is Alive..\033[0m")
        else:
            print(f"\033[91m[-] Host {result} is Down..\033[0m")
        time.sleep(0.5)


def scan_ip_range():
    ask = input("\nIP Range From (e.g. 192.168.1.1): ").strip()
    again = input("To (e.g. 192.168.1.10): ").strip()

    ask1 = ask.split(".")
    ask2 = again.split(".")

    # Ensure they belong to the same Class C subnet
    if ask1[0:3] == ask2[0:3]:
        base = f"{ask1[0]}.{ask1[1]}.{ask1[2]}"
        start = int(ask1[3])
        end = int(ask2[3])

        for ips in range(start, end + 1):
            full_ip = f"{base}.{ips}"
            if ping_host(full_ip) == 0:
                print(f"\033[92m[+] Host {full_ip} is Alive..\033[0m")
            else:
                print(f"\033[91m[-] Host {full_ip} is Down..\033[0m")
            time.sleep(0.5)
    else:
        print("\033[91mERROR: Target IPs must be in the same network range!\033[0m")


def view_previous_scan():
    print("\n--- HISTORICAL SCAN LOGS ---")
    try:
        with open("captured_ip.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No scan history found yet.")

# Main Application Controller Loop


def run_app():
    print(" --- IP SCANNER TOOL ---")
    time.sleep(0.5)

    while True:
        print("\n" + "="*30)
        print("[1.] Scan specific IPs")
        print("[2.] Scan IP range")
        print("[3.] View previous scan results")
        print("[4.] Exit")
        print("="*30)

        ask = input("Select an option: ").strip()

        if ask == "1":
            scan_specific_ip()
        elif ask == "2":
            scan_ip_range()
        elif ask == "3":
            view_previous_scan()
        elif ask == "4":
            print("\nExiting application cleanly. Goodbye!")
            break
        else:
            print("Invalid input. Please try choices 1-4.")
        time.sleep(1)


# Only execute if run directly
if __name__ == "__main__":
    try:
        run_app()
    except KeyboardInterrupt:
        print("\n\n[!] Execution interrupted by user (Ctrl+C). Exiting safely...")
        exit(0)
