import os 
import platform

def env():
    if os.path.exists("/data/data/com.termux"):
        return "termux"
    elif platform.system()=="Windows":
        return "windows"