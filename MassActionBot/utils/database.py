from MassActionBot import db
from typing import Final

chatsdb = db.chats


async def is_served_chat(chat_id : int) -> bool:
    check = chatsdb.find_one({"chat_id" : chat_id})
    if check:
        return True
    return False


async def add_served_chat(chat_id : Final[int]) :
    check_served = await is_served_chat(chat_id)
    if check_served:
        return
    return await chatsdb.insert_one({"chat_id" : chat_id})

async def rm_served_chat(chat_id : Final[int]):
    check_served = await is_served_chat(chat_id)
    if not check_served:
        return
    return await chatsdb.delete_one({"chat_id" : chat_id})


async def get_chats() -> list:
    chats = chatsdb.find({"chat_id" : {"$lt" : 0}})
    if not chats:
        return []
    chats_list = []
    for chat in await chats.to_list(length=1000000000):
        chats_list.append(chat)
    return chats_list    
