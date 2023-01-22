from MassActionBot import app,BOT_ID
from pyrogram import filters 

@app.on_message(filters.command("start"))
async def _start(_, message):
    print(BOT_ID)
    await message.reply_text("am started")
