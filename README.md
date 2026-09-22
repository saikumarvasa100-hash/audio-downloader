# Audio Downloader

Paste a direct audio link, get the file.

## 🌐 Use in browser (no install, no login)

**Live web app:** https://saikumarvasa100-hash.github.io/audio-downloader/

Open it, paste a direct audio link (`.mp3`, `.m4a`, `.wav`, `.ogg`, …),
press **Download**. Plays + saves right in the page.

## 💻 Run on your computer (any link, incl. YouTube)

```
pip install -r requirements.txt
python download_audio.py
```
Or double-click `download_audio.bat` on Windows.

MP3s save to `Downloads/Audio`. Paste another link, or type `q` to quit.
For video links you also need ffmpeg: https://ffmpeg.org/download.html
