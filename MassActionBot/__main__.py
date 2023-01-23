import asyncio
import importlib 
from pyrogram import idle 
from MassActionBot.plugins import ALL_MODULES 



async def start_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("MassActionBot.plugins." + all_module)
    LOG.print("[bold yellow]ɴᴏᴡ ᴀᴍ ʀᴇᴀᴅʏ ᴛᴏ ғɪɢʜᴛ ʙᴏss..")
    await idle() 
    LOG.print("[bold red]sᴛᴏᴘᴘɪɴɢ ᴛʜᴇ ʙᴏᴛ !")   


if __name__ == "__main__" :
    asyncio.get_event_loop().run_until_complete(start_bot()) 
    
