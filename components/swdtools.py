from pathlib import Path
import requests
from clint.textui import progress
import urllib

try:
    from components.sysinfo import *
except:
    from sysinfo import *

def download_file(url, path, local_path="./"):
    #Credits to ButterDog and Rich Jones on stackoverflow
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
            if chunk:
                f.write(chunk)
                f.flush()

def swd_existence_check():
    #fix this check test.py
    version_found = ''
    linux_386 = Path("swd-linux-386")
    linux_amd64 = Path("swd-linux-amd64")
    linux_arm = Path("swd-linux-arm")
    windows_386 = Path("swd-windows-386.exe")
    windows_amd64 = Path("swd-windows-amd64.exe")
    if linux_386.exists() == True:
        print('Found: Linux-386 version')
        version_found = 'swd-linux-386'
    elif linux_amd64.exists() == True:
        print('Found: Linux-amd64 version')
        version_found = 'swd-linux-amd64'
    elif linux_arm.exists() == True:
        print('Found: Linux-arm version')
        version_found = 'swd-linux-arm'
    elif windows_386.exists() == True:
        print('Found: Windows-386 version')
        version_found = 'swd-windows-386.exe'
    elif windows_amd64.exists() == True:
        print('Found: Windows-amd64 version')
        version_found = 'swd-windows-amd64.exe'
    else:
        version_found = 'none'
    return version_found

def swd_manager():
    swd_exis_check_res = swd_existence_check()
    if swd_exis_check_res != 'none':
        print('Version Installed: ' + swd_exis_check_res)
        return swd_exis_check_res
    elif swd_exis_check_res == 'none':
        print('Vesion Installed: None!')
        print('Downloading swd from https://github.com/SegoCode/swd')
        print('Checking device architecture and OS')
        device_system = get_system()
        print('Detected OS: ' + device_system)
        device_cpuarchitecture = get_cpuarchitecture()
        print('Detected CPU arch.: ' + device_cpuarchitecture)
        ftd = file_to_download(device_system, device_cpuarchitecture)
        download_file('https://github.com/SegoCode/swd/releases/download/1.3/' + ftd, ftd)
        swd_exis_check_res = ftd
        return swd_exis_check_res

def file_to_download(system, cpuarch):
    if system == 'Windows':
        if cpuarch == 'AMD64':
            reqver = 'swd-windows-amd64.exe'
            print('Your version is: ' + reqver)
            return reqver
    else:
        print('Device or CPU architecture unsupported.')
        exit()

def swd_command():
    version = swd_manager()
    system = get_system()
    if system == 'Windows':
        command = version
        return version