from configss._def_main_ import *

@Client.on_message(filters.command(["gen"], ["/", "."]))
async def gen(client, message):

            input = re.findall(r'[0-9]+',message.text)
            rank = get_user_rank(message.from_user.id)
            
            BIN = message.text[len("/bin"): 11]
            if len(BIN) <6:
                return await message.reply("<b> Usar <code>/gen 456789|rnd|rdn|rdn</code></b>")
            if not BIN:
                return await message.reply("<b> Usar <code>/gen 456789|rnd|rdn|rdn</code></b>")
            inputms = message.text.split(None, 1)[1]
            bincode = 6
            BINS = inputms[:bincode]
            req = requests.get(f"https://bins.antipublic.cc/bins/{BINS}").json()
            brand = req['brand']
            country = req['country']
            country_name = req['country_name']
            country_flag = req['country_flag']
            country_currencies = req['country_currencies']
            bank = req['bank']
            level = req['level']
            typea  = req['type']
        
            tiempoinicio = time.perf_counter()
            
            if len(input) == 1:
                cc = input[0]
                mes = 'x'
                ano = 'x'
                cvv = 'x'
            elif len(input) ==2:
                cc = input[0]
                mes = input[1]
                ano = 'x'
                cvv = 'x'
            elif len(input) ==3:
                cc = input[0]
                mes = input[1]
                ano = input[2]
                cvv = 'x'
            elif len(input) ==4:
                cc = input[0]
                mes = input[1]
                ano = input[2]
                cvv = input[3]
            else:
                cc = input[0]
                mes = input[1]
                ano = input[2]
                cvv = input[3]

            cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9,cc10, = cc_gen(cc,mes,ano,cvv)
            
            tiempofinal = time.perf_counter()
            text = f"""
<b>━━━● 𝗣𝗔𝗜𝗡 𝗖𝗛𝗞 𝗕𝗢𝗧 ●━

┏━━━━━━━━━━━━━━━━━━━━━━━━
┣𝘽𝙞𝙣 ➨ <code>{BINS}</code>
┣𝗜𝗡𝗙𝗢 ➨ {brand} - {typea} - {level}
┣𝘽𝙖𝙣𝙠 ➨ <code>{bank}</code>
┣𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➨ {country_name} [{country_flag}]
┗━━━━━━━━━━━━━━━━━━━━━━━

   ϟ 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧 𝘾𝙖𝙧𝙙𝙨 ϟ

┏━━━━━━━━━━━━━━━━━━━━━━━━━━
┣<code>{cc1}</code>
┣<code>{cc2}</code>
┣<code>{cc3}</code>
┣<code>{cc4}</code>
┣<code>{cc5}</code>
┣<code>{cc6}</code>
┣<code>{cc7}</code>
┣<code>{cc8}</code>
┣<code>{cc9}</code>
┣<code>{cc10}</code>
┗━━━━━━━━━━━━━━━━━━━━━━━━━

𝙈𝙤𝙣𝙩𝙤: 10
𝙏𝙞𝙢𝙚: <code>{tiempofinal - tiempoinicio:0.2} seconds</code>
𝘽𝙤𝙩 𝙗𝙮 ➨ @THE_ORGULLOT
𝘾𝙃𝙀𝘾𝙆𝙀𝘿 𝘽𝙔: <code>@{message.from_user.username}</code> [{rank}]</b>"""
            
            await client.send_message(message.chat.id, f'{text}',
                    reply_markup=InlineKeyboardMarkup(
                [
                    [
                
                        InlineKeyboardButton("REGEN", callback_data="regen")
                        
                    ]
                    
                ]

            )
            
        )
   