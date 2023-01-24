from MassActionBot import app
from pyrogram import filters , enums 
from MassActionBot.utils.database import chatsdb

@app.on_message(filters.command("start"))
async def _start(_, message): 
    chat_id = message.chat.id
    print(chat_id)    
    check = await chatsdb.find_one({"chat_id" : chat_id}) 
    if not check:
        await chatsdb.insert_one({"chat_id" : chat_id})       
    await message.reply_text("am started")
