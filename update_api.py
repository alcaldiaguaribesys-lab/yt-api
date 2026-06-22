import sys
import re

file_path = r"c:\Users\User\Documents\1Samp Gs\yt-api\main.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

s1 = """    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio',
        'quiet': True,
        'no_warnings': True,
        'simulate': True
    }"""
r1 = """    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio',
        'quiet': True,
        'no_warnings': True,
        'simulate': True,
        'extractor_args': {'youtube': {'player_client': ['android']}}
    }"""

content = content.replace(s1, r1)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated main.py extractor args")
