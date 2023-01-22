import os
import asyncio
from config import Config
from pyrogram import Client,idle
from rich.console import Console
from rich.table import Table
from motor.motor_asyncio import AsyncIOMotorClient
from MassActionBot.utils.data import LOG_MSG as START_TEXT

#getting variables
API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.BOT_TOKEN
SUDOES = Config.BAN_PROTECTED
OWNER_ID = Config.OWNER_ID
CLONE = Config.CLONE
START_PIC = Config.START_PIC
SUDOES.append(OWNER_ID)

#rich
LOG = Console()


#database
#mongo = AsyncIOMotorClient
#db = mongo.AMSTARK


#client
app = Client(
    "SupremeStark",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN,
    plugins=dict(root="MassActionBot/plugins"))

#bot info
BOT_ID = 0
BOT_NAME = ""
BOT_USERNAME = ""
MENTION = ""




os.system("clear")
header = Table(show_header=True, header_style="bold yellow")
header.add_column(START_TEXT)
LOG.print(header)
LOG.print("[bold yellow]ɢᴇᴛᴛɪɴɢ ɪɴғᴏ ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ.....")
app.start()
bot =  app.get_me()
BOT_ID = bot.id
BOT_USERNAME = bot.username
MENTION = bot.mention
if bot.last_name:
    BOT_NAME = bot.first_name + " " + bot.last_name
else:
    BOT_NAME = bot.first_name
asyncio.sleep(2)
LOG.print("[bold yellow]ɢᴏᴛ ᴀʟʟ ᴛʜᴇ ɪɴғᴏ......")
asyncio.sleep(1)
LOG.print(f"[bold cyan]ʙᴏᴛ ɪᴅ : {BOT_ID}\nʙᴏᴛ ɴᴀᴍᴇ : {BOT_NAME}\nʙᴏᴛ ᴜsᴇʀɴᴀᴍᴇ : {BOT_USERNAME}")
asyncio.sleep(0.5)
LOG.print("[bold yellow]ɴᴏᴡ ᴀᴍ ʀᴇᴀᴅʏ ᴛᴏ ғɪɢʜᴛ ʙᴏss..")
idle()    



#loop = asyncio.get_event_loop()
#loop.run_until_complete(MassActionBot())    



    
    

    
    



