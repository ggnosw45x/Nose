from pyrogram import Client, filters
from pyrogram.types import Message
from pulpos.plantillas import _Call_Charged, _Call_Gateways_buttons

@Client.on_callback_query(filters.regex("char"))
async def tools(client, message):
    await message.edit_message_text(_Call_Charged, reply_markup= _Call_Gateways_buttons)