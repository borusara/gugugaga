'''import os
import re
import random

from platform import python_version as kontol
from telethon import events, Button
from Messi.events import register
from Messi import telethn as tbot


PHOTO = "https://telegra.ph/file/41bacc868251e6ad04071.jpg"

@register(pattern=("Awake"))
async def awake(event):
  TEXT = f"""Hi {event.sender.first_name}, I'm Muichiro Tokito ."""\n
  TEXT += f"❄Muichiro Is Alive 🗿 **"\n\n
  TEXT += f"❄My Domain : (https://t.me/Knights_X_association/34)**"\n\n
  TEXT += f"❄ **Powered By: [Knights](https://t.me/hashira_association)**"\n\n
   Thanks For Adding Me Here ❤️ re ❤️ **"
  BUTTON = [[Button.url("Help", "https://t.me/Tokito_Muichiro_robot?start=help"), Button.url("Support", "https://t.me/shoushuke_support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
'''
