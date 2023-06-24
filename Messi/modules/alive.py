import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as x
from telethon import __version__ as y
from pyrogram import __version__ as z
from Messi.events import register
from Messi import telethn as tbot


PHOTO = "https://telegra.ph/file/56479f8c801e0fe022369.mp4"

@register(pattern=("Awake Muichiro"))
@register(pattern=("Awake muichiro"))
@register(pattern=("Awake muichirou"))
@register(pattern=("Awake Muichirou"))
@register(pattern=("Awake tokito"))
@register(pattern=("Awake Tokito"))
@register(pattern=("awake Muichiro"))
@register(pattern=("awake muichiro"))
@register(pattern=("awake muichirou"))
@register(pattern=("awake Muichirou"))
@register(pattern=("awake tokito"))
@register(pattern=("awake Tokito"))
@register(pattern=("/awake"))
@register(pattern=("/Awake"))
@register(pattern=("/alive"))
@register(pattern=("/Alive"))
          
          


async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Kawaki Uzumaki** \n\n"
  TEXT += "🗿 **I'm Working Properly** \n\n"
  TEXT += f"🗿 **My Developers : [Kawaki creators](https://t.me/shoushuke_updates/3)** \n\n"
  TEXT += f"🗿 **Library Version :** `{x}` \n\n"
  TEXT += f"🗿 **Telethon Version :** `{y}` \n\n"
  TEXT += f"🗿 **Pyrogram Version :** `{z}` \n\n"
  TEXT += "**🗿 Thanks For Adding Me Here **"
  BUTTON = [[Button.url("Help", "http://t.me/Uzumaki_Kawaki_Bot?start=help"), Button.url("My Headquarters", "https://t.me/shoushuke_support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
