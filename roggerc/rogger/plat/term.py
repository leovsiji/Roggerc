import yt_dlp
import os
import sys
import time


    

def rogger():

    dpat = os.path.expanduser("~/storage/downloads")
    while True:
        url = input("paste: ")
        if url in "e,E,exit":
            print("FI")
            sys.exit()
            break     
        else:
            ydl_opts = {
                "format": "best",  
                "outtmpl": f"{dpat}/%(title)s.mp3",
                "quiet": False,
            }




        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("Download complete ✅")
        except yt_dlp.utils.DownloadError as es:
            print("Download failed ❌")
            print(es)


       

    def choice():
        def bain():
            ban=[
              
                r"▒█▀▀█ █▀▀█ █▀▀▀ █▀▀▀ █▀▀ █▀▀█ ▒█▀▀█", 
                r"▒█▄▄▀ █░░█ █░▀█ █░▀█ █▀▀ █▄▄▀ ▒█░░░",
                r"▒█░▒█ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀░▀▀ ▒█▄▄█",
            ]
         
            for l in ban:
                print(l)
                time.sleep(0.45)
        
        bain()

 
        
        print("""
download:d
exit:e         
            """)
          
    
        i = input("rogger:> ")
        while True:
                if i in "e,E,exit":
                    print("FI")
                    sys.exit()
                elif i in "d,D":
                    rogger()
                    break
                else:
                    choice()
                    break

                
                

rogger()


