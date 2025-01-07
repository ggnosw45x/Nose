import requests 
from pyrogram import Client, filters
from pyrogram.types import Message
from configss._def_main_ import *
from pulpos.plantillas import _cmdbotons, _cmd

@Client.on_message(filters.command(["bin"], ["/", "."]))
async def bin(client, message):
    with open(file='plugins/usuarios/users.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            input = re.findall(r'[0-9]+',message.text)
            BIN = message.text[len("/bin"): 11]

            if len(BIN) < 6:
                return await message.reply("<b> 𝙐𝙨𝙚 <code>/bin 456789</code></b>")
            if not BIN:
                return await message.reply("<b> 𝙐𝙨𝙚 <code>/bin 456789</code></b>")
            inputm = message.text.split(None, 1)[1]
            bincode = 6
            BIN = inputm[:bincode]
            req = requests.get(f"https://bins.antipublic.cc/bins/{BIN}").json()
            if 'bin' not in req:
                await message.reply_text(f'<b> 𝗕𝗶𝗻 ⇾ no encontrado <code>{BIN} ❌</code></b>')
                
            else:
                brand = req['brand']
                country = req['country']
                country_name = req['country_name']
                country_flag = req['country_flag']
                country_currencies = req['country_currencies']
                bank = req['bank']
                level = req['level']
                typea  = req['type']

                await message.reply_text(f"""
               <b>
𝖵𝖺𝗅𝗂𝖽 𝗕𝗶𝗻✅
━━━━━━━━━━━━━━━━━
⸙ 𝖡𝗂𝗇⇾  <code>{BIN}</code>
⸙ 𝗗𝗮𝘁𝗮 ⇾ {brand}-{typea}-{level}
⸙ 𝖡𝖺𝗇𝗄⇾  <code>{bank}</code>
⸙ 𝖢𝗈𝗎𝗇𝗍𝗋𝗒⇾ {country}|{country_flag}|{country_name}
҂ Checked By: @{message.from_user.username}
━━━━━━━━━━━━━━━━━
                </b>""")
    
