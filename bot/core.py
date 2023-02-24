import  os 
from sys import platform




def platform_system():
    if platform == "linux" or platform == "linux2":
        return "linux"
    elif platform == "darwin":
        return "osx"
    elif platform == "win32":
        return "windows"
    

def shutdown_pc():
    if platform_system() == "linux":
        os.system("shutdown  now -h")
    elif platform_system() == "osx":
        os.system("shutdown now -h")
    elif platform_system() == "windows":
        os.system("shutdown /s /t 1") # 1 second delay


def restart_pc():
    if platform_system() == "linux":
        os.system("shutdown  now -r")
    elif platform_system() == "osx":
        os.system("shutdown now -r")
    elif platform_system() == "windows":
        os.system("shutdown /r /t 1") # 1 second delay
    
def sleep_pc():
    if platform_system() == "linux":
        os.system("systemctl suspend")
    elif platform_system() == "osx":
        os.system("pmset sleepnow")
    elif platform_system() == "windows":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") # 1 second delay
    
def hibernate_pc():
    if platform_system() == "linux":
        os.system("systemctl hibernate")
    elif platform_system() == "osx":
        os.system("pmset hibernatemode 25")
    elif platform_system() == "windows":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") # 1 second delay

def lock_pc():
    if platform_system() == "linux":
        os.system("loginctl lock-session")
    elif platform_system() == "osx":
        os.system("pmset displaysleepnow")
    elif platform_system() == "windows":
        os.system("rundll32.exe user32.dll,LockWorkStation") # 1 second delay

def unlock_pc():
    if platform_system() == "linux":
        os.system("loginctl unlock-session")
    elif platform_system() == "osx":
        os.system("open /System/Library/Frameworks/ScreenSaver.framework/Versions/A/Resources/ScreenSaverEngine.app/")
    elif platform_system() == "windows":
        os.system("tscon.exe %sessionname% /dest:console") # 1 second delay

def logout_pc():
    if platform_system() == "linux":
        os.system("loginctl terminate-session")
    elif platform_system() == "osx":
        os.system("osascript -e 'tell application \"loginwindow\" to «event aevtrlgo»'")
    elif platform_system() == "windows":
        os.system("logoff") # 1 second delay

def login_pc():
    if platform_system() == "linux":
        os.system("loginctl unlock-session")
    elif platform_system() == "osx":
        os.system("open /System/Library/Frameworks/ScreenSaver.framework/Versions/A/Resources/ScreenSaverEngine.app/")
    elif platform_system() == "windows":
        os.system("tscon.exe %sessionname% /dest:console") # 1 second delay


def wake_pc():
    if platform_system() == "linux":
        os.system("loginctl unlock-session")
    elif platform_system() == "osx":
        os.system("open /System/Library/Frameworks/ScreenSaver.framework/Versions/A/Resources/ScreenSaverEngine.app/")
    elif platform_system() == "windows":
        os.system("tscon.exe %sessionname% /dest:console") # 1 second delay