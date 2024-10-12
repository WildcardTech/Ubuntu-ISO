import subprocess

def install_software():
    # List of software to install
    software = [
        "chromium-browser",  # For Chromium
        "unclutter",         # For Unclutter
        "putty",             # For PuTTY
        "remmina",           # For Remmina
        "filezilla",         # For FileZilla
    ]

    # Install VS Code (requires extra steps for adding Microsoft repository)
    vscode_commands = [
        "wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg",
        "sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/",
        "sudo sh -c 'echo \"deb [arch=amd64] https://packages.microsoft.com/repos/code stable main\" > /etc/apt/sources.list.d/vscode.list'",
        "sudo apt update",
        "sudo apt install code"
    ]

    # Install Angry IP Scanner (requires manual download)
    angry_ip_commands = [
        "wget https://github.com/angryip/ipscan/releases/download/3.8.2/ipscan_3.8.2_amd64.deb",
        "sudo dpkg -i ipscan_3.8.2_amd64.deb",
        "sudo apt-get install -f"  # Fix any dependency issues
    ]

    try:
        # Update package list
        subprocess.run(["sudo", "apt", "update"], check=True)

        # Install software from default repositories
        for package in software:
            subprocess.run(["sudo", "apt", "install", "-y", package], check=True)

        # Install VS Code
        for cmd in vscode_commands:
            subprocess.run(cmd, shell=True, check=True)

        # Install Angry IP Scanner
        for cmd in angry_ip_commands:
            subprocess.run(cmd, shell=True, check=True)

        print("All software installed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    install_software()

