from configss._def_main_ import *


@Client.on_message(filters.command(["repre"], ["/", "."]))
async def register(_, m: Message):
    with open(file='plugins/rangos/admins.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(m.from_user.id) + '\n' in x:
            data = m.text.split(" ", 2)
            if len(data) < 2:
                await m.reply_text("<b>⎚ Usar <code>/key dias-id-credit</code></b>")
                return
            
            ccs  = data[1]
            card = ccs.split("-")
            hola   = card[0]

            with open('plugins/usuarios/premium.txt', 'r') as f:
                lineas = f.readlines()

            dato_a_eliminar = f'{hola}'
            lineas = [linea for linea in lineas if dato_a_eliminar not in linea]

            with open('plugins/usuarios/premium.txt', 'w') as f:
                f.writelines(lineas)

                await m.reply(f'<b>𝙇𝙄𝙎𝙏𝙊 𝙀𝙇 𝙐𝙎𝙐𝘼𝙍𝙄𝙊 <code>{hola}</code> 𝘼 𝘿𝙀𝙅𝘼𝘿𝙊 𝘿𝙀 𝙎𝙀𝙍 𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝙀𝙓𝙄𝙏𝙊𝙎𝘼𝙈𝙀𝙉𝙏𝙀✅</b>')
        else:
            return await m.reply(f'<b>⎚𝙀𝙨𝙩𝙚 𝙘𝙤𝙢𝙖𝙣𝙙𝙤 𝙚𝙨 𝙥𝙖𝙧𝙖 𝙖𝙙𝙢𝙞𝙣❌</b>')


