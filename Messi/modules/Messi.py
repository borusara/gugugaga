'''import os
import re
import random

from platform import python_version as kontol
from telethon import events, Button
from Messi.events import register
from Messi import telethn as tbot


PHOTO = "https://graph.org//file/9ec71582b5b6209a09f0c.jpg"

@register(pattern=("Awake"))
async def awake(event):
  TEXT = f"""Hi {event.sender.first_name}, I'M Kawaki Uzumaki ."""\n
  TEXT += f"❄Kwaki Uzumaki 🗿 **"\n\n
  TEXT += f"❄My Domain : (https://t.me/Knights_X_association/34)**"\n\n
  TEXT += f"❄ **Powered By: [Knights](https://t.me/hashira_association)**"\n\n
   Thanks For Adding Me Here ❤️ re ❤️ **"
  BUTTON = [[Button.url("Help", "http://t.me/Uzumaki_Kawaki_Bot?start=help"), Button.url("Support", "https://t.me/shoushuke_support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
'''
