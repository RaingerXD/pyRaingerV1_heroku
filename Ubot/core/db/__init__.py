import logging
import codecs
import pickle
from string import ascii_lowercase
from typing import Dict, List, Union
from Ubot.core.db.accesdb import *
from config import MONGO_URL
from motor.motor_asyncio import AsyncIOMotorClient


cli = motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client["pyRainger"]
