import random
import time
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ParseMode
from Yumeko import app

IMAGE_URLS = [
    "https://files.catbox.moe/k3orsl.jpg"
]

# Start command
@app.on_message(filters.command("start") & filters.private)
async def handle_start(client, message):
    await send_start_message(client, message.chat.id)

# Callback for "back_to_start" and "refresh"
@app.on_callback_query(filters.regex("back_to_start|refresh"))
async def handle_callback(client, callback_query):
    await callback_query.answer()  # Acknowledge callback
    await send_start_message(client, callback_query.message.chat.id, callback_query.message)

# Function to calculate ping
async def calculate_ping(client, chat_id):
    start_time = time.time()
    sent_message = await client.send_message(chat_id, "Calculating ping...")
    end_time = time.time()
    await sent_message.delete()
    ping = round((end_time - start_time) * 1000, 3)
    return ping

# Function to send or edit the start message
async def send_start_message(client, chat_id, message_to_edit=None):
    bot_user = await client.get_me()
    mention_bot = f"[{bot_user.first_name}](tg://user?id={bot_user.id})"
    img_url = random.choice(IMAGE_URLS)

    caption = """[Download all your favorite anime here!](https://t.me/boinker_bot/boinkapp?startapp=boink5630057244)
[🎥✨ Don't miss out on the latest episodes and classic series – grab them now!](https://t.me/boinker_bot/boinkapp?startapp=boink5630057244)

[Anime Upload Here ⬇️](https://t.me/boinker_bot/boinkapp?startapp=boink5630057244)

[Join the group ⬇️](https://t.me/PAWSOG_bot/PAWS?startapp=m5eBzU4U)"""

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Add Me To Your Group", url=f"https://t.me/{bot_user.username}?startgroup=true")],
            [InlineKeyboardButton("Download All Anime Free!!", url="https://t.me/PAWSOG_bot/PAWS?startapp=m5eBzU4U")],
            [InlineKeyboardButton("Download Blue Box!!", url="https://t.me/+qFcr7Hw_RaI3NDJl")],
            [InlineKeyboardButton("Download Dr Stone!!", url="https://t.me/+ZADU2yOd2b84YTQ1")],
            [
                InlineKeyboardButton("Download One Piece", url="https://t.me/+xsuErnqUX_A5YzE1"),
                InlineKeyboardButton("Support Group", url="https://t.me/GODL_FC"),
            ],
        ]
    )

    if message_to_edit:
        # Only edit if it's a photo message
        if message_to_edit.photo:
            await message_to_edit.edit_caption(
                caption=caption,
                reply_markup=keyboard,
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            # If not a photo, send a new one
            await client.send_photo(
                chat_id=chat_id,
                photo=img_url,
                caption=caption,
                reply_markup=keyboard,
                parse_mode=ParseMode.MARKDOWN
            )
    else:
        await client.send_photo(
            chat_id=chat_id,
            photo=img_url,
            caption=caption,
            reply_markup=keyboard,
            parse_mode=ParseMode.MARKDOWN
        )