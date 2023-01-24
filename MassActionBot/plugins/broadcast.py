from MassActionBot import app, OWNER_ID
from pyrogram import filters 
from MassActionBot.utils.database import get_chats


@app.on_message(filters.command("bcast"))
async def broadcast(_, message):
    chats = []
    schats = await get_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        print(chats)
