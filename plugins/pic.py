# This is bot coded by @No_OnE_Kn0wS_Me and used for educational purposes only
# Copyright of all images uploaded by this bot is goes to respected owners

import os
from pyrogram import Client,filters
from telegraph import upload_file
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup

STICKER_PCK = 'CAACAgUAAxkBAAIFNmBXNYZaoplsDsP_lyh5Lo170CLjAAKVAAMFqVIzXbJ5Od2V8nseBA' 

@Client.on_message(filters.command(["start"]))
async def start(client, message):
    await client.send_sticker(
        chat_id=message.chat.id,
        STICKER_PCK, 
        reply_to_message_id=message.message_id
    )

@Client.on_message(filters.command(["help"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"<b> No one's Gonna Help You 😂😂</b>",
        reply_to_message_id=message.message_id
    )

@Client.on_message(filters.text & filters.group)
async def text(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hello {message.from_user.first_name},\n<b> If You Didn't Get Your Requested Movie Please Check The Movie Spelling In [Google](www.google.com) Then Search In Shared Files With Correct Name",
        reply_to_message_id=message.message_id
    )
