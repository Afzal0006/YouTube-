import yt_dlp
import os

def download_youtube(url, audio=False):
    os.makedirs("downloads", exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best' if audio else 'best[height<=480]',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': True,
        'merge_output_format': 'mp4' if not audio else 'mp3'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

            # Agar audio hai to extension mp3 force karna
            if audio and not file_path.endswith(".mp3"):
                base, _ = os.path.splitext(file_path)
                file_path = base + ".mp3"

        return file_path
    except Exception as e:
        print(f"[Downloader Error] {e}")
        return None
