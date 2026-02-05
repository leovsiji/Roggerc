import os
from rogger.dec import env
from rogger.plat import win,term


g=env()


def main():
    if g=="termux":
        term.main()
    elif g=="windows":
        win.main()