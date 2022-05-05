import os
import re
import urllib
from youtube_dl import YoutubeDL

def querySearch(input : str):
    STANDARD_FORMAT = input.replace(" ", "+")
    try:
        webURL = urllib.request.urlopen("https://www.youtube.com/results?search_query="+STANDARD_FORMAT)
        webResponse = re.findall(r"watch\?v=(\S{11})", webURL.read().decode())
        return "https://www.youtube.com/watch?v="+webResponse[0]
    except: pass

def downloader(url: str):
    YDL_OPTIONS = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': '/'.join(os.getcwd().split('/')[:3])+'/music'+'/%(title)s.%(ext)s'
    }
    with YoutubeDL(YDL_OPTIONS) as ytdl:
        ytdl.download([url])
        return ytdl.extract_info(url, download=False)