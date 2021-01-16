from pytube import YouTube
import sys
import time
import os
from threading import Thread
from bs4 import BeautifulSoup
import requests
import platform
import getpass


song_name = None

def get_directory():
    username = getpass.getuser()
    if platform.system() == "Linux":
        directory = f"/home/{username}/Downloads"
    else:
        directory = f"C:\\Users\{username}\\Downloads"
    return directory

def get_song_name(url):
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'lxml')
    html_title = soup.find("title").text
    song_name = ' '.join(html_title.split(" - ")).strip(" YouTube")
    return song_name

def load_animation():
    while 1:
        sys.stdout.write('\rloading |')
        time.sleep(0.1)
        sys.stdout.write('\rloading /')
        time.sleep(0.1)
        sys.stdout.write('\rloading -')
        time.sleep(0.1)
        sys.stdout.write('\rloading \\')
        time.sleep(0.1)
        if str(song_name) + ".mp4" in os.listdir(get_directory()):
            sys.stdout.write('\rDone!     ')
            print(f"The file was saved in your Downloads directory as: {song_name}")
            print("\nThis script was made by MAOR SABAG!!")
            exit(0)

def downloader(url):
    yt = YouTube(url).streams.first().download(get_directory(),filename=song_name)

def usage():
    print(f"Usage: {sys.argv[0]} <YouTube URL Song> [Song File Name]")
    exit(0)

def main():
    if len(sys.argv) > 3 or len(sys.argv) < 2:
        usage() 
    if 'youtube' not in sys.argv[1]:
        usage()
    url = sys.argv[1]
    if len(sys.argv) == 2:
        global song_name
        song_name = get_song_name(url)
    else:
        song_name = sys.argv[2]
    t = Thread(target=load_animation)
    t.start()
    downloader(url)

if __name__ == '__main__':
    main()