import sys
from datetime import datetime, timezone
from typing import Union, Dict, Optional


BL_GCAST = [-1001755737234]
BL_GEEZ = [1245451624]
DEVS = [5615921474]
ADMINS = [5615921474]
BOT_VER = "1.1.0"
pemaen_lenong = []
pemaen_gendang = [5615921474]

def pemaen_gendang(client, message):
    chat_id = message.chat.id
    admins = client.get_chat_administrators(-1001755737234)
    admin_list = [admin.user.first_name for admin in admins]
    pemaen_gendang.append(admin_list)

async def join(client):
    try:
        await client.join_chat("raingersuppor")
        await client.join_chat("raingerproject")
        await client.join_chat("xtafes")
        await client.join_chat("xtafesgc")
    except BaseException:
        pass
