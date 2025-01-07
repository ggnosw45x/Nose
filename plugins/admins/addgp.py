from configss._def_main_ import *


Premium = 'plugins/rangos/premium.txt'
Keys = 'plugins/usuarios/keys.txt'
admin = 'plugins/rangos/admins.txt'

@Client.on_message(filters.command(["gp"], ["/", "."]))
async def addpre(client, message):
    rank = get_user_rank(message.from_user.id)
    with open(file=admin,mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            data = message.text.split(" ", 2)
            if len(data) < 2:
                await message.reply("<b>❀ Usar <code>/addgp chat ID</code></b>")
                return
            ccs  = data[1]
            card = ccs.split("-")
            hola   = card[1]
            
            with open(file='datos.py', mode='r+', encoding='utf-8') as archivo:
                x = archivo.readlines()
                archivo.seek(0)  # Mover el puntero al inicio del archivo
                archivo.write(x[-1].rstrip()[:-1])  # Eliminar el último carácter ("]") de la última línea
                archivo.write(', -{}'.format(hola))  # Agregar el nuevo chat ID en la misma línea
                archivo.write(']')  # Agregar el "]" al final
                archivo.flush()  # Forzar la escritura en el archivo
                await message.reply(f'''<b>
¡✅ 𝙄𝙉𝙏𝙀𝙉𝙏𝙊 𝙑𝘼𝙇𝙄𝘿𝙊 ✅!
┏━━━━━━━━━━━━━━━━━━━━━━━
┣𝙎𝙀 𝘼 𝘼𝙂𝙍𝙀𝙂𝘼𝘿𝙊 𝘼𝙇𝘼 𝙇𝙄𝙎𝙏𝘼 𝘿𝙀 𝙋𝙍𝙀𝙈𝙄𝙐𝙈 ┣𝙀𝙎𝙏𝙀 𝘾𝙃𝘼𝙏💎
┣
┣ 𝙄𝘿 𝘿𝙀𝙇 𝘾𝙃𝘼𝙏: <code>-{hola}</code>
┣𝙋𝙇𝘼𝙉 𝘿𝙀𝙇 𝘾𝙃𝘼𝙏: PREMIUM
┣ 𝘾𝙃𝘼𝙏 𝘼𝙂𝙍𝙀𝙂𝘼𝘿𝙊 𝙋𝙊𝙍: <code>@{message.from_user.username}</code>
┣ 𝙍𝘼𝙉𝙂𝙊 𝘿𝙀𝙇 𝘾𝙃𝘼𝙏: [{rank}]
┗━━━━━━━━━━━━━━━━━━━━━━━</b>''')
        else:
            return await message.reply(f'<b>❀ 𝙀𝙨𝙩𝙚 𝙘𝙤𝙢𝙖𝙣𝙙𝙤 𝙚𝙨 𝙥𝙖𝙧𝙖 𝙖𝙙𝙢𝙞𝙣</b>')