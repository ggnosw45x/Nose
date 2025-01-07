from configss._def_main_ import *

@Client.on_message(filters.command(["id"], ["/", "."]))
async def id(client,msg):
    await msg.reply(f"""    
<b> Chat id:</b> <b><code>{msg.chat.id}</code></b>
<b> User Id:</b> <b><code>{msg.from_user.id}</code></b>
    """)