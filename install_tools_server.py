#!/usr/bin/env python3
import subprocess

# List of packages to install
packages = [
    "arp-scan",
    "isc-dhcp-server",
    "bind9",
    "dnsutils",
    "samba",
    "nmap"
]

def run_command(command):
    """Run a shell command and print output live."""
    process = subprocess.Popen(command, shell=True)
    process.communicate()
    if process.returncode != 0:
        print(f"❌ Command failed: {command}")
    else:
        print(f"✅ Command succeeded: {command}")

def main():
    print("⚡ Updating package list...")
    run_command("apt-get update -y")

    print("⚡ Upgrading packages (dist-upgrade)...")
    run_command("apt-get dist-upgrade -y")

    print("⚡ Installing requested packages...")
    for pkg in packages:
        run_command(f"apt-get install -y {pkg}")

    print("🎉 All installations finished!")

if __name__ == "__main__":
    main()
