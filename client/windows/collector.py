import subprocess
import json

def get_wifi_report():
    subprocess.run("netsh wlan show wlanreport", shell=True)

def get_signal_strength():
    output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode()
    return output

if __name__ == "__main__":
    data = get_signal_strength()
    with open("../../data/logs/windows_log.txt", "w") as f:
        f.write(data)