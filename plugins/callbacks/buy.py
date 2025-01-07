from configss._def_main_ import *
from pulpos.plantillas import buycmd

@Client.on_callback_query(filters.regex('buy'))
async def exit(client, msg):
    await msg.edit_message_text(buy,reply_markup=buycmd)