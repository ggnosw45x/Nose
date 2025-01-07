from pyrogram import Client, filters

id = ...

@Client.on_message(filters.command(["referencia", "refe"],prefixes=['.','!','/',',','-','$','%','#','']))
async def referencia_command(client, message):
    if message.reply_to_message and message.reply_to_message.photo:
        # Obtener la foto o imagen enviada como respuesta
        photo = message.reply_to_message.photo.file_id
        mensaje = " ".join(message.command[1:])
        # Enviar la foto o imagen al grupo del personal con los appones de aprobación y denegación
        await client.send_photo(
            chat_id=id,
            photo=photo,
            caption=f"""<b>𝗥𝗲𝗳𝗲
━━━━━━━━━━━━
ꔷ ID ➜ [<a href="https://t.me/{message.from_user.username}">{message.from_user.id}</a>]
━━━━━━━━━━━━
ꔷ Message ➜ {mensaje}
━━━━━━━━━━━━</b>"""
        )

        await message.reply_text("Muchas gracias por tu referencia ")
     
    else:
        await message.reply_text("para poder mandar esta referencia debe de hacer: /refe + el mensaje y luego responder a la foto")
        