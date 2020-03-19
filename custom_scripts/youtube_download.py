#!/usr/bin/python3.7

import sys
import youtube_dl
import os

youtube_url = sys.argv[1]
out_name = sys.argv[2] if len(sys.argv) > 2 else 'temp'
out_folder = sys.argv[3] if len(sys.argv) > 3 else ''

full_file_path = f"""/config/www/audio/youtube/{out_folder}{out_name}"""

ydl = youtube_dl.YoutubeDL({'format': 'bestaudio', 'outtmpl': full_file_path})

with ydl:
    result = ydl.extract_info(youtube_url, download=True)
    os.system(
        f"""ffmpeg -i {full_file_path} -acodec libmp3lame {full_file_path}.mp3""")
    os.system(f"""rm {full_file_path}""")
