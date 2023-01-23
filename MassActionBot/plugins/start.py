from MassActionBot import app
from pyrogram import filters 

@app.on_message(filters.command("start"))
async def _start(_, message):
    BOT_ID = (await _.get_me()).id
    print(BOT_ID)
    await message.reply_text("am started")
