from MassActionBot import app,SUDOES
from pyrogram import filters
from MassActionBot.utils.chat_status import handle_status
from MassActionBot.plugins.cancel_process import SPAM_CHATS

@app.on_message(filters.command(["banall","unbanall"]))
@handle_status
async def _banUnban(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    SPAM_CHATS.append(chat_id)
    if message.command[0] == "banall":
        async for members in _.get_chat_members(chat_id):
            if chat_id not in SPAM_CHATS:
                break
            try:
               if user_id in SUDOES:
                   continue 
                
