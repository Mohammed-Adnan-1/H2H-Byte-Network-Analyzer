import subprocess

def get_wifi_info():
    cmd = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I"
    return subprocess.check_output(cmd, shell=True).decode()

if __name__ == "__main__":
    data = get_wifi_info()
    with open("../../data/logs/mac_log.txt", "w") as f:
        f.write(data)