from pyrogram import Client, filters
from pyrogram.types import Message
from pulpos.plantillas import _Call_Auth, _Call_Gateways_buttons

@Client.on_callback_query(filters.regex("auth"))
async def tools(client, message):
    await message.edit_message_text(_Call_Auth, reply_markup= _Call_Gateways_buttons)