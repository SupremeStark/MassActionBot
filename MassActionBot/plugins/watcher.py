from MassActionBot import app
from pyrogram import filters 
from MassActionBot.utils.database import chatsdb


@app.on_message(filters.new_chat_members,group=2)
async def addinDb(_, message):
    BOT_ID = (await _.get_me()).id
    chat_id = message.chat.id
    check = await chatsdb.find_one({"chat_id" : chat_id})
    if not check:
        await chatsdb.insert_one({"chat_id" : chat_id})
    for m in message.new_chat_members:
        try:
            if m.id == BOT_ID:
                await message.reply_text(f"ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ɪɴ {message.chat.title}. ғʀᴏᴍ ɴᴏᴡ ɪ ᴡɪʟʟ ᴋᴇᴇᴘ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴄʟᴇᴀɴ.")
        except Exception as idk:
            LOG.print(f"[bold red]{idk}")

