
import subprocess

def download_video_to_mp3(link):
    cmd = ["yt-dlp",
            "-x",
            "--audio-format",
            "mp3",
            link
            ]
    subprocess.call(cmd)



while(True):
    link = input("Youtube Link. Turns into mp3: ")
    download_video_to_mp3(link)
