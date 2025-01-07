from configss._def_main_ import *

@Client.on_callback_query(filters.regex('regen'))
async def regen(client, msg):
    men = msg.message.reply_to_message.text
    
    
    geneo = re.findall(r'[0-9]+',msg.message.text)
    binreq = requests.get(f'https://bins.antipublic.cc/bins/{geneo}')
    brand = binreq['brand']
    country = binreq['country']
    country_name = binreq['country_name']
    country_flag = binreq['country_flag']
    country_currencies = binreq['country_currencies']
    bank = binreq['bank']
    level = binreq['level']
    typea  = binreq['type']
    
    if len(geneo) == 1:
        cc = geneo[0]
        mes = 'x'
        ano = 'x'
        cvv = 'x'
    elif len(geneo) ==2:
        cc = geneo[0]
        mes = geneo[1]
        ano = 'x'
        cvv = 'x'
    elif len(geneo) ==3:
        cc = geneo[0]
        mes = geneo[1]
        ano = geneo[2]
        cvv = 'x'
    elif len(geneo) ==4:
        cc = geneo[0]
        mes = geneo[1]
        ano = geneo[2]
        cvv = geneo[3]
    else:
        cc = geneo[0]
        mes = geneo[1]
        ano = geneo[2]
        cvv = geneo[3]

    cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9,cc10, = cc_gen(cc,mes,ano,cvv)

    ms = gen.format(cc1=cc1,cc2=cc2,cc3=cc3,cc4=cc4,cc5=cc5,cc6=cc6,cc7=cc7,cc8=cc8,cc9=cc9,cc10=cc10,binif=binreq.json()['bin'],country = binreq.json()['country'],country_name = binreq.json()['country_name'],country_flag = binreq.json()['country_flag'])
    await msg.edit_message_text(ms,reply_markup=regen)

