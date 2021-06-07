

import os
from pyrogram import Client,filters 
from telegraph import upload_file



@Client.on_message(filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hello {message.from_user.first_name},\n<b>I'm a Telegram To Telegra.ph Image/Video Uploader Bot. \n Created By @MaI_BotS</b> \n  Do /help For More",
        reply_to_message_id=message.message_id
    )

@Client.on_message(filters.command(["help"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"<b> Send Me Any Video Or Photo I'll Upload It Into Telegra.ph. \n Created By @MaI_BotS</b>",
        reply_to_message_id=message.message_id
    )
    
@Client.on_message(filters.photo)
async def getimage(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    imgdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".jpg"
    dwn = await client.send_message(
          text="<b>Downloading...</b>",
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
        await dwn.edit_text(f"Oops Something Went Wrong\n{error} Contact @No_OnE_Kn0wS_Me")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(imgdir)
    except:
        pass

@Client.on_message(filters.video)
async def getvideo(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    viddir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".mp4"
    dwn = await client.send_message(
          text="<b>Downloading...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=viddir
        )
    await dwn.edit_text("<b>Uploading...</b>")
    try:
        response = upload_file(viddir)
    except Exception as error:
        await dwn.edit_text(f"Oops Something Went Wrong\n{error} Contact @No_OnE_Kn0wS_Me")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(viddir)
    except:
        pass

@Client.on_message(filters.sticker)
async def stikcer_s(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    animdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".webp"
    dwn = await client.send_message(
          text="<b>Downloading...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=animdir
        )
    await dwn.edit_text("<b>Uploading...</b>")
    try:
        response = upload_file(animdir)
    except Exception as error:
        await dwn.edit_text(f"Oops Something Went Wrong\n{error} Contact @No_OnE_Kn0wS_Me")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(animdir)
    except:
        pass

