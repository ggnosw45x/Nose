from pyrogram import Client, filters
from pulpos.plantillas import _Call_Regis
from configss._def_main_ import *

@Client.on_callback_query(filters.regex("register"))
async def tools(client, message):
    await message.edit_message_text(_Call_Regis, reply_markup= homedb)