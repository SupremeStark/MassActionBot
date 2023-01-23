import asyncio
import time 
from MassActionBot import app,SUDOES,get_readable_time
from pyrogram import filters,enums
from MassActionBot.utils.chat_status import handle_status
from MassActionBot.plugins.cancel_process import SPAM_CHATS
from pyrogram.errors import FloodWait 
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM 
from pyrogram.types import ChatPermissions


@app.on_message(filters.command(["banall","unbanall","kickall","muteall","unmuteall","kickthefools"]))
@handle_status
async def _banUnban(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    start = time.time()
    buttons = IKM([[IKB("❌ ᴄᴀɴᴄᴇʟ", callback_data="cancel_btn")]])
    SPAM_CHATS.append(chat_id)
    if message.command[0] == "banall":
        await message.reply_text("sᴛᴀʀᴛᴇᴅ ʙᴀɴɴɪɴɢ ᴛʜᴇ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ ᴛᴀᴘ ᴏɴ ᴄᴀɴᴄᴇʟ ʙᴜᴛᴛᴏɴ ᴏʀ /cancel ᴛᴏ sᴛᴏᴘ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴘʀᴏᴄᴇss.", reply_markup=buttons)
        async for members in _.get_chat_members(chat_id):
            if chat_id not in SPAM_CHATS:
                break  
            try:          
                if members.user.id in SUDOES:
                    pass
                else:
                    await _.ban_chat_member(chat_id,members.user.id)
                    await _.send_message(chat_id,f"ʙᴀɴɴᴇᴅ {members.user.mention} ɪɴ `{message.chat.title}`.") 
            except FloodWait as i:
                await asyncio.sleep(i.value)
            except Exception as er:
                pass 
        end = get_readable_time((time.time() - start))      
        await message.reply(f"sᴜᴄᴄᴇssғᴜʟʟʏ ʙᴀɴɴᴇᴅ ᴀʟʟ ᴍᴇᴍʙᴇʀs. ɪɴ `{end}`")        

    if message.command[0] == "unbanall":
        await message.reply_text("sᴛᴀʀᴛᴇᴅ ᴜɴʙᴀɴɴɪɴɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ ᴛᴀᴘ ᴏɴ ᴄᴀɴᴄᴇʟ ʙᴜᴛᴛᴏɴ ᴏʀ /cancel ᴛᴏ sᴛᴏᴘ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴘʀᴏᴄᴇss", reply_markup=buttons)
        banned_users = []
        x = 0
        async for m in _.get_chat_members(chat_id,filter=enums.ChatMembersFilter.BANNED):
            banned_users.append(m.user.id)
            if chat_id not in SPAM_CHATS:
                break       
            try:               
                await _.unban_chat_member(chat_id,banned_users[x])
                await _.send_message(chat_id,f"ᴜɴʙᴀɴɪɴɢ ᴀʟʟ ᴍᴄ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ {m.user.mention}")
                x += 1                                                                
            except FloodWait as e:
                await asyncio.sleep(e.value)           
        end = get_readable_time((time.time() - start))      
        await message.reply_text(f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴜɴʙᴀɴɴᴇᴅ ᴀʟʟ ᴍᴇᴍʙᴇʀs. ɪɴ `{end}`")
    if message.command[0] == "kickall":
        await message.reply_text("sᴛᴀʀᴛᴇᴅ ᴋɪᴄᴋɪɴɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ ᴛᴀᴘ ᴏɴ ᴄᴀɴᴄᴇʟ ʙᴜᴛᴛᴏɴ ᴏʀ /cancel ᴛᴏ sᴛᴏᴘ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴘʀᴏᴄᴇss.",reply_markup=buttons)
        async for member in _.get_chat_members(chat_id):
           if chat_id not in SPAM_CHATS:
                break       
           try:
               if member.user.id in SUDOES:
                   pass
               else:
                   await _.ban_chat_member(chat_id, member.user.id)
                   await _.send_message(chat_id,f"ᴋɪᴄᴋᴇᴅ {member.user.mention} ɪɴ {message.chat.title}.")
                   await _.unban_chat_member(chat_id,member.user.id)  
           except FloodWait as e:
               await asyncio.sleep(e.value)                                             
           except Exception:
               pass
        end = get_readable_time((time.time() - start))  
        await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴋɪᴄᴋᴇᴅ ᴀʟʟ ᴍᴇᴍʙᴇʀs.ɪɴ `{end}`")
    
    if message.command[0] == "kickthefools":
        text = await message.reply("ᴋɪᴄᴋɪɴɢ ᴍᴇᴍʙᴇʀs ᴡʜᴏ ᴡᴇʀᴇ ɪɴᴀᴄᴛɪᴠᴇ ғᴏʀ ᴀ ᴍᴏɴᴛʜ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ")      
        x = 0
        fools = []        
        async for member in _.get_chat_members(chat_id) :          
            user = member.user        
            if user.status == enums.UserStatus.LAST_MONTH:
                if user.id in SUDOES :
                    pass
                else:                            
                    fools.append(member.user.id)  
        if not fools:
           await text.edit("ᴛʜᴇʀᴇ ᴀʀᴇɴ'ᴛ ᴀɴʏ ғᴏᴏʟs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ")
        else:
            for i in fools:
                if chat_id not in SPAM_CHATS:
                    break 
                try:                         
                    await _.ban_chat_member(chat_id,fools[x])           
                    await _.unban_chat_member(chat_id,fools[x])  
                    x += 1                
                except IndexError:
                    pass
                except FloodWait as e:
                    asyncio.sleep(e.value)
            end = get_readable_time((time.time() - start))  
            await text.delete()
            await message.reply_text(f"ᴋɪᴄᴋᴇᴅ {len(fools)} ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ ᴡʜᴏ ᴡᴇʀᴇ ɪɴᴀᴄᴛɪᴠᴇ ғᴏʀ ᴀ ᴍᴏɴᴛʜ.\n⏰ ᴛɪᴍᴇ ᴛᴏᴏᴋ : {end}")
    if message.command[0] == "muteall":
        await _.set_chat_permissions(chat_id, ChatPermissions())
        await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴜᴛᴇᴅ ᴀʟʟ ᴍᴇᴍʙᴇʀs.")
    if message.command[0] == "unmuteall":
        await _.set_chat_permissions(
        chat_id,
            ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True))
        await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴜɴᴍᴜᴛᴇᴅ ᴀʟʟ ᴍᴇᴍʙᴇʀs.")

   
 

