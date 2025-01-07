from configss._def_main_ import *

Owner = 'plugins/rangos/owner.txt'
Premium = 'plugins/rangos/premium.txt'
Keys = 'plugins/usuarios/keys.txt'
admin = 'plugins/rangos/admins.txt'

@Client.on_message(filters.command(["addadmin"], ["/", "."]))
async def addadmin(client, message):
    with open(file=Owner, mode='r+', encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            data = message.text.split(" ", 2)
            if len(data) < 2:
                await message.reply("<b>⎚ Usar <code>/addadmin ID</code></b>")
                return
            ccs = data[1]
            card = ccs.split("-")
            hola = card[0]
            
            with open(file=admin, mode='r+', encoding='utf-8') as archivo:
                x = archivo.readlines()
                archivo.write('{}\n'.format(hola))
            print(f"User @{message.from_user.username} added admin {hola}") # added line
            
            canal_id = "-1001819851423"  # Replace with your channel ID
            canal = await client.get_chat(canal_id)
            canal_message = f"User @{message.from_user.username} added admin {hola}"
            await client.send_message(canal.id, canal_message)
            await message.reply(f'<b>𝙀𝙡 𝙪𝙨𝙪𝙖𝙧𝙞𝙤 <code>{hola}</code> 𝙖𝙝𝙤𝙧𝙖 𝙚𝙨 𝙖𝙙𝙢𝙞𝙣</b>')
        else:
            return await message.reply(f'<b>𝙀𝙨𝙩𝙚 𝙘𝙤𝙢𝙖𝙣𝙙𝙤 𝙚𝙨 𝙥𝙖𝙧𝙖 𝙚𝙡 𝙙𝙪𝙚ñ𝙤 💥</b>')
