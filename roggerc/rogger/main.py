import os
from rogger.dec import env
from rogger.plat import win,term


g=env()


def main():
    if os.path.exists("/data/data/com.termux"):
        term.rogger()
    elif g=="windows":
        win.rogger()