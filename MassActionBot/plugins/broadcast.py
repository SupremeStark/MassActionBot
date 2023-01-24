from MassActionBot import app, OWNER_ID
from pyrogram import filters 
from MassActionBot.utils.database import get_chats


@app.on_message(filters.command("bcast"))
async def broadcast(_, message):
    print(await get_chats())
