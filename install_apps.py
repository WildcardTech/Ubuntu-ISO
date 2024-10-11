import subprocess

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}: {e}")

def install_chrome():
    print("Installing Google Chrome...")
    run_command('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
    run_command('sudo dpkg -i google-chrome-stable_current_amd64.deb')
    run_command('sudo apt --fix-broken install -y')
    run_command('rm google-chrome-stable_current_amd64.deb')
    print("Google Chrome installed successfully.")

def install_putty():
    print("Installing PuTTY...")
    run_command('sudo apt update && sudo apt install -y putty')
    print("PuTTY installed successfully.")

def install_angry_ip_scanner():
    print("Installing Angry IP Scanner...")
    run_command('wget https://github.com/angryip/ipscan/releases/download/3.9.0/ipscan_3.9.0_amd64.deb')
    run_command('sudo dpkg -i ipscan_3.9.0_amd64.deb')
    run_command('sudo apt --fix-broken install -y')
    run_command('rm ipscan_3.9.0_amd64.deb')
    print("Angry IP Scanner installed successfully.")

def install_remmina():
    print("Installing Remmina...")
    run_command('sudo apt update && sudo apt install -y remmina remmina-plugin-rdp remmina-plugin-vnc')
    print("Remmina installed successfully.")

def install_filezilla():
    print("Installing FileZilla...")
    run_command('sudo apt update && sudo apt install -y filezilla')
    print("FileZilla installed successfully.")

def main():
    install_chrome()
    install_putty()
    install_angry_ip_scanner()
    install_remmina()
    install_filezilla()
    print("All applications installed successfully!")

if __name__ == "__main__":
    main()
