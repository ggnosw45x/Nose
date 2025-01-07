from configss._def_main_ import *


@Client.on_message(filters.command(["gkey"], ["/", "."]))
async def start(client, message):
    with open(file='plugins/rangos/admins.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            data = message.text.split(" ", 2)
            if len(data) < 2:
                await message.reply_text("<b>[ϟ] USE THE COMMAND  <code>key dias</code></b>")
                return

            ccs  = data[1]
            card = ccs.split("-")
            dia   = card[0]
        

            key = 'pain''-'+str(randint(1000,9000))+'-'f'PREMIUM'
            print(key)
            archivo.write('{}\n\n'.format(key))

            text = f"""<b>
┏━━━━━━━━━━━━━━━━━━━━
┣ 𝙆𝙀𝙔 𝙂𝙀𝙉𝙀𝙍𝘼𝘿𝘼 𝘾𝙊𝙉 𝙀𝙓𝙄𝙏𝙊✅
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ 𝙆𝙀𝙔: <code>{key}</code>
┣ 𝗜𝗗 𝗱𝗲𝗹 𝗨𝘀𝘂𝗮𝗿𝗶𝗼: <code>{message.from_user.id}</code>
┣ 𝙋𝙇𝘼𝙉: Premium
┣ 𝘾𝘼𝙉𝙅𝙀𝘼𝘿𝘼 𝙋𝙊𝙍: {message.from_user.first_name} {message.from_user.last_name}
┣ 𝙐𝙎𝘼 /claim
┣ 𝙊𝙒𝙉𝙀𝙍 𝘽𝙊𝙏: @THE_ORGULLOT
┗━━━━━━━━━━━━━━━━━━━
</b>"""

            
            await client.send_message(message.chat.id, f'{text}')
            
            with open(file='plugins/usuarios/keys.txt',mode='r+',encoding='utf-8') as archivo:
                        x = archivo.readlines()
                        
                        archivo.write('{}\n\n'.format(key))
        else:
            return await message.reply(f'<b>[ϟ] 𝙀𝙨𝙩𝙚 𝙘𝙤𝙢𝙖𝙣𝙙𝙤 𝙚𝙨 𝙥𝙖𝙧𝙖 𝙖𝙙𝙢𝙞𝙣❌</b>')



