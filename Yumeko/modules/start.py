import random
import time
import os
import aiohttp
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ParseMode
from Yumeko import app

# Reliable Telegram-compatible image (replace with your own)
IMAGE_URLS = [
    "https://telegra.ph/file/6e0f7d7c8b2a2b0e4f8d6.jpg"  # Use a valid telegra.ph image
]
LOCAL_FALLBACK_IMAGE = "fallback.jpg"  # Keep this file in your project folder

@app.on_message(filters.command("start") & filters.private)
async def handle_start(client, message):
    await send_start_message(client, message.chat.id)

@app.on_callback_query(filters.regex("back_to_start|refresh"))
async def handle_callback(client, callback_query):
    await callback_query.answer()
    await send_start_message(client, callback_query.message.chat.id, callback_query.message)

# Helper: check if URL works
async def is_valid_url(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.head(url) as resp:
                return resp.status == 200
    except:
        return False

async def send_start_message(client, chat_id, message_to_edit=None):
    bot_user = await client.get_me()
    img_url = random.choice(IMAGE_URLS)
    if not await is_valid_url(img_url):
        img_url = None

    caption = f"""Hello! I’m [{bot_user.first_name}](tg://user?id={bot_user.id}) 🤖

[🎥 Download all your favorite anime here!](https://t.me/boinker_bot/boinkapp?startapp=boink5630057244)
[🎬 Join the Anime Group](https://t.me/PAWSOG_bot/PAWS?startapp=m5eBzU4U)"""

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Add Me To Your Group", url=f"https://t.me/{bot_user.username}?startgroup=true")],
        [InlineKeyboardButton("Download All Anime Free!!", url="https://t.me/PAWSOG_bot/PAWS?startapp=m5eBzU4U")],
        [InlineKeyboardButton("Download Blue Box!!", url="https://t.me/+qFcr7Hw_RaI3NDJl")],
        [InlineKeyboardButton("Download Dr Stone!!", url="https://t.me/+ZADU2yOd2b84YTQ1")],
        [
            InlineKeyboardButton("Download One Piece", url="https://t.me/+xsuErnqUX_A5YzE1"),
            InlineKeyboardButton("Support Group", url="https://t.me/GODL_FC"),
        ]
    ])

    try:
        if message_to_edit and message_to_edit.photo:
            await message_to_edit.edit_caption(
                caption=caption,
                reply_markup=keyboard,
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            if img_url:
                await client.send_photo(
                    chat_id=chat_id,
                    photo=img_url,
                    caption=caption,
                    reply_markup=keyboard,
                    parse_mode=ParseMode.MARKDOWN
                )
            elif os.path.exists(LOCAL_FALLBACK_IMAGE):
                await client.send_photo(
                    chat_id=chat_id,
                    photo=LOCAL_FALLBACK_IMAGE,
                    caption=caption,
                    reply_markup=keyboard,
                    parse_mode=ParseMode.MARKDOWN
                )
            else:
                await client.send_message(
                    chat_id=chat_id,
                    text=caption,
                    reply_markup=keyboard,
                    parse_mode=ParseMode.MARKDOWN
                )
    except Exception as e:
        print(f"[ERROR] Failed to send start message: {e}")
        await client.send_message(chat_id, "⚠️ Failed to send image, sending text instead.")
        await client.send_message(chat_id, caption, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)