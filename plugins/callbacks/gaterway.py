from configss._def_main_ import *
from pulpos.plantillas import _cmdbotons

@Client.on_callback_query(filters.regex('gater'))
async def exit(client, msg):
    await msg.edit_message_text(gatertt,reply_markup=_cmdbotons)