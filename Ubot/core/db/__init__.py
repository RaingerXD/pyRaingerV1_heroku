from Ubotlibs.Ubot.Db import cli
from config import MONGO_URL
from .usersdb import *
from .accesdb import *

from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(MONGO_URL)
db = client["pyRainger"]
