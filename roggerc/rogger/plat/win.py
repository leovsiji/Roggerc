import yt_dlp
import os
import sys
import time

def bain():
        ban=[
            r"                                                                     ",
            r" /$$$$$$$                                                     /$$$$$$",
            r"| $$__  $$                                                   /$$__  $$",
            r"| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ | $$  \__/",
            r"| $$$$$$$/ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$      ",
            r"| $$__  $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/| $$",      
            r"| $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$_____/| $$      | $$    $$",
            r"| $$  | $$|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      |  $$$$$$/",
            r"|__/  |__/ \______/  \____  $$ \____  $$ \_______/|__/       \______/ ",
            r"                     /$$  \ $$ /$$  \ $$                              ",                              
            r"                    |  $$$$$$/|  $$$$$$/                              ",                              
            r"                     \______/  \______/                               "

            ]
         
        for l in ban:
            print(l)
            time.sleep(0.30)
    
    

def rogger():
    bain()

    print("""
download:d
exit:e         
            """)
    dpat=os.path.join(os.path.expanduser("~"),"Downloads")
    faa="rogger"
    pat=os.path.join(dpat,faa)

    if not os.path.exists(pat):
        os.mkdir(pat)

        
    i = input("rogger:> ")
    while True:
            if i in "e,E,exit":
                print("FI")
                sys.exit()
            elif i in "d,D":
                while True:
                    url = input("paste:> ")
                    if url in "e,E,exit":
                        print("FI")
                        sys.exit()
                        break     
                    else:
                        ydl_opts = {
                            "format": "best",  
                            "outtmpl": f"{pat}/%(title)s.mp3",
                            "quiet": False,
                        }
                
                        
                        try:
                            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                                ydl.download([url])
                                print("Download complete ✅")
                        except yt_dlp.utils.DownloadError as es:
                            print("Download failed ❌")
                            print(es)
            else:
                rogger()

def main():                              
    rogger()


