from pyrogram import Client , enums
from functools import wraps
from pyrogram.types import Message
from MassActionBot import BOT_ID,SUDOES



def handle_status(mystic):
    @wraps(mystic)
    async def wrapper(app : Client, message: Message):
        if message.chat.type == enums.ChatType.PRIVATE:
            await message.reply_text("ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ɢʀᴏᴜᴘs/ᴄʜᴀɴɴᴇʟs ɴᴏᴛ ɪɴ ᴘʀɪᴠᴀᴛᴇ.ʙᴀᴋᴀᴀ.....")
        chat_id = message.chat.id
        user_id = message.from_user.id
        BOT_ID = (await app.get_me()).id
        supreme_users = []
        async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            supreme_users.append(m.user.id)
        BOT = await app.get_chat_member(chat_id,BOT_ID)
        user = await app.get_chat_member(chat_id,user_id)       
        if BOT_ID not in supreme_users:
            return await message.reply_text("ᴡᴛғ ʙʀᴜʜ ɪ'ᴍ ɴᴏᴛ ᴇᴠᴇɴ ᴀᴅᴍɪɴ ʜᴏᴡ ᴄᴀɴ ɪ ᴘᴇʀғᴏʀᴍ ᴛʜᴇsᴇ ᴀᴄᴛɪᴏɴs 😒.")
        print(supreme_users)
        if (user_id not in supreme_users) and (user_id not in SUDOES):
            return await message.reply_text("ғᴜᴄᴋ ʏᴏᴜ 🖕.")
        if not BOT.privileges.can_restrict_members:
            return await message.reply_text("**ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛs ʏᴏᴜ ғᴏᴏʟ. ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ʀᴇsᴛʀɪᴄᴛɪᴏɴ ʀɪɢʜᴛ.**")
        if (user_id in supreme_users and not user.privileges.can_restrict_members) and user_id not in SUDOES :
            return await message.reply_text("`ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ɪᴛ. ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛs.`")
    
        return await mystic(app, message)

    return wrapper       
             
         
       
     
