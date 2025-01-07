from configss._def_main_ import *

Premium = 'plugins/rangos/premium.txt'
Keys = 'plugins/usuarios/keys.txt'
admin = 'plugins/rangos/admins.txt'
@Client.on_message(filters.command(["claim"], ["/", "."]))
async def claim_key(client, message):
    # Obtener la clave del mensaje
    key = message.text[len('/claim '):]

    # Verificar si la clave existe en el archivo llave.txt
    with open(Keys, 'r') as f:
        keys = f.read().splitlines()
    if key not in keys:
        await message.reply("<b>Esa key ya fue teclamada por otro usuario \n utiliza  <code>/claim pain-7657-xxxx</code> para reclamar otra</b>")
        return

    # Verificar si el usuario ya ha reclamado la clave
    with open(Premium, 'r+') as f:
        users = f.read().splitlines()
        if str(message.from_user.id) in users:
            await message.reply("Ya has reclamado una key antes.")
            return
        # Verificar si la clave ya ha sido reclamada por otro usuario
        for line in f:
            if key in line:
                await message.reply("Key ya reclamada por otro usuario")
                return

        # Eliminar la clave del archivo llave.txt
        keys.remove(key)
        f.seek(0)
        f.truncate()
        f.write('\n'.join(users + [str(message.from_user.id)]))

    with open(Keys, 'w') as f:
        f.write('\n'.join(keys))
                
    # Generar una respuesta aleatoria
    responses = [
f"""<b>● 𝙆𝙀𝙔 𝘾𝘼𝙉𝙅𝙀𝘼𝘿𝘼 𝘾𝙊𝙉 𝙀𝙓𝙄𝙏𝙊✅
┏━━━━━━━━━━━━━━━━━━━━━━━━
┣ 𝙐𝙨𝙚𝙧 : {message.from_user.username}
┣ 𝙐𝙨𝙚𝙧𝙄𝘿 : 「<code>{message.from_user.id}</code>」
┣ 𝙋𝙡𝙖𝙣 : Premium 
┣ Type : All Gates
┣━━━━━━━━━━━━━━━━━━━━━━━━
┣𝙊𝙬𝙣𝙚𝙧 : @THE_ORGULLOT Y @Swnfloxs
┗━━━━━━━━━━━━━━━━━━━━━━━━</b>"""]
                
    response = random.choice(responses)
    
    print(f"User @{message.from_user.username} claimed key {key}")
    # Enviar la respuesta al usuario
    await message.reply(response)

    # Enviar el mensaje al canal
    canal_id = "-1001819851423"  # Reemplazar con el ID del canal
    canal = await client.get_chat(canal_id)
    canal_message = f"""┏━━━━━━━━━━━━━━━━━━━━━━
⍟  𝙆𝙀𝙔 𝘾𝘼𝙉𝙅𝙀𝘼𝘿𝘼 𝘾𝙊𝙉 𝙀𝙓𝙄𝙏𝙊✅  ⍟
┗━━━━━━━━━━━━━━━━━━━━━━━━━

┏━━━━━━━━━━━━━━━━━━━━━━━━━
┣
┣ 𝗞𝗲𝘆 𝗿𝗲𝗰𝗹𝗮𝗺𝗮𝗱𝗮: <code>{key}</code>
┣
┣ 𝗨𝘀𝘂𝗮𝗿𝗶𝗼 𝗿𝗲𝗰𝗹𝗮𝗺𝗮𝗱𝗼𝗿: @{message.from_user.username}
┣
┣ 𝗜𝗗 𝗱𝗲𝗹 𝗨𝘀𝘂𝗮𝗿𝗶𝗼: <code>{message.from_user.id}</code>
┣
┣ 𝗨𝘀𝘂𝗮𝗿𝗶𝗼: {message.from_user.first_name} {message.from_user.last_name}
┣
┗━━━━━━━━━━━━━━━━━━━━━━━━"""
    await client.send_message(canal.id, canal_message)