import config
from pyrogram import Client, filters

api_id = config.API_ID
api_hash = config.API_HASH

app = Client(config.SHORT_NAME, api_id=api_id, api_hash=api_hash)

from core import routers
