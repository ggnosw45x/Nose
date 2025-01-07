import json
import requests
from luhn import *
import time
import asyncio
import re
from configss._def_main_ import *
from colored import fg, bg, attr
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
) 

Premium = 'plugins/rangos/premium.txt'
Keys = 'plugins/usuarios/keys.txt'
admin = 'plugins/rangos/admins.txt'

@Client.on_message(filters.command(["dkey"], ["/", "."]))
async def dkeys(client, message):
    with open(file=admin,mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            data = message.text.split(" ", 2)
            if len(data) < 2:
                await message.reply("<b>⎚ Usar <code>/dkey key</code></b>")
                return
            ccs  = data[1]
            card = ccs.split("-")
            hola   = card[0]
            with open(Keys, 'r') as f:
                lineas = f.readlines()
            dato_a_eliminar = f'{hola}'
            lineas = [linea for linea in lineas if dato_a_eliminar not in linea]
            with open(Keys, 'w') as f:
                f.writelines(lineas)
                await message.reply(f'<b>𝙇𝘼 𝙆𝙀𝙔 <code>{hola}</code> 𝘼 𝙎𝙄𝘿𝙊 𝙀𝙇𝙄𝙈𝙄𝙉𝘼𝘿𝘼 𝙀𝙓𝙄𝙏𝙊𝙎𝘼𝙈𝙀𝙉𝙏𝙀✅</b>')
        else:
            return await message.reply(f'<b>⎚𝙀𝙨𝙩𝙚 𝙘𝙤𝙢𝙖𝙣𝙙𝙤 𝙚𝙨 𝙥𝙖𝙧𝙖 𝙖𝙙𝙢𝙞𝙣❌</b>')