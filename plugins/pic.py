# This is used for educational purposes only
# Copyright of all images uploaded by this bot is goes to respected owners

import telegraph
import os
from pyrogram import Client,Filters
from telegraph import upload_file

@Client.on_message(Filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"<b>Hello</b> {message.from_user.first_name},\n I'm a Telegram Bot Which Helps You To Upload Images Into Telegra.ph \n\n <b>Made  By:</b> @MaI_bOtS",
        reply_to_message_id=message.message_id
    )
    
@Client.on_message(Filters.photo)
async def getimage(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    imgdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".jpg"
    dwn = await client.send_message(
          text="<b>Downloading... Pls Wait..</b> ",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("<b>Uploading...</b>")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"<b>Oops Something Went Wrong</b>\n{error} Contact @Mai_BoTs")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(imgdir)
    except:
        pass


@Client.on_message(Filters.text)
async def gettxt(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    txtdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id)
    dwn = await client.send_message(
          text="<b>Downloading... Pls Wait..</b> ",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_message(
            message=message,
            file_name=txtdir
        )
    await dwn.edit_text("<b>Uploading...</b>")
    try:
        response = upload_file(txtdir)
    except Exception as error:
        await dwn.edit_text(f"<b>Oops Something Went Wrong</b>\n{error} Contact @Mai_BoTs")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(txtdir)
    except:
        pass
