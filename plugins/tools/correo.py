from configss._def_main_ import *


@Client.on_message(filters.command(['mensajes'], prefixes=["/", ".", "!"], case_sensitive=False) & filters.text)
async def correo(Client,message):

    cookies = {
        '_ga': 'GA1.2.903061299.1681780740',
        '_gid': 'GA1.2.1925814643.1681780740',
        '__gads': 'ID=0266329222e0ada1-22d074371adf00d9:T=1681780750:RT=1681780750:S=ALNI_MYaSm1jYlm5wj3ro6YFoLZMJQswBA',
        '__gpi': 'UID=000009f11fa344c2:T=1681780750:RT=1681780750:S=ALNI_MYywItei-BN1sjhi7Lm8-ffKl5dXQ',
        '_gat': '1',
    }

    headers = {
        'authority': 'api.internal.temp-mail.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
        'application-name': 'web',
        'application-version': '2.2.29',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': '_ga=GA1.2.903061299.1681780740; _gid=GA1.2.1925814643.1681780740; __gads=ID=0266329222e0ada1-22d074371adf00d9:T=1681780750:RT=1681780750:S=ALNI_MYaSm1jYlm5wj3ro6YFoLZMJQswBA; __gpi=UID=000009f11fa344c2:T=1681780750:RT=1681780750:S=ALNI_MYywItei-BN1sjhi7Lm8-ffKl5dXQ; _gat=1',
        'origin': 'https://temp-mail.io',
        'referer': 'https://temp-mail.io/',
        'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48',
    }

    json_data = {
        'min_name_length': 10,
        'max_name_length': 10,
    }

    response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new', cookies=cookies, headers=headers, json=json_data).json()

    mail = response['email']

    try:
        inputm = message.text.split(None, 1)[1]
        lines = inputm.splitlines()
        mail = lines[0][:24]  # select the first line and take the first 24 characters
    except (IndexError, TypeError):
        return await message.reply_text(f"<b>Debes Introducir Un Correo Ejemplo:</b> <code>/mensajes {mail}</code>")
    
    

    cookies = {
        '_ga': 'GA1.2.903061299.1681780740',
        '_gid': 'GA1.2.1925814643.1681780740',
        '__gads': 'ID=0266329222e0ada1-22d074371adf00d9:T=1681780750:RT=1681780750:S=ALNI_MYaSm1jYlm5wj3ro6YFoLZMJQswBA',
        '__gpi': 'UID=000009f11fa344c2:T=1681780750:RT=1681780750:S=ALNI_MYywItei-BN1sjhi7Lm8-ffKl5dXQ',
        '_gat': '1',
    }

    headers = {
        'authority': 'api.internal.temp-mail.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
        'application-name': 'web',
        'application-version': '2.2.29',
        # 'cookie': '_ga=GA1.2.903061299.1681780740; _gid=GA1.2.1925814643.1681780740; __gads=ID=0266329222e0ada1-22d074371adf00d9:T=1681780750:RT=1681780750:S=ALNI_MYaSm1jYlm5wj3ro6YFoLZMJQswBA; __gpi=UID=000009f11fa344c2:T=1681780750:RT=1681780750:S=ALNI_MYywItei-BN1sjhi7Lm8-ffKl5dXQ; _gat=1',
        'origin': 'https://temp-mail.io',
        'referer': 'https://temp-mail.io/',
        'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48',
    }

    response = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{mail}/messages',cookies=cookies,headers=headers).json()

    try:
        response = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{mail}/messages', cookies=cookies, headers=headers).json()
        if 'code' in response and response['code'] == 101:
            await message.reply_text("<b>El correo electrónico ingresado no es válido.</b>")
        else:
            await message.reply(response)
    except Exception as e:
        await message.reply(f"<b>No Tienes Ningun Message En La Bandeja De Entrada De</b> <code>{mail}</code>")