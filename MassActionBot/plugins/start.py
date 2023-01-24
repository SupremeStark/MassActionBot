from MassActionBot import app,START_PIC
from pyrogram import filters , enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from MassActionBot.utils.data import *


START_TEXT = """
ʜᴇʏ {},
ɪ'ᴍ  {}. ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴄʟᴇᴀɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍʏ ᴀʙɪʟɪᴛɪᴇs.
"""

HELP_TEXT = """
ʜᴇʀᴇ ᴀʀᴇ ᴀʟʟ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs

 ⦾ /banall - ʙᴀɴs ᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ.

 ⦾ /unbanall - ᴜɴʙᴀɴs ᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ.

 ⦾ /kickall - ᴋɪᴄᴋs ᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ.

 ⦾ /muteall - ᴍᴜᴛᴇs ᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ.

 ⦾ /unmuteall - ᴜɴᴍᴜᴛᴇs ᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ.

 ⦾ /kickthefools - ᴋɪᴄᴋs ᴛʜᴇ ᴍᴇᴍʙᴇʀs ɪɴ ɢʀᴏᴜᴘs ᴡʜᴏ ᴡᴇʀᴇ ɪɴᴀᴄᴛɪᴠᴇ ғᴏʀ ᴀ ᴍᴏɴᴛʜ.


ᴄʀᴇᴅɪᴛ ɢᴏᴇs ᴛᴏ - @STEVE_R0GERS_101
"""
@app.on_message(filters.command("start"))
async def _start(_, message): 
    chat_id = message.chat.id
    BOT_MENTION = (await _.get_me()).mention  
    BOT_USERNAME = (await _.get_me()).username 
    USER_MENTION = message.from_user.mention 
    buttons = InlineKeyboardMarkup([[InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ➕",url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],[
        InlineKeyboardButton(text="⚡ ʜᴇʟᴘ ⚡", callback_data="help_btn")]])
    
    await message.reply_photo(
        photo = START_PIC,
        caption = START_TEXT.format(USER_MENTION,BOT_MENTION),reply_markup=buttons)
           
    
@app.on_callback_query(filters.regex("help_btn"))
async def help(_, query):
    await query.message.edit_caption(HELP_TEXT)
