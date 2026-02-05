import os
from rogger.dec import env
from rogger.plat import win,term

print("hi")
g=env()
print(g)

def main():
    if g=="termux":
        term.main()
    elif g=="windows":
        print("hi")
        win.main()