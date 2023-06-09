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

from asyncio import sleep

from pyrogram import Client, enums, filters
from pyrogram.raw import functions
from pyrogram.types import Message
from Ubotlibs.Ubot import Ubot
from Ubotlibs.Ubot.helper.PyroHelpers import ReplyCheck
from Ubot import cmds
from Ubot.modules.basic import add_command_help
from Ubot.core.db.accesdb import *
from .help import add_command_help

commands = {
    "ftyp": enums.ChatAction.TYPING,
    "fvid": enums.ChatAction.RECORD_VIDEO,
    "faud": enums.ChatAction.RECORD_AUDIO,
    "frou": enums.ChatAction.RECORD_VIDEO_NOTE,
    "fpho": enums.ChatAction.UPLOAD_PHOTO,
    "fstick": enums.ChatAction.CHOOSE_STICKER,
    "fdoc": enums.ChatAction.UPLOAD_DOCUMENT,
    "floc": enums.ChatAction.FIND_LOCATION,
    "fgame": enums.ChatAction.PLAYING,
    "fcon": enums.ChatAction.CHOOSE_CONTACT,
    "fstop": enums.ChatAction.CANCEL,
    "fscreen": "screenshot",
}

@Ubot(list(commands), cmds)
@check_access
async def fakeactions_handler(client: Client, message: Message):
    cmd = message.command[0]
    try:
        sec = int(message.command[1])
        if sec > 60:
            sec = 60
    except:
        sec = None
    await message.delete()
    action = commands[cmd]
    try:
        if action != "screenshot":
            if sec and action != enums.ChatAction.CANCEL:
                await client.send_chat_action(chat_id=message.chat.id, action=action)
                await sleep(sec)
            else:
                return await client.send_chat_action(
                    chat_id=message.chat.id, action=action
                )
        else:
            for _ in range(sec if sec else 1):
                await client.send(
                    functions.messages.SendScreenshotNotification(
                        peer=await client.resolve_peer(message.chat.id),
                        reply_to_msg_id=0,
                        random_id=client.rnd_id(),
                    )
                )
                await sleep(0.1)
    except Exception as e:
        return await client.send_message(
            message.chat.id,
            f"**ERROR:** `{e}`",
            reply_to_message_id=ReplyCheck(message),
        )
