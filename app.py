"""Full web version: paste any video/audio link, get back an MP3.

Deploy free on Hugging Face Spaces (Gradio SDK), or run locally:
    pip install -r requirements.txt
    python app.py
"""

import tempfile
from pathlib import Path

import gradio as gr
from yt_dlp import YoutubeDL


def grab_audio(url: str):
    url = (url or "").strip().strip("'\"")
    if not url.startswith(("http://", "https://")):
        raise gr.Error("Paste a full link starting with https://")

    tmp = Path(tempfile.mkdtemp())
    with YoutubeDL({
        "format": "bestaudio/best",
        "outtmpl": str(tmp / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }) as ydl:
        ydl.download([url])

    files = sorted(tmp.glob("*.mp3"))
    if not files:
        raise gr.Error("Couldn't extract audio from that link.")
    return str(files[0])


demo = gr.Interface(
    fn=grab_audio,
    inputs=gr.Textbox(label="Link", placeholder="Paste a YouTube / SoundCloud / direct mp3 link…"),
    outputs=gr.Audio(label="Audio (MP3)", type="filepath"),
    title="🎧 Audio Downloader",
    description="Paste a link, get the audio as MP3. No install needed.",
    allow_flagging="never",
)

if __name__ == "__main__":
    demo.launch()
