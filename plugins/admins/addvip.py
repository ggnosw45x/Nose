from configss._def_main_ import *


@Client.on_message(filters.command(["addvip"], ["/", "."]))
async def addpre(client, m: Message):
    with open(file='plugins/rangos/admins.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(m.from_user.id) + '\n' in x:
            data = m.text.split(" ", 2)
            if len(data) < 2:
                await m.reply_text("<b>[☃]Please use the command  <code>/addpre id-dias-</code></b>")
                return
            
            ccs  = data[1]
            card = ccs.split("-")
            hola   = card[0]
            dia = card[1]

            with open(file='plugins/rangos/vip.txt',mode='r+',encoding='utf-8') as archivo:
                x = archivo.readlines()
                archivo.write('{}\n'.format(hola))

            print(f"User @{m.from_user.username} added Premium {hola} and dias {dia} added user premium") # added line
            
            #canal_id = '-1001819851423'  # Replace with your channel ID
            #canal = await client.get_chat(canal_id)
            #canal_m = f'User @{m.from_user.username} added premium {hola} and dia {dia} added user premium'
            #await client.send_m(canal.id, canal_m)
            await m.reply(f'<b>𝙀𝙡 𝙪𝙨𝙪𝙖𝙧𝙞𝙤 <code>{hola}</code> 𝙖𝙝𝙤𝙧𝙖 𝙚𝙨 𝙑𝙞𝙥 𝘿𝙞𝙖𝙨: {dia}</b>')
        else:
            return await m.reply(f'<b>[☃] 𝙀𝙨𝙩𝙚 𝙘𝙤𝙢𝙖𝙣𝙙𝙤 𝙚𝙨 𝙥𝙖𝙧𝙖 𝙖𝙙𝙢𝙞𝙣</b>')
