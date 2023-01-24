from MassActionBot import app
from pyrogram import filters , enums 
from MassActionBot.utils.database import chatsdb

@app.on_message(filters.command("start"))
async def _start(_, message): 
    chat_id = message.chat.id
 #   print(chat_id)
    if message.chat.type == enums.ChatType.PRIVATE:
            
    await message.reply_text("am started")
