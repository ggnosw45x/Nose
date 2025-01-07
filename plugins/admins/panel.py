from configss._def_main_ import *




Premium = 'plugins/usuarios/premium.txt'
Keys = 'plugins/usuarios/keys.txt'
admin = 'plugins/rangos/admins.txt'

with open(admin) as f:
    admins = [line.strip() for line in f]
        
@Client.on_message(filters.command(["panel"], ["/", "."]))
async def panels(client, message):
    user_id = message.from_user.id
    
    if str(user_id) not in admins:
        await message.reply("𝙎𝙤𝙡𝙤 𝙡𝙤𝙨 𝙖𝙙𝙢𝙞𝙣𝙞𝙨𝙩𝙧𝙖𝙙𝙤𝙧𝙚𝙨 𝙥𝙪𝙚𝙙𝙚𝙣 𝙪𝙨𝙖𝙧 𝙚𝙨𝙩𝙚 𝙘𝙤𝙢𝙖𝙣𝙙𝙤.")
        return
        
    # Envía un mensaje "verificando si eres administrador/a ..."
    msg = await message.reply("Verificando si eres administrador/a ...")

    await time.sleep(3)

    # Edita el mensaje para incluir el panel del admin
    await msg.edit_text("""<b>
[⨉ ] 𝗣𝗔𝗡𝗘𝗟 𝗗𝗘 𝗔𝗗𝗠𝗜𝗡𝗜𝗦𝗧𝗥𝗔𝗗𝗢𝗥𝗘𝗦

－－－－－－－－－－
[⨉ ] Para generar una key premium /key dias-id

↯ Ejemplo:  /gkey 1-1234567890

[⨉ ] Para eliminar una key /dkey (key)

↯ Ejemplo:  /dkey (key)
－－－－－－－－－－
[⨉ ] Para añadir un usuario premium /addpre (id)

↯ Ejemplo: /addprem (id)

[⨉ ] Eliminar usuario premium

↯ Ejemplo: /reprem 12345678
－－－－－－－－－－
[⨉ ] mira la lista de usuarios premium /prelist
－－－－－－－－－－
[⨉ ] autoriza un grupon /gp

↯pronto
－－－－－－－－－－
[⨉ ] 
</b>""")