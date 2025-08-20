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
    process = subprocess.Popen(command, shell=True, executable="/bin/bash")
    process.communicate()
    if process.returncode != 0:
        print(f"❌ Command failed: {command}")
    else:
        print(f"✅ Command succeeded: {command}")

def write_bind_config():
    """Write a new /etc/bind/named.conf.options file."""
    config = """options {
        directory "/var/cache/bind";

        // Google DNS as forwarders
        forwarders {
            8.8.8.8;
            8.8.4.4;
        };

        dnssec-validation auto;

        listen-on-v6 { any; };
    };
    """

    # Use tee with sudo so file permissions stay correct
    command = f"echo '{config}' | tee /etc/bind/named.conf.options > /dev/null"
    run_command(command)

def main():
    print("⚡ Setting timezone to America/Chicago...")
    run_command("timedatectl set-timezone America/Chicago")

    print("⚡ Updating package list...")
    run_command("apt-get update -y")

    print("⚡ Upgrading packages (dist-upgrade)...")
    run_command("apt-get dist-upgrade -y")

    print("⚡ Installing requested packages...")
    for pkg in packages:
        run_command(f"apt-get install -y {pkg}")

    print("⚡ Writing BIND config...")
    write_bind_config()

    print("⚡ Restarting BIND service...")
    run_command("systemctl restart bind9")

    print("🎉 All installations and configuration finished!")

if __name__ == "__main__":
    main()
