import asyncio
from MassActionBot.utils.database import chatsdb,get_chats
from pyrogram import filters
from MassActionBot import app ,LOG, OWNER_ID
from pyrogram.errors import FloodWait 

@app.on_message(filters.new_chat_members, group=2)
async def addinDb(_, message):
    chat_id = message.chat.id
    BOT_ID = (await _.get_me()).id
    check = await chatsdb.find_one({"chat_id" : chat_id})
    if not check:
        await chatsdb.insert_one({"chat_id" : chat_id})
    for m in message.new_chat_members:
        try:
            if m.id == BOT_ID:
                await message.reply_text(f"ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ɪɴ {message.chat.title}.ғʀᴏᴍ ɴᴏᴡ ɪ ᴡɪʟʟ ᴋᴇᴇᴘ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴄʟᴇᴀɴ.")                                                   
        except Exception as er:
            LOG.print(f"[bold red]{er}")  


   
@app.on_message(filters.command("bcast"))
async def broadcast_(_, message):
    if message.reply_to_message:
        x = message.reply_to_message.id
        y = message.chat.id
        sent = 0
        chats = []
        schats = await get_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await app.forward_messages(i, y, x)                
                sent += 1
            except FloodWait as e:
                await asyncio.sleep(e.value)
            except Exception:
                pass
        await message.reply_text(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ ɪɴ {sent} ᴄʜᴀᴛs.**")
        return
    elif len(message.command) < 2:
        await message.reply_text(
            "**ᴇxᴀᴍᴩʟᴇ :**\n/broadcast [ᴍᴇssᴀɢᴇ] ᴏʀ [ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ]"
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    chats = []
    schats = await get_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await app.send_message(i, text=text)           
            sent += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception:
            pass
    await message.reply_text(f"**» sᴜᴄᴄᴇssғᴜʟʟʏ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ ɪɴ {sent} ᴄʜᴀᴛs.**")
