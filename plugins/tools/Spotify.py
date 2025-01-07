import os
import requests
import string
import random
import requests
from pyrogram import Client, filters


def getRandomString(length):
    pool = string.ascii_lowercase + string.digits
    return "".join(random.choice(pool) for i in range(length))


def getRandomText(length):
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))


def generate():
    nick = getRandomText(8)
    passw = getRandomString(12)
    email = nick + "@" + "gmail" + ".com"

    headers = {
        "Accept-Encoding": "gzip",
        "Accept-Language": "en-US",
        "App-Platform": "Android",
        "Connection": "Keep-Alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "spclient.wg.spotify.com",
        "User-Agent": "Spotify/8.6.72 Android/29 (SM-N976N)",
        "Spotify-App-Version": "8.6.72",
        "X-Client-Id": getRandomString(32)
    }

    payload = {
        "creation_point": "client_mobile",
        "gender": "male" if random.randint(0, 1) else "female",
        "birth_year": random.randint(1990, 2000),
        "displayname": nick,
        "iagree": "true",
        "birth_month": random.randint(1, 11),
        "password_repeat": passw,
        "password": passw,
        "key": "142b583129b2df829de3656f9eb484e6",
        "platform": "Android-ARM",
        "email": email,
        "birth_day": random.randint(1, 20)
    }
    proxies = {
  "http": "http://gate.proxiware.com:2000",
  "https": "http://gate.proxiware.com:2000"
}

    r = requests.post(
        'https://spclient.wg.spotify.com/signup/public/v1/account/',
        headers=headers,
        data=payload)

    if r.status_code == 200:
        if r.json()['status'] == 1:
            text = f"""<b>Auto Spotify Created! ✅
Plan -» FREE 
Email -» <code>{email}</code>
Password -»<code>{passw}</code></b>"""

            return (text)
        else:
            #Details available in r.json()["errors"]
            #print(r.json()["errors"])
            return (False, "Could not create the account, some errors occurred")
    else:
        return (False,
                "Could not load the page. Response code: " + str(r.status_code))


@Client.on_message(filters.command(["spotify"], ["/", "."]))
async def spoti(client, message):
    proxies = {
  "http": "http://gate.proxiware.com:2000",
  "https": "http://gate.proxiware.com:2000"
}
    
    return await message.reply(generate())