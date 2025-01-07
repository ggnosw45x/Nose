from pyrogram import Client, filters
import asyncio
import os
import sys
from pyrogram.types import Message
from configs import Config                 

Bot = Client(
    "XD",
    api_hash=Config.API_HASH,
    api_id=Config.API_ID,
    bot_token=Config.BOT_TOKEN, 
    plugins=dict(root="plugins"),
    )

@Bot.on_callback_query()
async def callpri(app, callback_query):
    if callback_query.message.reply_to_message is not None and callback_query.message.reply_to_message.from_user.id != callback_query.from_user.id:
        await callback_query.answer("❗️ Error Markup ❗️")
        return
    else:
        await callback_query.continue_propagation()

 

@Client.on_message(filters.command(["reiniciar"], ["/", "."]))
async def re_start(_, m: Message):

  with open(file='plugins/rangos/owner.txt', mode='r+',
            encoding='utf-8') as archivo:
    x = archivo.readlines()
    if str(m.from_user.id) + '\n' in x:

      q = await m.reply_text("<b>Reiniciando</b>")
      await asyncio.sleep(1.9)
      qq = await q.edit("<b>SE ESTA REINICIADO SU BOT ESPERE 16 SEGUNDOS PARA QUE SE INICIE.</b>")
     
      os.execv(sys.executable, ['python'] + sys.argv)

    else:
      return await m.reply(f'<b>Este comando es para Owner</b>')


try:
	os.system('cls')    
	print('iniciado !')         
	Bot.run()
        
except Exception as e:
  print(e)