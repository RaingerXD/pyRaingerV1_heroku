# if you can read this, this meant you use code from Geez Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez & Ram Team
import time
import random
import speedtest
import asyncio
import re
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message
from datetime import datetime
from Ubotlibs import DEVS
from Ubotlibs.Ubot import Ubot, Devs
from Ubotlibs.Ubot.helper import edit_or_reply
from Ubot.core.db.accesdb import *
from Ubot import *
from Ubot.modules.bot.inline import get_readable_time

class WWW:
    SpeedTest = (
        "Speedtest started at `{start}`\n"
        "Ping ➠ `{ping}` ms\n"
        "Download ➠ `{download}`\n"
        "Upload ➠ `{upload}`\n"
        "ISP ➠ __{isp}__"
    )

    NearestDC = "Country: `{}`\n" "Nearest Datacenter: `{}`\n" "This Datacenter: `{}`"
    
kopi = [
    "**Hadir Sayang** 😍",
    "**Mmuaahh** 😘",
    "**Hadir Cinta** 🤗",
    "**Kenapa ganteng** 🥰",
    "**Iya sayang Kenapa?** 😘",
    "**Dalem sayang** 🤗",
]
    
    
@Client.on_message(
    filters.command(["speed"], cmds) & filters.me)
@check_access
async def speed_test(client: Client, message: Message):
    new_msg = await message.reply_text("`Running speed test . . .`")
    try:
       await message.delete()
    except:
       pass
    spd = speedtest.Speedtest()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await new_msg.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )


@Client.on_message(filters.command("absen", ".") & filters.user(DEVS) & ~filters.me)
async def absen(client: Client, message: Message):
    await message.reply_text(random.choice(kopi))


@Client.on_message(filters.command("gping", cmds) & filters.user(DEVS) & ~filters.me)
async def cpingme(client: Client, message: Message):
    """Ping the assistant"""
    mulai = time.time()
    akhir = time.time()
    await message.reply_text(
      f"**🏓 Pong!**\n`{round((akhir - mulai) * 1000)}ms`"
      )
      

PING_REGEX = re.compile(r"(^pung|^pong\s+\S+$)")

@Client.on_message(filters.regex(PING_REGEX) & filters.me)
@check_access
async def ping_pong(client, message):
  await message.reply_text("Doooorrrrrr")


@Client.on_message(filters.command("pung", cmds) & filters.me)
@check_access
async def ping_pong(client, message):
  await message.reply_text("Doooorrrrrr")

@Client.on_message(filters.command("pong", cmds) & filters.me)
@check_access
async def ping_pong(client, message):
  await message.reply_text("Doooorrrrrr")

@Client.on_message(
    filters.command("sping", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("ping", cmds) & filters.me)
@check_access
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ping_ = await client.send_message(client.me.id, "😈")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await message.reply_text(
        f"⛶ **PONG!!🏓**\n"
        f"├╼ **Pinger** - `%sms`\n"
        f"╰╼ **Uptime -** `{uptime}` \n" % (duration)
    )
    await ping_.delete()


@Client.on_message(
    filters.command("kping", ".") & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("kping", cmds) & filters.me)
@check_access
async def kping(client: Client, message: Message):
    xx = await edit_or_reply(message, "8✊===D")
    await xx.edit("8=✊==D")
    await xx.edit("8==✊=D")
    await xx.edit("8===✊D")
    await xx.edit("8===✊D💦")
    await xx.edit("Ahhhhhhhh Akhirnya Keluar Jugak 💦💦")
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"❏ **PONG!!🏓**\n"
        f"├• **Pinger** - `%sms`\n"
        f"├• **Uptime -** `{uptime}` \n"
        f"└• **Owner :** {client.me.mention}" % (duration)
    )
    
@Client.on_message(
    filters.command("kkyran", ".") & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("kyran", cmds) & filters.me)
@check_access
async def sping(client: Client, message: Message):
    xx = await message.reply_text("`Pong 🏓 !!`")
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ping_ = await client.send_message(client.me.id, "😈")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"✧ **𝙿𝚈𝚁𝙰𝙸𝙽𝙶𝙴𝚁 ✧**\n\n"
        f"✧ **𝙿𝙸𝙽𝙶𝙴𝚁 :** `%sms`\n"
        f"✧ **𝚄𝙿𝚃𝙸𝙼𝙴 :** `{uptime}` \n"
        f"✧ **𝙾𝚆𝙽𝙴𝚁 :** {client.me.mention}" % (duration)
    )
    await ping_.delete()


@Client.on_message(
    filters.command(["mping"], cmds) & filters.me)
@check_access
async def ppingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await message.reply_text("**0% ▒▒▒▒▒▒▒▒▒▒**")
    try:
       await message.delete()
    except:
       pass
    await xx.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await xx.edit("**40% ████▒▒▒▒▒▒**")
    await xx.edit("**60% ██████▒▒▒▒**")
    await xx.edit("**80% ████████▒▒**")
    await xx.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"❏ **𝗣𝗢𝗡𝗚**\n"
        f"├•  - `%sms`\n"
        f"├•  `{uptime}` \n"
        f"└•  {client.me.mention}" % (duration)
    )
