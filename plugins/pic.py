# This is bot coded by Happyboy and used for educational purposes only
# Copyright of all images uploaded by this bot is goes to respected owners

import os
from pyrogram import Client,Filters
from telegraph import upload_file

@Client.on_message(Filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hello {message.from_user.first_name},\n<b>I'm a Telegram To Telegra.ph Image Uploader Bot Created By @MaI_BotS</b>",
        reply_to_message_id=message.message_id
    )
    
@Client.on_message(Filters.photo)
async def getimage(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    imgdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".jpg"
    dwn = await client.send_message(
          text="Downloading...",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("Uploading...")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"Oops Something Went Wrong\n{error} Contact @No_OnE_Kn0wS_Me")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(imgdir)
    except:
        pass

@Client.on_message(Filters.text)
async def text(client, message):
await client.send_message(
    text=f"Hello {message.from_user.first_name},\n<b>Please Don't Spam Here I can Only Upload Pictures For Now \n Text To Telegra.ph Will Be Updated Soon \n Support: @mai_BoTs</b>", 
    chat_id=message.chat.id,
    reply_to_message_id=message.message_id
)
