from Ubot.core.db import *
from config import MONGO_URL
from Ubot.core.db.usersdb import *
from Ubot.core.db .accesdb import *

from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(MONGO_URL)
db = client["pyRainger"]
