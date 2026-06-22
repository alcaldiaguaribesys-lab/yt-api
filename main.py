from fastapi import FastAPI, HTTPException
import yt_dlp
import asyncio

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API de YouTube en la Nube activa!"}

@app.get("/search")
async def search_videos(q: str):
    ydl_opts = {
        'extract_flat': True,
        'quiet': True,
        'no_warnings': True,
    }
    try:
        # Ejecutamos yt_dlp de forma asincrona para no bloquear
        def fetch():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                return ydl.extract_info(f"ytsearch15:{q}", download=False)
                
        info = await asyncio.to_thread(fetch)
        
        results = []
        if 'entries' in info:
            for entry in info['entries']:
                # yt-dlp puede retornar nil/None para algunos campos, sanitizamos
                results.append({
                    "id": entry.get("id", ""),
                    "title": entry.get("title", ""),
                    "duration": entry.get("duration", 0)
                })
                
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get-url")
async def get_url(id: str):
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio',
        'quiet': True,
        'no_warnings': True,
        'simulate': True
    }
    try:
        def fetch():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                return ydl.extract_info(f"https://www.youtube.com/watch?v={id}", download=False)
                
        info = await asyncio.to_thread(fetch)
        
        url = info.get("url", "")
        if url:
            return {"url": url}
        else:
            raise HTTPException(status_code=404, detail="No URL found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
