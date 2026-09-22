# Audio Downloader

Paste a link, get an MP3.

## 🌐 Use in browser (no install)

**Live web app:** https://saikumarvasa100-hash.github.io/audio-downloader/

Open it, paste a link, press **Get audio**.
- Direct audio links download right in the page.
- Video pages (YouTube etc.) can't be converted by a static page alone —
  for those, use the full version below (free, ~2 min setup).

## Full version — any link including YouTube (free web app)

1. Go to https://huggingface.co/new-spaces
2. Create a Space with SDK **Gradio**, then upload `app.py` + `requirements.txt` from this repo.
3. Open your Space URL, paste any link, get MP3. Share that URL with anyone.

## 💻 Run on your computer

```
pip install -r requirements.txt
python download_audio.py
```
Or double-click `download_audio.bat` on Windows.

MP3s save to `Downloads/Audio`. Paste another link, or type `q` to quit.
For video links you also need ffmpeg: https://ffmpeg.org/download.html
