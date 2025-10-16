import random
import time
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ParseMode
from Yumeko import app
import aiohttp
import os

# IMAGE SETTINGS
IMAGE_URLS = [
    "https://files.catbox.moe/k3orsl.jpg"  # Make sure this URL works in browser
]
LOCAL_FALLBACK_IMAGE = "fallback.jpg"  # Place a local image in your project folder

# START COMMAND
@app.on_message(filters.command("start") & filters.private)
async def handle_start(client, message):
    await send_start_message(client, message.chat.id)

# CALLBACK HANDLER FOR BACK & REFRESH
@app.on_callback_query(filters.regex("back_to_start|refresh"))
async def handle_callback(client, callback_query):
    await callback_query.answer()  # avoid timeout
    await send_start_message(client, callback_query.message.chat.id, callback_query.message)

# HELPER: Validate URL
async def is_valid_url(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.head(url) as resp:
                return resp.status == 200
    except:
        return False

# SEND OR EDIT START MESSAGE
async def send_start_message(client, chat_id, message_to_edit=None):
    bot_user = await client.get_me()
    mention_bot = f"[{bot_user.first_name}](tg://user?id={bot_user.id})"

    # Pick random image
    img_url = random.choice(IMAGE_URLS)
    if not await is_valid_url(img_url):
        img_url = None  # fallback to local image

    caption = f"""Hello! I am {mention_bot} 🤖

[Download all your favorite anime here!](https://t.me/boinker_bot/boinkapp?startapp=boink5630057244)
[Join the Anime Group](https://t.me/PAWSOG_bot/PAWS?startapp=m5eBzU4U)"""

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

    # Edit if possible
    if message_to_edit and message_to_edit.photo:
        await message_to_edit.edit_caption(
            caption=caption,
            reply_markup=keyboard,
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        # Use URL if valid, else fallback to local
        if img_url:
            await client.send_photo(
                chat_id=chat_id,
                photo=img_url,
                caption=caption,
                reply_markup=keyboard,
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            # Ensure local fallback image exists
            if os.path.exists(LOCAL_FALLBACK_IMAGE):
                await client.send_photo(
                    chat_id=chat_id,
                    photo=LOCAL_FALLBACK_IMAGE,
                    caption=caption,
                    reply_markup=keyboard,
                    parse_mode=ParseMode.MARKDOWN
                )
            else:
                # If no image available, send plain text
                await client.send_message(
                    chat_id=chat_id,
                    text=caption,
                    reply_markup=keyboard,
                    parse_mode=ParseMode.MARKDOWN
                )