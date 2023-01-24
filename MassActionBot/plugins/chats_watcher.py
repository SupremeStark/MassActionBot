from MassActionBot import app
from pyrogram import filters 
from MassActionBot.utils.database import add_served_chat


@app.on_message(filters.new_chat_members,group=2)
async def addinDb(_, message):
    BOT_ID = (await _.get_me()).id
    chat_id = message.chat.id
    h = await add_served_chat(chat_id)
    print(h)
    for m in message.new_chat_members:
        try:
            if m.id == BOT_ID:
                await message.reply_text("ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ɪɴ {}. ғʀᴏᴍ ɴᴏᴡ ɪ ᴡɪʟʟ ᴋᴇᴇᴘ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴄʟᴇᴀɴ.")
        except Exception as idk:
            LOG.print(f"[bold red]{idk}")
