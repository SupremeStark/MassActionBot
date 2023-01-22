from MassActionBot import app
from pyrogram import filters
from MassActionBot.utils.chat_status import handle_status

@app.on_message(filters.command("muteall"))
@handle_status
async def ntg(_, message):
    await message.reply_text("yes done")
