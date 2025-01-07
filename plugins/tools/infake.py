from configss._def_main_ import *

@Client.on_message(filters.command(["rnd"], ["/", "."]))
async def rnd(_, m: Message):
    
    rnd = m.text[len("/rnd"):]
    if not rnd:
        await m.reply("Use de /nnd Us | /pais")
    
    spli = rnd.split()
    rnd = spli[0]

    rnd_api = requests.get(f'https://www.bestrandoms.com/api/?nat={rnd}').json()
#CAPTURAS
#data = /rnd["data"]
    name = rnd_api["results"][0]["name"]
    gender = rnd_api["results"][0]["gender"]
    age = rnd_api["results"][0]["dob"]["age"]
    birthdate = rnd_api["results"][0]["dob"]["date"]
    street = rnd_api["results"][0]["location"]["street"]['number']
    street1 = rnd_api["results"][0]["location"]["street"]['name']
    city = rnd_api["results"][0]["location"]["city"]
    state = rnd_api["results"][0]["location"]["state"]
    postal = rnd_api["results"][0]["location"]["postcode"]
    email = rnd_api["results"][0]["email"]
    country = rnd_api["results"][0]["location"]["country"]


    edit1 = await m.reply_text("<b>Buscando Infomaciones.</b>")
    await time.sleep(1.5)
    
    await edit1.edit(f"""
<b>

Name : <code>{name["first"]} {name["last"]}</code>
Gender :<code> {gender}</code>
Age :<code> {age}</code>
Birthdate :<code> {birthdate}</code>
Country :<code> {country}</code>
Street :<code> {street}, {street1}</code>
City :<code> {city}</code>
State : <code>{state}</code>
Postal Code :<code> {postal}</code>
Email :<code> {email}</code></b>
</b>
""")


