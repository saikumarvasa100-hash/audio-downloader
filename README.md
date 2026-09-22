# Audio Downloader

Paste a link, get an MP3. That's it.

## Use (2 steps)

1. Install what it needs (one time):
   ```
   pip install -r requirements.txt
   ```
   For video links (YouTube etc.) also install ffmpeg: https://ffmpeg.org/download.html

2. Run it:
   ```
   python download_audio.py
   ```
   Or double-click `download_audio.bat` on Windows.

Paste a link when asked. MP3 is saved to `Downloads/Audio`.
Paste another link, or type `q` to quit.

Works with YouTube, Vimeo, SoundCloud, and direct mp3 links.
