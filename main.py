from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yt_dlp
from pytubefix import YouTube

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API YouTube activa"}

@app.get("/search")
def search(q: str):
    ydl_opts = {
        'extract_flat': True,
        'quiet': True,
        'no_warnings': True,
        'simulate': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch15:{q}", download=False)
            results = []
            for entry in info.get('entries', []):
                results.append({
                    "id": entry.get("id"),
                    "title": entry.get("title"),
                    "duration": entry.get("duration")
                })
            return {"results": results}
        except Exception as e:
            return {"error": str(e)}

@app.get("/get-url")
def get_url(id: str):
    try:
        # Usar pytubefix para extraer el enlace de audio, que evita bloqueos de bot
        url = f"https://www.youtube.com/watch?v={id}"
        yt = YouTube(url, use_po_token=False)
        ys = yt.streams.get_audio_only()
        if ys and ys.url:
            return {"url": ys.url}
        else:
            return {"error": "No audio stream found"}
    except Exception as e:
        return {"error": str(e)}
