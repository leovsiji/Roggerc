from rogger.dec import env
from rogger.plat import win,term


g=env()


def main():
    if g=="termux":
        term.rogger()
    elif g=="windows":
        win.rogger()