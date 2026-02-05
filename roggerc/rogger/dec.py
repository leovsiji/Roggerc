import os 
import platform

def env():
    if "TERMUX_VERSION" in os.environ:
        return "termux"
    elif platform.system()=="windows":
        return "windows"