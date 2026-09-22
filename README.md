# Audio Downloader

Paste a link, get an MP3.

## 🌐 Use in browser (no install)

**Live web app:** https://saikumarvasa100-hash.github.io/audio-downloader/

1. Open it, paste a link, press **Get audio**.
2. **Direct audio links** → download instantly, right in the page.
3. **Video links (YouTube etc.)** → press **Get MP3**, submit the opened
   GitHub request (free login), and a bot replies with your MP3 link in
   about a minute. No setup, nothing to deploy.

## 💻 Run on your computer

```
pip install -r requirements.txt
python download_audio.py
```
Or double-click `download_audio.bat` on Windows.

MP3s save to `Downloads/Audio`. Paste another link, or type `q` to quit.
For video links you also need ffmpeg: https://ffmpeg.org/download.html

## 🤖 How the web bot works

Video requests are handled by `.github/workflows/audio-request.yml`:
an issue with the `audio-request` label triggers a GitHub Action that runs
`yt-dlp` + `ffmpeg`, uploads the MP3 to the `audio-downloads` release,
and comments the download link back on the issue.
