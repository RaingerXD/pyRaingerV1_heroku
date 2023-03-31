import importlib
import time
from datetime import datetime
import asyncio
#from asyncio import get_event_loop_policy
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
    LOGGER("Ubot").info("Memulai Ubot Pyro..")
    for all_module in ALL_MODULES:
        importlib.import_module("Ubot.modules" + all_module)
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            user_id = ex.id
            await buat_log(bot)
            botlog_chat_id = await get_botlog(user_id)
            LOGGER("Info").info("Startup Completed")
            LOGGER("√").info(f"Started as {ex.first_name} | {ex.id} ")
            await join(bot)
            await bot.send_message(botlog_chat_id, MSG_ON.format(BOT_VER, py(), pyro))
            ids.append(ex.id)
        except Exception as e:
            LOGGER("X").info(f"{e}")
    await idle()
    await aiosession.close()
    await app.stop()
    

if __name__ == "__main__":
    LOGGER("Ubot").info("Starting  Ubot")
    install()
    LOOP.run_until_complete(main())
