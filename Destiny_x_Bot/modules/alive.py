import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Destiny_x_Bot.events import register
from Destiny_x_Bot import telethn as tbot


PHOTO = "https://telegra.ph/file/474d63c62a377356ab705.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = "ยคยค ๐๐๐ฒ ๐๐๐๐ฌ๐ญ๐ซ๐จ, ๐'๐ฆ ๐๐ง๐ฆ๐๐ข! ยคยค\n\n"
    TEXT += f"รธ ๐๐๐๐ก!! ๐๐จ๐ง'๐ญ ๐๐จ๐ญ๐ก๐๐ซ ๐๐๐จ๐ฎ๐ญ ๐ฆ๐ฒ ๐ฌ๐ฉ๐๐๐ ๐๐จ๐ซ ๐ง๐จ๐ฐ รธ\n\n"
    TEXT += f"รธ ๐๐๐๐๐ : ๐๐๐๐๐๐ ๐๐๐๐๐๐๐ รธ\n\n"
    TEXT += f"รธ ๐๐ฒ ๐๐๐๐ฌ๐ญ๐ซ๐จ (๐๐ซ๐๐๐ญ๐จ๐ซ) : [ ๐๐ก๐จ๐ญ๐จ](http://t.me/yameteee_yamete_kudasai) รธ\n\n"
    TEXT += f"รธ แดษดส ษช๐ผ๐ผแดแด๐ผ แดแดษดแดแดแดแด us สแดสแด : @unmei_support รธ\n\n"
    TEXT += "โฅ แดสแดษดแด สแดแด าแดส แดแดแดษชษดษข แดแด โฅ (ใฃโโกโ)ใฃ "
    BUTTON = [
        [
            Button.url("๐ข Updates", "https://t.me/unmei_updates"),
            Button.url("๐ Support", "https://t.me/unmei_support"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
