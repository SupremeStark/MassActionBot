from MassActionBot import app,START_PIC
from pyrogram import filters , enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from MassActionBot.utils.data import *


START_TEXT = """
ʜᴇʏ {},
ɪ'ᴍ  {}. ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴄʟᴇᴀɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍʏ ᴀʙɪʟɪᴛɪᴇs.
"""
@app.on_message(filters.command("start"))
async def _start(_, message): 
    chat_id = message.chat.id
    BOT_MENTION = (await _.get_me()).mention  
    BOT_USERNAME = (await _.get_me()).username 
    USER_MENTION = message.from_user.mention 
    buttons = InlineKeyboardMarkup([[InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕",url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],[
        InlineKeyboardButton(text="⚡ ʜᴇʟᴘ ⚡", callback_data="help_back")]])
    
    await message.reply_photo(
        photo = START_PIC,
        caption = START_TEXT.format(USER_MENTION,BOT_MENTION),reply_markup=buttons)
           
    
