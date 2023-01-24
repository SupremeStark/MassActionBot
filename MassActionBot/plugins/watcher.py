from MassActionBot.utils.database import chatsdb

@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(_, message: Message):
    chat_id = message.chat.id
    check = await chatsdb.find_one({"chat_id" : chat_id})
    if not check:
        await chatsdb.insert_one({"chat_id" : chat_id})
    for member in message.new_chat_members:
        try:
            if member.id == botid:
                send =  await message.reply_text(
                    f"Thanks for having me in {message.chat.title}\n\n{botname} is alive."
                )
                await put_cleanmode(message.chat.id, send.message_id)
        except:
            return
