import sys
import re

file_path = r"c:\Users\User\Documents\1Samp Gs\yt-api\main.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("yt = YouTube(url, use_po_token=True)", "yt = YouTube(url, use_po_token=False)")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated main.py to disable po_token")
