from MassActionBot import app,SUDOES
from pyrogram import filters , enums , Client
from MassActionBot.utils.chat_status import handle_status
from pyrogram.types import CallbackQuery

SPAM_CHATS = []


@app.on_message(filters.command("cancel"))
@handle_status
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try :
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass   
        return await message.reply_text("sᴛᴏᴘᴘᴇᴅ ᴛʜᴇ ᴘʀᴏᴄᴇss.")     
                                     
    else :
        await message.reply_text("**ᴛʜᴇʀᴇ ɪs ɴᴏ ᴘʀᴏᴄᴇss ɢᴏɪɴɢ ᴏɴ ʙᴀʙʏ.**")  
        return       


@app.on_callback_query(filters.regex("cancel_btn"))
async def _cancel(app : Client, query : CallbackQuery):
    chat_id = query.message.chat.id
    user_id = query.from_user.id 
    administrators = []
    async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)     
    administrators.extend(SUDOES)
    if user_id in administrators:
        if chat_id in SPAM_CHATS:
            try :
                SPAM_CHATS.remove(chat_id)
            except Exception:
                pass   
            await app.answer_callback_query(query.id,text="sᴛᴏᴘᴘᴇᴅ ᴛʜᴇ ᴘʀᴏᴄᴇss.",show_alert=True)     
                                     
        else :
            await app.answer_callback_query(query.id,text="ᴛʜᴇʀᴇ ɪs ɴᴏ ᴘʀᴏᴄᴇss ɢᴏɪɴɢ ᴏɴ ʙᴀʙʏ.",show_alert=True)
    else:
        await app.answer_callback_query(query.id, text="ʙᴇ ɪɴ ʏᴏᴜʀ ʟɪᴍɪᴛs ᴍғ.", show_alert=True)     
               

    
