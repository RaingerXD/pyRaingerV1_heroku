from Ubot.core.db import *
from config import MONGO_URL
from Ubot.core.db import usersdb
from Ubot.core.db import accesdb

from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(MONGO_URL)
db = client["pyRainger"]
