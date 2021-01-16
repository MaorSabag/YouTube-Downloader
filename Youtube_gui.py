import easygui
from pytube import YouTube
import os
import requests
from bs4 import BeautifulSoup
from threading import Thread

song_name = None

def loading():
    easygui.msgbox("Please be patient download as started....", title="YouTube Downloader - Maor")
    while 1:
        if str(song_name) + ".mp4" in os.listdir(get_directory()):
            easygui.msgbox(f"The File has been downloaded successfuly as: {song_name} at you Downloads folder", title="YouTube Downloader - Maor")
            exit(0)

def get_directory():
    directory = os.path.expanduser("~") + "/Downloads"
    return directory


def get_song_name(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    html_title = soup.find("title").text
    song_name = ' '.join(html_title.split(" - ")).strip(" YouTube")
    return song_name


def downloader(url):
    yt = YouTube(url).streams.first().download(get_directory(),filename=song_name)


def main():
    try:
        url = easygui.enterbox("Enter the YouTube's url of the song you want to download:\n", title="YouTube Downloader - Maor")
        if 'youtube' not in url.lower():
            easygui.msgbox("Please enter a YouTube link!")
            exit(0)
        global song_name
        song_name = get_song_name(url)
        t = Thread(target=downloader, args=(url,))
        t.start()
        loading()
    except Exception as e:
        easygui.msgbox(f"{e}", title="YouTube Downloader - Maor")
if __name__ == "__main__":
    main()