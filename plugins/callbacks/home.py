from pyrogram import Client, filters
from pyrogram.types import Message
from pulpos.plantillas import mainstart, _cmd

@Client.on_callback_query(filters.regex("home"))
async def home(client, message):
    await message.edit_message_text(
        _cmd,
        reply_markup=mainstart
    )

