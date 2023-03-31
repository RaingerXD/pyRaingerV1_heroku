import importlib
import time
from datetime import datetime
import asyncio
from asyncio import get_event_loop_policy
from pyrogram import idle
from uvloop import install
from Ubotlibs import *
from Ubot import BOTLOG_CHATID, aiosession, bots, app, ids, LOOP
from platform import python_version as py
from Ubot.logging import LOGGER
from pyrogram import __version__ as pyro
from Ubot.modules import ALL_MODULES
from Ubotlibs import *
from Ubot.core.db.activedb import *
from Ubot.core.db.usersdb import *
from config import SUPPORT, CHANNEL, CMD_HNDLR, ADMIN1_ID
import os
from dotenv import load_dotenv


MSG_BOT = """
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
• **Alive
• **Phython**: `{}`
• **Pyrogram**: `{}`
• **Users**: `{}`
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""

MSG_ON = """
**pyRainger Actived ✅**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
• **Versi** : `{}`
• **Phython** : `{}`
• **Pyrogram** : `{}`
• **Masa Aktif** : `{}`
• **Akan Berakhir**: `{}`
**Ketik** `{}alive` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""

MSG = """
**Users**: `{}`
**ID**: `{}`
"""


async def main():
    await app.start()
    LOGGER("Ubot").info("Memulai Rainger Userbot Pyro..")
    for all_module in ALL_MODULES:
        importlib.import_module("Ubot.modules" + all_module)
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
            	await app.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, py, pyro))
            except BaseException as a:
                LOGGER("✓").warning(f"{a}")
            LOGGER("✓").info("Startup Completed")
            LOGGER("✓").info(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            LOGGER("X").info(f"{e}")
    await idle()
    await aiosession.close()

              
if __name__ == "__main__":
   install()
   LOOP.run_until_complete(main())
   LOGGER("Ubot").info("Starting Ubot pyRainger Userbot")
