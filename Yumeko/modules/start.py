import os
from pyrogram import Client
from pyrogram.types import InputMediaPhoto, InputMediaVideo
from config import config
import aiohttp
import tempfile

async def send_safe_media(client: Client, chat_id: int, filename: str = None, url: str = None, caption: str = None, reply_markup=None):
    """
    Send media safely. Supports local files or URLs.
    """
    if filename:
        # Local file path
        file_path = os.path.join(config.DOWNLOAD_LOCATION, filename)
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            print(f"[ERROR] File does not exist or is empty: {file_path}")
            return

        ext = file_path.lower().split('.')[-1]
        try:
            if ext in ["jpg", "jpeg", "png", "webp"]:
                await client.send_photo(chat_id, file_path, caption=caption, reply_markup=reply_markup)
            elif ext in ["mp4", "mkv", "mov"]:
                await client.send_video(chat_id, file_path, caption=caption, reply_markup=reply_markup)
            elif ext in ["mp3", "wav", "ogg"]:
                await client.send_audio(chat_id, file_path, caption=caption, reply_markup=reply_markup)
            else:
                await client.send_document(chat_id, file_path, caption=caption, reply_markup=reply_markup)
            print(f"[INFO] Sent local media: {file_path}")
        except Exception as e:
            print(f"[ERROR] Failed to send local media: {file_path}\n{e}")

    elif url:
        # URL media
        try:
            await client.send_photo(chat_id, url, caption=caption, reply_markup=reply_markup)
            print(f"[INFO] Sent media from URL: {url}")
        except Exception as e:
            print(f"[ERROR] Failed to send media from URL: {url}\n{e}")