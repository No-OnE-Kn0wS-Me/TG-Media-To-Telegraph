# This is used for educational purposes only
# Copyright of all images uploaded by this bot is goes to respected owners
from typing import Optional, List
import logging
from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async
from telegraph import Telegraph
import os
from telethon import events
from pyrogram import Client,Filters
from telegraph import upload_file

LOGGER = logging.getLogger(__name__)


@Client.on_message(Filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"<b>Hello</b> {message.from_user.first_name},\n I'm a Telegram Bot Which Helps You To Upload Images Into Telegra.ph \n\n <b>Made  By:</b> @MaI_bOtS",
        reply_to_message_id=message.message_id
    )

@Client.on_message(Filters.photo)
async def getimage(client, message, event):
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
def post_telegraph(bot: Bot, update: Update, args: List[str]):
    short_name = "Done By @Mai_BotS"
    msg = update.effective_message # type: Optional[Message]
    telegraph = Telegraph()
    r = telegraph.create_account(short_name=short_name)
    auth_url = r["auth_url"]
    LOGGER.info(auth_url)
    title_of_page = " ".join(args)
    page_content = msg.reply_to_message.text
    page_content = page_content.replace("\n", "<br>")
    response = telegraph.create_page(
        title_of_page,
        html_content=page_content
    )
    msg.reply_text("https://telegra.ph/{}".format(response["path"]))

