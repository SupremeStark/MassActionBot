from MassActionBot import app,BOT_ID
from pyrogram import filters
from MassActionBot.utils.chat_status import handle_status

@app.on_message(filters.command(["banall","unbanall"]))
@handle_status
async def _banUnban(_, message):
        
