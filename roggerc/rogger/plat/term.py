import yt_dlp
import os
import sys
import time

def bain():
    ban = [
        r"▒█▀▀█ █▀▀█ █▀▀▀ █▀▀▀ █▀▀ █▀▀█ ▒█▀▀█",
        r"▒█▄▄▀ █░░█ █░▀█ █░▀█ █▀▀ █▄▄▀ ▒█░░░",
        r"▒█░▒█ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀░▀▀ ▒█▄▄█",
    ]
    for l in ban:
        print(l)
        time.sleep(0.45)

def roggerc():
    
    dpat = os.path.expanduser("~/storage/downloads")
    while True:
        bain()
        print("""
download: d
exit: e
        """)

        choice = input("rogger:> ")

        if choice in ["e", "exit"]:
            print("FI")
            sys.exit()

        elif choice in ["d", "download"]:
            while True:
                url = input("paste:> ")

                if url.lower() in ["e", "exit"]:
                    sys.exit() 

                ydl_opts = {
                    "format": "best",
                    "outtmpl": f"{dpat}/%(title)s.%(ext)s",
                    "quiet": False,
                }

                try:
                    print(f"Downloading to: {dpat}...")
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    print("Download complete ✅")
                except yt_dlp.utils.DownloadError as es:
                    print("Download failed ❌")
                    print(es)


def main():
    roggerc()