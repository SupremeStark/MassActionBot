from pyrogram import Client , enums
from functools import wraps
from pyrogram.types import Message
from MassActionBot import BOT_ID,SUDOES


async def get_admins(app : Client,chat_id : int):
    admins = []
    async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        admins.append(m.user.id)
    return admins


async def handle_status(func):
    @wraps(func)
    async def wrapper(app : Client, message: Message):
        if message.chat.type == enums.ChatType.PRIVATE:
            await message.reply_text("ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ɢʀᴏᴜᴘs/ᴄʜᴀɴɴᴇʟs ɴᴏᴛ ɪɴ ᴘʀɪᴠᴀᴛᴇ.ʙᴀᴋᴀᴀ.....")
        chat_id = message.chat.id
        user_id = message.from_user.id
        supreme_users = await get_admins(app,chat_id)
        BOT = await app.get_chat_member(chat_id,BOT_ID)
        user = await app.get_chat_member(chat_id,user_id)       
        if BOT_ID not in supreme_users:
            return await message.reply_text("ᴡᴛғ ʙʀᴜʜ ɪ'ᴍ ɴᴏᴛ ᴇᴠᴇɴ ᴀᴅᴍɪɴ ʜᴏᴡ ᴄᴀɴ ɪ ᴘᴇʀғᴏʀᴍ ᴛʜᴇsᴇ ᴀᴄᴛɪᴏɴs 😒.")
        if user_id not in (supreme_users or SUDOES):
            return await message.reply_text("ғᴜᴄᴋ ʏᴏᴜ 🖕.")
        if not BOT.privileges.can_restrict_members:
            return await message.reply_text("**ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛs ʏᴏᴜ ғᴏᴏʟ. ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ʀᴇsᴛʀɪᴄᴛɪᴏɴ ʀɪɢʜᴛ.**")
        if (user_id in supreme_users and not user.privileges.can_restrict_members) and user_id not in SUDOES :
            return await message.reply_text("`ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ɪᴛ. ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛs.`")
    
        return func(app, message)
    return wrapper       
             
         
       
     
