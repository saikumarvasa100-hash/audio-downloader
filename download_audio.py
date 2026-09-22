#!/usr/bin/env python3
"""
Just run it:
  python download_audio.py

Then paste a link when asked. That's it.
File is saved as MP3 in Downloads/Audio.
Paste another link, or type q to quit.

Works with YouTube, Vimeo, SoundCloud, etc. and direct mp3 links.
First run auto-installs what it needs (yt-dlp, requests).
ffmpeg must be installed for video links: https://ffmpeg.org/download.html
"""

import re
import subprocess
import sys
from pathlib import Path


def ensure(package: str, import_name: str = ""):
    try:
        __import__(import_name or package)
    except ImportError:
        print(f"Installing {package} (first run only)...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])


ensure("requests")
ensure("yt-dlp", "yt_dlp")

import requests
from yt_dlp import YoutubeDL

# Fixed location so user never has to choose
SAVE_FOLDER = Path.home() / "Downloads" / "Audio"
DIRECT_AUDIO_EXTS = (".mp3", ".m4a", ".aac", ".wav", ".opus", ".ogg", ".flac", ".wma")


def download_direct(url: str) -> Path:
    SAVE_FOLDER.mkdir(parents=True, exist_ok=True)
    name = url.split("?")[0].split("#")[0].rstrip("/").split("/")[-1] or "audio.mp3"
    if "." not in name:
        name += ".mp3"
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    dest = SAVE_FOLDER / name
    print(f"Downloading to {dest} ...")
    with requests.get(url, stream=True, timeout=30) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    print(f"Saved: {dest}")
    return dest


def download_audio(url: str):
    SAVE_FOLDER.mkdir(parents=True, exist_ok=True)
    clean = url.split("?")[0].split("#")[0].lower()

    # Direct mp3-style link: fast download, no conversion
    if clean.endswith(DIRECT_AUDIO_EXTS):
        try:
            return download_direct(url)
        except Exception as e:
            print(f"Direct download failed ({e}), trying other method...")

    # Everything else (YouTube etc.): extract audio only as mp3
    print("Downloading audio... please wait.")
    with YoutubeDL({
        "format": "bestaudio/best",
        "outtmpl": str(SAVE_FOLDER / "%(title)s.%(ext)s"),
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
    print(f"Saved to {SAVE_FOLDER}")


def main():
    print("=== Audio Downloader ===")
    print(f"Files save to: {SAVE_FOLDER}\n")
    while True:
        url = input("Paste link (or q to quit): ").strip().strip("'\"")
        if url.lower() in ("q", "quit", "exit", ""):
            if url == "":
                continue
            break
        if not re.match(r"^https?://", url, re.IGNORECASE):
            print("That doesn't look like a link. Copy the full link starting with https://\n")
            continue
        try:
            download_audio(url)
            print("Done!\n")
        except Exception as e:
            print(f"Couldn't download that link: {e}\n")


if __name__ == "__main__":
    main()
