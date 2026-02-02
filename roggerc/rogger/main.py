import yt_dlp
import os



def rogger():

    def banner():
        print(r"""

 /$$$$$$$                                                     /$$$$$$ 
| $$__  $$                                                   /$$__  $$
| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ | $$  \__/
| $$$$$$$/ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$      
| $$__  $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/| $$      
| $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$_____/| $$      | $$    $$
| $$  | $$|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      |  $$$$$$/
|__/  |__/ \______/  \____  $$ \____  $$ \_______/|__/       \______/ 
                     /$$  \ $$ /$$  \ $$                              
                    |  $$$$$$/|  $$$$$$/                              
                     \______/  \______/                               



              """)
        
    
    banner()

    dpat=os.path.join(os.path.expanduser("~"),"Downloads")
    faa="rogger"
    pat=os.path.join(dpat,faa)

    if not os.path.exists(pat):
        os.mkdir(pat)

    url = input("paste: ")


    ydl_opts = {
        "format": "best",   # IMPORTANT: no merging
        "outtmpl": f"{pat}/%(title)s.mp3",
        "quiet": False,
    }




    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download complete ✅")

    except yt_dlp.utils.DownloadError as e:
        print("Download failed ❌")
        print(e)
    

def main():
    rogger()