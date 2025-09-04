import yt_dlp
import os

def download_youtube(url, audio=False):
    ydl_opts = {
        'format': 'bestaudio/best' if audio else 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }

    os.makedirs("downloads", exist_ok=True)
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info)
    return file_path
