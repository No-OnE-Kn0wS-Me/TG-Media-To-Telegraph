# This is bot coded by @No_OnE_Kn0wS_Me and used for educational purposes only
# Copyright of all images uploaded by this bot is goes to respected owners

import os
from pyrogram import Client,Filters
from telegraph import upload_file

@Client.on_message(Filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hello {message.from_user.first_name},\n<b> I'll Only Work On @MoVieLiNks_oNlY \n You Can't Use Me Here</b>",
        reply_to_message_id=message.message_id
    )

@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"<b> No one's Gonna Help You 😂😂</b>",
        reply_to_message_id=message.message_id
    )

@Client.on_message(Filters.text & Filters.group)
async def text(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hello {message.from_user.first_name},\n<b> If You Didn't Get Your Requested Movie Please Click On The Must Read Button",
        reply_to_message_id=message.message_id
    )
