from MassActionBot import app,BOT_ID
from pyrogram import filters
from MassActionBot.utils.chat_status import handle_status

@app.on_message(filters.command("muteall"))
@handle_status
async def ntg(_, message):
    print(BOT_ID)
    await message.reply_text("yes done")
