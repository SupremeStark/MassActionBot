from config import Config
from pyrogram import Client
from rich.console import Console


#getting variables
API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.BOT_TOKEN
SUDOES = Config.BAN_PROTECTED
CLONE = Config.CLONE


#rich
LOG = Console()

app = Client(
    "SupremeStark",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN )




