from pyrogram import Client, filters
from pyrogram.types import Message
from pulpos.plantillas import _Call_mass, _Call_Gateways_buttons

@Client.on_callback_query(filters.regex("mass"))
async def mass(client, message):
    await message.edit_message_text(_Call_mass, reply_markup= _Call_Gateways_buttons)