import requests
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
) 



@Client.on_message(filters.command(["ccs"], ["/", "."]))
async def hma(client, message):
    
    
    response = requests.get(f"https://api.namefake.com/gen.json?country=mx")
    data = response.json()
    
    name = data["name"]
    address = data["address"]  
    latitude = data["latitude"]  
    longitude = data["longitude"] 
    maiden_name = data["maiden_name"] 
    birth_data = data["birth_data"]
    phone = data["phone_h"]
    phone2 = data["phone_w"]
    email = data["email_u"]
    e2 = data["email_d"]
    user = data["username"]
    pas = data["password"]
    d = data["domain"]
    usera = data["useragent"]
    i4 = data["ipv4"]
    mac = data["macaddress"]
    p = data["plasticcard"]
    exc = data["cardexpir"]
    b = data["bonus"]
    co = data["company"]
    cl = data["color"]
    uu = data["uuid"]
    he = data["height"]
    we = data["weight"]
    bl = data["blood"]
    pi = data["pict"]
    ip4 = data["ipv4_url"]
    emur = data["email_url"]
    dmur = data["domain_url"]
             
    await message.reply(f"\nName: {name}\nCard: {p}\nExpire Card: {exc}\nBonus: {b}\n")